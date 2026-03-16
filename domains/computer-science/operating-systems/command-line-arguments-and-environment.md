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

## Explainer

From your understanding of process environments and exit codes, you know that every process carries an environment — a collection of state that defines its execution context. Command-line arguments and environment variables are two of the most important parts of that environment, and they serve complementary purposes: arguments tell a process *what to do right now*, while environment variables tell it *what context it is running in*.

When you type `ls -l /home/user` in a shell, the shell creates a new process and passes three strings as **command-line arguments**: `"ls"`, `"-l"`, and `"/home/user"`. In C, the process receives these through the `main` function's parameters: `argc` (the count, here 3) and `argv` (an array of string pointers). The first element, `argv[0]`, is conventionally the program's own name. This mechanism is simple and direct — the arguments exist only for this invocation and are not inherited by any processes that `ls` might spawn. They are the equivalent of function parameters in a programming language.

**Environment variables** work differently. They are key-value pairs (like `PATH=/usr/bin:/bin` or `HOME=/home/user`) stored in a block of memory that the process can access through the `environ` global variable or the `getenv()` function. Unlike arguments, environment variables are **inherited by child processes** through `fork()` and `exec()`. When the shell launches `ls`, `ls` inherits the shell's entire environment — `PATH`, `HOME`, `LANG`, `TERM`, and dozens of others. This inheritance chain is how configuration propagates through a process hierarchy without every program needing to know about every setting. A program that needs to know the user's preferred language checks `LANG`; a program that needs to find executables checks `PATH`.

The shell plays a crucial role in constructing both mechanisms. Before passing arguments to a new process, the shell performs **expansions**: wildcards like `*.txt` are expanded into matching filenames, variables like `$HOME` are replaced with their values, and quotes control which expansions apply. The command `echo $HOME/*.txt` might reach the process as `echo /home/user/notes.txt /home/user/todo.txt` — the process never sees the wildcard or the variable reference. Understanding that these transformations happen *in the shell before the process starts* is essential to predicting what a program actually receives.

A process can modify its own environment (using `setenv()` or `putenv()`) and these changes are inherited by any children it subsequently creates, but they never propagate *upward* to the parent. This is why running `export PATH=/new/path` in a script does not change the shell that launched the script — the script runs in a child process whose environment changes die with it. To affect the parent shell's environment, you must *source* the script (`. script.sh` or `source script.sh`), which executes the commands in the current shell process rather than a child.
