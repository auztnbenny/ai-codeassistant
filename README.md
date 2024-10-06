# AI-Code-Assistant

## Overview

Code-Assistant-Code-Assistant is a Python-based application that leverages the Hugging Face API to provide a code teaching assistant named CodeGuru. This assistant is designed to offer clear and concise Python code solutions to user queries. The application uses Gradio for creating a user-friendly interface.

## Features

- **Code Assistance**: Provides Python code solutions based on user prompts.
- **Interactive Interface**: Utilizes Gradio to create an easy-to-use web interface.
- **API Integration**: Connects to Hugging Face's inference API to generate responses.

## Requirements

- Python 3.x
- Hugging Face API token
- Required Python packages (listed in `requirements.txt`)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/auztnbenny/ai-codeassistant.git
   cd Code-Assistant
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Create a `.env` file in the root directory.
   - Add your Hugging Face API token:
     ```
     HUGGINGFACE_API_TOKEN=your_api_token_here
     ```

## Usage

1. **Run the application**:
   ```bash
   python app.py
   ```

2. **Access the interface**:
   - Open your web browser and go to the URL provided by Gradio (usually `http://localhost:7860`).

3. **Interact with CodeGuru**:
   - Enter your Python-related queries in the text box and receive code solutions.

