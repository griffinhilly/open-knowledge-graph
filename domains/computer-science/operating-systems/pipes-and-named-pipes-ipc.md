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
status: validated
---

# Pipes and Named Pipes (FIFOs) for IPC

## Core Idea
Pipes are unidirectional communication channels between processes; unnamed pipes work only for parent-child processes, while named pipes (FIFOs) allow communication between arbitrary processes. Pipes are simple to use and deeply integrated into the Unix shell for composing commands but are limited to byte-stream communication. Named pipes enable flexible inter-process data flow by appearing as files in the filesystem.

## Questions

```yaml
- question: "Two completely unrelated processes — a log producer and a log consumer started independently — need to stream data between them. Which statement is correct?"
  type: multiple-choice
  options:
    - "An unnamed pipe works; the kernel automatically connects processes that want to communicate"
    - "A named pipe (FIFO) works; an unnamed pipe would not, because unnamed pipes require file descriptors shared through fork()"
    - "Neither works; only sockets support communication between unrelated processes"
    - "Both work as long as both processes run as the same user"
  answer: 1
  explanation: "Unnamed pipes are created by pipe() and their file descriptors live only in the process that called pipe(). The only way to share them is through fork() — so only parent-child or sibling processes can use them. A named pipe (FIFO) solves this by creating a filesystem path via mkfifo; any process with access to that path can open it independently, with no shared ancestry required. The kernel still buffers data in memory — no disk I/O occurs."

- question: "A process writes 'hello' and then 'world' to a pipe in two separate write() calls. What can the reader reliably expect?"
  type: multiple-choice
  options:
    - "Exactly two reads: first 'hello', then 'world' — pipes preserve write boundaries"
    - "Any byte split: 'helloworld' in one read, 'hel'+'loworld', or other arbitrary divisions — pipes are byte streams"
    - "Only the second write survives — 'world' — because pipes work like a single-slot queue"
    - "The reader blocks indefinitely because pipes don't support back-to-back writes"
  answer: 1
  explanation: "Pipes transfer raw byte streams with no message framing. The kernel buffers all bytes in order, but the reader's read() calls have no obligation to align with the writer's write() calls. A single read() might return all 10 bytes at once, or the data might arrive in arbitrary splits depending on timing and buffer state. If message boundaries matter, use a higher-level IPC mechanism — message queues or sockets — that preserves framing."

- question: "Data written to a named pipe (FIFO) travels through a kernel memory buffer and is never written to disk, even though the FIFO appears as a file in the filesystem."
  type: true-false
  answer: true
  explanation: "The filesystem entry for a named pipe is purely a rendezvous point — a name that unrelated processes can open. The actual data flows through a kernel memory buffer, identical to how unnamed pipes work. This makes named pipes fast (no disk I/O) but non-persistent: data exists only while processes hold the pipe open. If all processes close the FIFO, any unread data in the buffer is discarded."

- question: "When a writer process finishes and closes its end of a pipe, the reader receives an error code indicating failure on its next read() call."
  type: true-false
  answer: false
  explanation: "When all write ends of a pipe are closed, the reader's read() returns 0 — the standard Unix end-of-file signal — not an error. This is intentional: it allows pipelines to compose cleanly. The reader distinguishes 'no data available yet, block and wait' (write end still open, buffer empty) from 'writing is done, nothing more will come' (write end closed, returns 0). Errors (negative return values) indicate actual I/O failures, not normal completion."

- question: "Explain why an unnamed pipe cannot be used between two unrelated processes, and what mechanism named pipes use to solve this problem."
  type: short-answer
  answer: "Unnamed pipes exist only as file descriptors in the creating process's memory — there is no filesystem name an unrelated process can discover. The file descriptors can only be shared by inheriting them through fork(), limiting unnamed pipes to related (parent-child or sibling) processes. Named pipes solve this by registering a filesystem path via mkfifo; any process that can access that path can open the pipe by name, providing a rendezvous independent of process ancestry."
  explanation: "The filesystem namespace is the key: it's a shared naming system that any process can consult, regardless of heritage. Just as two unrelated programs can both open /tmp/foo.txt, they can both open /tmp/myfifo. The kernel then connects their reads and writes through the same in-memory buffer mechanism as unnamed pipes. The filesystem entry is just a door — the actual communication channel is always in-memory, never on disk."
```

## Explainer

From your study of inter-process communication mechanisms, you know that processes need ways to exchange data, and from file system concepts, you understand that the OS presents I/O resources through file descriptors. **Pipes** are the simplest IPC mechanism in Unix — so simple that you've almost certainly used them without thinking about the underlying mechanics. When you type `ls | grep ".txt"` in a shell, the `|` character creates a pipe: the output of `ls` flows directly into the input of `grep` without ever touching the disk.

An **unnamed pipe** is created by the `pipe()` system call, which returns two file descriptors: one for reading and one for writing. Data written to the write end appears at the read end, flowing through a small kernel buffer (typically 64KB on Linux). The pipe is **unidirectional** — data flows only from writer to reader. If you need bidirectional communication, you create two pipes. The critical limitation is that both file descriptors must be inherited through `fork()`: the parent creates the pipe, forks a child, and then each process closes the end it doesn't need. The parent might keep the write end and close the read end, while the child keeps the read end and closes the write end. This is why unnamed pipes work only between related processes — unrelated processes have no way to obtain the file descriptors.

**Named pipes** (also called **FIFOs**) remove this limitation by giving the pipe a name in the filesystem. You create one with `mkfifo /tmp/myfifo`, and now any process that can access that path can open it for reading or writing, just like a regular file. The kernel still provides the same byte-stream buffer — no data is written to disk — but the filesystem entry acts as a rendezvous point that unrelated processes can discover. A common pattern is a logging architecture where multiple producer processes write to a named pipe and a single consumer reads and processes the log entries. Named pipes support the same `read()` and `write()` system calls as regular files, so programs that work with files often work with named pipes without modification.

Both types of pipes have important behavioral properties. Reads on an empty pipe **block** until data is available (or until all write ends are closed, at which point `read()` returns 0, signaling end-of-file). Writes to a full pipe block until the reader drains some data. Writing to a pipe with no readers delivers a **SIGPIPE** signal to the writer, which by default terminates it — this is how `head` can terminate a long pipeline early without the upstream commands hanging. Pipes transfer raw byte streams with no message boundaries: if one process writes "hello" and then "world," the reader might receive "helloworld" in a single read, or "hel" and "loworld" in two reads. For structured communication with message boundaries, you'd use message queues or sockets instead. Despite this simplicity, pipes are the backbone of the Unix philosophy of composing small, focused tools into powerful pipelines — each program does one thing, and pipes connect them.
