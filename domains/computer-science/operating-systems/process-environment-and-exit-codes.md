---
id: process-environment-and-exit-codes
title: Process Environment and Exit Codes
domain: computer-science
course: operating-systems
prerequisites:
- id: process-concept-in-os
  type: hard
- id: system-calls
  type: soft
builds-toward:
- command-line-arguments-and-environment
tags:
- process
- environment
- exit
stage: formal-systems
status: draft
---

# Process Environment and Exit Codes

## Core Idea
Each process has an environment consisting of environment variables, working directory, file descriptors, and resource limits. When a process exits, it returns an exit code (0 for success, non-zero for failure) that parent processes can retrieve via wait(). The parent must reap terminated children to prevent zombie processes from accumulating.
