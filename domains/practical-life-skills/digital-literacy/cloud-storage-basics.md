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

## Questions

```yaml
- question: "Priya saves all her vacation photos to Google Drive, then deletes them from her phone to free up space. Later she finds they are missing from Google Drive too. What most likely happened?"
  type: multiple-choice
  options:
    - "Google Drive has a storage limit that automatically deleted her photos"
    - "The sync client interpreted the local deletion as an intentional change and deleted the cloud copies as well"
    - "Google Drive does not support photo storage"
    - "She needed to share the photos before they would be saved to the cloud"
  answer: 1
  explanation: "This is the critical sync-vs-backup distinction. Sync clients mirror your current state everywhere — when Priya deleted photos locally, the sync client propagated that deletion to the cloud. Sync does not protect you from yourself. A true backup stores a separate, independent copy that does not mirror deletions. This is the most common way people lose files they thought were safely stored in the cloud."

- question: "You share a report with a colleague using a view-only cloud link. Two days later, you fix a typo in the document. What does your colleague see if they click the same link?"
  type: multiple-choice
  options:
    - "The original version with the typo, because the link was created before the fix"
    - "The corrected version, because the link points to the live cloud file — not a frozen snapshot"
    - "An error message, because the document was modified after sharing"
    - "The corrected version, but only if you reshare the link after editing"
  answer: 1
  explanation: "Cloud sharing links point to the live file on the server, not a copy made at the moment of sharing. Any changes you make are immediately reflected when the recipient accesses the link. This is a key advantage over email attachments: with an attachment, each person has an isolated copy and edits do not propagate. The tradeoff is that if you accidentally break the document, collaborators see the broken version too."

- question: "Cloud sync is a reliable backup strategy because any file stored in the cloud is protected from accidental deletion."
  type: true-false
  answer: false
  explanation: "Sync is not backup. The core property of a sync client is that it mirrors your current state — deletions and overwrites included. If you accidentally delete a file and the sync runs before you notice, the cloud copy is deleted too. A true backup maintains a separate copy that does not mirror destructive changes, often with version history so you can recover older states."

- question: "When you share a cloud file via a link with view-only permissions, the recipient can read the file but cannot modify it, and you can revoke their access by disabling the link."
  type: true-false
  answer: true
  explanation: "View-only sharing means read access but no write access. Because the link points to a server-side permission, revoking the link or changing permissions immediately removes access. This is the fundamental difference from an email attachment, where the recipient's copy is permanent and cannot be recalled."

- question: "Explain the difference between cloud sync and a true backup, and describe a situation where treating sync as backup could lead to data loss."
  type: short-answer
  answer: "Cloud sync mirrors your current file state to the cloud and all devices in real time — any add, change, or delete is propagated everywhere. A true backup stores a separate, independent copy that does not mirror destructive actions and lets you recover older versions. Treating sync as backup fails when you accidentally delete a file: the sync client propagates the deletion to the cloud before you realize the mistake, leaving no copy to recover. Similarly, if ransomware encrypts local files, the encrypted versions sync to the cloud and overwrite the originals."
  explanation: "The distinction matters because sync and backup solve different problems. Sync solves 'access everywhere.' Backup solves 'recover from mistakes and disasters.' They are complementary, not interchangeable. Many cloud providers offer both as distinct products for this reason."
```

## Explainer

From your study of file systems, you know that files live in a hierarchy of folders on a physical disk, and every file has a location — a path. Cloud storage extends that mental model by moving the disk off of your device and onto servers owned by a company (Google, Apple, Microsoft, Dropbox, etc.). The folder hierarchy works exactly the same way; the difference is that the files don't live locally. When you open a file from Google Drive, your device downloads it from the remote server. When you save changes, those changes are sent back. From the user's perspective it feels like a local folder, but the actual storage is elsewhere.

**Sync clients** — the small background apps these services install — automate this mirroring continuously. When you drop a file into your Google Drive folder, the sync client detects the change and uploads it. When you edit a file on your phone, the change propagates to your laptop within seconds. This is genuinely useful, but it introduces a critical property you must understand: **sync is not backup**. If you delete a file locally, the sync client interprets that as an intentional change and deletes the cloud copy too. If you accidentally overwrite a file, the overwritten version syncs. Sync preserves your latest state everywhere — it does not protect you from yourself. True backup stores a separate, independent copy that does not mirror deletions (which is why cloud services offer a separate "backup" product distinct from "sync").

**Sharing** is where cloud storage becomes a collaboration tool. Instead of emailing a 50 MB file, you store it once and share a link. The recipient accesses the same file from the server — no attachment bloat, no version confusion. Permissions let you control what recipients can do: **view-only** access means they can read but not change; **edit** access means they can modify the file directly (which also means their changes propagate to your copy). Shared links can be scoped to specific people or made public. Crucially, access can be revoked at any time — the recipient never "owns" a copy unless they explicitly download and save one. This is the key difference from an email attachment, where the recipient's copy is permanent.

A few practical habits follow from these mechanics. First, understand your storage limit and track what's consuming it — video files fill quotas quickly. Second, if you are relying on cloud storage as a backup, periodically verify that your sync is actually running; a misconfigured sync that has silently stopped updating is not protecting you. Third, before sharing edit access to an important document, consider whether you want version history enabled (most services offer it) so that accidental edits can be reversed. Cloud storage is powerful and convenient, but treating sync as infallible backup is the most common way people lose files they thought were safe.

