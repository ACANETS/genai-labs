# Lab 3: Retrieval-Augmented Generation and a Tool-Using Agent

EECE.4860/5860 Introduction to Generative AI, UMass Lowell, Spring 2027

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/acanets/genai-labs/blob/spring27/labs/lab3/lab3.ipynb)

**Released:** Week 8 · **Due:** see Canvas (Sunday 11:59 pm ET) · **Lectures:** L09–L10 · **Work individually.**

## What you will do

| Part | Who | Topic | You implement |
|---|---|---|---|
| A | all students | Chunking; dense vs. BM25 vs. hybrid (reciprocal rank fusion) vs. reranked retrieval, measured with recall@k and MRR on 32 labeled questions; answers with citations | `chunk_text`, `recall_at_k`, `reciprocal_rank`, `rrf_fuse` |
| B | EECE.5860 only | A tool-calling agent loop without a framework (search, calculator, course calendar); its success rate on 10 tasks; an indirect prompt-injection test and a mitigation | `run_agent`, `wrap` |

**Data** (`data/`):
* `corpus.jsonl`: the abstracts of 75 papers from the course reading list (arXiv metadata, CC0), two course documents, and **one synthetic document planted for the prompt-injection exercise**. It is labeled as synthetic in its `source` field.
* `retrieval_questions.jsonl`: 32 questions with the ids of their relevant documents.
* `agent_tasks.jsonl`: 10 agent tasks with expected answers.

Models: all-MiniLM-L6-v2 (embeddings), ms-marco-MiniLM-L6-v2 (reranker), and Qwen3-1.7B (generation and agent), all Apache-2.0. GPU time on a free Colab T4: about 10 minutes per part.

## Getting started

1. Click **Open in Colab**, then *File > Save a copy in Drive*; select *Runtime > Change runtime type > T4 GPU*.
2. Enter your student-ID digits and section in the first code cell; run the cells in order.
3. Each step prints a `[CHECK lab3.…] PASS/FAIL` line.

## Grading (15 points)

| Component | Points |
|---|---|
| Notebook runs top to bottom, outputs saved | 2 |
| Checks in Part A | 8 |
| Report section (summary, problems and fixes, Q1–Q4, lessons learned) | 5 |
| *EECE.5860 only:* Part B checks (3) + Q5–Q6 (2) | +5, total scaled to 15 |

## Submit on Canvas

The notebook with all outputs (`.ipynb`) and a PDF of it (*File > Print > Save as PDF*). Keep the `[CHECK …]` and `GENAI-RESULTS` lines.

## References

* Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*, NeurIPS 2020. arXiv:2005.11401
* Reimers & Gurevych, *Sentence-BERT*, EMNLP 2019. arXiv:1908.10084
* Robertson & Zaragoza, *The Probabilistic Relevance Framework: BM25 and Beyond*, Foundations and Trends in IR, 2009.
* Cormack, Clarke & Buettcher, *Reciprocal Rank Fusion Outperforms Condorcet and Individual Rank Learning Methods*, SIGIR 2009. doi:10.1145/1571941.1572114
* Yao et al., *ReAct: Synergizing Reasoning and Acting in Language Models*, ICLR 2023. arXiv:2210.03629
* Greshake et al., *Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection*, 2023. arXiv:2302.12173
* Debenedetti et al., *Defeating Prompt Injections by Design* (CaMeL), 2025. arXiv:2503.18813
