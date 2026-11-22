# Lab setup: Google Colab

All exercises and labs in EECE.4860/5860 run in **Google Colab** on the free tier. You need:

1. **A Google account** (a personal Gmail account works; Colab runs in your browser).
2. **A free Hugging Face account** ([huggingface.co/join](https://huggingface.co/join)). The course models don't require one, but a token makes downloads more reliable (step 4).

GitHub is optional. You submit your work on Canvas.

## 1. Open a notebook

Every notebook in this repository has an **Open in Colab** badge. Click it, then choose *File > Save a copy in Drive*. Changes you make to the original are not saved, so always work in your copy.

## 2. Turn on the GPU

*Runtime > Change runtime type > Hardware accelerator: T4 GPU > Save.* Then run the first code cell. It prints the device it found, for example `Device: cuda (Tesla T4, 14.7 GiB, compute capability 7.5)`.

What the free tier gives you (Google does not publish exact limits, and they change):
* an NVIDIA **T4** GPU with about 15 GB of memory, **when one is available**;
* sessions of up to about 12 hours, which disconnect after roughly 90 minutes without activity;
* a weekly GPU allowance that varies. If you see "cannot connect to GPU backend", wait a few hours.

How to work with these limits:
* **Start early.** GPUs are hardest to get on Sunday evenings before deadlines.
* Each lab says how many GPU minutes it needs; most parts need well under an hour.
* Disconnect when you are done (*Runtime > Disconnect and delete runtime*), so your allowance isn't wasted.
* Files you create in Colab disappear when the session ends. Labs that train models tell you how to save checkpoints to Google Drive.
* The course notebooks choose the number format for you (`float16` on a T4). If you write your own code, use `setup_env()`'s returned `dtype` rather than hard-coding `bfloat16`.

## 3. Install the course helper

The first code cell of each notebook installs the course helper package automatically:

```python
%pip install -q "git+https://github.com/acanets/genai-labs@spring27"
```

It provides `setup_env()` (device check and seeding), `Checker` (the `[CHECK ...]` lines), `variant()`, and `measure()` (time and GPU memory).

## 4. (Recommended) Add your Hugging Face token

1. On Hugging Face: *Settings > Access Tokens > Create new token* (type **Read**).
2. In Colab: click the key icon (*Secrets*) in the left sidebar, add a secret named `HF_TOKEN` with your token, and turn on *Notebook access*.

The Hugging Face libraries pick up `HF_TOKEN` automatically. Never paste a token into a notebook cell you submit.

## 5. Submitting

For each lab, upload two files to Canvas:
1. the notebook with all outputs (*File > Download > Download .ipynb*);
2. a PDF of it (*File > Print > Save as PDF*).

Keep the `[CHECK ...]` and `GENAI-RESULTS` lines in your outputs; they are part of your grade.

## Troubleshooting

See [FAQ.md](FAQ.md). If you're still stuck, post on the Canvas discussion board (no full solutions, please) or bring it to the weekly chat.
