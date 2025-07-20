import os, datetime
from langchain.tools import Tool
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3,
    google_api_key=os.getenv("GOOGLE_API_KEY")  # 👈 This line is critical
)

def log_mood_entry(entry: str):
    os.makedirs("logs", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"logs/{datetime.datetime.now():%Y%m%d}_log.txt"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {entry}\n")
    return f"Entry logged at {timestamp}"

def suggest_activity(mood: str):
    response = llm.invoke(f"The user is feeling {mood}. Suggest a helpful activity.")
    return response.content

tools = [
    Tool(name="log_mood_entry", func=log_mood_entry, description="Log mood entry"),
    Tool(name="suggest_activity", func=suggest_activity, description="Suggest self-care tip")
<<<<<<< HEAD
]
=======
]
>>>>>>> 519fb10bab39203805c4421cdf636ce0e1e4582e
