---
id: pipes-and-named-pipes-ipc
title: Pipes and Named Pipes (FIFOs) for IPC
domain: computer-science
course: operating-systems
prerequisites:
- id: inter-process-communication-mechanisms
  type: hard
- id: file-system-concepts
  type: soft
builds-toward:
- shell-execution-model
tags:
- ipc
- pipes
- fifo
stage: formal-systems
status: draft
---

# Pipes and Named Pipes (FIFOs) for IPC

## Core Idea
Pipes are unidirectional communication channels between processes; unnamed pipes work only for parent-child processes, while named pipes (FIFOs) allow communication between arbitrary processes. Pipes are simple to use and deeply integrated into the Unix shell for composing commands but are limited to byte-stream communication. Named pipes enable flexible inter-process data flow by appearing as files in the filesystem.
