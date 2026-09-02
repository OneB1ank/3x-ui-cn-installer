#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"
git restore --source 8effa60^ -- install-cn.sh x-ui-cn.sh scripts/translate-cn.py
echo "Restored files to pre-fix commit 8effa60^"
