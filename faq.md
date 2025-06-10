# FAQ

1. **How to configure trainer to save checkpoints of the model?**

    The locations of the checkpoints depend on the `save_steps`(https://huggingface.co/docs/transformers/v4.49.0/en/main_classes/trainer#transformers.TrainingArguments.save_steps) and `output_dir` (https://huggingface.co/docs/transformers/v4.49.0/en/main_classes/trainer#transformers.TrainingArguments.save_steps) parameters that you have in your TrainingArguments. All the checkpoints will be stored in a directory with the name you set for `output_dir` and each checkpoint will be saved at the interval you configure in `save_steps`. For example, if you have `save_steps=500` and `output_dir='finetuned-model'`, the trainer will save a checkpoint of your model every 500 steps (so it will save checkpoints in: ./finetuned-model/checkpoint-500, ./finetuned-model/checkpoint-1000, ./finetuned-model/checkpoint-1500, ...).

2. **How do you resolve `ImportError: Using IPEX but IPEX is not installed or IPEX's version does not match current PyTorch, please refer to https://github.com/intel/intel-extension-for-pytorch.` when running trainer on PyTorch 2.6 kernel?**

    Remove the `use_ipex=True` training argument. This is no longer needed in PyTorch >= 2.6.

3. **How to resolve out of memory or insufficent resources errors when running trainer?**

    Make sure you are using memory reduction techniques such as LoRA or QLoRA. Try reducing your training and/or evaluation batch size. If you are only getting an OOM error right before/during the validation, you most likely did not set the `per_device_eval_batch_size` argument or set it too high (https://huggingface.co/docs/transformers/v4.49.0/en/main_classes/trainer#transformers.TrainingArguments.per_device_eval_batch_size).

4. **How do you resolve runtime errors when importing torch in the PyTorch 2.6 kernel?**

    The most common issue is installing a older version of torch/ipex in your local site-packages directory (~/.local/lib/python3.10/site-packages/). One simple solution to test if this is the problem clear your local site-packages and reinstall the dependencies for the notebook (make sure to reset your kernel after the dependencies are reinstalled).

    You can "clear" and create a backup of the site-packages at the same time by just renaming the old python3.10 directory to python3.10. Afterwards, when you install a new package it will see that `~/.local/lib/python3.10` and create it.

    ```
    mv ~/.local/lib/python3.10 ~/.local/lib/python3.10.bak
    ```

    If this does not solve the issue you can always restore your old site-packages by removing the new one and restoring the name of the old directory.

    ```
    rm -r ~/.local/lib/python3.10
    mv ~/.local/lib/python3.10.bak ~/.local/lib/python3.10
    ```
5. **Which notebooks do you launch to select either the PyTorch GPU kernel or the PyTorch 2.7 kernel?**

    Please refer to the [Get Started with JupyterLab](https://github.com/ACANETS/genai-labs/blob/main/StartHere.md#get-started-with-jupyterlab) section in the Start Here guide.






