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
