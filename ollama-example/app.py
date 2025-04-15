# @title Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# EECE.4860/5860 Intro to GenAI at UMass Lowell  
# 
# Ollama example with LangChain toolchain
# 
# Author: Sage Lyon
# Date: April 10, 2025

from langchain_community.document_loaders import PyPDFLoader
from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.indexes import VectorstoreIndexCreator
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
import streamlit as st
from typing import Annotated
import tempfile

# Tools
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_community.tools import DuckDuckGoSearchResults
tools = load_tools(["stackexchange", "ddg-search", "wikipedia"])
search_results = DuckDuckGoSearchResults(output_format="list", verbose=True)
tools.append(search_results)

# Ollama LLM, Embedding, and Memory for agent
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langgraph.checkpoint.memory import MemorySaver

llm = ChatOllama(model="llama3.2:3b", temperature=0.1, num_predict=256)

# Retain memory checkpoint through session
if 'memory' not in st.session_state:
    st.session_state['memory'] = MemorySaver()

st.title("Local Tool-Calling Ollama Agent")
st.write("If you are asking a question related to a document that you uploaded, it is helpful to specify that in your prompt")

uploaded_file = st.file_uploader("Upload your PDF file here", type="pdf")

if uploaded_file:
    with tempfile.NamedTemporaryFile(mode="wb+", delete=True) as temp_file:
        temp_file.write(uploaded_file.getvalue())
        temp_file.seek(0)

        loader = PyPDFLoader(temp_file.name)
        docs = loader.load()

        chunk_size = 1000
        overlap = 50
        top_k=1
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
        splits = text_splitter.split_documents(docs)

        index = VectorstoreIndexCreator(
            embedding=HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-large-instruct"),
            text_splitter=text_splitter
        ).from_loaders([loader])

    @tool
    def query_documents(input: Annotated[str, "Query"]) -> str:
        """Provides context on user questions from documents they provided."""

        print(f"Received input query: {input}\n")

        results = index.vectorstore.similarity_search(input, k=top_k)

        if not results:
            print("No results found for the query.\n\n")

        results = index.vectorstore.similarity_search(input, k=top_k)
        context = "\n".join([document.page_content for document in results])

        if context:
            print(f"Context found:\n{context}\n\n")

        return context

    tools.append(query_documents)


config = {"configurable": {"thread_id": "1"}}
langgraph_agent_executor = create_react_agent(llm, tools, checkpointer=st.session_state['memory'])

user_input = st.text_input("Ask a question:")

if user_input:
    messages = langgraph_agent_executor.invoke({"messages": [("human", user_input)]}, config=config)
    response = messages["messages"][-1].content
    st.write("**Response:**")
    st.write(response)

