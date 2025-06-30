# Running an LLM Chatbot Locally with Ollama

### What is Ollama?

Ollama (short for Omni-Layer Learning Language Acquisition Model) is a free and open source tool that can be used to run models locally on your own machine. It enables users to download and run pretrained models without relying on cloud-based services. It provides a user-friendly CLI for interacting with the models and also exposes a REST API for connecting the LLMs to external applications.

You can install Ollama using one of the following links:

* [Download Ollama for Windows](https://ollama.com/download/windows)
* [Download Ollama for Mac](https://ollama.com/download/mac)
* [Download Ollama for Linux](https://ollama.com/download/linux)

After installing Ollama on your local machine, try pulling Meta's Llama 3.2 model (or model of your choice):
```
ollama pull llama3.2:3b
```

To run the LLM that you just pulled interactively in the terminal, use Ollama's run command:
```
ollama run llama3.2:3b
```

### Description of Chatbot Application
This script uses Streamlit, LangChain, and a local LLM from Ollama to create a chatbot assistant. Streamlit is a Python framework for building custom web apps. You can create a functional user interface with very little code using Streamlit. Using LangChain along with Ollama, allows us to create a tool-calling agent that runs on our local machine. In this script, there are four tools that the agent can use: web search via DuckDuckGo, querying Wikipedia, querying StackExchange, and using RAG on a user-provided document (this is only enabled if the user uploads a document). One thing to keep in mind is that Streamlit automatically reruns the entire script every time the user interacts with the web interface. Because of this, any data not stored in the `st.session_state` dictionary will be lost between interactions. To preserve the chatbot's memory across prompts, we use LangGraph’s `MemorySaver` checkpoint object and store it in `st.session_state`.

### Running the Chatbot Application
Install script dependencies
```
python3 -m pip install langchain langchain-experimental langchain-community streamlit langchain-ollama langgraph duckduckgo-search langchain_huggingface pypdf stackapi wikipedia
```

Run the script using Streamlit
```
streamlit run app.py
```

After you run the Streamlit app, your default browser should open automatically to the web interface that you will use to interact with the chatbot. If it does not open automatically, you can click on any of the links that Streamlit writes to the terminal.

Now that you have access to the Streamlit web interface, you can now prompt the chatbot. The chatbot will use the tools mentioned above to assist it in answering your questions. You can also upload a PDF document (only one at a time), which will add a custom RAG tool to the agent. If you want to be sure the chatbot uses your PDF document to answer your prompt, you may have to explicitly instruct it to use the document in your prompt. For example, you could add this phrase at the end of your prompt: "Please use the user-provided document to answer the prompt."
