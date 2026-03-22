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

## Questions

```yaml
- question: "A file /home/alice/report.txt is deleted. Which statement most accurately describes what happens to the file's data?"
  type: multiple-choice
  options:
    - "The data is immediately erased from disk"
    - "The directory entry is removed; the data persists until the OS reclaims the blocks"
    - "The inode is deleted, but the data blocks remain indefinitely"
    - "Nothing happens until the file system is unmounted"
  answer: 1
  explanation: "Deleting a file removes the directory entry that maps the name to the inode — not the inode or data itself. The OS marks the blocks as free space only when no directory entries point to the inode (link count reaches zero), and even then the data persists until overwritten. This is why deleted files can sometimes be recovered."

- question: "Files /home/alice/notes.txt and /home/bob/backup.txt are hard links to the same inode. Alice deletes her copy. What happens to Bob's file?"
  type: multiple-choice
  options:
    - "Both files are deleted because they share the same inode"
    - "Bob's file is deleted because Alice's was the original link"
    - "Bob's file still works; the inode and data persist because one link remains"
    - "The data is copied to Bob's path before Alice's link is removed"
  answer: 2
  explanation: "An inode persists as long as at least one directory entry (hard link) points to it. Deleting one name only removes that directory entry and decrements the inode's link count. When the link count reaches zero, the OS frees the inode and data blocks. Since Bob's link still exists, the file is fully accessible — the concept of an 'original' link is a misconception; all hard links are equal."

- question: "A file's name is stored in the inode alongside its permissions, size, and timestamps."
  type: true-false
  answer: false
  explanation: "The file's name lives in a directory entry, not the inode. The inode stores metadata — permissions, size, timestamps, owner, and data block pointers — but has no record of what names point to it. This separation is why hard links work: multiple directory entries in different directories can map different names to the same inode number, giving one file multiple names."

- question: "On a Unix file system, a single file can be accessed through multiple different pathnames simultaneously."
  type: true-false
  answer: true
  explanation: "Hard links allow multiple directory entries — in the same or different directories — to map to the same inode. All names are equally valid; none is more 'original' than another. The file's data and metadata are shared; only the name-to-inode mappings are separate entries in directory files."

- question: "Why is the separation between a file's name (stored in a directory entry) and its metadata and data (stored in an inode) architecturally significant? Give one concrete consequence of this design."
  type: short-answer
  answer: "Because the name is separate from the inode, the same underlying file can have multiple names (hard links) pointing to it. Deleting one name only removes that directory entry; the file persists until no names remain. Other consequences include: renaming a file is cheap (just update the directory entry, no data moves), and stat() returns inode metadata regardless of which name was used to access the file."
  explanation: "This separation is the key insight of Unix file system design. The name is ephemeral — a pointer in a directory; the inode is the authoritative record of the file's existence. This also explains why deleting a file that another process has open doesn't destroy it immediately: the process holds an open file descriptor referencing the inode directly, independent of any directory entry."
```

## Explainer

At its heart, a file system answers a deceptively simple question: how do you store named data on a device that only understands numbered blocks? A hard disk or SSD is just a flat array of fixed-size blocks (typically 512 bytes or 4 KB). The file system builds the abstractions of files, directories, names, and permissions on top of this raw storage — much like how an operating system builds the abstraction of processes on top of raw CPU time. If you have worked with basic I/O, you have used the result of this abstraction every time you called `open()`, `read()`, or `write()`.

A **file** is the fundamental unit: a named, persistent sequence of bytes. But a file is more than its data. The OS stores **metadata** alongside each file — the owner, permissions, timestamps (created, modified, accessed), size, and the physical locations of its data blocks on disk. This metadata is typically stored in a structure called an **inode** (on Unix-like systems) or a Master File Table entry (on NTFS). The key insight is that the file's name is *not* part of the inode. The name lives in a **directory entry**, which is simply a mapping from a human-readable name to an inode number. This separation is why hard links work: two different names in two different directories can point to the same inode, and therefore the same data. The file exists as long as at least one name points to it.

The **file system interface** that the OS exposes to programs is deliberately uniform. Whether the underlying storage is a magnetic disk, an SSD, a USB drive, or a network share, you use the same operations: **open** (get a file descriptor), **read** (copy bytes from the file into memory), **write** (copy bytes from memory to the file), **seek** (move the read/write position), and **close** (release the file descriptor). This abstraction is powerful because application code does not need to know or care about the physical storage technology. The OS translates these logical operations into the appropriate device-specific commands — sequential reads on a hard disk, page-level writes on an SSD, or network packets for a remote file system.

Directories provide the organizational structure. A **directory** is itself a special file whose contents are a list of (name, inode number) pairs. Directories can contain other directories, creating the familiar hierarchical tree structure — `/home/user/documents/report.txt` is a path through four directories to reach a file. This hierarchy is a namespace: it allows millions of files to coexist with human-readable, organized names. The file system must also manage **free space** — tracking which blocks on the device are available for new data — and enforce **access control** — ensuring that only authorized users can read, write, or execute a file. These concerns are what separate a file system from a simple key-value store, and they become central when you study file system implementation next.
