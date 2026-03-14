@echo off
REM OKG Autonomous Build — Windows Task Scheduler wrapper
REM Runs the overnight orchestrator with resume + sonnet model
cd /d "C:\Users\griff\open-knowledge-graph"
C:\Python314\python.exe tools\overnight\orchestrator.py --resume --model sonnet
