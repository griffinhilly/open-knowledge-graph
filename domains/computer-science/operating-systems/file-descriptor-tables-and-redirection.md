---
id: file-descriptor-tables-and-redirection
title: File Descriptor Tables and I/O Redirection
domain: computer-science
course: operating-systems
prerequisites:
- id: file-system-concepts
  type: hard
- id: process-concept
  type: soft
tags:
- file-descriptors
- io
- redirection
stage: formal-systems
status: validated
---

# File Descriptor Tables and I/O Redirection

## Core Idea
Each process maintains a file descriptor table mapping small integers to open files, sockets, and pipes. Standard file descriptors 0 (stdin), 1 (stdout), and 2 (stderr) are inherited from the parent and can be redirected by closing and reopening different files. File descriptor manipulation is the basis for shell I/O redirection, piping, and inter-process communication.

## Questions

```yaml
- question: "When a shell executes `ls > output.txt`, which sequence of operations does the child process perform before running `ls`?"
  type: multiple-choice
  options:
    - "It modifies the `ls` binary to write to a file instead of the terminal"
    - "It closes file descriptor 1, then opens output.txt — which receives fd 1 as the lowest available slot"
    - "It opens output.txt as a new file descriptor and passes that number as an argument to `ls`"
    - "It tells the kernel to intercept `ls`'s output and redirect it to the file"
  answer: 1
  explanation: "The shell forks a child, which inherits the parent's fd table. Before exec-ing `ls`, the child closes fd 1 (stdout), then calls `open('output.txt', ...)` — the kernel assigns fd 1 because it is now the lowest available integer. When `ls` runs and writes to fd 1 as usual, it writes to the file. The `ls` binary is completely unmodified and unaware that anything changed — it just writes to fd 1 as always."

- question: "When the shell sets up a pipe for `ls | grep foo`, what does it actually create?"
  type: multiple-choice
  options:
    - "A temporary file that `ls` writes to and `grep` reads from sequentially"
    - "A shared memory region that both processes access concurrently"
    - "A kernel buffer with a write-end file descriptor wired to `ls`'s stdout and a read-end wired to `grep`'s stdin"
    - "A network socket connecting the two processes through the loopback interface"
  answer: 2
  explanation: "A pipe is a kernel-managed buffer with two file descriptors: one for writing (write-end) and one for reading (read-end). The shell creates the pipe, forks both child processes, then wires the pipe's write-end to `ls`'s fd 1 (stdout) and the read-end to `grep`'s fd 0 (stdin) using dup2 or close/open. Each program just reads/writes its standard descriptors as always — neither knows it is connected to the other rather than a terminal."

- question: "The kernel enforces that file descriptor 1 usually refers to the terminal (stdout), which is why programs can rely on writing to fd 1 to display output."
  type: true-false
  answer: false
  explanation: "File descriptor 1 is just a convention — an integer in the per-process table that can point to any open file, pipe, socket, or device. The kernel assigns no special meaning to fd 1. The convention is established by the shell, which sets up fd 0, 1, and 2 before launching programs. Programs written to write to fd 1 happen to write to whatever that slot currently points to — which could be a terminal, a file, or a pipe, depending on how the shell set things up."

- question: "When a process is created via fork(), the child process inherits a copy of the parent's file descriptor table."
  type: true-false
  answer: true
  explanation: "fork() creates a copy of the parent's process state, including the file descriptor table. Both parent and child start with the same file descriptors pointing to the same underlying open-file entries in the kernel. This inheritance is what makes shell I/O redirection possible: the shell can set up fds in the child (after fork but before exec) without affecting the parent's own stdin/stdout, and the exec'd program inherits whatever fds the child had arranged."

- question: "Why can `ls > output.txt` redirect ls's output to a file without any modification to the `ls` source code?"
  type: short-answer
  answer: "Because `ls` writes to file descriptor 1 (stdout) without knowing or caring what that descriptor points to. The shell, not `ls`, performs the redirection: it forks a child process, closes fd 1 in the child, opens output.txt (which gets assigned fd 1), then execs `ls`. From `ls`'s perspective, it just writes to fd 1 as always — the OS transparently delivers those writes to the file. This indirection through integer file descriptors is what makes Unix programs composable without modification."
  explanation: "This is the architectural insight behind Unix I/O: programs operate on abstract integer handles, not on specific files or devices. The kernel mediates all I/O through the fd table, and the shell (or any parent process) can rewire those handles before the program starts. The `dup2()` system call makes this explicit. The same principle underlies piping, network I/O, and terminal multiplexing — all operate on the same abstraction."
```

## Explainer

From your understanding of file systems and processes, you know that the OS manages open files on behalf of processes and that each process runs in its own isolated environment. The **file descriptor table** is the mechanism that connects these two ideas: it is a per-process array where each entry maps a small non-negative integer (the file descriptor) to an entry in the kernel's system-wide open file table. When a process calls `open()`, the kernel finds the lowest available integer in the process's table, fills it in with a pointer to the file's kernel state, and returns that integer. All subsequent operations — `read()`, `write()`, `close()` — use this integer as a handle.

The convention that file descriptors **0**, **1**, and **2** correspond to standard input, standard output, and standard error is just that — a convention. Nothing in the kernel enforces these meanings. What makes the convention work is that the shell sets up these three descriptors before launching any program, and programs are written to read from 0 and write to 1 and 2 by default. When you type `ls` in a shell, the shell forks a child process (which inherits the parent's file descriptor table), then execs `ls`, which writes its output to file descriptor 1 — your terminal.

**I/O redirection** exploits the fact that file descriptors are just integers that can be reassigned. When you write `ls > output.txt`, the shell forks, and before executing `ls`, the child process closes file descriptor 1 (stdout), then opens `output.txt` — which gets assigned file descriptor 1 because it is now the lowest available integer. When `ls` runs and writes to file descriptor 1, it writes to the file instead of the terminal, without `ls` knowing or caring that anything changed. The `dup2()` system call makes this even more explicit: `dup2(fd, 1)` copies whatever `fd` points to into slot 1, so stdout now refers to the same underlying file as `fd`.

**Piping** extends this pattern to connect two processes. When the shell encounters `ls | grep foo`, it creates a pipe (a kernel buffer with two file descriptors — one for reading, one for writing), forks two children, and wires the write end of the pipe to `ls`'s stdout and the read end to `grep`'s stdin. Each program reads and writes its standard descriptors as usual, unaware that they are connected to each other rather than to a terminal. This composability — programs that operate on abstract file descriptors rather than specific files — is the architectural insight that makes Unix pipelines possible.
