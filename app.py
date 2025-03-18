import streamlit as st
from langchain_groq import ChatGroq
import yfinance as yf
import os
from dotenv import load_dotenv 
load_dotenv()
from langchain.agents import AgentExecutor
from langchain.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_groq import ChatGroq
import yfinance as yf

# Set up API keys (Use environment variables instead of hardcoding)
os.environ["GROQ_API_KEY"] = os.environ.get("GROQ_API_KEY")
os.environ["TAVILY_API_KEY"] = os.environ.get("TAVILY_API_KEY")

# Streamlit UI
st.title("LangChain & Finance Data Viewer")

# Select AI Model
model_name = st.selectbox("Select AI Model:", ["gemma2-9b-it"])

# Initialize LLM
llm = ChatGroq(model_name = "gemma2-9b-it")

# Stock Data Section
st.header("Stock Market Data")
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL):")
if st.button("Get Stock Data"):
    if ticker:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1yr")
        st.write(hist)
    else:
        st.warning("Please enter a valid stock ticker.")

# AI Response Section
st.header("AI Chatbot")
user_input = st.text_area("Ask something:")
if st.button("Get AI Response"):
    if user_input:
        response = llm.invoke(user_input)
        st.write(response.content)
    else:
        st.warning("Please enter a query.")
