# FAQ

1. **How to configure trainer to save checkpoints of the model?**

    The locations of the checkpoints depend on the `save_steps`(https://huggingface.co/docs/transformers/v4.49.0/en/main_classes/trainer#transformers.TrainingArguments.save_steps) and `output_dir` (https://huggingface.co/docs/transformers/v4.49.0/en/main_classes/trainer#transformers.TrainingArguments.save_steps) parameters that you have in your TrainingArguments. All the checkpoints will be stored in a directory with the name you set for `output_dir` and each checkpoint will be saved at the interval you configure in `save_steps`. For example, if you have `save_steps=500` and `output_dir='finetuned-model'`, the trainer will save a checkpoint of your model every 500 steps (so it will save checkpoints in: ./finetuned-model/checkpoint-500, ./finetuned-model/checkpoint-1000, ./finetuned-model/checkpoint-1500, ...).

2. **How to resolve out of memory or insufficent resources errors when running trainer?**

    Make sure you are using memory reduction techniques such as LoRA or QLoRA. Try reducing your training and/or evaluation batch size. If you are only getting an OOM error right before/during the validation, you most likely did not set the `per_device_eval_batch_size` argument or set it too high (https://huggingface.co/docs/transformers/v4.49.0/en/main_classes/trainer#transformers.TrainingArguments.per_device_eval_batch_size).
