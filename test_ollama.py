import requests
import json

def test_ollama():
    """Test if Ollama is running and accessible"""
    try:
        # Test if Ollama server is running
        response = requests.get("http://localhost:11434/api/tags")
        
        if response.status_code == 200:
            models = response.json()
            print("✅ Ollama is running!")
            print(f"Available models: {[model['name'] for model in models.get('models', [])]}")
            return True
        else:
            print("❌ Ollama server not responding")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Ollama not running. Please start Ollama first.")
        print("Install: curl -fsSL https://ollama.ai/install.sh | sh")
        print("Start: ollama serve")
        return False

def test_ollama_chat():
    """Test Ollama chat functionality"""
    try:
        payload = {
            "model": "llama3.1:8b",
            "messages": [
                {"role": "user", "content": "Hello! Respond with 'Ollama is working!'"}
            ],
            "stream": False
        }
        
        response = requests.post(
            "http://localhost:11434/api/chat",
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Ollama Chat Test Successful!")
            print(f"Response: {result['message']['content']}")
            return True
        else:
            print(f"❌ Chat test failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Chat test error: {str(e)}")
        return False

if __name__ == "__main__":
    print("Testing Ollama setup...")
    if test_ollama():
        test_ollama_chat()