---
id: directory-structures
title: Directory Structures and Path Resolution
domain: computer-science
course: operating-systems
prerequisites:
- id: file-system-concepts
  type: hard
builds-toward:
- file-system-implementation
tags:
- directory
- path
- hard-link
- symbolic-link
- DAG
- tree-structure
stage: formal-systems
status: validated
---

# Directory Structures and Path Resolution

## Core Idea
A directory is a special file that maps filenames to file identifiers (inode numbers on Unix), organizing files into a hierarchical namespace. The standard model is a rooted tree of directories, but hard links allow a single file to appear in multiple directories, technically making the structure a DAG. Path resolution is the process of traversing this hierarchy: for an absolute path like /usr/bin/python, the OS starts at the root inode, looks up 'usr' to find a directory inode, looks up 'bin' in that directory, and so on. Symbolic (soft) links store a target path as data and are resolved at access time, unlike hard links which are direct inode references.

## Common Misconceptions
- Hard links cannot span file systems because inode numbers are only unique within one filesystem.
- Deleting a file with multiple hard links only removes one directory entry; the file persists until all hard links are deleted and the link count reaches zero.

## Explainer

From your study of file system concepts, you know that a file system provides persistent, named storage — it gives structure to raw disk blocks so that users and programs can create, find, and organize files. **Directory structures** are the organizational layer that maps human-readable names to the underlying file data, and **path resolution** is the algorithm the OS uses to navigate that structure.

A directory is itself a file, but instead of holding user data, it holds a table of entries, each mapping a name (like `report.txt`) to an **inode number** — the internal identifier the file system uses to locate the file's metadata and data blocks. When you type `ls`, the OS reads the directory file and shows you the names. When you open `/home/alice/report.txt`, the OS performs **path resolution**: it starts at the root directory's inode (always inode 2 on most Unix systems), looks up the entry named `home` to find its inode, reads that directory to find `alice`, reads that directory to find `report.txt`, and finally retrieves the file's inode to access its data. Each `/` in a path is a directory lookup.

The basic directory structure is a **tree** — each file has exactly one parent directory, and the hierarchy fans out from the root. But Unix file systems support two features that complicate this picture. A **hard link** creates an additional directory entry pointing to the same inode. The file does not get copied; two names simply refer to the same underlying data. This turns the tree into a **directed acyclic graph** (DAG), because one inode can be reachable through multiple paths. The file is only deleted when its **link count** (the number of directory entries pointing to it) drops to zero. A **symbolic link** (symlink) works differently: it is a small file whose content is a path string. When the OS encounters a symlink during path resolution, it reads the stored path and restarts resolution from that point. Unlike hard links, symlinks can cross file system boundaries and can point to directories, but they can also **dangle** — if the target is deleted, the symlink points to nothing.

Understanding these mechanisms explains many everyday behaviors. Moving a file within the same file system is instant because it only changes directory entries, not data. Renaming is the same operation. Copying is slow because it creates a new inode and duplicates data blocks. The `..` entry in every directory is a hard link to the parent directory, which is why directories always have a link count of at least 2 (the directory's own entry in its parent, plus the `.` entry inside itself). These details matter when you encounter permission errors, circular symlinks, or puzzling disk usage reports — they all trace back to how directories map names to inodes.
