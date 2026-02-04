const API_BASE_URL = 'http://localhost:5000';

// Agent status management
const agents = ['analyzer', 'brute', 'optimizer', 'edge', 'code', 'manager'];
let currentAgentIndex = 0;

function resetAgentStatus() {
    agents.forEach(agent => {
        const statusElement = document.getElementById(`status-${agent}`);
        const cardElement = document.getElementById(`agent-${agent}`);
        
        statusElement.textContent = '⏳';
        statusElement.className = 'status-indicator waiting';
        cardElement.className = 'agent-card';
    });
    currentAgentIndex = 0;
}

function updateAgentStatus(agentIndex, status) {
    if (agentIndex >= agents.length) return;
    
    const agent = agents[agentIndex];
    const statusElement = document.getElementById(`status-${agent}`);
    const cardElement = document.getElementById(`agent-${agent}`);
    
    if (status === 'thinking') {
        statusElement.textContent = '🤔';
        statusElement.className = 'status-indicator thinking';
        cardElement.className = 'agent-card thinking';
    } else if (status === 'done') {
        statusElement.textContent = '✅';
        statusElement.className = 'status-indicator done';
        cardElement.className = 'agent-card done';
    }
}

function simulateAgentProgress() {
    // Remove fake simulation - we'll rely on real backend timing
    return null;
}

async function solveProblem() {
    const problemInput = document.getElementById('problemInput');
    const solveBtn = document.getElementById('solveBtn');
    const loading = document.getElementById('loading');
    const resultsSection = document.getElementById('resultsSection');
    const errorMessage = document.getElementById('errorMessage');
    
    const problem = problemInput.value.trim();
    
    if (!problem) {
        showError('Please enter a problem description');
        return;
    }
    
    // Reset UI state
    resetAgentStatus();
    solveBtn.disabled = true;
    solveBtn.textContent = '🤖 Agents Working...';
    loading.style.display = 'block';
    resultsSection.style.display = 'none';
    errorMessage.style.display = 'none';
    
    try {
        const response = await fetch(`${API_BASE_URL}/solve`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ problem: problem })
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            displayResults(data);
        } else {
            showError(data.error || 'Failed to solve problem');
        }
        
    } catch (error) {
        console.error('Error:', error);
        showError('Failed to connect to the backend. Make sure the server is running.');
    } finally {
        // Mark all agents as complete
        agents.forEach((_, index) => updateAgentStatus(index, 'done'));
        
        solveBtn.disabled = false;
        solveBtn.textContent = '🚀 Solve Problem';
        loading.style.display = 'none';
    }
}

function displayResults(data) {
    const resultsSection = document.getElementById('resultsSection');
    const explanationContent = document.getElementById('explanationContent');
    const codeContent = document.getElementById('codeContent');
    const complexityContent = document.getElementById('complexityContent');
    
    // Display individual agent results if available
    if (data.agent_results && data.agent_results.length > 0) {
        let agentResultsHtml = '<div class="agent-results">';
        
        data.agent_results.forEach((agentResult, index) => {
            agentResultsHtml += `
                <div class="agent-result-card">
                    <h4>🤖 ${agentResult.agent}</h4>
                    <div class="agent-output">
                        <pre style="white-space: pre-wrap; background: #f8fafc; padding: 15px; border-radius: 8px; color: #4a5568; max-height: 300px; overflow-y: auto;">${agentResult.result}</pre>
                    </div>
                </div>
            `;
        });
        
        agentResultsHtml += '</div>';
        explanationContent.innerHTML = agentResultsHtml;
    } else {
        // Fallback to original display
        explanationContent.innerHTML = `
            <div class="solution-overview">
                <h4>Multi-Agent Collaboration Result:</h4>
                <p>The following solution was developed through collaboration between ${data.agents_used.length} specialized agents:</p>
                <ul>
                    ${data.agents_used.map(agent => `<li><strong>${agent}</strong></li>`).join('')}
                </ul>
            </div>
            <div class="solution-details">
                <h4>Solution Analysis:</h4>
                <pre style="white-space: pre-wrap; background: #f8fafc; padding: 15px; border-radius: 8px; color: #4a5568;">${data.solution}</pre>
            </div>
        `;
    }
    
    // Extract code from final solution
    const codeMatch = data.solution.match(/```python\n([\s\S]*?)\n```/);
    if (codeMatch) {
        codeContent.textContent = codeMatch[1];
    } else {
        codeContent.textContent = data.solution;
    }
    
    // Show complexity analysis
    complexityContent.innerHTML = `
        <div class="complexity-analysis">
            <h4>Performance Analysis:</h4>
            <p>The agents analyzed both brute-force and optimized approaches:</p>
            <div style="background: #f8fafc; padding: 15px; border-radius: 8px; margin-top: 10px;">
                <p><strong>Final Solution:</strong> The Manager Agent coordinated all specialists to produce the optimal solution.</p>
            </div>
        </div>
    `;
    
    resultsSection.style.display = 'block';
    togglePanel('explanation');
}

function showError(message) {
    const errorMessage = document.getElementById('errorMessage');
    errorMessage.textContent = message;
    errorMessage.style.display = 'block';
}

function togglePanel(panelId) {
    const panel = document.getElementById(panelId);
    const header = panel.previousElementSibling;
    
    if (panel.classList.contains('active')) {
        panel.classList.remove('active');
        header.classList.remove('active');
    } else {
        // Close all other panels
        document.querySelectorAll('.panel-content').forEach(p => {
            p.classList.remove('active');
            p.previousElementSibling.classList.remove('active');
        });
        
        // Open this panel
        panel.classList.add('active');
        header.classList.add('active');
    }
}

// Initialize the app
document.addEventListener('DOMContentLoaded', function() {
    // Test backend connection
    fetch(`${API_BASE_URL}/`)
        .then(response => response.json())
        .then(data => {
            console.log('Backend connected:', data.message);
        })
        .catch(error => {
            console.warn('Backend not available:', error);
            showError('Backend server is not running. Please start the backend server first.');
        });
    
    // Add enter key support for textarea
    document.getElementById('problemInput').addEventListener('keydown', function(e) {
        if (e.ctrlKey && e.key === 'Enter') {
            solveProblem();
        }
    });
});