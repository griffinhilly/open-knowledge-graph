---
id: downloading-uploading-files
title: Downloading and Uploading Files
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: web-browser-essentials
  type: hard
builds-toward:
- device-security-desktop-mobile
tags:
- downloads
- uploads
- file-transfer
- attachments
stage: abstract-reasoning
status: draft
---

# Downloading and Uploading Files

## Core Idea
Downloading saves a file from the internet to your device; uploading sends a file from your device to a website. Both operations involve security considerations—knowing where downloads go, recognizing dangerous file types, and understanding when sharing files is safe. Learning to manage downloads helps you stay organized and avoid malware.

## How It's Best Learned
Download a document from a website and find it on your computer. Upload a file to a cloud service. Practice changing your download location in browser settings.

## Common Misconceptions
- Downloading a file is always safe.
- Downloaded files automatically disappear after you close the website.
- You can upload any file anywhere without consequences.

## Questions

```yaml
- question: "When you click a download link and the file arrives on your computer, what has happened to the original file on the web server?"
  type: multiple-choice
  options:
    - "It has been moved to your device — the server no longer has a copy"
    - "It has been encrypted and held temporarily until you confirm the download"
    - "A copy has been sent to your device; the server's original file is unchanged"
    - "It has been compressed and will be deleted from the server after 24 hours"
  answer: 2
  explanation: "Downloading is always a copy operation, never a move. The web server retains the original file — that's why thousands of people can download the same file. Your device receives a duplicate that is saved to your downloads folder. Understanding this also explains why downloaded files persist on your device indefinitely; the server doesn't track or remove your local copy."

- question: "A colleague sends you a Word document (.docx) as an email attachment from their known work address. Before opening it, what is the best security practice?"
  type: multiple-choice
  options:
    - "Open it immediately — it came from a known sender, so it is safe"
    - "Check that it ends in .docx; documents with common extensions are always safe to open"
    - "Be aware that even .docx files can contain macros or embedded scripts; consider disabling macros or scanning the file before opening"
    - "Upload it to cloud storage first — cloud services neutralize all file-based threats before you open them"
  answer: 2
  explanation: "File extensions don't guarantee safety. Even common document formats like .docx, .pdf, or .zip can contain macros, embedded scripts, or malicious content. A file from a known sender can still be dangerous if that sender's account was compromised or if they unknowingly forwarded infected content. The safest approach is to be aware of the risk, disable macros by default in Office, and scan unfamiliar or unexpected files. Option A is the most common mistake — source familiarity does not equal file safety."

- question: "Files you download from the internet are automatically deleted when you close the browser tab or website you downloaded them from."
  type: true-false
  answer: false
  explanation: "Downloaded files are saved to a permanent location on your device (typically a Downloads folder) and remain there until you manually delete them. The website has no ability to delete files already saved to your computer. This is why downloads folders accumulate clutter over time and why managing them periodically is good digital hygiene. The browser and the website lose all connection to the file once the download completes."

- question: "Uploading a photo to a public website may share your physical location with others, even if you don't type your address anywhere."
  type: true-false
  answer: true
  explanation: "Photos taken on smartphones typically contain EXIF metadata embedded in the file, which can include GPS coordinates, the date and time the photo was taken, and device information. When you upload a photo without stripping this metadata, anyone who downloads the file can read those coordinates. Many social media platforms strip EXIF data automatically, but not all services do. Being aware of metadata is a key part of thoughtful file sharing."

- question: "What security consideration applies specifically when uploading a file that does not apply in the same way when simply browsing a website?"
  type: short-answer
  answer: "When uploading, you must think about what information the file itself contains — both its intended content and embedded metadata. A photo may carry GPS coordinates; a Word document may contain revision history, author names, or comments. Simply browsing a website involves receiving information, but uploading means sending your own data to an external server. Once uploaded, you often cannot control how that data is stored, shared, or indexed. You should verify the platform is trusted, consider what metadata is embedded in the file, and think about whether the file's contents are appropriate to share in that context."
  explanation: "Browsing is largely passive — you receive content. Uploading is active — you send potentially sensitive data. The security risks run in both directions of file transfer, but the upload direction requires thinking about data you are exposing rather than data being pushed to you. This is particularly important for files containing private information like location data, personal details, or confidential documents."
```

## Explainer

You already know the essentials of navigating a browser — clicking links, entering URLs, filling out forms. **Downloading** and **uploading** are the two transfer operations that extend browsing from passive reading to active file exchange. Understanding both — where files go, what happens to them, and what risks are involved — turns you from a passive consumer of the web into someone who can move information between the internet and your device with confidence and care.

When you click a download link, your browser asks the web server to send a copy of that file. The file travels over the network in small data packets, is reassembled on your device, and saved to a default **downloads folder** (usually `C:\Users\YourName\Downloads` on Windows or `~/Downloads` on Mac and Linux). The original file on the server is unchanged — downloading is always a copy, never a move. Files accumulate in this folder indefinitely unless you manage them; knowing where it is, checking it occasionally, and deleting what you no longer need is basic digital hygiene. You can also change the default download location in your browser settings to route PDFs, images, or documents directly into organized subfolders.

Not every file is safe to open. **Executable files** — ending in `.exe`, `.bat`, `.msi`, or `.dmg` — run code the moment you open them and can install software, modify your system, or introduce malware. Even documents from untrusted sources (`.docx`, `.pdf`, `.zip`) can contain macros or embedded scripts. The safest practice: download files only from sources you trust, check the file extension before opening, and scan unfamiliar files with antivirus software before running them. A PDF from a university library is a very different risk profile from an `.exe` labeled "free movie player" on an unknown site.

**Uploading** reverses the direction: you select a file on your device and send it to a web server. This happens when you attach a file to an email, submit an assignment on a course platform, or share a photo. The same security awareness applies in reverse — think about what information a file contains before you share it. Photos carry embedded **metadata** including GPS location and device information; Word documents store author names and revision history. Checking a file's properties before uploading sensitive documents, and using only trusted platforms for private information, keeps your data under your control. The download/upload framework — copy in, copy out, with security consideration in both directions — is the foundation of all file transfer you will encounter online.
