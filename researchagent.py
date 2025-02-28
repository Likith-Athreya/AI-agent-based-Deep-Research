import os
from typing import Dict, Any
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.tools import Tool
from langchain.agents import AgentExecutor, initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain.llms import HuggingFacePipeline
from transformers import pipeline
from tavily import TavilyClient
from tenacity import retry, stop_after_attempt, wait_exponential

tavily_api_key = "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"  

try:
    tavily_client = TavilyClient(api_key=tavily_api_key)
    print("[INFO] Tavily client initialized successfully.")
except Exception as e:
    print("[ERROR] Failed to initialize Tavily client:", str(e))
    raise ValueError("Invalid Tavily API key. Please check your key and try again.")

try:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    print("[INFO] Summarization model loaded successfully.")
except Exception as e:
    print("[ERROR] Failed to load summarization model:", str(e))
    raise e

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def search_with_retry(query: str) -> Dict[str, Any]:
    print("[Research Agent] Searching for:", query)
    try:
        results = tavily_client.search(query=query, max_results=5)
        return results
    except Exception as e:
        print("[Error] Tavily search failed:", str(e))
        return {"error": "Search failed."}

def format_search_results(results: Dict[str, Any]) -> str:
    if not results or "results" not in results or not results["results"]:
        return "No search results found."

    formatted_results = []
    for result in results["results"]:
        title = result.get("title", "No title")
        url = result.get("url", "No URL")
        content = result.get("content", "No content")
        # Only include results with meaningful content and related to AI safety research
        if content != "No content" and len(content) > 50 and "safety" in content.lower():
            formatted_results.append(f"Title: {title}\nURL: {url}\nContent: {content}\n")

    return "\n".join(formatted_results)

def tavily_search_tool(query: str) -> str:
    results = search_with_retry(query)
    formatted_results = format_search_results(results)
    return formatted_results

def summarization_tool(text: str) -> str:
    try:
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        return summary[0]["summary_text"]
    except Exception as e:
        print("[Error] Summarization failed:", str(e))
        return "Failed to generate response."

tools = [
    Tool(
        name="Tavily Search",
        func=tavily_search_tool,
        description="Useful for searching the web for relevant information."
    ),
    Tool(
        name="Summarization",
        func=summarization_tool,
        description="Useful for summarizing long texts into concise responses."
    )
]

memory = ConversationBufferMemory(memory_key="chat_history")

llm = HuggingFacePipeline(pipeline=summarizer)

agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",  # Use a simple agent for this example
    memory=memory,
    verbose=True
)

def main_workflow(query: str) -> str:
    search_results = tavily_search_tool(query)
    if search_results == "No search results found.":
        return "No relevant information found."

    summary = summarization_tool(search_results)
    return summary

if __name__ == "__main__":
    user_query = "Latest advancements in AI safety research alignment robustness ethics"
    response = main_workflow(user_query)
    print("\n[Final Response]\n", response)