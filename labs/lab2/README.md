# Lab 2: Fine-Tuning with LoRA and Reinforcement Learning with Verifiable Rewards

EECE.4860/5860 Introduction to Generative AI, UMass Lowell, Spring 2027

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/acanets/genai-labs/blob/spring27/labs/lab2/lab2.ipynb)

**Released:** Week 5 · **Due:** see Canvas (Sunday 11:59 pm ET) · **Lectures:** L05–L07 · **Work individually.**

## What you will do

| Part | Who | Topic | You implement |
|---|---|---|---|
| A | all students | LoRA fine-tuning of Qwen3-0.6B for dialogue summarization (DialogSum); ROUGE before and after | `to_prompt_completion`, `compute_rouge`, `expected_lora_params` |
| B | all students | Peak GPU memory and speed of LoRA vs. QLoRA (4-bit NF4 base model) on Qwen3-1.7B | the `BitsAndBytesConfig` |
| C | EECE.5860 only | GRPO with rule-based (verifiable) rewards on arithmetic problems | `format_reward`, `correctness_reward` |

Your LoRA rank depends on your student-ID digits, so your parameter counts will differ from your classmates'.

GPU time on a free Colab T4: about 15 minutes for Parts A–B and about 10 minutes for Part C. Part B needs a CUDA GPU.

## Getting started

1. Click **Open in Colab**, then *File > Save a copy in Drive*; select *Runtime > Change runtime type > T4 GPU*.
2. Enter your student-ID digits and section in the first code cell, and run the cells in order.
3. Watch for `[CHECK lab2.…] PASS/FAIL` lines; a `FAIL` shows the expected value.
4. Optional: set `OUT_DIR` to a folder in your Google Drive so your adapter survives a disconnect.

## Grading (15 points)

| Component | Points |
|---|---|
| Notebook runs top to bottom, outputs saved | 2 |
| Checks in Parts A–B | 8 |
| Report section (summary, problems and fixes, Q1–Q4, lessons learned) | 5 |
| *EECE.5860 only:* Part C checks (3) + Q5–Q6 (2) | +5, total scaled to 15 |

## Submit on Canvas

The notebook with all outputs (`.ipynb`) and a PDF of it (*File > Print > Save as PDF*). Keep the `[CHECK …]` and `GENAI-RESULTS` lines.

## References

* Hu et al., *LoRA: Low-Rank Adaptation of Large Language Models*, ICLR 2022. arXiv:2106.09685
* Dettmers et al., *QLoRA: Efficient Finetuning of Quantized LLMs*, NeurIPS 2023. arXiv:2305.14314
* Lin, *ROUGE: A Package for Automatic Evaluation of Summaries*, ACL Workshop 2004.
* Chen et al., *DialogSum: A Real-Life Scenario Dialogue Summarization Dataset*, Findings of ACL 2021. arXiv:2105.06762
* Shao et al., *DeepSeekMath* (introduces GRPO), 2024. arXiv:2402.03300
* DeepSeek-AI, *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning*, 2025. arXiv:2501.12948
