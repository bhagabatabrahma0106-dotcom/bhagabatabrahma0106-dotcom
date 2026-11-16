#!/usr/bin/env python3
"""Compatibility entrypoint for current and legacy profile validation calls."""
from validate_premium import run

if __name__ == "__main__":
    problems = run()
    if problems:
        for item in problems:
            print("FAIL:", item)
        raise SystemExit(1)
    print("Premium GitHub profile QA passed.")
