import os
from google import genai

# Get API key from environment variable
api_key = os.environ.get("GEMINI_API_KEY")

# Check if API key is available
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set. Please set it before running this script.")

# Initialize the client with the API key from environment
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)
