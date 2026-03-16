---
id: programming-fundamentals-file-io
title: File Input and Output
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-console-io
  type: soft
- id: programming-fundamentals-strings-introduction
  type: hard
tags:
- io
- files
- input
- output
stage: abstract-reasoning
status: draft
---

# File Input and Output

## Core Idea
File I/O reads data from and writes data to files on disk. Opening a file prepares it for reading or writing; closing it releases the resource. Files persist after the program ends.

## Explainer

Up to this point, every program you've written has been ephemeral — it takes input, does work, and when it finishes, everything it computed disappears. Console I/O lets you interact with users in real time, but the moment the program ends, those printed lines are gone. **File I/O** bridges this gap: it lets your program read data that already exists on disk and write data that persists after the program terminates. This is how real software works — configuration files, saved games, log files, databases, and spreadsheets all rely on file I/O.

The basic pattern has three steps: **open**, **read or write**, and **close**. Opening a file creates a connection between your program and a file on disk. You specify a **mode** that declares your intent: read mode (`"r"`) for reading existing data, write mode (`"w"`) for creating or overwriting a file, and append mode (`"a"`) for adding to the end of an existing file. In Python, `f = open("data.txt", "r")` opens a file for reading and gives you a **file object** stored in the variable `f`. You then call methods on that object — `f.read()` to get the entire contents as a string, or `f.readline()` to get one line at a time.

Closing a file with `f.close()` is essential because the operating system limits how many files a program can have open simultaneously, and data you've written may not actually reach the disk until the file is closed. Forgetting to close files is such a common bug that Python provides the `with` statement as a safety net: `with open("data.txt", "r") as f:` automatically closes the file when the indented block ends, even if an error occurs. This pattern is strongly preferred over manual open/close.

Because file contents arrive as strings, your string-handling skills from earlier become directly relevant. Reading a CSV file means reading lines of text and using `split(",")` to break each line into fields. Writing output means building strings with formatting and calling `f.write()`. The key mental shift is that files are sequential — you read from beginning to end, like a tape. Understanding this sequential access model prepares you for working with larger data sources where you can't load everything into memory at once.
