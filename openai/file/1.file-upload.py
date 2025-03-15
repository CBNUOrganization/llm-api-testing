from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

## purpose metadata:
# - assistants: Used in the Assistants API 
# - batch: Used in the Batch API 
# - fine-tune: Used for fine-tuning 
# - vision: Images used for vision fine-tuning 
# - user_data: Flexible file type for any purpose 
# - evals: Used for eval data sets
client.files.create(
  file=open("./uploaded-file/deep_research_blog.pdf", "rb"),
  purpose="user_data"    
)
