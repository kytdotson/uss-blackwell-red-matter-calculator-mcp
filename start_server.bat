@echo off
cd /d "%~dp0"
set MCP_USE_ANONYMIZED_TELEMETRY=false
.venv\Scripts\python.exe server.py
