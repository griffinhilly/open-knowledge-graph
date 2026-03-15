---
id: file-compression-and-archives
title: File Compression and Archives
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: file-system-basics
  type: hard
- id: exponents-intro
  type: soft
tags:
- compression
- zip
- archives
- files
stage: abstract-reasoning
status: draft
---

# File Compression and Archives

## Core Idea
File compression reduces the size of files or groups of files by encoding their data more efficiently, making them faster to transfer and easier to store. Archive formats like ZIP bundle multiple files and folders into a single package, which is especially useful for email attachments and downloads. Compression works better on some file types than others — text and documents compress dramatically, while photos and videos (already compressed) shrink very little. Password-protecting an archive adds a layer of security for sensitive files in transit.

## How It's Best Learned
Create a ZIP archive from a folder of mixed files (documents, images, a video) and compare the original folder size to the ZIP size. Extract the archive to a different location and verify the files are identical. Then create a password-protected archive and try opening it without the password.

## Common Misconceptions
- Compressing a JPEG image or MP4 video into a ZIP file will barely reduce its size, because these formats are already internally compressed.
- Double-clicking a ZIP file on most operating systems shows its contents but does not fully extract them — files may behave unexpectedly until properly extracted to a folder.
- RAR and 7z files are not broken or corrupted just because Windows cannot open them natively; they simply require a compatible extraction tool like 7-Zip.
