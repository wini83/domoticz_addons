# PEKA virtual monitor

This repository retains the historical PEKA virtual monitor helper. All other retired Domoticz scripts and their old runtime requirements have been moved into [archive/](archive/) for reference.

## Active code

- [lib/pekaVmonitor.py](lib/pekaVmonitor.py) — PEKA virtual departure monitor client, retaining its original public API.
- [tests/test_peka_vmonitor.py](tests/test_peka_vmonitor.py) — offline tests.
- [pyproject.toml](pyproject.toml) — minimal uv-based development setup.

The PEKA endpoint is unofficial. Its live availability and HTTPS support have **not** been verified.

```python
from lib.pekaVmonitor import pekaVmonitor

monitor = pekaVmonitor()
print(monitor.get_1st_departure("IPNZ02"))
```

## Development

Install [uv](https://docs.astral.sh/uv/), then run:

```sh
uv sync
uv run pytest
uv run ruff check
```

The project has no external runtime dependencies. The optional developer environment includes pytest and Ruff.

## Archive

The [archive/](archive/) directory contains old, unmaintained Domoticz scripts, earlier experiments, sample configuration and historical `requirements.txt`. Its contents are **not** installed, tested or supported. Do not use the archived examples as production configuration; review them before reuse.

To restore an old script, retrieve it from Git history or `archive/` and audit its dependencies first.
