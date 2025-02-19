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
    Generate a concise description without text formatting and a touch of humour for my Facebook Marketplace ad of {product_name}.
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
    with open("out.txt", "w", encoding="utf-8") as file:
        file.write("Pickup is in Rutherford SW, T6W1J6.\n\n")
        file.write("I ignore messages asking if it's still available, let's not waste each other's time please.\n\n")
        file.write(description)