---
id: file-system-journaling-crash-consistency
title: Crash Consistency and Journaling File Systems
domain: computer-science
course: operating-systems
prerequisites:
- id: file-system-implementation
  type: hard
- id: file-system-concepts
  type: hard
- id: write-ahead-logging
  type: soft
builds-toward: []
tags:
- file-systems
- journaling
- crash-consistency
- fsck
- write-ahead-logging
- persistence
stage: formal-systems
status: validated
---
# Crash Consistency and Journaling File Systems

## Core Idea
A single file operation, such as appending one block, changes several on-disk structures: the data block, the inode and the free-space bitmap. The disk writes them one at a time, so a power loss or crash in between can leave the structures disagreeing with one another. Crash consistency is the problem of making sure the file system can always return to a consistent state. Journaling solves it by first writing a description of the planned updates to a log (the journal), marking it committed, and only then writing the updates in place, so recovery can simply replay committed entries.

## How It's Best Learned
List the three writes needed to append a block, then enumerate every crash point and the state each leaves behind, as in the OSTEP chapter on crash consistency. Compare the cost of the older fix, a full-disk scan with `fsck`, against replaying a small journal. Finish by comparing data journaling with ordered (metadata-only) journaling, which ext4 uses by default.

## Common Misconceptions
- Writing blocks in a careful order is enough to avoid all inconsistency. (A crash can still fall between any two writes; ordering alone can reduce harm but cannot make a multi-block update atomic.)
- Journaling avoids extra disk writes. (It writes journaled blocks twice, once to the log and once to their final location, and trades that cost for fast, reliable recovery.)
- A journaling file system never loses recent data. (It keeps the structures consistent, but updates that were not yet committed to the journal at the time of the crash are lost.)

## Questions

```yaml
- question: "To append a block to a file, a file system must write a new data block, update the inode to point to it, and mark the block as used in the data bitmap. Suppose a crash occurs after the inode write reaches the disk but before the bitmap write. What is the problem after reboot?"
  type: multiple-choice
  options:
    - "There is no problem; the file is complete"
    - "The inode points to a block that the bitmap says is free, so the block could later be given to another file"
    - "The bitmap says a block is used, but no inode points to it, so the block is leaked"
    - "The file's old contents are erased"
  answer: 1
  explanation: "The inode and bitmap now disagree. Because the bitmap marks the block free, the allocator may hand it to another file, and two files would share one block. (If the data block itself was not yet written, the inode would also point to old, garbage contents.) Option C describes the reverse crash, where the bitmap was written but the inode was not."

- question: "In a journaling file system, at what point is a transaction considered committed, so that recovery will replay it?"
  type: multiple-choice
  options:
    - "When the transaction-begin block is written to the journal"
    - "When the first metadata block is written to the journal"
    - "When the transaction-end (commit) block has been written to the journal after the rest of the transaction"
    - "When all blocks have been written to their final locations on disk"
  answer: 2
  explanation: "The commit block is written only after the other journal blocks are safely on disk. On recovery, a transaction with a valid commit block is replayed; one without it is discarded. Writing blocks to their final locations, called checkpointing, happens after the commit."

- question: "Journaling improves crash recovery partly because it writes each journaled metadata block to disk only once."
  type: true-false
  answer: false
  explanation: "Journaled blocks are written twice: first into the journal, then to their home locations during checkpointing. The benefit is that recovery reads only the small journal instead of scanning the whole disk."

- question: "Why is recovery with a journal usually much faster than running fsck on a large disk?"
  type: short-answer
  answer: "fsck must scan all of the file system's metadata (every inode, bitmap and directory) to find and repair inconsistencies, so its time grows with the size of the disk. Journal recovery reads only the recent, small journal and replays committed transactions, so its time depends on how much recent activity there was, not on disk size."
  explanation: "As disks grew to terabytes, full scans took long enough to make journaling, used in ext3, ext4, NTFS and others, the standard approach."
```

## Explainer

From file system implementation you know that a file is described by an inode, its contents live in data blocks, and a bitmap records which blocks are free. Now look at an ordinary operation: appending 4 KB to a file. Three on-disk structures must change. A new **data block** is written, the **inode** gains a pointer to it and a larger size, and the **data bitmap** marks the block used.

The disk can persist only one write at a time, and the system may crash or lose power between any two. Each crash point leaves a different mess. If only the data block is written, nothing points to it, so the data is lost but the structures still agree. If only the inode is written, it points to a block that may hold old garbage, and the bitmap still calls that block free. If only the bitmap is written, a block is marked used but belongs to no file, so space leaks. This is the **crash-consistency problem**.

The older answer was to let crashes happen and repair afterward. A tool called **fsck** scans every inode, directory and bitmap and fixes disagreements. It works, but it is slow, because its time grows with the size of the disk. On a large disk it can take many minutes or longer.

**Journaling**, a form of write-ahead logging, avoids the scan. Before touching the real structures, the file system writes a **transaction** to a reserved area called the journal: a begin block, copies of the blocks it is about to change, and finally a **commit** block. Once the commit block is on disk, the transaction is durable. The file system then writes the blocks to their real locations, a step called **checkpointing**, and later frees that journal space. After a crash, recovery reads the journal, replays every transaction that has a commit block, and ignores incomplete ones. Either the whole update happens or none of it does.

Copying user data into the journal doubles the cost of every write, so most systems journal only metadata. In ext4's default **ordered** mode, the data block is written to its final location before the metadata transaction commits. That way an inode never ends up pointing at garbage. Other file systems, such as ZFS and Btrfs, use **copy-on-write** instead. They never overwrite live blocks in place, and they switch to the new version with a single atomic pointer update.
