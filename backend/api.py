from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import logging
import uuid
from dotenv import load_dotenv
from crew_setup import solve_problem

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

@app.route('/', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "message": "Multi-Agent LeetCode Solver API is running",
        "agents": [
            "Problem Analyzer",
            "Brute Force Agent",
            "Optimization Agent", 
            "Edge Case Agent",
            "Code Generator",
            "Manager Agent"
        ]
    })

@app.route('/solve', methods=['POST'])
def solve_leetcode_problem():
    """Main endpoint to solve LeetCode problems using multi-agent system"""
    
    try:
        request_id = str(uuid.uuid4())
        logger.info("🚀 request_id=%s event=solve_request_received", request_id)

        # Get problem description from request
        data = request.get_json()
        
        if not data or 'problem' not in data:
            logger.info("❌ request_id=%s event=solve_request_invalid reason=missing_problem", request_id)
            return jsonify({
                "status": "error",
                "error": "Problem description is required"
            }), 400
        
        problem_description = data['problem'].strip()
        
        if not problem_description:
            logger.info("❌ request_id=%s event=solve_request_invalid reason=empty_problem", request_id)
            return jsonify({
                "status": "error", 
                "error": "Problem description cannot be empty"
            }), 400
        
        logger.info("✅ request_id=%s event=solve_request_valid", request_id)
        logger.info("🤖 request_id=%s event=agents_starting", request_id)

        # Solve the problem using CrewAI multi-agent system
        result = solve_problem(problem_description, request_id=request_id, log_fn=logger.info)
        
        logger.info("🎉 request_id=%s event=solve_request_complete status=%s", request_id, result.get("status"))
        return jsonify(result)
        
    except Exception as e:
        logger.exception("💥 event=solve_request_exception")
        return jsonify({
            "status": "error",
            "error": f"Internal server error: {str(e)}"
        }), 500

@app.route('/agents', methods=['GET'])
def get_agents_info():
    """Get information about available agents"""
    return jsonify({
        "agents": [
            {
                "name": "Problem Analyzer",
                "role": "Problem Understanding Specialist",
                "responsibility": "Extract inputs, outputs, constraints, and classify problem type"
            },
            {
                "name": "Brute Force Agent", 
                "role": "Baseline Solver",
                "responsibility": "Generate naive solution with complexity analysis"
            },
            {
                "name": "Optimization Agent",
                "role": "Performance Optimizer", 
                "responsibility": "Improve efficiency using advanced algorithms"
            },
            {
                "name": "Edge Case Agent",
                "role": "Validator and Tester",
                "responsibility": "Identify edge cases and potential bugs"
            },
            {
                "name": "Code Generator",
                "role": "Code Author",
                "responsibility": "Write clean, production-ready Python code"
            },
            {
                "name": "Manager Agent",
                "role": "System Coordinator",
                "responsibility": "Coordinate agents and produce final solution"
            }
        ]
    })

if __name__ == '__main__':
    # Check for OpenAI API key
    if not os.getenv('GOOGLE_API_KEY'):
        print("Warning: OPENAI_API_KEY not found in environment variables")
        print("Please set your OpenAI API key to use the multi-agent system")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
