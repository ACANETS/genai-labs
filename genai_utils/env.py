"""Environment checks for Google Colab (T4 GPU) and local machines."""
from __future__ import annotations

import contextlib
import os
import platform
import random
import time


def seed_everything(seed: int = 0) -> None:
    """Seed Python, NumPy and PyTorch so runs are repeatable."""
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    try:
        import numpy as np

        np.random.seed(seed)
    except ImportError:
        pass
    try:
        import torch

        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
    except ImportError:
        pass


def setup_env(seed: int = 0, need_gpu: bool = True, quiet: bool = False):
    """Print the runtime, seed everything, and return ``(device, dtype)``.

    * CUDA GPU (Colab T4): ``("cuda", torch.float16)``; bf16-capable GPUs get ``torch.bfloat16``.
    * Apple silicon: ``("mps", torch.float32)``.  * CPU: ``("cpu", torch.float32)``.
    """
    import torch

    seed_everything(seed)
    if torch.cuda.is_available():
        device = "cuda"
        dtype = torch.bfloat16 if torch.cuda.is_bf16_supported(including_emulation=False) else torch.float16
        props = torch.cuda.get_device_properties(0)
        hw = f"{props.name}, {props.total_memory / 2**30:.1f} GiB, compute capability {props.major}.{props.minor}"
    elif getattr(torch.backends, "mps", None) and torch.backends.mps.is_available():
        device, dtype, hw = "mps", torch.float32, "Apple GPU (MPS)"
    else:
        device, dtype, hw = "cpu", torch.float32, platform.processor() or "CPU"
    if not quiet:
        try:
            import transformers

            tf = transformers.__version__
        except ImportError:
            tf = "not installed"
        print(f"Python {platform.python_version()} | torch {torch.__version__} | transformers {tf}")
        print(f"Device: {device} ({hw}) | default dtype for models: {str(dtype).replace('torch.', '')} | seed {seed}")
    if need_gpu and device != "cuda":
        print(
            "WARNING: no CUDA GPU found. In Colab choose Runtime > Change runtime type > T4 GPU, then rerun.\n"
            "If Colab has no GPU available right now, you can keep going on CPU with the smaller settings "
            "noted in the notebook (slower), or try again later."
        )
    return device, dtype


@contextlib.contextmanager
def measure(label: str = "", results: dict | None = None):
    """Time a block and report peak GPU memory (CUDA only).

    Example::

        stats = {}
        with measure("generate", stats):
            out = model.generate(**inputs)
        # stats == {"seconds": 3.1, "peak_mem_gb": 2.4}   (peak_mem_gb is None without CUDA)
    """
    try:
        import torch

        cuda = torch.cuda.is_available()
    except ImportError:
        cuda = False
    if cuda:
        torch.cuda.synchronize()
        torch.cuda.reset_peak_memory_stats()
    t0 = time.perf_counter()
    yield
    if cuda:
        torch.cuda.synchronize()
    secs = time.perf_counter() - t0
    peak = torch.cuda.max_memory_allocated() / 2**30 if cuda else float("nan")
    if results is not None:
        results.update(seconds=round(secs, 2), peak_mem_gb=round(peak, 3) if cuda else None)
    print(f"[{label or 'block'}] {secs:.1f} s" + (f", peak GPU memory {peak:.2f} GiB" if cuda else ""))
