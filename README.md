# Gauntlet

Standalone adversarial testing engine for LLM applications — 57 built-in attack scenarios, multi-provider comparison, and a React dashboard.

## Features

- **57 attack scenarios** across 8 categories (prompt injection, jailbreaking, info extraction, social engineering, context manipulation, model exploitation, multi-turn, compliance)
- **Refusal-aware evaluation**: sentence-level analysis to avoid false-positive bypass scoring
- **Honeypot-aware scoring**: detects honey token decoys
- **Multi-turn attacks**: escalating conversation sequences
- **Multi-provider comparison**: benchmark multiple LLMs side-by-side
- **Click CLI**: run, stats, serve, demo, replay, export commands
- **React dashboard**: command center, scenario library, session details, provider comparison, scheduler, reports
- **Tool integrations**: PyRIT, DeepTeam, AIX, Garak
- **Cron scheduler**: automated recurring red team runs with webhook notifications
- **PDF reports**: generate security assessment reports
- **OWASP & MITRE mapping**: every scenario mapped to frameworks

## Install

```bash
pip install gauntlet
```

With optional extras:

```bash
pip install "gauntlet[flask]"      # API server + dashboard
pip install "gauntlet[pdf]"        # PDF report generation
pip install "gauntlet[sentinel]"   # Sentinel (AI firewall) integration
pip install "gauntlet[all]"        # Everything
```

## Quick Start

### CLI

```bash
# Run all scenarios against a target
gauntlet run --target http://localhost:5000/api/chat

# Filter by category or difficulty
gauntlet run --category jailbreaking --difficulty hard

# Start the dashboard
gauntlet serve --port 8666

# Demo mode with mock target
gauntlet demo
```

### Python API

```python
from gauntlet import RedTeamOrchestrator, ScenarioLoader, AttackExecutor, ResultEvaluator

loader = ScenarioLoader()
executor = AttackExecutor(target_url="http://localhost:5000/api/chat")
evaluator = ResultEvaluator()
orchestrator = RedTeamOrchestrator(loader, executor, evaluator)

results = orchestrator.run_all()
print(f"Bypass rate: {results['bypass_rate']:.1%}")
```

### Target API Contract

Your target endpoint should accept POST requests:

```json
{"message": "user input here"}
```

And return:

```json
{"response": "LLM output here"}
```

## License

Apache 2.0
