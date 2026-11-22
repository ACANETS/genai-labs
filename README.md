# genai-labs

Exercises and labs for **EECE.4860/5860 Introduction to Generative AI** at UMass Lowell (Spring 2027).
Everything runs in Google Colab on the free tier: click a badge, then *File > Save a copy in Drive*.

**Start here:** [Colab setup guide](setup/COLAB_QUICKSTART.md) · [FAQ](setup/FAQ.md)

- **Exercise:** a complete, runnable notebook that demonstrates one idea. Not graded; no code changes needed.
- **Lab:** a notebook with `TODO` steps you complete, built-in `[CHECK ...]` lines that tell you whether each step works, and a short report section. Graded; submit the `.ipynb` and a PDF on Canvas.

## Labs

| Lab | Topic | Weeks | Open |
|---|---|---|---|
| 1 | [LLM inference, decoding, and structured output](labs/lab1/README.md) | 2–5 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/acanets/genai-labs/blob/spring27/labs/lab1/lab1.ipynb) |
| 2 | [Fine-tuning (LoRA/QLoRA) and RL with verifiable rewards](labs/lab2/README.md) | 5–8 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/acanets/genai-labs/blob/spring27/labs/lab2/lab2.ipynb) |
| 3 | [Retrieval-augmented generation and a tool-calling agent](labs/lab3/README.md) | 8–11 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/acanets/genai-labs/blob/spring27/labs/lab3/lab3.ipynb) |
| 4 | [Controlled diffusion, CLIP, and LLM watermarking](labs/lab4/README.md) | 11–14 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/acanets/genai-labs/blob/spring27/labs/lab4/lab4.ipynb) |

## Exercises

| Ex | Topic | Open |
|---|---|---|
| 0 | Colab and GPU check | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/acanets/genai-labs/blob/spring27/exercises/ex0_colab_check.ipynb) |
| 1 | Handwritten digit recognition with PyTorch | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/acanets/genai-labs/blob/spring27/exercises/ex1_mnist.ipynb) |
| 2 | Hugging Face basics: tokenizers, pipelines, chat templates | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/acanets/genai-labs/blob/spring27/exercises/ex2_hf_basics.ipynb) |
| 3 | Attention from scratch and a tiny GPT | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/acanets/genai-labs/blob/spring27/exercises/ex3_attention_tiny_gpt.ipynb) |
| 4 | Efficient inference: quantization, KV cache, speculative decoding | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/acanets/genai-labs/blob/spring27/exercises/ex4_efficient_inference.ipynb) |
| 5 | Simple RAG | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/acanets/genai-labs/blob/spring27/exercises/ex5_simple_rag.ipynb) |
| 6 | Text-to-image and image-to-image | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/acanets/genai-labs/blob/spring27/exercises/ex6_text_to_image.ipynb) |
| 7 | Toxicity classifiers and guard models | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/acanets/genai-labs/blob/spring27/exercises/ex7_toxicity.ipynb) |

## Course helper package

Notebooks install [`genai_utils`](genai_utils/) automatically: `pip install "git+https://github.com/acanets/genai-labs@spring27"`.
