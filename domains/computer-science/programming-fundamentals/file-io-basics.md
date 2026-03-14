---
id: file-io-basics
title: File I/O Basics
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: basic-input-output
  type: hard
- id: string-operations
  type: hard
- id: error-handling-exceptions
  type: soft
tags:
- file I/O
- open
- read
- write
- context manager
- persistence
stage: abstract-reasoning
status: validated
---

# File I/O Basics

## Core Idea
File I/O allows programs to persist data beyond a single run by reading from and writing to files on disk. Files are opened with an open() call specifying a mode (read 'r', write 'w', append 'a'); they must be closed after use to flush buffers and release the file handle. Context managers (with open(...) as f:) handle closing automatically even if an error occurs. Reading returns strings; numeric data must be parsed after reading and formatted before writing.

## How It's Best Learned
Write a program that saves a to-do list to a file and reads it back on the next run. Experiment with write vs. append mode. Handle the FileNotFoundError that occurs when the file does not yet exist.

## Common Misconceptions
- Forgetting to close files, leading to incomplete writes when the buffer is not flushed.
- Opening in write ('w') mode when intending to add to existing content — 'w' truncates the file.
- Assuming file.read() returns numbers — all file content is text and must be converted.
