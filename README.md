# Process Boss
![Python CI Build](https://github.com/kristof9851/process-boss/actions/workflows/python-ci.yml/badge.svg)
![PyPI Downloads](https://img.shields.io/pypi/dm/process-boss)

*A Cron job scheduler implemented in Python*

## 1. Installation

```bash
pip install process-boss
```

## 2. Usage
Create a configuration file in `config.yaml` somewhere on disk, then run process boss:

```bash
python -m process-boss ~/config.yaml
```

### Example: Run a script on Monday mornings

```yaml
processes:
  - id: test-job
    cron: "0 7 * * MON" # every Monday at 7:00 AM
    command: "echo 'Hello World!'"
```

## 3. Configuration reference

```yaml
processes:
  - id: test-job
    cron: "0 7 * * MON" # every Monday at 7:00 AM
    command: "echo 'Hello World!'"
```

## 4. Maintainer documentation
See: [README_MAINTAINER.md](docs/README_MAINTAINER.md)
