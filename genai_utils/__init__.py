"""Small helpers shared by the EECE.4860/5860 Generative AI labs and exercises.

    from genai_utils import setup_env, Checker, variant, measure
"""
from .env import measure, seed_everything, setup_env
from .check import Checker, variant

__all__ = ["setup_env", "seed_everything", "measure", "Checker", "variant"]
__version__ = "2027.1.0"
