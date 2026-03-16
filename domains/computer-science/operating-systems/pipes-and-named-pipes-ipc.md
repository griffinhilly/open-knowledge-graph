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

## Explainer

From your study of inter-process communication mechanisms, you know that processes need ways to exchange data, and from file system concepts, you understand that the OS presents I/O resources through file descriptors. **Pipes** are the simplest IPC mechanism in Unix — so simple that you've almost certainly used them without thinking about the underlying mechanics. When you type `ls | grep ".txt"` in a shell, the `|` character creates a pipe: the output of `ls` flows directly into the input of `grep` without ever touching the disk.

An **unnamed pipe** is created by the `pipe()` system call, which returns two file descriptors: one for reading and one for writing. Data written to the write end appears at the read end, flowing through a small kernel buffer (typically 64KB on Linux). The pipe is **unidirectional** — data flows only from writer to reader. If you need bidirectional communication, you create two pipes. The critical limitation is that both file descriptors must be inherited through `fork()`: the parent creates the pipe, forks a child, and then each process closes the end it doesn't need. The parent might keep the write end and close the read end, while the child keeps the read end and closes the write end. This is why unnamed pipes work only between related processes — unrelated processes have no way to obtain the file descriptors.

**Named pipes** (also called **FIFOs**) remove this limitation by giving the pipe a name in the filesystem. You create one with `mkfifo /tmp/myfifo`, and now any process that can access that path can open it for reading or writing, just like a regular file. The kernel still provides the same byte-stream buffer — no data is written to disk — but the filesystem entry acts as a rendezvous point that unrelated processes can discover. A common pattern is a logging architecture where multiple producer processes write to a named pipe and a single consumer reads and processes the log entries. Named pipes support the same `read()` and `write()` system calls as regular files, so programs that work with files often work with named pipes without modification.

Both types of pipes have important behavioral properties. Reads on an empty pipe **block** until data is available (or until all write ends are closed, at which point `read()` returns 0, signaling end-of-file). Writes to a full pipe block until the reader drains some data. Writing to a pipe with no readers delivers a **SIGPIPE** signal to the writer, which by default terminates it — this is how `head` can terminate a long pipeline early without the upstream commands hanging. Pipes transfer raw byte streams with no message boundaries: if one process writes "hello" and then "world," the reader might receive "helloworld" in a single read, or "hel" and "loworld" in two reads. For structured communication with message boundaries, you'd use message queues or sockets instead. Despite this simplicity, pipes are the backbone of the Unix philosophy of composing small, focused tools into powerful pipelines — each program does one thing, and pipes connect them.
