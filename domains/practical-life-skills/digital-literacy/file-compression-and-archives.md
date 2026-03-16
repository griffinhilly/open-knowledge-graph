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

## Explainer

You already know from your file system experience that files have sizes — a text document might be 50 KB, a photo 3 MB, a video 1 GB. **File compression** exploits the fact that most files contain redundant or predictable patterns, and that redundancy can be encoded more efficiently than storing every byte separately. The result is a smaller file containing exactly the same information, which can be restored to its original form without any loss.

The intuition behind **lossless compression** (the kind used in ZIP files) is substitution. Instead of storing the same sequence of bytes repeatedly, store a compact rule. A text document containing the word "the" five hundred times could instead store a short code for "the" plus a lookup table — taking up far less space. Run-length encoding does something similar: instead of writing ten identical bytes in a row, write "10 × [value]." These substitutions accumulate dramatically for text, spreadsheets, and program code, which have lots of repetitive structure. A plain text document often compresses to 10–30% of its original size.

However, files that are already compressed gain almost nothing from a second compression pass — and sometimes grow slightly. JPEG photos, MP3 audio, and MP4 videos have already had their redundancy removed by specialized compressors designed specifically for each format. When you add them to a ZIP file, the ZIP algorithm finds almost no patterns to exploit and adds its own small overhead on top. This is the most important practical fact about compression: it only helps when unexploited redundancy remains. Your exponent intuition applies here — compression ratios multiply, so compressing already-compressed data gives you a ratio near 1×, meaning almost no reduction.

**Archive formats** like ZIP, TAR, and 7z serve a second purpose beyond compression: bundling. They package an entire folder hierarchy — multiple files and subfolders at any nesting depth — into a single file, which is far easier to transfer or attach to an email than a loose collection. ZIP does both operations simultaneously (bundle and compress). TAR bundles without compressing; a separate compression step (gzip or bzip2) then compresses the bundle, producing filenames like `.tar.gz` — "bundled, then compressed." Password-protecting an archive encrypts its contents so they cannot be read without the correct key, adding privacy for sensitive files in transit. Together, compression and archiving are two distinct operations that often happen to travel together in common formats.
