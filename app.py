import requests
import gradio as gr
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Hugging Face API endpoint
API_URL = "https://api-inference.huggingface.co/models/bigcode/starcoder"
# Get the API token from the environment variable
API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

headers = {"Authorization": f"Bearer {API_TOKEN}"}

history = []

def generate_response(prompt):
    # Add a system prompt to guide the model
    system_prompt = (
        "You are a code teaching assistant named CodeGuru created by Austin. "
        "Provide clear and concise Python code solutions to the questions asked.\n"
    )
    
    # Limit history to the last 3 prompts to avoid confusion
    if len(history) > 3:
        history.pop(0)
    
    history.append(prompt)
    final_prompt = system_prompt + "\n".join(history)

    payload = {
        "inputs": final_prompt,
        "parameters": {
            "max_new_tokens": 150,  # Adjusted to focus on concise responses
            "temperature": 0.3,     # Lower temperature for more deterministic output
            "top_p": 0.8,           # Adjusted top_p for more focused sampling
            "do_sample": True,
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()[0]['generated_text'].split("AI:")[-1].strip()
    else:
        return f"Error: {response.status_code}, {response.text}"

interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4, placeholder="Enter your Prompt"),
    outputs="text"
)

# Test API connection
def test_api():
    test_payload = {
        "inputs": "def fibonacci(n):",
        "parameters": {"max_new_tokens": 50}
    }
    response = requests.post(API_URL, headers=headers, json=test_payload)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")

test_api()

if __name__ == "__main__":
    interface.launch()