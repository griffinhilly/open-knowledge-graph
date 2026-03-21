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

## Questions

```yaml
- question: "A file called 'data.txt' already contains several lines of saved records. A programmer opens it with open('data.txt', 'w') and writes one new line. What happens to the original records?"
  type: multiple-choice
  options:
    - "The new line is added after the original records, which are preserved"
    - "The original records are preserved and the file now has both old and new content"
    - "The file is overwritten from the beginning — all original records are permanently deleted"
    - "An error is raised because the file already exists and write mode requires an empty file"
  answer: 2
  explanation: "Write mode ('w') creates a new empty file at the specified path — or, if the file already exists, truncates it to zero length before writing. This destroys all existing content before a single byte of new content is written. To add to an existing file without destroying its contents, use append mode ('a'), which positions the write cursor at the end of the existing file. Confusing 'w' and 'a' is one of the most common and consequential file I/O mistakes because data loss is silent and immediate."

- question: "Why is the 'with open(...)' pattern preferred over manually calling open() and later f.close()?"
  type: multiple-choice
  options:
    - "It reads files significantly faster by using buffered I/O internally"
    - "It removes the need to specify a file mode, choosing the correct mode automatically"
    - "It automatically closes the file when the block exits, even if an error occurs inside the block, preventing resource leaks"
    - "It allows multiple files to be open simultaneously without hitting OS limits"
  answer: 2
  explanation: "The 'with' statement implements a context manager that guarantees the file is closed when the indented block exits — whether that exit is normal completion or an exception. With manual open/close, if an error occurs between open() and close(), close() is never called, leaving the file handle open (a resource leak) and potentially leaving buffered write data unflushed to disk. The 'with' pattern makes the close automatic and unconditional, eliminating this bug class entirely."

- question: "When a Python program ends without explicitly closing a file it opened for writing, the data written to that file is guaranteed to be saved to disk."
  type: true-false
  answer: false
  explanation: "File writes may be buffered — the operating system or Python runtime may hold written data in memory temporarily before flushing it to disk. Closing a file explicitly (or using a 'with' block) triggers the flush, ensuring buffered data reaches disk. If the program ends without closing the file, the buffer may not be flushed, and the last writes may be lost — especially if the program crashes or is killed. This is why 'always close your files' is not just about resource management but about data integrity."

- question: "In basic file I/O, files are accessed sequentially — reading proceeds from the beginning toward the end, rather than jumping to arbitrary positions."
  type: true-false
  answer: true
  explanation: "The sequential access model means a file handle maintains a current position that advances as you read or write. f.readline() reads the next line from wherever the cursor currently is; f.read() reads from the current position to the end. This is analogous to reading a tape or a scroll — you move forward through the content in order. While Python does support random access (using f.seek()), the default and conceptually primary model is sequential, which prepares learners for working with large data sources where loading everything into memory at once is impractical."

- question: "Why does the choice of file mode ('r', 'w', or 'a') matter, and what would happen if you used 'w' when you intended 'a'?"
  type: short-answer
  answer: "The mode declares your intent to the operating system and determines how the file handle behaves. 'r' opens an existing file for reading only — writing raises an error. 'w' creates a new file or, critically, truncates an existing file to zero bytes before writing, permanently deleting all previous content. 'a' opens an existing file and positions the write cursor at the end, so new content is appended after everything already there. Using 'w' instead of 'a' silently destroys all existing file content before writing your new data — a data loss bug with no warning or recovery unless a backup exists."
  explanation: "The key danger is that write mode's destructive behavior is silent and immediate. There is no 'are you sure?' prompt. A program that opens a log file in 'w' mode on each run will start each run with a fresh empty file, erasing all history from previous runs — which may be exactly what a naive programmer expects, but catastrophic if the intent was to accumulate records over time. Understanding what each mode does before using it is an essential habit."
```

## Explainer

Up to this point, every program you've written has been ephemeral — it takes input, does work, and when it finishes, everything it computed disappears. Console I/O lets you interact with users in real time, but the moment the program ends, those printed lines are gone. **File I/O** bridges this gap: it lets your program read data that already exists on disk and write data that persists after the program terminates. This is how real software works — configuration files, saved games, log files, databases, and spreadsheets all rely on file I/O.

The basic pattern has three steps: **open**, **read or write**, and **close**. Opening a file creates a connection between your program and a file on disk. You specify a **mode** that declares your intent: read mode (`"r"`) for reading existing data, write mode (`"w"`) for creating or overwriting a file, and append mode (`"a"`) for adding to the end of an existing file. In Python, `f = open("data.txt", "r")` opens a file for reading and gives you a **file object** stored in the variable `f`. You then call methods on that object — `f.read()` to get the entire contents as a string, or `f.readline()` to get one line at a time.

Closing a file with `f.close()` is essential because the operating system limits how many files a program can have open simultaneously, and data you've written may not actually reach the disk until the file is closed. Forgetting to close files is such a common bug that Python provides the `with` statement as a safety net: `with open("data.txt", "r") as f:` automatically closes the file when the indented block ends, even if an error occurs. This pattern is strongly preferred over manual open/close.

Because file contents arrive as strings, your string-handling skills from earlier become directly relevant. Reading a CSV file means reading lines of text and using `split(",")` to break each line into fields. Writing output means building strings with formatting and calling `f.write()`. The key mental shift is that files are sequential — you read from beginning to end, like a tape. Understanding this sequential access model prepares you for working with larger data sources where you can't load everything into memory at once.
