#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TASKS_DIR="$ROOT/.tasks"
RULE="$ROOT/.cursor/rules/00_execution-protocol.mdc"
TPL="$ROOT/templates/task_file_template.md"

mkdir -p "$TASKS_DIR"

DATE_STR="$(date +'%Y-%m-%d')"
TIME_STR="$(date +'%H:%M:%S')"
DT_STR="$(date +'%Y-%m-%d_%H:%M:%S')"
USER_NAME="$(whoami)"
MAIN_BRANCH="${MAIN_BRANCH:-main}"
AUTO_RUN="${AUTO_RUN:-on}"
TASK_IDENT="${TASK_IDENT:-base-learning}"
COUNT="$(find "$TASKS_DIR" -maxdepth 1 -name "${DATE_STR}_*" | wc -l | tr -d ' ')"
SEQ="$((COUNT + 1))"
TASK_FILE_NAME="${DATE_STR}_${SEQ}"
TASK_BRANCH="task/${TASK_IDENT}_${DATE_STR}_${SEQ}"
OUT_FILE="$TASKS_DIR/${TASK_FILE_NAME}_${TASK_IDENT}.md"

# Extract the Execution Protocol block verbatim
EXEC_PROTO="$(awk '/^Execution Protocol:/{flag=1;print;next}/^Task File Template:/{flag=0}flag' "$RULE")"

# Build the task file from template
sed \
 -e "s/\[TASK_FILE_NAME\]/${TASK_FILE_NAME}_${TASK_IDENT}/g" \
 -e "s/\[DATETIME\]/${DT_STR}/g" \
 -e "s/\[USER_NAME\]/${USER_NAME}/g" \
 -e "s/\[MAIN BRANCH\]/${MAIN_BRANCH}/g" \
 -e "s/\[TASK BRANCH\]/${TASK_BRANCH}/g" \
 -e "s/\[AUTO-RUN MODE\]/${AUTO_RUN}/g" \
 -e "s|\[EXECUTION_PROTOCOL_VERBATIM\]|${EXEC_PROTO//|/\\|}|g" \
 "$TPL" > "$OUT_FILE"

echo "[✓] Created task file: $OUT_FILE"
echo "[i] Next: create branch and begin step 1:"
echo "    git checkout -b ${TASK_BRANCH}"
