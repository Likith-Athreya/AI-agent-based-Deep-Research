# AI-agent-based-Deep-Research

Welcome to the **AI-agent-based-Deep-Research** This project is a smart, dual-agent system designed to help you gather and summarize information from the web effortlessly. Whether you're researching the latest advancements in AI or exploring any topic, this system has got you covered.

# What Does It Do?

This system combines the power of **Tavily** for web research, **LangGraph** for workflow management, and **LangChain** for modularity and memory. Here's how it works:

1. **Research Agent**: Crawls the web using Tavily to find the most relevant information based on your query.
2. **Answer Drafting Agent**: Summarizes the gathered data into a concise and structured response using a fine-tuned language model.

The result? A **high-quality summary** that saves you time and effort!

# Features

- **Web Crawling**: Uses Tavily to search and retrieve information from the web.
- **Dual-Agent System**: 
  - **Research Agent**: Handles data collection.
  - **Answer Drafting Agent**: Generates summaries.
- **LangChain Integration**: Modular and extensible design with tools and memory management.
- **Summarization**: Powered by Hugging Face's `facebook/bart-large-cnn` model for concise and accurate summaries.

# How to Set It Up

Getting started is easy! Follow these steps:

1. Clone the Repository
First, clone this repository to your local machine. Open your terminal and run:
bash

git clone https://github.com/your-username/AI-agent-based-Deep-Research.git

3. Install Dependencies
Make sure you have Python installed. Then, navigate to the project directory and install the required dependencies:

bash

cd AI-agent-based-Deep-Research
pip install -r requirements.txt

3. Set Up Your Environment
You'll need a Tavily API key to use the web search functionality.

4. Run the System
Once everything is set up, you can run the system with your query. For example:

bash

python researchagent.py

The system will ask for a query (e.g., "Latest advancements in AI safety research") and generate a summary based on the search results.

Example Output
Here’s what the system can do:

Input Query:

Latest advancements in AI safety research alignment robustness ethics
Output:
[Final Response]
This paper reviews four primary methodologies for evaluating alignment in Large Language Models (LLMs): human feedback, adversarial testing by domain experts, AI red teaming, and the constitutional approach to AI safety. It involves setting up systems to evaluate model behavior against human values consistently.
How It Works
Research Agent
The Research Agent uses Tavily to search the web for relevant information.

It filters and formats the search results to ensure only meaningful data is passed to the next step.

Answer Drafting Agent
The Answer Drafting Agent uses a fine-tuned language model (facebook/bart-large-cnn) to summarize the search results.

The result is a concise and well-structured response.

LangChain Integration
Tools: The system uses LangChain's Tool abstraction to define reusable components (e.g., Tavily search, summarization).

Memory: LangChain's ConversationBufferMemory stores conversation history for context-aware responses.

Agents: A simple agent manages the interaction between tools and chains.

Future Enhancements
This project is just the beginning! Here are some ideas for future improvements:

Validation Agent: Add a step to validate the accuracy and relevance of the summary.

Advanced Models: Integrate GPT-4 or other advanced models for better summarization.

User Interface: Build a web or CLI interface for easier interaction.

Multi-Turn Conversations: Enable the system to handle follow-up questions and iterative refinement.

Why I Built This
I created this project to explore the potential of AI-powered research tools. As someone passionate about AI and its applications, I wanted to build a system that could simplify the process of gathering and summarizing information. This project combines my love for coding, problem-solving, and AI into one neat package!

Acknowledgments
Tavily: For providing an excellent web search API.

Hugging Face: For the amazing facebook/bart-large-cnn model.

LangChain: For making it easy to build modular and extensible AI systems.
Please contact incase of any confusions.
Thank you for checking out my project! I hope you find it as exciting as I do.
