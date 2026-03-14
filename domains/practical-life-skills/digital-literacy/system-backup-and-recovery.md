---
id: system-backup-and-recovery
title: System Backup and Recovery
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: backup-and-data-protection
  type: hard
- id: file-system-basics
  type: soft
tags:
- backup
- recovery
- system-image
- disaster-recovery
stage: concrete-operations
status: draft
---

# System Backup and Recovery

## Core Idea
System backup goes beyond saving individual files — it captures the entire state of your operating system, installed programs, settings, and data so that a failed hard drive, ransomware attack, or corrupted update does not mean starting from scratch. System restore points save snapshots of critical system files that can roll back problematic changes, while full image backups clone your entire drive so it can be restored onto new hardware. Creating bootable recovery media (a USB or DVD that can start your computer when the main drive fails) is the safety net that makes recovery actually possible.

## How It's Best Learned
Create a system restore point on your computer right now and note how quickly it completes. Then create a full image backup to an external drive using your OS's built-in tool (Windows Backup, Time Machine on Mac). Finally, create a bootable recovery USB so you have the means to restore if your main drive fails.

## Common Misconceptions
- Cloud sync services like OneDrive or Google Drive are not system backups — they back up files but cannot restore your operating system, programs, or settings.
- System restore points do not save personal files — they only roll back system files, drivers, and registry changes.
- A backup you have never tested restoring is not a reliable backup; verification is a necessary part of any backup strategy.
