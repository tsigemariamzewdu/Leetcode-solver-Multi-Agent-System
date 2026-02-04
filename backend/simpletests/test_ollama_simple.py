from crewai import LLM
import time

# Test Ollama LLM
ollama_llm = LLM(
    model="ollama/llama3.1:8b",
    base_url="http://localhost:11434"
)

# Simple test with timing
start_time = time.time()
response = ollama_llm.call("Write a Python function to add two numbers")
end_time = time.time()

print(f"Response time: {end_time - start_time:.2f} seconds")
print(response)