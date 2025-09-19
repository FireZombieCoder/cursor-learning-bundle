# Cursor Learning Bundle (Base L2 / Python / Foundry)

This bundle gives you:
- `.cursor/rules/00_execution-protocol.mdc` — your always-on entrypoint (Otto)
- Curriculum, Python, Foundry/Security rules under `.cursor/rules/`
- Custom commands under `.cursor/commands/`
- `bootstrap_learning_env.sh` — creates a Task File in `.tasks/` pre-filled with the **Execution Protocol**
- Python scaffolding and `.env.example`

## Install
1) Extract this zip at your repo root.
2) Create a Python venv (optional) and `pip install -r python/requirements.txt`.
3) Copy `.env.example` → `.env` and set your RPC/keys.

## Bootstrap
```bash
./bootstrap_learning_env.sh
git checkout -b task/base-learning_$(date +%Y-%m-%d)_1  # if not already created by protocol
```

Open Cursor, add your goals under **User Input** in `00_execution-protocol.mdc`, and run your commands:
- `/curriculum build stage=0 topic="Tooling on Base-Sepolia"`
- `/exercise topic="storage vs memory" stage=1`
- `/trace-lab contract="Demo" method="queryDouble(address,uint256)"`
