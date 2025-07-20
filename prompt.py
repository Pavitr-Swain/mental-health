import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from tools import tools
from schema import MoodResponse

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3,
    google_api_key=os.getenv("GOOGLE_API_KEY")  # 👈 This line is critical
)

parser = PydanticOutputParser(pydantic_object=MoodResponse)

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a caring mental health assistant.
Your task:
1. Ask the user how they are feeling.
2. Acknowledge with empathy.
3. Use the tool suggest_activity.
4. Log the user's message using log_mood_entry.
5. Reply only in this strict JSON format:

{{
  "mood_summary": "...",
  "suggestion": "...",
  "log_status": "..."
}}

Do NOT include nested objects. Every field must be a simple string.
"""),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}")
]).partial(format_instructions=parser.get_format_instructions())

prompt.input_variables = ["query", "chat_history", "agent_scratchpad"]
