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
stage: formal-systems
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

## Questions

```yaml
- question: "A file named 'data.txt' contains the text 'Hello World'. A program opens it with open('data.txt', 'w') and writes 'Goodbye'. What does the file contain after the program finishes?"
  type: multiple-choice
  options:
    - "'Hello WorldGoodbye' — the new content is appended to the existing content"
    - "'Goodbye\nHello World' — the new content is prepended"
    - "'Goodbye' — opening in 'w' mode erases the file before any writing occurs"
    - "An error is raised because the file already exists"
  answer: 2
  explanation: "Opening a file in 'w' (write) mode truncates the file immediately — the existing contents are destroyed the moment open() is called, before a single character is written. This happens even if the program crashes before writing anything. 'Hello World' is gone and 'Goodbye' is all that remains. This is one of the most dangerous pitfalls in file I/O. To add content without erasing, use 'a' (append) mode. To read and rewrite selectively, read the file first, modify in memory, then write back."

- question: "A file contains the line '42'. After reading it with line = f.readline(), a student writes result = line + 10. What happens?"
  type: multiple-choice
  options:
    - "result is the integer 52"
    - "result is the string '4210'"
    - "A TypeError is raised — you cannot add a string and an integer"
    - "result is '42\\n10' — the newline from readline is included"
  answer: 2
  explanation: "All file content is read as strings — f.readline() returns '42\\n' (with a trailing newline), not the integer 42. Attempting to add a string and an integer raises a TypeError. To do arithmetic, you must explicitly convert: result = int(line.strip()) + 10. This type conversion step is always required when reading numeric data from files, user input, or network responses — they all arrive as text. Forgetting this produces TypeErrors or, in languages with implicit coercion, silent concatenation bugs like '4210'."

- question: "Using a context manager (with open(...) as f:) guarantees that the file is closed even if an exception occurs inside the with block."
  type: true-false
  answer: true
  explanation: "This is the primary purpose of the context manager pattern for files. The with statement calls f.__exit__() when the block ends, whether normally or due to an exception. f.__exit__() calls f.close(), which flushes the write buffer and releases the file handle. Without a context manager, an exception before f.close() would leave the file open and potentially lose buffered data. The context manager is not just a stylistic preference — it is the safe, standard way to guarantee proper cleanup."

- question: "Forgetting to close a file after writing is a minor stylistic issue; all written data will be saved correctly as long as the write() calls completed without error."
  type: true-false
  answer: false
  explanation: "This is a dangerous misconception. When you write to a file, data is often held in a memory buffer before being flushed to disk. If the program ends abnormally, or if the file is not explicitly closed (which triggers a flush), buffered data can be lost — even if write() returned no error. The buffer-to-disk flush only happens when close() is called (or flush() is called explicitly). This is why unclosed files can result in truncated output or missing data. The context manager pattern prevents this by guaranteeing close() is always called."

- question: "Explain the difference between opening a file in 'w' mode versus 'a' mode. Why is confusing these two modes particularly dangerous?"
  type: short-answer
  answer: "'w' (write) mode truncates the file immediately on open — any existing content is destroyed before you write a single byte. 'a' (append) mode opens the file and positions the write pointer at the end, so new content is added after existing content. Confusing them is dangerous because the data loss from 'w' mode is immediate and silent: no error is raised, and by the time you realize the mistake, the original content is gone. There is no 'undo' — the file is overwritten at the OS level."
  explanation: "A common scenario: a developer means to log to an existing log file but uses 'w' instead of 'a', silently erasing weeks of logs on the next program run. The distinction matters most when working with files that accumulate data over time (logs, journals, databases). A safe workflow when unsure: read the file first, modify in memory, then write back — or use 'a' when the intent is to add, never to replace. Some programs even back up files before writing to avoid this class of error entirely."
```

## Explainer

From basic input/output, you know how to get data from the user (`input()`) and display results (`print()`). But that interaction vanishes the moment the program ends — nothing is saved. If you want a program's data to survive between runs, you need to write it to a **file** on disk. File I/O extends the input/output model you already know: instead of reading from the keyboard and writing to the screen, you read from and write to named files in the file system.

The fundamental workflow has three steps: **open**, **read or write**, **close**. When you call `open('data.txt', 'r')`, the operating system locates the file, checks permissions, and returns a **file handle** — an object your program uses to interact with the file. The second argument is the **mode**: `'r'` for reading (the file must already exist), `'w'` for writing (creates a new file or *erases* an existing one), and `'a'` for appending (adds to the end without erasing). The distinction between `'w'` and `'a'` is critical — opening a file with `'w'` that already contains data will destroy that data immediately, before you write a single character.

Reading a file returns **strings**, always. If your file contains the number `42`, reading it gives you the string `"42"`, not the integer 42. You must explicitly convert with `int()` or `float()` before doing arithmetic. Similarly, when writing, you must convert numbers to strings first — `f.write(str(42))` — because `write()` only accepts strings. This is because files are fundamentally sequences of characters (in text mode), not typed data. Reading can be done all at once (`f.read()` returns the entire file as one string), line by line (`f.readline()` or iterating with `for line in f:`), or as a list of lines (`f.readlines()`). For most tasks, iterating line by line is the most memory-efficient and practical approach.

The most important practical rule is to **always close your files**. When you write to a file, the data often sits in a memory buffer before being flushed to disk. If your program crashes or you forget to call `f.close()`, that buffered data can be lost. The **context manager** pattern — `with open('data.txt', 'r') as f:` — solves this elegantly. The `with` block guarantees that `f.close()` is called when the block exits, even if an exception occurs inside it. This is not just a convenience; it is the standard, expected way to handle files in Python. Combining file I/O with your knowledge of string operations (splitting lines, stripping whitespace, parsing fields) gives you the ability to read structured data like CSV files, configuration files, and logs — a skill that opens the door to data persistence, configuration management, and processing real-world datasets.
