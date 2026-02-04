from crewai import Task

def create_tasks(problem_description):
    """Create tasks for each agent based on the problem description"""
    
    # Task 1: Problem Analysis
    analyze_task = Task(
        description=f"""
        Analyze this coding problem: {problem_description}
        
        Extract and provide:
        1. Problem summary in simple terms
        2. Input format and constraints
        3. Expected output format
        4. Problem classification (array, string, DP, graph, etc.)
        5. Key insights or patterns you notice
        
        Format your response as structured analysis.
        """,
        expected_output="Structured problem analysis with classification and key insights",
        agent=None  # Will be assigned in crew_setup.py
    )
    
    # Task 2: Brute Force Solution
    brute_force_task = Task(
        description="""
        Based on the problem analysis, create a brute-force solution.
        
        Provide:
        1. Step-by-step approach explanation
        2. Pseudocode or algorithm outline
        3. Time complexity analysis
        4. Space complexity analysis
        5. Why this approach works (correctness proof)
        
        Focus on correctness over efficiency.
        """,
        expected_output="Brute-force solution with complexity analysis and correctness explanation",
        agent=None
    )
    
    # Task 3: Optimization
    optimize_task = Task(
        description="""
        Optimize the brute-force solution using advanced techniques.
        
        Provide:
        1. Identified bottlenecks in brute-force approach
        2. Optimization strategy (data structures, algorithms)
        3. Improved algorithm explanation
        4. New time and space complexity
        5. Trade-offs made during optimization
        
        Aim for the most efficient solution possible.
        """,
        expected_output="Optimized solution with improved complexity and detailed optimization rationale",
        agent=None
    )
    
    # Task 4: Edge Case Analysis
    edge_case_task = Task(
        description="""
        Validate the optimized solution by identifying edge cases.
        
        Provide:
        1. List of critical edge cases to test
        2. Potential failure scenarios
        3. Input validation requirements
        4. Boundary condition handling
        5. Stress test considerations
        
        Think like a thorough tester.
        """,
        expected_output="Comprehensive edge case analysis with potential failure scenarios",
        agent=None
    )
    
    # Task 5: Code Generation
    code_generation_task = Task(
        description="""
        Write the final Python implementation based on the optimized solution.
        
        Requirements:
        1. Clean, readable Python code
        2. Proper variable naming and structure
        3. Inline comments explaining key logic
        4. LeetCode-style function signature
        5. Handle edge cases identified earlier
        6. Include complexity analysis as comments
        
        Write production-ready code.
        """,
        expected_output="Clean Python code with comments and complexity analysis",
        agent=None
    )
    
    # Task 6: Final Coordination
    coordination_task = Task(
        description="""
        Coordinate all previous outputs into a final comprehensive solution.
        
        Compile:
        1. Problem explanation
        2. Solution approach (brute-force vs optimized)
        3. Final Python code
        4. Complexity analysis
        5. Edge cases covered
        6. Any additional insights
        
        Ensure consistency and completeness across all agent outputs.
        """,
        expected_output="Final comprehensive solution with all components integrated",
        agent=None
    )
    
    return [analyze_task, brute_force_task, optimize_task, edge_case_task, code_generation_task, coordination_task]