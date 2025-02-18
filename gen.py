import sys
import google.generativeai as genai
from pathlib import Path
import os

# Load environment variables
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('KEY')

# Configure Gemini API
genai.configure(api_key=API_KEY)

def generate_description(product_name):
    """Generates an engaging product description using Google Gemini API."""
    prompt = f"""
    Generate an engaging and concise product description for a {product_name}. 
    Mention key features, specifications, and a persuasive selling point. 
    Keep it under 150 words.
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return response.text.strip() if response and response.text else "No description generated."

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_description.py \"Product Name\"")
        sys.exit(1)

    product_name = " ".join(sys.argv[1:])  # Join all command-line arguments to handle multi-word names
    description = generate_description(product_name)
    print("\nGenerated Description:\n")
    print(description)