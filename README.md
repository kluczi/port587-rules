# port587-rules

Rule engine for a larger thing I co-author - a [cold email infrastructure partner](https://github.com/port587). It evaluates campaign metrics (e.g. cold email): load context from JSON, define rules with conditions and actions, and run the engine to see which rules pass and which actions to execute.

## Features

- **Context** — Load campaign data (e.g. `reply_rate`, `bounce_rate`, `sent_today`) from JSON into a `Context`.
- **Conditions** — Compare a field to a threshold using `>`, `<`, `==`, `>=`, `<=`.
- **Rules** — Combine multiple conditions with **AND** or **OR**; attach a list of **actions** when the rule passes.
- **Actions** — `PAUSE_CAMPAIGN`, `REDUCE_VOLUME`, `INCREASE_VOLUME`, `HARD_STOP` with a payload and source rule name.
- **Engine** — Run all rules on a context; get per-rule results, pass/fail counts, and a list of actions to execute (from rules that passed).

## Requirements

- Python 3.10+
- `pytest` for running the test suite (`pip install pytest`)

## Usage

1. Put your campaign metrics in a JSON file (e.g. `sample.json`):

```json
{
    "reply_rate": 0.012,
    "bounce_rate": 0.045,
    "sent_today": 1200,
    "positive_replies": 4
}
```

2. Define rules and run the engine (see `main.py`):

```python
from core.context import Context
from core.condition import Condition, ComparisonOperator
from core.rule import Rule, LogicalOperator
from core.action import Action, ActionType
from core.engine import Engine

context = Context(data)  # or load from JSON
rules = [ ... ]  # list of Rule instances
engine = Engine(rules)
result = engine.run(context)

# result.results     — list of RuleResult (per-rule pass/fail and reasons)
# result.passed_rules / result.failed_rules
# result.passed_count / result.failed_count
# result.actions      — list of Action to execute (from rules that passed)
```

3. Run the sample:

```bash
python main.py
```

`main.py` loads `sample.json`, builds the example rules (high bounce, good reply, low reply + high volume), runs the engine, and prints rule results and actions.

## Tests

- **Run all tests**:

```bash
pytest
```

This will discover and run tests under the `tests/` directory (e.g. `tests/test_condition.py`).

## Project structure

```
port587-rules/
├── core/
│   ├── __init__.py
│   ├── action.py
│   ├── condition.py
│   ├── context.py
│   ├── engine.py
│   ├── rule.py
│   └── trace.py
├── examples/
│   ├── main.py
│   └── sample.json
├── tests/
│   ├── test_condition.py
│   ├── test_engine.py
│   └── test_rule.py
├── .gitignore
├── pytest.ini
└── README.md
```

## Example rules (from `main.py`)

| Rule                  | Conditions                                      | When passed     |
| --------------------- | ----------------------------------------------- | --------------- |
| High Bounce Rule      | `bounce_rate` > 0.03                            | Pause campaign  |
| Good Reply Rule       | `reply_rate` >= 0.02                            | Increase volume |
| Low Reply High Volume | `reply_rate` < 0.01 **and** `sent_today` > 1000 | Reduce volume   |
