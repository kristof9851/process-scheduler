@echo off
call ..\..\..\venv\Scripts\activate.bat
set PYTHONDONTWRITEBYTECODE=1
@echo on
call python %*
@echo off
call ..\..\..\venv\Scripts\deactivate.bat
