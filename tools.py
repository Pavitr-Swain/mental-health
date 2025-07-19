import os, datetime
from langchain.tools import Tool

def log_mood_entry(entry: str):
    os.makedirs("logs", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"logs/{datetime.datetime.now():%Y%m%d}_log.txt"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {entry}\n")
    return f"Entry logged at {timestamp}"

def suggest_activity(mood: str):
    mood = mood.lower()
    if "anxious" in mood:
        return "Try deep breathing for 5 minutes or write down what you're feeling."
    elif "sad" in mood:
        return "Call a friend or take a walk in nature."
    elif "angry" in mood:
        return "Pause and breathe deeply for 60 seconds."
    elif "tired" in mood:
        return "Take a power nap or rest your eyes for 10 minutes."
    elif "calm" in mood or "happy" in mood:
        return "That's great! Write in your gratitude journal or enjoy your favorite song."
    else:
        return "Try light stretching or a short mindfulness break."

tools = [
    Tool(name="log_mood_entry", func=log_mood_entry, description="Log mood entry"),
    Tool(name="suggest_activity", func=suggest_activity, description="Suggest self-care tip")
]
