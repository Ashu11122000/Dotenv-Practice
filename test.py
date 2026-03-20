import os
from dotenv import load_dotenv

# Load Environment Variables 
load_dotenv()

# Access Variables
api_key=os.getenv("API_KEY")
password = os.getenv("SECRET_PASSWORD")

# Print to verify 
print("API_KEY:", api_key)
print("SECRET_PASSWORD:", password)