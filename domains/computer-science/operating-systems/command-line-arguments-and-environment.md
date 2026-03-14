---
id: command-line-arguments-and-environment
title: Command-Line Arguments and Environment Variables
domain: computer-science
course: operating-systems
prerequisites:
- id: process-environment-and-exit-codes
  type: hard
builds-toward:
- shell-execution-model
tags:
- process
- arguments
- environment
stage: formal-systems
status: draft
---

# Command-Line Arguments and Environment Variables

## Core Idea
Processes receive command-line arguments through argc/argv and environment variables through an environment array, providing the primary means of configuring process behavior at startup. The shell constructs these when executing a command, expanding wildcards and substituting variable values. Both are inherited by child processes unless explicitly modified.
