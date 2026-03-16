---
id: cloud-storage-basics
title: Cloud Storage Basics
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: file-system-basics
  type: hard
- id: internet-safety-basics
  type: soft
builds-toward:
- backup-and-data-protection
tags:
- cloud
- storage
- sync
- sharing
- backup
stage: concrete-operations
status: validated
---

# Cloud Storage Basics

## Core Idea
Cloud storage services (Google Drive, Dropbox, iCloud, OneDrive) store files on remote servers, making them accessible from any device with internet access. Sync clients automatically mirror local folders to the cloud, providing a form of continuous backup. Sharing files via link rather than email attachments is more efficient and allows version control. Understanding storage limits, sharing permissions (view vs. edit), and the difference between sync and backup prevents data loss.

## How It's Best Learned
Set up a cloud folder, upload several files, share one via link with view-only access, and verify the file appears on a second device. Then practice revoking access.

## Common Misconceptions
- Cloud storage is not the same as a backup — if you delete a file locally and it syncs, the cloud copy is also deleted.
- Sharing a link does not mean the recipient has a permanent copy; access can be revoked.
- Free storage tiers have limits; large media libraries can exhaust them quickly.

## Explainer

From your study of file systems, you know that files live in a hierarchy of folders on a physical disk, and every file has a location — a path. Cloud storage extends that mental model by moving the disk off of your device and onto servers owned by a company (Google, Apple, Microsoft, Dropbox, etc.). The folder hierarchy works exactly the same way; the difference is that the files don't live locally. When you open a file from Google Drive, your device downloads it from the remote server. When you save changes, those changes are sent back. From the user's perspective it feels like a local folder, but the actual storage is elsewhere.

**Sync clients** — the small background apps these services install — automate this mirroring continuously. When you drop a file into your Google Drive folder, the sync client detects the change and uploads it. When you edit a file on your phone, the change propagates to your laptop within seconds. This is genuinely useful, but it introduces a critical property you must understand: **sync is not backup**. If you delete a file locally, the sync client interprets that as an intentional change and deletes the cloud copy too. If you accidentally overwrite a file, the overwritten version syncs. Sync preserves your latest state everywhere — it does not protect you from yourself. True backup stores a separate, independent copy that does not mirror deletions (which is why cloud services offer a separate "backup" product distinct from "sync").

**Sharing** is where cloud storage becomes a collaboration tool. Instead of emailing a 50 MB file, you store it once and share a link. The recipient accesses the same file from the server — no attachment bloat, no version confusion. Permissions let you control what recipients can do: **view-only** access means they can read but not change; **edit** access means they can modify the file directly (which also means their changes propagate to your copy). Shared links can be scoped to specific people or made public. Crucially, access can be revoked at any time — the recipient never "owns" a copy unless they explicitly download and save one. This is the key difference from an email attachment, where the recipient's copy is permanent.

A few practical habits follow from these mechanics. First, understand your storage limit and track what's consuming it — video files fill quotas quickly. Second, if you are relying on cloud storage as a backup, periodically verify that your sync is actually running; a misconfigured sync that has silently stopped updating is not protecting you. Third, before sharing edit access to an important document, consider whether you want version history enabled (most services offer it) so that accidental edits can be reversed. Cloud storage is powerful and convenient, but treating sync as infallible backup is the most common way people lose files they thought were safe.

