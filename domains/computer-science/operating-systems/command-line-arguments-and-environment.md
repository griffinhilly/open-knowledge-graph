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

## Questions

```yaml
- question: "A shell script contains the line: export DATABASE_URL=postgres://localhost/mydb. After the script finishes, you check the variable in your interactive shell and find it is not set. What explains this?"
  type: multiple-choice
  options:
    - "The export keyword only sets variables for the script's own use, not for child processes"
    - "The script ran in a child process; environment changes in child processes do not propagate to the parent"
    - "The variable was set incorrectly — DATABASE_URL cannot contain slashes"
    - "Environment variables set in scripts are automatically unset when the script exits"
  answer: 1
  explanation: "When a shell executes a script normally (./script.sh), it creates a child process to run it. That child inherits the parent's environment and can modify its own copy freely — but those modifications die with the child process. The parent never sees them. Environment inheritance flows downward (parent → child), never upward. To make the script's changes affect the current shell, you must *source* it (. script.sh or source script.sh), which runs the commands in the current shell process rather than a child."

- question: "What is the difference between running ./configure.sh and source ./configure.sh with respect to environment variables?"
  type: multiple-choice
  options:
    - "source runs the script faster because it skips process creation overhead"
    - "source executes the script's commands in the current shell process, so any environment changes persist in the calling shell; ./configure.sh runs in a child process where changes are invisible to the parent"
    - "There is no difference — both methods inherit the parent environment and return it after completion"
    - "source prevents the script from accessing the parent shell's environment variables for security reasons"
  answer: 1
  explanation: "Sourcing a script (. script.sh or source script.sh) is fundamentally different from executing it: sourcing runs the commands directly in the current shell's process, so variable assignments, exports, and directory changes all affect the current shell's state. Executing (./script.sh) creates a new child process, which gets a copy of the environment — changes to that copy vanish when the child exits. This distinction is why .bashrc, .profile, and Python virtualenv activation scripts must be sourced, not executed."

- question: "Environment variable changes made by a child process are not visible to the parent process that launched it."
  type: true-false
  answer: true
  explanation: "This is a fundamental property of Unix process model: environment variable changes propagate downward through fork/exec (parent → child) but never upward. When a child calls setenv() or putenv(), it modifies only its own in-memory copy of the environment. The parent's copy is unchanged. This isolation is intentional — it prevents child processes from inadvertently (or maliciously) modifying the environment of the process that launched them."

- question: "When a shell expands wildcards like *.txt before passing arguments to a program, the program receives the original *.txt pattern and performs its own expansion internally."
  type: true-false
  answer: false
  explanation: "Shell expansion happens *before* the program starts, in the shell process. By the time the target program's main() function is called, argv already contains the expanded filenames — the program never sees *.txt. This is why the same program behaves differently when called from different shells: the shell, not the program, controls what argv contains. It also means a program cannot distinguish between `cp *.txt dest/` (wildcard expanded by shell) and `cp file1.txt file2.txt dest/` (explicit filenames) — both arrive in argv as individual filenames."

- question: "Why do command-line arguments and environment variables serve complementary rather than identical purposes, and when is each appropriate?"
  type: short-answer
  answer: "Command-line arguments communicate what a process should do *in this specific invocation* — they are transient, per-run instructions. Environment variables communicate the context the process is running in — they are persistent configuration that is inherited by all child processes. Arguments are appropriate for things that change between invocations (which files to process, which operation to perform); environment variables are appropriate for things that stay constant across many invocations (the user's home directory, the search path for executables, the preferred language). Because arguments are not inherited, they cannot propagate configuration down a process hierarchy; environment variables can."
  explanation: "The distinction maps to function parameters vs. global state in programming. Arguments are like parameters — explicit, local, per-call. Environment variables are like a configured global context — implicit, inherited, session-wide. Mixing up these roles (e.g., passing PATH as a command-line argument to every program) would be impractical; the inheritance model is what makes environment variables useful for system-wide configuration."
```

## Explainer

From your understanding of process environments and exit codes, you know that every process carries an environment — a collection of state that defines its execution context. Command-line arguments and environment variables are two of the most important parts of that environment, and they serve complementary purposes: arguments tell a process *what to do right now*, while environment variables tell it *what context it is running in*.

When you type `ls -l /home/user` in a shell, the shell creates a new process and passes three strings as **command-line arguments**: `"ls"`, `"-l"`, and `"/home/user"`. In C, the process receives these through the `main` function's parameters: `argc` (the count, here 3) and `argv` (an array of string pointers). The first element, `argv[0]`, is conventionally the program's own name. This mechanism is simple and direct — the arguments exist only for this invocation and are not inherited by any processes that `ls` might spawn. They are the equivalent of function parameters in a programming language.

**Environment variables** work differently. They are key-value pairs (like `PATH=/usr/bin:/bin` or `HOME=/home/user`) stored in a block of memory that the process can access through the `environ` global variable or the `getenv()` function. Unlike arguments, environment variables are **inherited by child processes** through `fork()` and `exec()`. When the shell launches `ls`, `ls` inherits the shell's entire environment — `PATH`, `HOME`, `LANG`, `TERM`, and dozens of others. This inheritance chain is how configuration propagates through a process hierarchy without every program needing to know about every setting. A program that needs to know the user's preferred language checks `LANG`; a program that needs to find executables checks `PATH`.

The shell plays a crucial role in constructing both mechanisms. Before passing arguments to a new process, the shell performs **expansions**: wildcards like `*.txt` are expanded into matching filenames, variables like `$HOME` are replaced with their values, and quotes control which expansions apply. The command `echo $HOME/*.txt` might reach the process as `echo /home/user/notes.txt /home/user/todo.txt` — the process never sees the wildcard or the variable reference. Understanding that these transformations happen *in the shell before the process starts* is essential to predicting what a program actually receives.

A process can modify its own environment (using `setenv()` or `putenv()`) and these changes are inherited by any children it subsequently creates, but they never propagate *upward* to the parent. This is why running `export PATH=/new/path` in a script does not change the shell that launched the script — the script runs in a child process whose environment changes die with it. To affect the parent shell's environment, you must *source* the script (`. script.sh` or `source script.sh`), which executes the commands in the current shell process rather than a child.
