# Lab 4: Controlled Diffusion, CLIP, and LLM Watermarking

EECE.4860/5860 Introduction to Generative AI, UMass Lowell, Spring 2027

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/acanets/genai-labs/blob/spring27/labs/lab4/lab4.ipynb)

**Released:** Week 11 · **Due:** see Canvas (Thursday 4/29, 11:59 pm ET) · **Lectures:** L11–L13 · **Work individually.**

## What you will do

| Part | Who | Topic | You implement |
|---|---|---|---|
| A | all students | Stable Diffusion 1.5 with a ControlNet edge map: guidance scale × denoising steps sweep, conditioning scale, scored with your own CLIPScore | `clip_score` |
| B | all students | Zero-shot classification of CIFAR-10 images with CLIP; effect of prompt templates and ensembling | `zero_shot_predict` |
| C | EECE.5860 only | The green-list watermark for LLM text: generation, z-test detection, and a token-editing attack | `green_list`, the watermark `LogitsProcessor`, `z_score` |

Models:
* Stable Diffusion 1.5 (`stable-diffusion-v1-5/stable-diffusion-v1-5`) and ControlNet-Canny (`lllyasviel/sd-controlnet-canny`), both under OpenRAIL licenses; the safety checker stays on.
* CLIP ViT-B/32.
* Qwen3-0.6B.

Data: CIFAR-10 test images (Krizhevsky, 2009), used for teaching only.

GPU time on a free Colab T4: about 10 minutes for Part A, 3 for Part B, and 5 for Part C.

## Getting started

1. Click **Open in Colab**, then *File > Save a copy in Drive*; select *Runtime > Change runtime type > T4 GPU*.
2. Enter your student-ID digits and section in the first code cell; run the cells in order. Your digits pick your prompt and image subset.
3. Optional: in Part A you can upload your own photo (`MY_IMAGE`) instead of the drawn house.

## Grading (15 points)

| Component | Points |
|---|---|
| Notebook runs top to bottom, outputs saved | 2 |
| Checks in Parts A–B | 8 |
| Report section (summary, problems and fixes, Q1–Q4, lessons learned) | 5 |
| *EECE.5860 only:* Part C checks (3) + Q5–Q6 (2) | +5, total scaled to 15 |

No late submissions are accepted after Friday, April 30, 2027.

## Submit on Canvas

The notebook with all outputs (`.ipynb`) and a PDF of it (*File > Print > Save as PDF*). Keep the `[CHECK …]` and `GENAI-RESULTS` lines. Generated images must follow the model licenses and the course conduct policy.

## References

* Zhang, Rao & Agrawala, *Adding Conditional Control to Text-to-Image Diffusion Models* (ControlNet), ICCV 2023. arXiv:2302.05543
* Rombach et al., *High-Resolution Image Synthesis with Latent Diffusion Models*, CVPR 2022. arXiv:2112.10752
* Ho & Salimans, *Classifier-Free Diffusion Guidance*, 2022. arXiv:2207.12598
* Radford et al., *Learning Transferable Visual Models From Natural Language Supervision* (CLIP), ICML 2021. arXiv:2103.00020
* Hessel et al., *CLIPScore: A Reference-free Evaluation Metric for Image Captioning*, EMNLP 2021. arXiv:2104.08718
* Kirchenbauer et al., *A Watermark for Large Language Models*, ICML 2023. arXiv:2301.10226
