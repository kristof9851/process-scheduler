# Maintainer documentation

## 1. Clone project and install pip/python

## 2. Create virtual env and install project dependencies

Install `virtualenv` to set up your virtual environment
```bash
pip install --upgrade virtualenv
```

Go to project root and create your virtual environment
```bash
cd <PROJECT_ROOT>
python -m venv venv
```

Activate your virtual environment
```bash
# Windows
.\venv\Scripts\activate

# Linux
source venv/bin/activate
```

Install project dependencies
```bash
pip install -r requirements.txt
```

Install module locally, so you can import it as a module
```bash
pip install -e .
```

## 3. Run the project

Define your configuration in a YAML file
```yaml
loopRefreshSeconds: 15
maxWorkers: 10
schedulerLogDir: "C:\\Desktop\\apps\\process_boss\\logs\\scheduler"
processLogDir: "C:\\Desktop\\apps\\process_boss\\logs\\process"
processes:
  - id: test-job
    cron: "0 7 * * mon"                          # == 7:00 AM every Monday
    command: "python C:\\Desktop\\my-process.py" # Invoke my python script
    runAtStartup: true                           # Run immediately when scheduler starts, then follow cron definition
```

Run it
```bash
# Windows
python -m process_boss C:\\Desktop\\config.yaml

# Linux
python -m process_boss ~/config.yaml
```

## 4. Run the tests

### Prerequisites
Steps 1. and 2. above

### How to run

```bash
# Windows
.\wtests.bat

# Linux
./tests.sh
```

## 5. Build and upload release

Install dependencies

```bash
pip install --upgrade setuptools wheel build twine
```

Build the package (wheel and sdist)
```bash
python -m build 
```

Ensure `.pypirc` in user folder is correct, then upload
```bash
python -m twine upload dist/*
```
