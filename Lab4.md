# Lab 4 - EECE.4860/5860 at UMass Lowell - Spring 2025

In this lab, you will practice controlling generative models for image generation (via ControlNet) and deploy a local chatbot app using Ollama. You will explore how structural cues and external tools can steer the generation process. The goal is to better understand the mechanisms and practical applications of controlled generation using both visual and textual modalities. Local deployment of LLM enables users to download and run pretrained models without relying on cloud-based services. You will run Jupyter notebooks on Intel Tiber AI cloud. 

## **Note** There are two parts in this lab. Parts 1 is for all the students. Part 2 is an additional requirement intended for EECE.5860 students only. There are some questions for each part, and you need to answer them in your lab report.

## Part 1:   Controlled Generation (10 points)

You will use the ControlNet_PythonCodeTutorial.ipynb notebook to explore ControlNet, a conditioning system that guides image generation using structures like edge maps, poses, or depth information. Run the notebook with different control types (e.g., Canny, Depth, Pose). **Try to change the prompts to see how results are different**. Summarize how the control input influenced the generation results.

Your part 1 of the lab will be graded as follows:

* Controlled image generation results and screenshots (4 points)
* Parameter/prompt exploration and observations (3 points)
* Written answers to included questions (3 points)

### Questions: 

1) Why is it necessary to use a pretrained pose detector like `OpenposeDetector` to preprocess the conditioning input, and what format does this model output to make it compatible with the ControlNet pipeline?
2) How does integrating a specific ControlNet model into the `StableDiffusionControlNetPipeline` alter the generative process compared to using vanilla Stable Diffusion, and what are the technical implications of specifying `torch_dtype=torch.float16` and targeting the `xpu` device?
3) What is the role of the `image` argument in conjunction with the `prompt` for `pipe()`, and how does ControlNet internally combine these two conditioning signals during inference to produce a coherent output?

## Part 2: Local LLM Chatbot App using Ollama and LangChain (10 points)

In this part, you will create and run a local chatbot app powered by a model from Ollama. The chatbot uses Streamlit for the UI and LangChain with tool-calling support, running entirely on your own machine. The step-by-step instruction can be found in [README.md](ollama-example/README.md). The Python application is given in [app.py](ollama-example/app.py)

Your Part 2 of the lab will be graded as follows:
* Proper installation and chatbot running (3 points)
* Demonstration of tool usage and screenshots (4 points)
* Observations and answers to reflection questions (3 points)

### Questions: 

1) Streamlit reruns the script on every user interaction. How does storing objects like the `MemorySaver` checkpoint in `st.session_state` preserve chatbot memory across user prompts, and what potential pitfalls might arise if this step is skipped or incorrectly implemented?
2) How does LangChain abstract the use of external APIs into tools, and how might you extend this setup to incorporate a new tool (e.g., querying arXiv or GitHub repositories)?
3) Ollama allows running large language models locally through a REST API. What are the advantages and trade-offs of running an LLM locally with Ollama compared to using cloud-hosted models, particularly in terms of latency, privacy, resource usage, and scalability?


# Lab submission 

You need to follow the lab report guidelines (on blackboard) for report writing. Submit your lab report on Blackboard by the posted deadline.

You will need to manage your source code on github.com under your own private repository. Do not copy/paste complete source code in your lab report. Instead include in the report a link to your github repo.

