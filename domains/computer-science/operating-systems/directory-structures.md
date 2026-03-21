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

## Questions

```yaml
- question: "A Unix file /home/alice/project.txt has a link count of 2. Alice runs 'rm /home/alice/project.txt'. What happens to the file's data on disk?"
  type: multiple-choice
  options:
    - "The file data is immediately deleted because rm removes files"
    - "The data is moved to a trash folder and deleted after 30 days"
    - "The file data persists because a second hard link still points to the same inode; only this directory entry is removed and the link count drops to 1"
    - "The file data is corrupted because removing one hard link damages the shared inode"
  answer: 2
  explanation: "rm removes a directory entry and decrements the inode's link count. Since the link count drops from 2 to 1 (still positive), the file system does not deallocate the inode or its data blocks. The file remains fully accessible through the second hard link. Data is only reclaimed when the link count reaches zero — meaning all directory entries pointing to that inode have been removed."

- question: "A user tries to create a hard link on filesystem A pointing to a file on a mounted external drive (filesystem B). The OS refuses. Why?"
  type: multiple-choice
  options:
    - "Hard links can only be created by root for security reasons"
    - "Hard links cannot span file systems because inode numbers are only unique within a single file system; the reference would be meaningless on the other device"
    - "Hard links are not supported on external drives, only on the main partition"
    - "The OS refuses because cross-filesystem hard links would create cycles in the directory tree"
  answer: 1
  explanation: "A hard link stores an inode number. Inode numbers are indices into a specific file system's inode table — inode 12345 on filesystem A refers to a completely different (or nonexistent) file than inode 12345 on filesystem B. A cross-filesystem hard link would be nonsensical. Symbolic links sidestep this problem by storing a path string rather than an inode number; the OS re-resolves the path at access time, so the target can live anywhere."

- question: "Moving a file to a different directory within the same file system is instantaneous regardless of file size, because the operation only updates directory entries without touching the file's data blocks."
  type: true-false
  answer: true
  explanation: "A same-filesystem move is implemented as a rename: the OS removes the directory entry in the source directory and creates one in the destination directory, both referencing the same inode. No data is read or written; only the two directory files are modified. This is why moving a 50 GB file across folders on the same drive is instant, while copying it — which must allocate new data blocks and duplicate all content — takes proportional time."

- question: "Creating a hard link to a file produces a second copy of the file's data blocks, similar to the cp command."
  type: true-false
  answer: false
  explanation: "A hard link creates only a new directory entry pointing to the existing inode. No data is duplicated. Both names resolve to the same inode, which points to the same data blocks on disk. Running 'ls -i' on both names will show the same inode number. Only the cp command allocates a new inode and copies data blocks. Hard links use negligible disk space and are created instantaneously — they are name aliases, not copies."

- question: "Explain what causes a symbolic link to 'dangle,' and why this cannot happen with a hard link pointing to the same target file."
  type: short-answer
  answer: "A symbolic link stores its target as a path string. If the target file is deleted or moved, the OS can no longer resolve that path — the symlink dangles, pointing at nothing. A hard link stores a direct reference to the inode. As long as any hard link exists, the inode's link count is at least 1, so the file system will not deallocate the inode or its data. The data can only be deleted when every hard link has been removed and the link count reaches zero."
  explanation: "A hard link is part of the file's identity — it keeps the file alive by contributing to the link count. A symbolic link is external to the file — deleting the target file does not update or invalidate the symlink. This asymmetry also explains why hard links cannot reference directories in most Unix implementations: allowing them could create cycles in the directory graph, breaking path-resolution algorithms that assume an acyclic hierarchy."
```

## Explainer

From your study of file system concepts, you know that a file system provides persistent, named storage — it gives structure to raw disk blocks so that users and programs can create, find, and organize files. **Directory structures** are the organizational layer that maps human-readable names to the underlying file data, and **path resolution** is the algorithm the OS uses to navigate that structure.

A directory is itself a file, but instead of holding user data, it holds a table of entries, each mapping a name (like `report.txt`) to an **inode number** — the internal identifier the file system uses to locate the file's metadata and data blocks. When you type `ls`, the OS reads the directory file and shows you the names. When you open `/home/alice/report.txt`, the OS performs **path resolution**: it starts at the root directory's inode (always inode 2 on most Unix systems), looks up the entry named `home` to find its inode, reads that directory to find `alice`, reads that directory to find `report.txt`, and finally retrieves the file's inode to access its data. Each `/` in a path is a directory lookup.

The basic directory structure is a **tree** — each file has exactly one parent directory, and the hierarchy fans out from the root. But Unix file systems support two features that complicate this picture. A **hard link** creates an additional directory entry pointing to the same inode. The file does not get copied; two names simply refer to the same underlying data. This turns the tree into a **directed acyclic graph** (DAG), because one inode can be reachable through multiple paths. The file is only deleted when its **link count** (the number of directory entries pointing to it) drops to zero. A **symbolic link** (symlink) works differently: it is a small file whose content is a path string. When the OS encounters a symlink during path resolution, it reads the stored path and restarts resolution from that point. Unlike hard links, symlinks can cross file system boundaries and can point to directories, but they can also **dangle** — if the target is deleted, the symlink points to nothing.

Understanding these mechanisms explains many everyday behaviors. Moving a file within the same file system is instant because it only changes directory entries, not data. Renaming is the same operation. Copying is slow because it creates a new inode and duplicates data blocks. The `..` entry in every directory is a hard link to the parent directory, which is why directories always have a link count of at least 2 (the directory's own entry in its parent, plus the `.` entry inside itself). These details matter when you encounter permission errors, circular symlinks, or puzzling disk usage reports — they all trace back to how directories map names to inodes.
