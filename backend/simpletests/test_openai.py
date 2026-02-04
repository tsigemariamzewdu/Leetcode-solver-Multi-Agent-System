import openai
import os
from dotenv import load_dotenv

# Load environment variables from backend/.env
load_dotenv('backend/.env')

def test_openai_api():
    """Simple test to check if OpenAI API key is working"""
    
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("❌ No OpenAI API key found!")
        print("Please set OPENAI_API_KEY in backend/.env file")
        return False
    
    if api_key == "your_openai_api_key_here":
        print("❌ Please replace 'your_openai_api_key_here' with your actual OpenAI API key")
        return False
    
    print(f"Found API key: {api_key[:20]}...")
    
    try:
        client = openai.OpenAI(api_key=api_key)
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Hello! Can you respond with 'OpenAI API is working!'?"}
            ],
            max_tokens=50,
            temperature=0.1
        )
        
        print("✅ OpenAI API Test Successful!")
        print(f"Response: {response.choices[0].message.content}")
        return True
        
    except Exception as e:
        print("❌ OpenAI API Test Failed!")
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    print("Testing OpenAI API key...")
    test_openai_api()