#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
CSPELL_CONFIG="$ROOT_DIR/cspell.json"

if [[ ! -f "$CSPELL_CONFIG" ]]; then
  echo "cspell.json não encontrado em $ROOT_DIR" >&2
  exit 1
fi

TMP="$(mktemp)"
trap 'rm -f "$TMP"' EXIT

# Executa cspell e captura somente as palavras marcadas (uma por linha)
npx -y cspell --config "$CSPELL_CONFIG" --no-progress --no-summary --words-only "${@:-.}" | sort -u > "$TMP"

if [[ ! -s "$TMP" ]]; then
  echo "Nenhuma palavra nova detectada pelo cspell."
  exit 0
fi

updated=false

while IFS= read -r word; do
  if grep -qF "\"$word\"" "$CSPELL_CONFIG"; then
    continue
  fi
  # Insere a palavra dentro da lista `words`
  python - <<PY
from pathlib import Path
import json

config_path = Path("$CSPELL_CONFIG")
data = json.loads(config_path.read_text())
words = set(data.get("words", []))
words.add("$word")
data["words"] = sorted(words)
config_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
PY
  updated=true
done < "$TMP"

if [[ "$updated" == true ]]; then
  echo "cspell.json atualizado."
else
  echo "Todas as palavras já estavam presentes."
fi
