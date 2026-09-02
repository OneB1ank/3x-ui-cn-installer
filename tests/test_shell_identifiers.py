#!/usr/bin/env python3
"""Regression checks for translated shell identifiers."""

import importlib.util
import re
from pathlib import Path


spec = importlib.util.spec_from_file_location("translate_cn", Path(__file__).parents[1] / "scripts/translate-cn.py")
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


def test_parameter_expansion_is_preserved() -> None:
    translated = module.translate_text('WebPort="${WebPort:-80}" Port:')
    assert '${WebPort:-80}' in translated
    assert 'Web端口：-80' not in translated
    assert '端口：' in translated


def test_generated_scripts_have_ascii_parameter_names() -> None:
    expansion = re.compile(r"\$\{[^}\n]*\}")
    for name in ("install-cn.sh", "x-ui-cn.sh"):
        text = (Path(__file__).parents[1] / name).read_text(encoding="utf-8")
        for match in expansion.finditer(text):
            assert all(ord(char) < 128 for char in match.group(0)), match.group(0)


if __name__ == "__main__":
    test_parameter_expansion_is_preserved()
    test_generated_scripts_have_ascii_parameter_names()
    print("pass")
