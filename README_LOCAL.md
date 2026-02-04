# 🤖 Multi-Agent LeetCode Problem Solver

A sophisticated Multi-Agent System (MAS) built with CrewAI that collaborates to solve LeetCode-style coding problems. Six specialized AI agents work together to analyze, solve, and optimize coding challenges.

## 🎯 Project Overview

This system demonstrates key Multi-Agent Systems concepts:
- **Agent Autonomy**: Each agent has distinct roles and capabilities
- **Distributed Problem Solving**: Problem broken down across multiple specialists
- **Coordination & Cooperation**: Agents share context and build upon each other's work
- **Communication**: Structured information flow between agents
- **Emergent Solutions**: Final solution emerges from collaborative effort

## 🤖 Agent Architecture

### 1. Problem Analyzer Agent 🔍
- **Role**: Problem Understanding Specialist
- **Responsibility**: Extract inputs/outputs, identify constraints, classify problem type

### 2. Brute Force Agent ⚡
- **Role**: Baseline Solution Developer  
- **Responsibility**: Create working naive solution with complexity analysis

### 3. Optimization Agent 🚀
- **Role**: Performance Optimization Expert
- **Responsibility**: Improve efficiency using advanced algorithms and data structures

### 4. Edge Case Agent 🛡️
- **Role**: Solution Validator and Tester
- **Responsibility**: Identify edge cases and potential failure scenarios

### 5. Code Generator Agent 💻
- **Role**: Clean Code Author
- **Responsibility**: Write production-ready Python code with proper documentation

### 6. Manager Agent 👑
- **Role**: System Coordinator
- **Responsibility**: Orchestrate the process and ensure coherent final output

## 🏗️ System Architecture

```
Frontend (React-like UI)
    ↓ HTTP API
Backend (Flask + CrewAI)
    ↓ Sequential Process
Multi-Agent Collaboration
    ↓ Structured Output
Final Solution
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- OpenAI API key
- Modern web browser

### Backend Setup

1. **Navigate to backend directory**:
```bash
cd backend
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Configure environment**:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

4. **Start the backend server**:
```bash
python api.py
```

The backend will run on `http://localhost:5000`

### Frontend Setup

1. **Navigate to frontend directory**:
```bash
cd frontend
```

2. **Open in browser**:
```bash
# Simply open index.html in your browser, or use a local server:
python -m http.server 8080
```

The frontend will be available at `http://localhost:8080`

## 💻 Usage

1. **Open the frontend** in your web browser
2. **Paste a LeetCode problem** in the text area
3. **Click "Solve Problem"** to start the multi-agent collaboration
4. **Watch the agents work** - status indicators show progress
5. **Review the results** in expandable panels:
   - Problem Analysis & Approach
   - Final Solution Code  
   - Complexity Analysis

### Example Problem

```
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

## 🔧 API Endpoints

### `GET /`
Health check endpoint

### `POST /solve`
Main problem-solving endpoint
- **Input**: `{"problem": "problem description"}`
- **Output**: Structured solution with agent outputs

### `GET /agents`
Get information about available agents

## 🧠 Multi-Agent System Concepts Demonstrated

### Agent Autonomy
Each agent operates independently with its own:
- Role definition
- Goal specification
- Specialized knowledge
- Decision-making capability

### Distributed Problem Solving
The coding problem is decomposed into:
- Problem analysis
- Baseline solution creation
- Performance optimization
- Validation and testing
- Code generation
- Final coordination

### Coordination Mechanisms
- **Sequential Process**: Agents execute in logical order
- **Shared Memory**: Context flows between agents
- **Manager Coordination**: Final agent ensures coherence

### Communication Patterns
- **Task-based Communication**: Each agent receives specific tasks
- **Context Sharing**: Previous agent outputs inform subsequent agents
- **Structured Output**: Standardized information exchange

## 📁 Project Structure

```
leetcodesolver/
├── backend/
│   ├── agents/
│   │   └── agents.py          # Agent definitions
│   ├── tasks/
│   │   └── tasks.py           # Task definitions
│   ├── crew_setup.py          # CrewAI orchestration
│   ├── api.py                 # Flask API server
│   ├── requirements.txt       # Python dependencies
│   └── .env.example          # Environment template
├── frontend/
│   ├── index.html            # Main UI
│   ├── style.css             # Styling
│   └── script.js             # Frontend logic
└── README.md                 # This file
```

## 🔍 Technical Implementation

### CrewAI Integration
- **Sequential Process**: Ensures logical agent execution order
- **Memory Enabled**: Agents share context across tasks
- **Verbose Logging**: Detailed execution tracking

### Agent Design Patterns
- **Role-based Architecture**: Each agent has clear responsibilities
- **Goal-oriented Behavior**: Agents work toward specific objectives
- **Backstory Context**: Provides behavioral guidance

### Task Orchestration
- **Dependency Management**: Later tasks depend on earlier outputs
- **Context Propagation**: Information flows through the system
- **Error Handling**: Graceful failure management

## 🎓 Educational Value

This project demonstrates:
- **Multi-Agent Systems principles** in a practical application
- **Distributed AI problem solving** techniques
- **Agent coordination** and **communication** patterns
- **Emergent behavior** from collaborative agents
- **Real-world MAS implementation** using modern tools

## 🛠️ Customization

### Adding New Agents
1. Define agent in `backend/agents/agents.py`
2. Create corresponding task in `backend/tasks/tasks.py`
3. Update crew setup in `backend/crew_setup.py`
4. Add UI elements in frontend

### Modifying Agent Behavior
- Update agent `role`, `goal`, and `backstory`
- Adjust task descriptions and expected outputs
- Modify coordination logic in manager agent

## 🚨 Troubleshooting

### Backend Issues
- **OpenAI API Key**: Ensure valid key in `.env` file
- **Dependencies**: Run `pip install -r requirements.txt`
- **Port Conflicts**: Backend runs on port 5000 by default

### Frontend Issues
- **CORS Errors**: Backend includes CORS headers
- **API Connection**: Check backend is running on localhost:5000

## 📚 Learning Resources

- [CrewAI Documentation](https://docs.crewai.com/)
- [Multi-Agent Systems Concepts](https://en.wikipedia.org/wiki/Multi-agent_system)
- [LangChain Integration](https://python.langchain.com/)

## 🤝 Contributing

This is an educational project demonstrating MAS concepts. Feel free to:
- Add new agent types
- Improve coordination mechanisms
- Enhance the UI/UX
- Add more sophisticated problem-solving strategies

---

**Built for Multi-Agent Systems Course** - Demonstrating practical MAS implementation with modern AI tools.