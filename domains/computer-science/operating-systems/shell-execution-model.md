---
id: shell-execution-model
title: Shell Execution Model and Command Processing
domain: computer-science
course: operating-systems
prerequisites:
- id: process-creation-fork-exec
  type: hard
- id: inter-process-communication-mechanisms
  type: soft
builds-toward:
- file-descriptor-tables-and-redirection
tags:
- shell
- execution
- processes
stage: formal-systems
status: draft
---

# Shell Execution Model and Command Processing

## Core Idea
The shell parses commands, applies expansions (wildcards, variables), handles redirection and pipes, and uses fork/exec to create child processes. Input redirection (<) and output redirection (>) modify the child's file descriptors before exec(). Pipes connect the stdout of one process to the stdin of another, enabling powerful composition and data flow between programs.

## Explainer

You already understand that `fork()` creates a copy of the current process and `exec()` replaces that copy's code with a new program. The shell is the program that orchestrates this dance every time you type a command. When you enter `ls -l`, the shell does not run `ls` inside itself — it forks a child process, sets up that child's environment, and then calls `exec()` to replace the child with the `ls` program. The shell (parent) waits for the child to finish, then prints the next prompt. This fork-then-exec pattern is the heartbeat of every command you run.

What makes the shell powerful is what happens between fork and exec. After forking but before calling exec, the child process can modify its own file descriptors — and those modifications persist through the exec call. This is how **redirection** works. When you type `sort < data.txt > sorted.txt`, the shell forks, and the child process opens `data.txt` and connects it to file descriptor 0 (stdin), then opens `sorted.txt` and connects it to file descriptor 1 (stdout). Only then does the child exec into `sort`. The `sort` program has no idea its input and output were redirected — it just reads from stdin and writes to stdout as usual. The shell did all the wiring in advance.

**Pipes** extend this idea to chain processes together. When you write `cat log.txt | grep ERROR | wc -l`, the shell creates two pipes (each a pair of connected file descriptors), forks three child processes, and wires each one's stdin and stdout to the appropriate pipe ends. All three processes run concurrently — `cat` produces data, `grep` filters it, and `wc` counts lines — with the kernel buffering data in the pipe as needed. This compositional model lets you build complex data-processing pipelines from small, single-purpose tools without any of those tools needing to know about each other.

Before any of this happens, the shell also performs **expansion**: it replaces `*.txt` with matching filenames (globbing), substitutes `$HOME` with its value (variable expansion), and processes backticks or `$(...)` by running the enclosed command and inserting its output (command substitution). These transformations happen in the shell process itself, before fork, so the child process sees only the final, expanded arguments. Understanding this sequence — parse, expand, fork, redirect, exec — demystifies shell behavior and explains why quoting matters: quotes control which expansions the shell performs before handing arguments to the child program.
