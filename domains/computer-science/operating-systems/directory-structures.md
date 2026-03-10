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
status: draft
---

# Directory Structures and Path Resolution

## Core Idea
A directory is a special file that maps filenames to file identifiers (inode numbers on Unix), organizing files into a hierarchical namespace. The standard model is a rooted tree of directories, but hard links allow a single file to appear in multiple directories, technically making the structure a DAG. Path resolution is the process of traversing this hierarchy: for an absolute path like /usr/bin/python, the OS starts at the root inode, looks up 'usr' to find a directory inode, looks up 'bin' in that directory, and so on. Symbolic (soft) links store a target path as data and are resolved at access time, unlike hard links which are direct inode references.

## Common Misconceptions
- Hard links cannot span file systems because inode numbers are only unique within one filesystem.
- Deleting a file with multiple hard links only removes one directory entry; the file persists until all hard links are deleted and the link count reaches zero.
