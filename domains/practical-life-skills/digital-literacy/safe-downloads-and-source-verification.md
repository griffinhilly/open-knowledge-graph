---
id: safe-downloads-and-source-verification
title: Safe Downloads and Source Verification
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: file-system-basics
  type: hard
- id: downloading-uploading-files
  type: hard
- id: internet-safety-basics
  type: soft
builds-toward:
- malware-and-antivirus-basics
tags:
- security
- downloads
- file-safety
stage: abstract-reasoning
status: draft
---

# Safe Downloads and Source Verification

## Core Idea
Safe downloading means verifying that a website is legitimate before clicking download links, checking file names for anything suspicious, and scanning downloads for malware. Most computer infections occur through downloads from untrusted sources or deceptive links.

## How It's Best Learned
Download a file from a trusted source while noting the verification steps: checking the URL legitimacy, confirming the file name matches your expectations, and scanning with antivirus software before opening.

## Explainer

You already know how to navigate the file system and move files around — now the question is: should you trust the file in the first place? Most malware doesn't exploit some exotic technical vulnerability. It exploits trust. Someone clicks a download link that looked legitimate, and a file that appears to be a PDF or a software installer turns out to be something else entirely. Safe downloading is really just developing the habit of asking a few questions before you click.

The most important checkpoint is the **source URL**. Before downloading anything, look at the full address in your browser's address bar — not just the visible text on the page, which can say anything. Legitimate download sites for major software (browsers, office tools, media players) will come from the developer's own domain. A link that says "Download Chrome" but points to `chrome-free-download.net` rather than `google.com` is a red flag. When in doubt, go directly to the developer's official website rather than following a link from a search result or email.

The second checkpoint is the **file name and extension**. Your experience with the file system means you know that `.exe` and `.msi` files on Windows are executable programs — they run code when you open them. A file named `invoice.pdf.exe` is not a PDF; it is a program disguised with a misleading name. Many systems hide file extensions by default, which makes this harder to catch. A document that claims to be a PDF but prompts you to enable macros, or an image that asks you to run it, is not behaving like it should. Trust what the file *does*, not just what it is named.

The third checkpoint is **verification and scanning**. For high-stakes downloads — software you are installing, files you received by email from an unknown sender, or anything from an unfamiliar website — use your antivirus software to scan the file before opening it. Many antivirus tools integrate into your file browser and let you right-click and scan. For software installers specifically, some developers provide a **checksum** (a long string of characters like `sha256: a3f...`) alongside their download. Running the matching hash function on the file you downloaded and comparing it to the published value confirms the file was not tampered with in transit. This is an advanced step, but it is the gold standard for verifying that what you downloaded is exactly what the developer published.

The practical summary: most legitimate software is distributed through the developer's official website, major app stores, or well-known package managers. If you are downloading from somewhere else, that is reason enough to pause and verify before proceeding. The cost of a few extra seconds of verification is trivially low; the cost of running an infected file can range from a nuisance to a serious compromise of your files or accounts.
