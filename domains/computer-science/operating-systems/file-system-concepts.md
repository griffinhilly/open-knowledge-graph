---
id: file-system-concepts
title: File System Concepts
domain: computer-science
course: operating-systems
prerequisites:
- id: basic-input-output
  type: soft
- id: file-io-basics
  type: soft
builds-toward:
- file-system-implementation
- directory-structures
tags:
- file
- metadata
- file-attributes
- file-operations
- file-types
stage: formal-systems
status: validated
---

# File System Concepts

## Core Idea
A file is the OS abstraction for persistent named data — a sequence of bytes stored on a device that survives process termination. Every file has metadata: name, type, size, permissions, timestamps, and a unique identifier. The file system is the OS subsystem responsible for organizing files into a hierarchical namespace, tracking their locations on storage devices, managing free space, and enforcing access control. The OS provides a uniform file interface (open, read, write, seek, close) that abstracts over the physical storage device, whether it is a hard disk, SSD, or network share.

## How It's Best Learned
Use stat() in Python or C to inspect a file's full metadata. Then read the ext4 or NTFS Wikipedia article to see how these abstractions are implemented.

## Common Misconceptions
- A file's name is not the file; the name is a directory entry pointing to metadata, so hard links can give one file multiple names.
- Deleting a file removes the directory entry; the data persists until the space is reused.
