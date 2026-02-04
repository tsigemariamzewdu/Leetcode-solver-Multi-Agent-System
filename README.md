# LeetCode Solver - Multi-Agent System

A collaborative AI system that solves coding problems using specialized agents powered by CrewAI framework.

## Architecture

**6 Specialized Agents:**
- **Problem Analyzer** - Extracts requirements and constraints
- **Brute Force Agent** - Creates baseline solutions
- **Optimization Agent** - Improves algorithmic efficiency
- **Edge Case Agent** - Validates code and identifies corner cases
- **Code Generator** - Produces clean, production-ready code
- **Manager Agent** - Coordinates the entire process

**Technology Stack:**
- Backend: Flask + CrewAI + Gemini 1.5 Flash
- Frontend: Vanilla HTML/CSS/JavaScript
- Custom Tools: Code Validator (AST-based syntax checking)

## Quick Start

### Prerequisites
```bash
pip install crewai flask flask-cors python-dotenv
```

### Setup
1. Clone repository
2. Add Google API key to `backend/.env`:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
3. Start backend:
   ```bash
   cd backend && python3 api.py
   ```
4. Open `frontend/index.html` in browser

## Usage

1. Enter LeetCode problem description
2. Click "Solve Problem"
3. Watch agents collaborate in real-time
4. View individual agent results and final solution

## Features

- **Real-time Progress Tracking** - Visual agent status indicators
- **Individual Agent Results** - See each specialist's contribution
- **Custom Tool Integration** - Code validation without execution
- **Professional UI** - LeetCode-style dark theme interface
- **Comprehensive Logging** - Detailed backend activity tracking

## API Endpoints

- `GET /` - Health check
- `POST /solve` - Solve coding problem
- `GET /agents` - Agent information

## License

MIT