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
status: validated
---

# Safe Downloads and Source Verification

## Core Idea
Safe downloading means verifying that a website is legitimate before clicking download links, checking file names for anything suspicious, and scanning downloads for malware. Most computer infections occur through downloads from untrusted sources or deceptive links.

## How It's Best Learned
Download a file from a trusted source while noting the verification steps: checking the URL legitimacy, confirming the file name matches your expectations, and scanning with antivirus software before opening.

## Questions

```yaml
- question: "You search for 'free VLC download' and find a result. The page says 'Download VLC 3.0 now' and the button looks official. What is the most important thing to check before clicking the download link?"
  type: multiple-choice
  options:
    - "That the page has a professional-looking design and company logo"
    - "That the actual URL in the address bar points to the developer's official domain"
    - "That the file size listed seems reasonable for the software"
    - "That the download link opens in a new tab"
  answer: 1
  explanation: "The visible appearance of a page — logos, professional design, even the text of the link — can all be faked. The actual URL in the browser's address bar is the only reliable indicator of where the file will come from. A link can say 'Download VLC' while pointing to a malicious domain rather than videolan.org. Always verify the domain in the address bar before downloading from a new source."

- question: "You download a file called 'invoice.pdf' from an email attachment. When you try to open it, Windows asks if you want to 'Run' the file rather than opening it in a PDF reader. What does this most likely indicate?"
  type: multiple-choice
  options:
    - "The PDF is corrupted and needs to be re-downloaded"
    - "The file is actually an executable program disguised with a .pdf name, such as invoice.pdf.exe"
    - "Your PDF reader is not installed correctly"
    - "Large PDFs always prompt for permission before opening"
  answer: 1
  explanation: "Legitimate PDFs open in a PDF viewer, not as executable programs. A 'Run' prompt means the file is an executable (.exe, .msi, etc.) — its actual extension reveals this. Many systems hide file extensions by default, so 'invoice.pdf' might actually be 'invoice.pdf.exe' with the .exe suffix hidden. The OS behavior (asking to run rather than open) exposes what the file really is. This is a classic malware delivery technique."

- question: "A file that has a .pdf extension is safe to open because PDF files can rarely contain malware."
  type: true-false
  answer: false
  explanation: "This is false on two counts. First, PDF files can contain malicious code — PDFs support JavaScript and other active content that has been exploited in attacks. Second, a file named 'document.pdf' might actually be 'document.pdf.exe' with the true extension hidden by the operating system. The file name and visible extension are not reliable guarantees of what a file contains or will do when opened."

- question: "Downloading software directly from the developer's official website is generally safer than downloading the same software from a third-party aggregator or file-sharing site."
  type: true-false
  answer: true
  explanation: "True. When you download from the official developer's website, you get the file the developer published. Third-party aggregator sites may bundle malware, adware, or modified installers alongside the original software. The distribution chain matters: every step away from the original source is an opportunity for tampering. For well-known software (browsers, media players, office tools), the developer's official domain is the authoritative and safest source."

- question: "Why is checking the displayed text of a download link — such as 'Download Chrome Now' — insufficient for verifying that the download is safe?"
  type: short-answer
  answer: "The visible text of a link can say anything, regardless of where the link actually points. The underlying URL — what the browser will actually navigate to — is what determines the source. A link displaying 'Download Chrome Now' could point to any domain, including one that distributes malware. Only the actual URL in the browser's address bar (not the link text) tells you where the file comes from."
  explanation: "This is the core deception technique in phishing and malware distribution: make the visible presentation look legitimate while pointing to a malicious destination. Trust is built on the destination, not the label. Verifying the actual URL is the primary habit that separates safe from unsafe downloading."
```

## Explainer

You already know how to navigate the file system and move files around — now the question is: should you trust the file in the first place? Most malware doesn't exploit some exotic technical vulnerability. It exploits trust. Someone clicks a download link that looked legitimate, and a file that appears to be a PDF or a software installer turns out to be something else entirely. Safe downloading is really just developing the habit of asking a few questions before you click.

The most important checkpoint is the **source URL**. Before downloading anything, look at the full address in your browser's address bar — not just the visible text on the page, which can say anything. Legitimate download sites for major software (browsers, office tools, media players) will come from the developer's own domain. A link that says "Download Chrome" but points to `chrome-free-download.net` rather than `google.com` is a red flag. When in doubt, go directly to the developer's official website rather than following a link from a search result or email.

The second checkpoint is the **file name and extension**. Your experience with the file system means you know that `.exe` and `.msi` files on Windows are executable programs — they run code when you open them. A file named `invoice.pdf.exe` is not a PDF; it is a program disguised with a misleading name. Many systems hide file extensions by default, which makes this harder to catch. A document that claims to be a PDF but prompts you to enable macros, or an image that asks you to run it, is not behaving like it should. Trust what the file *does*, not just what it is named.

The third checkpoint is **verification and scanning**. For high-stakes downloads — software you are installing, files you received by email from an unknown sender, or anything from an unfamiliar website — use your antivirus software to scan the file before opening it. Many antivirus tools integrate into your file browser and let you right-click and scan. For software installers specifically, some developers provide a **checksum** (a long string of characters like `sha256: a3f...`) alongside their download. Running the matching hash function on the file you downloaded and comparing it to the published value confirms the file was not tampered with in transit. This is an advanced step, but it is the gold standard for verifying that what you downloaded is exactly what the developer published.

The practical summary: most legitimate software is distributed through the developer's official website, major app stores, or well-known package managers. If you are downloading from somewhere else, that is reason enough to pause and verify before proceeding. The cost of a few extra seconds of verification is trivially low; the cost of running an infected file can range from a nuisance to a serious compromise of your files or accounts.
