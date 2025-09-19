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

# Build the task file from template using awk to avoid sed escaping issues
awk -v task_file_name="${TASK_FILE_NAME}_${TASK_IDENT}" \
    -v datetime="$DT_STR" \
    -v user_name="$USER_NAME" \
    -v main_branch="$MAIN_BRANCH" \
    -v task_branch="$TASK_BRANCH" \
    -v auto_run="$AUTO_RUN" \
    -v exec_proto="$EXEC_PROTO" '
{
    gsub(/\[TASK_FILE_NAME\]/, task_file_name)
    gsub(/\[DATETIME\]/, datetime)
    gsub(/\[USER_NAME\]/, user_name)
    gsub(/\[MAIN BRANCH\]/, main_branch)
    gsub(/\[TASK BRANCH\]/, task_branch)
    gsub(/\[AUTO-RUN MODE\]/, auto_run)
    gsub(/\[EXECUTION_PROTOCOL_VERBATIM\]/, exec_proto)
    print
}
' "$TPL" > "$OUT_FILE"

echo "[✓] Created task file: $OUT_FILE"
echo "[i] Next: create branch and begin step 1:"
echo "    git checkout -b ${TASK_BRANCH}"
