# Lab 1: LLM Inference, Decoding, and Structured Output

EECE.4860/5860 Introduction to Generative AI, UMass Lowell, Spring 2027

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/acanets/genai-labs/blob/spring27/labs/lab1/lab1.ipynb)

**Released:** Week 2 · **Due:** see Canvas (Sunday 11:59 pm ET) · **Lectures:** L02–L04 · **Work individually.**

## What you will do

| Part | Who | Topic | You implement |
|---|---|---|---|
| A | all students | Tokenizers; temperature and top-p; decoding diversity | `softmax_with_temperature`, `top_p_indices`, `distinct_n`, one text of your own |
| B | all students | JSON extraction with zero-shot, few-shot, and validate-and-retry prompting | `parse_and_validate`, the instruction and few-shot prompt, `few_shot_with_retry` |
| C | EECE.5860 only | Test-time compute: direct vs. chain-of-thought vs. thinking mode vs. self-consistency on GSM8K | `extract_answer`, `majority_vote` |

The models are Qwen3-0.6B and Qwen3-1.7B (Apache-2.0, no access request needed). Everything runs on a free Google Colab T4 GPU in about 15 minutes of GPU time (Parts A–B), plus about 10 minutes for Part C.

## Getting started

1. Click **Open in Colab** above, then *File > Save a copy in Drive*.
2. *Runtime > Change runtime type > T4 GPU*.
3. Enter the last 4 digits of your student ID and your section (`"4860"` or `"5860"`) in the first code cell. Your digits pick your personal prompt and problem set.
4. Run the cells in order. Cells marked `TODO` raise `NotImplementedError` until you complete them.
5. Each step prints a check line, for example `[CHECK lab1.A.top_p] PASS`. A `FAIL` line tells you what was expected. Fix the code and rerun that cell.

If Colab says no GPU is available, try again later or keep going on CPU (much slower). Start early: GPUs are scarcest on Sunday evenings.

## Grading (15 points)

| Component | Points | How it is graded |
|---|---|---|
| Runs top to bottom | 2 | Every code cell executed in order, outputs saved, no errors |
| Checks (Parts A–B) | 8 | The `[CHECK ...]` results in your saved notebook |
| Report | 5 | The *Report* section at the end of the notebook: summary, problems and fixes, answers to Q1–Q5, lessons learned |
| *EECE.5860 only:* Part C | +5 | 3 for the Part C checks, 2 for Q6–Q7. The 5860 total (20) is scaled to 15 |

If you cannot get the code working, you can still earn up to 5 points by describing what you tried in the report.

## Submit on Canvas

1. The notebook **with all outputs**: *File > Download > Download .ipynb*.
2. A PDF of the same notebook: *File > Print > Save as PDF*.

Do not delete or edit the `[CHECK ...]` or `GENAI-RESULTS` lines; the grader reads them. Late submissions follow the policy in the syllabus.

## References

* Holtzman et al., *The Curious Case of Neural Text Degeneration*, ICLR 2020 (top-p sampling). arXiv:1904.09751
* Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*, 2022. arXiv:2201.11903
* Wang et al., *Self-Consistency Improves Chain of Thought Reasoning in Language Models*, 2022. arXiv:2203.11171
* Cobbe et al., *Training Verifiers to Solve Math Word Problems* (GSM8K), 2021. arXiv:2110.14168
* Qwen Team, *Qwen3 Technical Report*, 2025. arXiv:2505.09388
