---
id: shell-execution-model
title: Shell Execution Model and Command Processing
domain: computer-science
course: operating-systems
prerequisites:
- id: process-creation-fork-exec
  type: hard
- id: inter-process-communication
  type: soft
builds-toward:
- file-descriptor-tables-and-redirection
tags:
- shell
- execution
- processes
stage: formal-systems
status: validated
---

# Shell Execution Model and Command Processing

## Core Idea
The shell parses commands, applies expansions (wildcards, variables), handles redirection and pipes, and uses fork/exec to create child processes. Input redirection (<) and output redirection (>) modify the child's file descriptors before exec(). Pipes connect the stdout of one process to the stdin of another, enabling powerful composition and data flow between programs.

## Questions

```yaml
- question: "When you run `sort < input.txt > output.txt`, which entity actually opens the files and connects them to the process's stdin and stdout?"
  type: multiple-choice
  options:
    - "The sort program reads the redirection syntax and opens the files itself"
    - "The shell opens the files and connects them to file descriptors in the child process before calling exec"
    - "The kernel parses the redirection operators and routes I/O automatically"
    - "The shell passes the filenames as command-line arguments to sort"
  answer: 1
  explanation: "The shell handles all redirection setup. After forking a child process, the shell (in the child) opens input.txt and connects it to file descriptor 0 (stdin), opens output.txt and connects it to file descriptor 1 (stdout), *then* calls exec to replace the child with sort. The sort program simply reads from stdin and writes to stdout — it has no knowledge of any redirection. This is why redirection works with any program, even those with no awareness of it."

- question: "In the pipeline `cmd1 | cmd2 | cmd3`, when does cmd1 begin executing relative to cmd2 and cmd3?"
  type: multiple-choice
  options:
    - "cmd1 runs to completion, then its output is passed to cmd2, which runs to completion, then cmd3 runs"
    - "All three commands are forked and run concurrently, connected by pipes the shell created"
    - "The shell runs cmd1 in the foreground and cmd2, cmd3 in the background sequentially"
    - "cmd3 starts first to prepare its input buffer, then cmd2, then cmd1"
  answer: 1
  explanation: "Pipeline commands run concurrently. The shell creates the pipes, forks all three processes, wires their file descriptors to the appropriate pipe endpoints, and lets them all run simultaneously. The kernel buffers data as needed: cmd1 writes, cmd2 reads and writes, cmd3 reads. This concurrency is what makes pipelines efficient — cmd2 can start processing cmd1's output before cmd1 has finished. Option A (sequential execution) is the most common misconception about pipeline behavior."

- question: "Variable expansion (e.g., $HOME) and glob expansion (e.g., *.txt) happen inside the child process after exec() is called."
  type: true-false
  answer: false
  explanation: "All expansion happens in the shell process *before* fork. The shell substitutes $HOME with its value, expands *.txt to the matching list of filenames, and processes command substitutions, all before creating any child process. The child receives only the final, expanded arguments. This is why quoting matters: `echo '$HOME'` suppresses expansion and the child sees the literal string, while `echo \"$HOME\"` allows it and the child sees the expanded value."

- question: "A child process created by the shell inherits its parent's open file descriptors, including stdin, stdout, and stderr."
  type: true-false
  answer: true
  explanation: "Fork creates a nearly identical copy of the parent process, including its open file descriptor table. The child inherits all open file descriptors from the shell — including stdin (0), stdout (1), and stderr (2). This inheritance is what makes redirection possible: the shell can modify these file descriptors in the child *after fork but before exec*, and those modifications persist through the exec call. The executed program starts with whatever file descriptors the shell set up."

- question: "Explain why quoting matters in shell commands. What specific shell behavior does quoting control, and what problem does it prevent?"
  type: short-answer
  answer: "Quoting controls which expansions the shell performs before passing arguments to the child program. Single quotes suppress all expansion; double quotes suppress glob expansion but allow variable and command substitution. Without quoting, a filename containing spaces becomes multiple arguments, and a variable containing spaces splits on whitespace into multiple words. Quoting prevents word splitting and glob expansion from corrupting arguments that should be passed as single units."
  explanation: "The shell performs expansion and word splitting before fork, so the child program receives the results. If a variable contains spaces and is unquoted, the shell splits it into multiple arguments — the program sees more arguments than intended. If a glob pattern is unquoted and matches no files, it may be passed as a literal string or cause an error. Quoting signals to the shell: 'treat this as one unit, don't expand or split it.'"
```

## Explainer

You already understand that `fork()` creates a copy of the current process and `exec()` replaces that copy's code with a new program. The shell is the program that orchestrates this dance every time you type a command. When you enter `ls -l`, the shell does not run `ls` inside itself — it forks a child process, sets up that child's environment, and then calls `exec()` to replace the child with the `ls` program. The shell (parent) waits for the child to finish, then prints the next prompt. This fork-then-exec pattern is the heartbeat of every command you run.

What makes the shell powerful is what happens between fork and exec. After forking but before calling exec, the child process can modify its own file descriptors — and those modifications persist through the exec call. This is how **redirection** works. When you type `sort < data.txt > sorted.txt`, the shell forks, and the child process opens `data.txt` and connects it to file descriptor 0 (stdin), then opens `sorted.txt` and connects it to file descriptor 1 (stdout). Only then does the child exec into `sort`. The `sort` program has no idea its input and output were redirected — it just reads from stdin and writes to stdout as usual. The shell did all the wiring in advance.

**Pipes** extend this idea to chain processes together. When you write `cat log.txt | grep ERROR | wc -l`, the shell creates two pipes (each a pair of connected file descriptors), forks three child processes, and wires each one's stdin and stdout to the appropriate pipe ends. All three processes run concurrently — `cat` produces data, `grep` filters it, and `wc` counts lines — with the kernel buffering data in the pipe as needed. This compositional model lets you build complex data-processing pipelines from small, single-purpose tools without any of those tools needing to know about each other.

Before any of this happens, the shell also performs **expansion**: it replaces `*.txt` with matching filenames (globbing), substitutes `$HOME` with its value (variable expansion), and processes backticks or `$(...)` by running the enclosed command and inserting its output (command substitution). These transformations happen in the shell process itself, before fork, so the child process sees only the final, expanded arguments. Understanding this sequence — parse, expand, fork, redirect, exec — demystifies shell behavior and explains why quoting matters: quotes control which expansions the shell performs before handing arguments to the child program.
