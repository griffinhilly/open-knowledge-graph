---
id: backup-and-data-protection
title: Backup and Data Protection
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: file-system-basics
  type: hard
- id: cloud-storage-basics
  type: soft
tags:
- backup
- data-loss
- recovery
- redundancy
stage: concrete-operations
status: validated
---

# Backup and Data Protection

## Core Idea
Data loss from hardware failure, ransomware, accidental deletion, or theft is a matter of when, not if, for most people. The 3-2-1 backup rule is the standard: keep 3 copies of data, on 2 different media types, with 1 stored offsite (or in the cloud). Backups must be tested by performing a restore — an untested backup is not a backup. Automating backups removes the dependency on remembering to do them manually.

## How It's Best Learned
Implement a 3-2-1 backup for your most important files: local external drive + cloud. Set backups to run automatically, then practice restoring a file from the backup to confirm it works.

## Common Misconceptions
- Having one copy 'in the cloud' is one copy, not a backup strategy on its own.
- RAID (mirrored drives) is redundancy, not backup — it does not protect against ransomware or accidental deletion.
- Backups are unnecessary until you experience a loss — by then it is too late.
