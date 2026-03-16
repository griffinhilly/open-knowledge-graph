---
id: file-descriptor-tables-and-redirection
title: File Descriptor Tables and I/O Redirection
domain: computer-science
course: operating-systems
prerequisites:
- id: file-system-concepts
  type: hard
- id: process-concept-in-os
  type: soft
tags:
- file-descriptors
- io
- redirection
stage: formal-systems
status: draft
---

# File Descriptor Tables and I/O Redirection

## Core Idea
Each process maintains a file descriptor table mapping small integers to open files, sockets, and pipes. Standard file descriptors 0 (stdin), 1 (stdout), and 2 (stderr) are inherited from the parent and can be redirected by closing and reopening different files. File descriptor manipulation is the basis for shell I/O redirection, piping, and inter-process communication.

## Explainer

From your understanding of file systems and processes, you know that the OS manages open files on behalf of processes and that each process runs in its own isolated environment. The **file descriptor table** is the mechanism that connects these two ideas: it is a per-process array where each entry maps a small non-negative integer (the file descriptor) to an entry in the kernel's system-wide open file table. When a process calls `open()`, the kernel finds the lowest available integer in the process's table, fills it in with a pointer to the file's kernel state, and returns that integer. All subsequent operations — `read()`, `write()`, `close()` — use this integer as a handle.

The convention that file descriptors **0**, **1**, and **2** correspond to standard input, standard output, and standard error is just that — a convention. Nothing in the kernel enforces these meanings. What makes the convention work is that the shell sets up these three descriptors before launching any program, and programs are written to read from 0 and write to 1 and 2 by default. When you type `ls` in a shell, the shell forks a child process (which inherits the parent's file descriptor table), then execs `ls`, which writes its output to file descriptor 1 — your terminal.

**I/O redirection** exploits the fact that file descriptors are just integers that can be reassigned. When you write `ls > output.txt`, the shell forks, and before executing `ls`, the child process closes file descriptor 1 (stdout), then opens `output.txt` — which gets assigned file descriptor 1 because it is now the lowest available integer. When `ls` runs and writes to file descriptor 1, it writes to the file instead of the terminal, without `ls` knowing or caring that anything changed. The `dup2()` system call makes this even more explicit: `dup2(fd, 1)` copies whatever `fd` points to into slot 1, so stdout now refers to the same underlying file as `fd`.

**Piping** extends this pattern to connect two processes. When the shell encounters `ls | grep foo`, it creates a pipe (a kernel buffer with two file descriptors — one for reading, one for writing), forks two children, and wires the write end of the pipe to `ls`'s stdout and the read end to `grep`'s stdin. Each program reads and writes its standard descriptors as usual, unaware that they are connected to each other rather than to a terminal. This composability — programs that operate on abstract file descriptors rather than specific files — is the architectural insight that makes Unix pipelines possible.
