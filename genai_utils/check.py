"""Checkpoints that tell you (and the grader) whether each lab step worked.

Every check prints one line such as::

    [CHECK lab1.A.top_p] PASS value=3

and ``Checker.summary()`` prints a one-line JSON record that starts with
``GENAI-RESULTS``. Keep these outputs in the notebook you submit: the grading
script reads them from the saved ``.ipynb``. Do not edit them by hand.
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import math
from typing import Any, Callable

TERM_SALT = "spring27"


def variant(student_last4: str, n: int, salt: str = TERM_SALT) -> int:
    """Map the last 4 digits of a student ID to a variant number in ``range(n)``.

    Deterministic, so the grader can recompute it.
    """
    s = str(student_last4).strip()
    if not (len(s) == 4 and s.isdigit()):
        raise ValueError("Set STUDENT_ID_LAST4 to the last 4 digits of your student ID, e.g. '0427'.")
    return int(hashlib.sha256(f"{salt}-{s}".encode()).hexdigest(), 16) % n


def _short(v: Any) -> str:
    if isinstance(v, float):
        return f"{v:.4g}"
    s = repr(v)
    return s if len(s) <= 60 else s[:57] + "..."


def _jsonable(v: Any) -> Any:
    try:
        json.dumps(v)
        return v
    except TypeError:
        if hasattr(v, "item"):
            return v.item()
        return repr(v)


class Checker:
    """Collects PASS/FAIL checks and metrics for one lab.

    >>> ck = Checker("lab0", student_last4="1234", section="4860")
    >>> ck.expect_true("A.demo", 1 + 1 == 2, value=2)
    [CHECK lab0.A.demo] PASS value=2
    True
    """

    def __init__(self, lab: str, student_last4: str, section: str = "4860"):
        section = str(section).strip()
        if section not in ("4860", "5860"):
            raise ValueError("SECTION must be '4860' or '5860'.")
        self.lab = lab
        self.student = str(student_last4).strip()
        variant(self.student, 2)  # validates the ID format
        self.section = section
        self.checks: dict[str, dict] = {}
        self.metrics: dict[str, Any] = {}

    # ---- checks -------------------------------------------------------
    def _log(self, name: str, ok: bool, value: Any = None, note: str = "") -> bool:
        self.checks[name] = {"pass": bool(ok), "value": _jsonable(value), "note": note}
        tag = "PASS" if ok else "FAIL"
        extra = f" value={_short(value)}" if value is not None else ""
        extra += f"  ({note})" if note and not ok else ""
        print(f"[CHECK {self.lab}.{name}] {tag}{extra}")
        return bool(ok)

    def expect_true(self, name: str, condition: bool, value: Any = None, note: str = "") -> bool:
        return self._log(name, bool(condition), value, note)

    def expect_close(self, name: str, actual: float, expected: float, tol: float = 1e-4) -> bool:
        try:
            ok = math.isclose(float(actual), float(expected), rel_tol=tol, abs_tol=tol)
        except (TypeError, ValueError):
            ok = False
        return self._log(name, ok, actual, f"expected {expected} ± {tol}")

    def expect_range(self, name: str, value: float, lo: float, hi: float) -> bool:
        try:
            ok = lo <= float(value) <= hi
        except (TypeError, ValueError):
            ok = False
        return self._log(name, ok, value, f"expected between {lo} and {hi}")

    def expect_fn(self, name: str, fn: Callable, cases: list[tuple[tuple, Any]], tol: float | None = None) -> bool:
        """Run ``fn(*args)`` on test cases and compare with expected outputs."""
        failed = []
        for args, want in cases:
            try:
                got = fn(*args)
                if tol is not None:
                    ok = all(math.isclose(g, w, rel_tol=tol, abs_tol=tol) for g, w in zip(_flat(got), _flat(want)))
                    ok = ok and len(_flat(got)) == len(_flat(want))
                else:
                    ok = got == want
            except Exception as e:  # noqa: BLE001 - report any student error as a failed case
                got, ok = f"{type(e).__name__}: {e}", False
            if not ok:
                failed.append(f"{args!r} -> {got!r}, expected {want!r}")
        return self._log(name, not failed, f"{len(cases) - len(failed)}/{len(cases)} cases", "; ".join(failed[:2]))

    def record(self, name: str, value: Any) -> None:
        """Store a metric without pass/fail (for your report table)."""
        self.metrics[name] = _jsonable(value)

    # ---- summary ------------------------------------------------------
    def summary(self, path: str | None = None) -> dict:
        try:
            import torch

            gpu = torch.cuda.get_device_name(0) if torch.cuda.is_available() else "none"
        except ImportError:
            gpu = "unknown"
        rec = {
            "lab": self.lab,
            "student": self.student,
            "section": self.section,
            "checks": self.checks,
            "metrics": self.metrics,
            "gpu": gpu,
            "utc": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        }
        n_pass = sum(c["pass"] for c in self.checks.values())
        print(f"\n{self.lab}: {n_pass}/{len(self.checks)} checks passed")
        for k, c in self.checks.items():
            print(f"  {'PASS' if c['pass'] else 'FAIL'}  {k}")
        if self.metrics:
            print("Metrics:")
            for k, v in self.metrics.items():
                print(f"  {k}: {_short(v)}")
        print("GENAI-RESULTS " + json.dumps(rec, sort_keys=True))
        with open(path or f"results_{self.lab}.json", "w") as f:
            json.dump(rec, f, indent=2, sort_keys=True)
        return rec


def _flat(x: Any) -> list:
    if isinstance(x, (list, tuple)):
        out = []
        for y in x:
            out.extend(_flat(y))
        return out
    return [x]
