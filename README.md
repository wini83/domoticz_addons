> ⚠️ **LEGACY / LIMITED MAINTENANCE**
>
> This repository contains older personal Domoticz add-ons. The PEKA helper has received a small maintenance refresh, but other integrations have not been audited for compatibility.

## PEKA virtual monitor

`lib/pekaVmonitor.py` queries the unofficial PEKA virtual monitor endpoint and retains the original `pekaVmonitor` class and methods for compatibility.

```python
from lib.pekaVmonitor import pekaVmonitor

monitor = pekaVmonitor()
print(monitor.get_1st_departure("IPNZ02"))
```

The example requires network access and a valid PEKA bollard symbol. The live PEKA endpoint has **not** been verified as part of this cleanup. HTTPS is used; if that endpoint does not support HTTPS, it will need adjustment. Network errors raise exceptions, while an empty or unrecognized departure list returns `"error"` for backward compatibility.

## Development

Install [uv](https://docs.astral.sh/uv/), then run:

```sh
uv sync
uv run pytest
uv run ruff check
```

The `pyproject.toml` defines **development tools only**. It intentionally does not migrate the old runtime `requirements.txt` because the legacy Domoticz integrations may depend on older packages or environments. No packaging or installation of add-ons is implied by `uv sync`.

## Legacy dependencies

`requirements.txt` is preserved for historical reference. Its `git://` dependency URL is outdated and should be reviewed before attempting to install the complete legacy stack.
