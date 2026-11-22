# FAQ

**Colab says "Cannot connect to GPU backend" or "You cannot currently connect to a GPU due to usage limits."**
The free tier gives GPUs only when they are available and within a weekly allowance. Try again in a few hours, and start labs early. You can still run CPU-only cells (tokenizers, the functions you implement, report writing) in the meantime.

**`CUDA out of memory`.**
*Runtime > Restart session*, then rerun from the top; models left over from earlier cells keep using memory. In training cells, lower `per_device_train_batch_size` (and raise `gradient_accumulation_steps` to keep the same effective batch). Lower `per_device_eval_batch_size` too if the error appears during evaluation.

**My session disconnected and my files are gone.**
Colab's disk is temporary. Your notebook itself is saved in Drive if you made a copy (*File > Save a copy in Drive*). Labs that train models show how to save checkpoints to Drive (`from google.colab import drive; drive.mount('/content/drive')`).

**A `[CHECK ...]` line says FAIL.**
Read the message after it: it shows the expected value or the first failing test case. Fix your code and rerun that cell; the latest result is what counts. Rerun the *Results summary* cell at the end before you submit.

**Can I run the labs on my own computer?**
Yes, if you have an NVIDIA GPU with at least 12 GB of memory, or you are patient on CPU or Apple silicon. Install Python 3.11+, `torch`, `transformers`, `datasets`, and the course helper (`pip install "git+https://github.com/acanets/genai-labs@spring27"`). Submissions are graded the same way.

**How do I save a trainer checkpoint?**
Checkpoints are written to `output_dir` every `save_steps` steps (for example `output_dir="ckpt", save_steps=100` writes `ckpt/checkpoint-100`, `ckpt/checkpoint-200`, and so on). Point `output_dir` to a folder in your mounted Google Drive to keep them.
