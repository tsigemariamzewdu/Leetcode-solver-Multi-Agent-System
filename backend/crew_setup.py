from crewai import Crew, Process
from agents.agents import (
    problem_analyzer, brute_force_agent, optimization_agent,
    edge_case_agent, code_generator_agent, manager_agent
)
from tasks.tasks import create_tasks

def setup_crew(problem_description, request_id=None, log_fn=None):
    """Setup and configure the CrewAI crew for solving the problem"""
    
    if log_fn:
        log_fn("request_id=%s event=crew_setup_start", request_id)

    # Create tasks
    tasks = create_tasks(problem_description)
    
    # Assign agents to tasks
    tasks[0].agent = problem_analyzer      # Analysis task
    tasks[1].agent = brute_force_agent     # Brute force task
    tasks[2].agent = optimization_agent    # Optimization task
    tasks[3].agent = edge_case_agent       # Edge case task
    tasks[4].agent = code_generator_agent  # Code generation task
    tasks[5].agent = manager_agent         # Coordination task
    
    # Create crew with sequential process
    crew = Crew(
        agents=[
            problem_analyzer,
            brute_force_agent,
            optimization_agent,
            edge_case_agent,
            code_generator_agent,
            manager_agent
        ],
        tasks=tasks,
        process=Process.sequential,  # Agents work in sequence
        verbose=True,  # Enable detailed logging
        memory=False  # Disable CrewAI memory to avoid OpenAI embedding dependency
    )
    
    if log_fn:
        log_fn("request_id=%s event=crew_setup_complete tasks=%d", request_id, len(tasks))

    return crew

def solve_problem(problem_description, request_id=None, log_fn=None):
    """Main function to solve a coding problem using the multi-agent system"""
    
    try:
        # Setup the crew
        crew = setup_crew(problem_description, request_id=request_id, log_fn=log_fn)
        
        if log_fn:
            log_fn("🚀 request_id=%s event=crew_kickoff_start", request_id)

        # Execute the crew
        result = crew.kickoff()
        
        if log_fn:
            log_fn("✅ request_id=%s event=crew_kickoff_complete", request_id)

        # Get individual task results
        task_results = []
        for i, task in enumerate(crew.tasks):
            agent_name = [
                "Problem Analyzer", "Brute Force Agent", "Optimization Agent",
                "Edge Case Agent", "Code Generator", "Manager Agent"
            ][i]
            
            task_results.append({
                "agent": agent_name,
                "result": str(task.output) if hasattr(task, 'output') and task.output else "No output available"
            })

        # Structure the response
        response = {
            "status": "success",
            "problem": problem_description,
            "solution": str(result),
            "agent_results": task_results,
            "agents_used": [
                "Problem Analyzer",
                "Brute Force Agent", 
                "Optimization Agent",
                "Edge Case Agent",
                "Code Generator",
                "Manager Agent"
            ]
        }
        
        return response
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "problem": problem_description
        }
