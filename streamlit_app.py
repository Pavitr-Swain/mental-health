import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import tools
from prompt import prompt, parser, llm

load_dotenv()

st.set_page_config(page_title="Mental Health Check-in Bot")
st.title("💬 Mental Health Check-in")

agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)
executor = AgentExecutor(agent=agent, tools=tools, verbose=False)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("How are you feeling today?", key="input")

if user_input:
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    response = executor.invoke({
        "query": user_input,
        "chat_history": st.session_state.chat_history
    })

    try:
        output = parser.parse(response["output"])
        st.success("✅ Mood Logged!")
        st.write("📝 **Mood Summary:**", output.mood_summary)
        st.write("🧘 **Suggestion:**", output.suggestion)
        st.write("📁 **Log:**", output.log_status)
        st.session_state.chat_history.append(AIMessage(content=output.mood_summary))
    except Exception as e:
        st.error("❌ Error parsing response.")
        st.code(response.get("output"))
