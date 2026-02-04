from crewai import Agent, LLM
from crewai_tools import CodeInterpreterTool, SerperDevTool
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize LLM with Gemini
llm = LLM(
    model="gemini-2.5-flash",
    temperature=0.1,
    api_key=os.getenv("GOOGLE_API_KEY")
)

# Initialize Tools
code_executor = CodeInterpreterTool()
researcher = SerperDevTool()
# Problem Analyzer Agent - Understands the problem structure
problem_analyzer = Agent(
    role="Problem Understanding Specialist",
    goal="Extract and analyze the core problem requirements, constraints, and classify the problem type",
    backstory="You are an expert at breaking down complex coding problems into clear, structured components. You identify patterns and classify problems accurately.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Brute Force Agent - Creates baseline solution
brute_force_agent = Agent(
    role="Baseline Solution Developer",
    goal="Create a working brute-force solution that prioritizes correctness over efficiency",
    backstory="You specialize in creating straightforward, easy-to-understand solutions. You focus on correctness first, efficiency second.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Optimization Agent - Improves performance
optimization_agent = Agent(
    role="Performance Optimization Expert",
    goal="Transform brute-force solutions into efficient algorithms using optimal data structures and techniques",
    backstory="You are a master of algorithms and data structures. You can identify bottlenecks and apply the right optimization techniques.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Edge Case Agent - Validates solutions
edge_case_agent = Agent(
    role="Solution Validator and Tester",
    goal="Identify edge cases, potential bugs, and ensure solution robustness",
    backstory="You have a keen eye for finding corner cases and potential failures. You think like a tester and debugger.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Code Generator Agent - Produces final code
code_generator_agent = Agent(
    role="Clean Code Author",
    goal="Write production-ready, well-commented Python code following LeetCode conventions",
    backstory="You write clean, readable, and well-documented code. You follow best practices and coding standards.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Manager Agent - Coordinates the process
manager_agent = Agent(
    role="System Coordinator",
    goal="Orchestrate the problem-solving process and ensure coherent final output",
    backstory="You coordinate multiple specialists to produce the best possible solution. You resolve conflicts and ensure quality.",
    verbose=True,
    allow_delegation=True,
    llm=llm
)