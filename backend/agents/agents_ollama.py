from crewai import Agent, LLM
from crewai_tools import CodeInterpreterTool, SerperDevTool
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize LLM with Ollama (best for tools)
llm = LLM(
    model="ollama/llama3.1:8b",  # Best tool support
    base_url="http://localhost:11434"
)

# Initialize Tools
code_executor = CodeInterpreterTool()
researcher = SerperDevTool()

# Problem Analyzer Agent
problem_analyzer = Agent(
    role="Problem Understanding Specialist",
    goal="Extract and analyze the core problem requirements, constraints, and classify the problem type",
    backstory="You are an expert at breaking down complex coding problems into clear, structured components. You identify patterns and classify problems accurately.",
    verbose=True,
    allow_delegation=False,
    tools=[researcher],  # Can research similar problems
    llm=llm
)

# Brute Force Agent
brute_force_agent = Agent(
    role="Baseline Solution Developer",
    goal="Create a working brute-force solution that prioritizes correctness over efficiency",
    backstory="You specialize in creating straightforward, easy-to-understand solutions. You focus on correctness first, efficiency second.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Optimization Agent
optimization_agent = Agent(
    role="Performance Optimization Expert",
    goal="Transform brute-force solutions into efficient algorithms using optimal data structures and techniques",
    backstory="You are a master of algorithms and data structures. You can identify bottlenecks and apply the right optimization techniques.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Edge Case Agent
edge_case_agent = Agent(
    role="Solution Validator and Tester",
    goal="Identify edge cases, potential bugs, and ensure solution robustness by testing code",
    backstory="You have a keen eye for finding corner cases and potential failures. You think like a tester and debugger. You can execute code to verify it works.",
    verbose=True,
    allow_delegation=False,
    tools=[code_executor],  # Can execute and test code
    llm=llm
)

# Code Generator Agent
code_generator_agent = Agent(
    role="Clean Code Author",
    goal="Write production-ready, well-commented Python code following LeetCode conventions and verify it works",
    backstory="You write clean, readable, and well-documented code. You follow best practices and coding standards. You can execute code to ensure it works correctly.",
    verbose=True,
    allow_delegation=False,
    tools=[code_executor],  # Can execute and verify code
    llm=llm
)

# Manager Agent
manager_agent = Agent(
    role="System Coordinator",
    goal="Orchestrate the problem-solving process and ensure coherent final output",
    backstory="You coordinate multiple specialists to produce the best possible solution. You resolve conflicts and ensure quality.",
    verbose=True,
    allow_delegation=True,
    llm=llm
)