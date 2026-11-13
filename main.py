
import os
import anthropic
from dotenv import load_dotenv

# Step 1: Load environment variables from .env
load_dotenv()

# Step 2: Create an Anthropic client
client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# Step 3: Send a message to Claude
message = client.messages.create(
    
    model="claude-haiku-5-5",
    max_tokens=300,
    messages=[
        {
            "role": "user",
            "content": "Hello Claude! I am building an Order Enquiry Agent. Introduce yourself."
        }
    ]
)

# Step 4: Display Claude's response
for block in message.content:
    if block.type == "text":
        print(block.text)
