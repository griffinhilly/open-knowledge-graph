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

## Explainer

From basic input/output, you know how to get data from the user (`input()`) and display results (`print()`). But that interaction vanishes the moment the program ends — nothing is saved. If you want a program's data to survive between runs, you need to write it to a **file** on disk. File I/O extends the input/output model you already know: instead of reading from the keyboard and writing to the screen, you read from and write to named files in the file system.

The fundamental workflow has three steps: **open**, **read or write**, **close**. When you call `open('data.txt', 'r')`, the operating system locates the file, checks permissions, and returns a **file handle** — an object your program uses to interact with the file. The second argument is the **mode**: `'r'` for reading (the file must already exist), `'w'` for writing (creates a new file or *erases* an existing one), and `'a'` for appending (adds to the end without erasing). The distinction between `'w'` and `'a'` is critical — opening a file with `'w'` that already contains data will destroy that data immediately, before you write a single character.

Reading a file returns **strings**, always. If your file contains the number `42`, reading it gives you the string `"42"`, not the integer 42. You must explicitly convert with `int()` or `float()` before doing arithmetic. Similarly, when writing, you must convert numbers to strings first — `f.write(str(42))` — because `write()` only accepts strings. This is because files are fundamentally sequences of characters (in text mode), not typed data. Reading can be done all at once (`f.read()` returns the entire file as one string), line by line (`f.readline()` or iterating with `for line in f:`), or as a list of lines (`f.readlines()`). For most tasks, iterating line by line is the most memory-efficient and practical approach.

The most important practical rule is to **always close your files**. When you write to a file, the data often sits in a memory buffer before being flushed to disk. If your program crashes or you forget to call `f.close()`, that buffered data can be lost. The **context manager** pattern — `with open('data.txt', 'r') as f:` — solves this elegantly. The `with` block guarantees that `f.close()` is called when the block exits, even if an exception occurs inside it. This is not just a convenience; it is the standard, expected way to handle files in Python. Combining file I/O with your knowledge of string operations (splitting lines, stripping whitespace, parsing fields) gives you the ability to read structured data like CSV files, configuration files, and logs — a skill that opens the door to data persistence, configuration management, and processing real-world datasets.
