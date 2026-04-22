# contextweave

> **Self-healing context collapse for long-running AI agents.**

---

## The Problem

Long-running AI agents degrade. Context windows fill. Signal drowns in noise. The agent that was sharp at minute one is confused at minute sixty — not because it got dumber, but because it lost the thread.

Contextweave is the missing context management layer: aggressive, intelligent compression that keeps agents sharp over long sessions.

---

## Features

- **History snipping** — removes noise and redundancy from prior exchanges
- **Microcompact** — token-efficient recent context preservation
- **Context collapse** — structured summarization at threshold
- **Autocompact** — emergency compression when context is critical
- **IBA-ready** — integrates with IBA Intent Bound Authorization for governed long-running agent sessions
- **Simple plug-and-play API** — wraps any agent session

---

## Quick Start

```bash
git clone https://github.com/Grokipaedia/contextweave.git
cd contextweave
pip install -r requirements.txt
python example.py
```

---

## IBA Integration

Contextweave is designed to work alongside IBA Intent Bound Authorization. A long-running agent session that survives context collapse must remain within its declared intent boundary — not drift into unauthorized scope simply because earlier context was compressed away.

```python
from contextweave import ContextWeave
# Wrap your agent session
cw = ContextWeave(max_tokens=8000)
cw.add_message("user", "Start authorized task...")
compressed = cw.get_context()  # Intelligently compressed
```

The IBA cert governs what the agent is permitted to do. Contextweave governs how long it can stay sharp doing it.

---

## Related Repos

| Repo | Track |
|------|-------|
| [iba-governor](https://github.com/Grokipaedia/iba-governor) | Core gate · any agent |
| [iba-devstack-governor](https://github.com/Grokipaedia/iba-devstack-governor) | Dev stack governance |
| [dreamweave](https://github.com/Grokipaedia/dreamweave) | Long-term dreaming memory |

---

## Patent & Standards Record

```
Patent:   GB2603013.0 (Pending) · UK IPO · Filed February 10, 2026
Conception: February 5, 2026 · OTS timestamp + witness email
WIPO DAS: Confirmed April 15, 2026 · Access Code C9A6
PCT:      150+ countries · Protected until August 2028
IETF:     draft-williams-intent-token-00 · CONFIRMED LIVE
          datatracker.ietf.org/doc/draft-williams-intent-token/
NIST:     13 filings · NIST-2025-0035
NCCoE:    10 filings · AI Agent Identity & Authorization
```

---

## Acquisition Enquiries

IBA Intent Bound Authorization is available for acquisition.

**Jeffrey Williams**
IBA@intentbound.com
IntentBound.com
Patent GB2603013.0 Pending · WIPO DAS C9A6 · IETF draft-williams-intent-token-00
