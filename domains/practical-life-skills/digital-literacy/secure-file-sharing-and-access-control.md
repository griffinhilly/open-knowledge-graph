---
id: secure-file-sharing-and-access-control
title: Secure File Sharing and Access Control
domain: practical-life-skills
course: digital-literacy
prerequisites:
- id: cloud-storage-basics
  type: hard
- id: shared-document-editing-and-collaboration
  type: hard
builds-toward:
- digital-identity-management
tags:
- sharing
- collaboration
- security
stage: formal-systems
status: draft
---

# Secure File Sharing and Access Control

## Core Idea
When sharing files in cloud storage, you can control who has access—granting read-only, edit, or download permissions—and expire access at a specified date. This prevents unauthorized viewing or modification and limits exposure if a shared link is compromised.

## Questions

```yaml
- question: "You email a shareable link to a financial report to one trusted colleague. They accidentally forward the email to an external contact who now has access to the document. Which access control design decision would have prevented this?"
  type: multiple-choice
  options:
    - "Using individual account-based access rather than a link, so only the specified colleague can open it"
    - "Granting edit permissions instead of read-only, so the colleague could delete the file after reading"
    - "Sharing via link but adding a password, which prevents forwarding entirely"
    - "Setting an expiring link, which would have revoked access before the colleague could forward it"
  answer: 0
  explanation: "A shareable link works for anyone who possesses it — it can be forwarded, posted, or discovered unintentionally. Individual account-based access requires the recipient to be signed into a specific account, so forwarding the link to someone else grants them nothing. Option C is wrong because a password-protected link can still be forwarded along with the password. Option D might limit exposure after the fact but does not prevent unauthorized access at the time of forwarding."

- question: "A contractor needs to review and annotate a draft report but must not be able to change the actual content. Which permission level is most appropriate?"
  type: multiple-choice
  options:
    - "Editor/contributor — so they can track changes and suggest edits directly"
    - "Viewer/read-only — so they can see and download the document"
    - "Commenter — so they can annotate without altering the content"
    - "No access — contractors should receive a static PDF copy instead"
  answer: 2
  explanation: "Comment-only access is exactly the middle tier designed for this scenario: it lets someone annotate and flag issues without altering the actual document. Viewer/read-only (option B) would prevent them from adding annotations at all. Editor access (option A) would let them accidentally overwrite content. This question tests whether students know there are more than two permission levels."

- question: "Expiring shared links are a useful security practice because they automatically revoke access after a set time, reducing the risk of forgotten active links."
  type: true-false
  answer: true
  explanation: "Expiring links are a practical application of the principle of least privilege over time — you grant access for exactly as long as it's needed. Without expiration, a link shared for a one-time review may remain active indefinitely, creating ongoing exposure if the link is later discovered or if the recipient's account is compromised."

- question: "A shared document link protected by a strong password is as secure as individual account-based access for sensitive files."
  type: true-false
  answer: false
  explanation: "A password-protected link can still be forwarded along with the password — the protection travels with the link. Individual account-based access, by contrast, binds access to a verified identity: even if someone receives the link, they cannot access the file unless they are signed into the specific authorized account. For sensitive documents, individual access provides a meaningfully higher security guarantee."

- question: "What is the 'principle of least privilege,' and how does it apply when deciding what permissions to grant when sharing a file?"
  type: short-answer
  answer: "The principle of least privilege means giving someone exactly the access they need to accomplish their task — nothing more. When sharing a file, this means choosing the minimum permission level required: read-only if they only need to view it, comment-only if they need to annotate, edit only if they need to change the content. It also means preferring individual access over link-based sharing for sensitive documents, and using expiring links when access is only needed temporarily."
  explanation: "The principle of least privilege limits the blast radius when something goes wrong: if a link leaks, an account is compromised, or a collaborator acts carelessly, overly broad permissions amplify the damage. Granting only what is necessary means that a compromised or misdirected access cannot do more harm than the task required."
```

## Explainer

You already know how cloud storage works and how collaborators can edit shared documents together. What you haven't yet controlled is *who* gets in. By default, many cloud platforms create sharing links that work for anyone who receives them — like handing someone a key and hoping they don't pass it along. **Access control** is the practice of deciding not just what you share, but who can access it, what they can do with it, and for how long.

The most important distinction is between **permission levels**. Read-only (or "viewer") access lets someone see and download a file but not change it — appropriate for a report you want a client to review. Edit (or "contributor") access lets them make changes — appropriate for a collaborator working on the same document. Some platforms offer a middle tier: **comment-only** access, which lets someone annotate without altering the content. Choosing the wrong level is the most common mistake: sharing edit access when you only meant to share a view, and then finding your document altered or accidentally overwritten.

**Link-based sharing** vs. **individual access** is a second key distinction. A shareable link grants access to anyone who possesses it — it can be forwarded, posted, or discovered unintentionally. Individual access, by contrast, requires the recipient to be signed into a specific account. For sensitive documents (financial records, personal information, confidential drafts), individual access is far more secure. For low-stakes content you want to share broadly, a link is convenient. **Expiring links** add a time limit, so a link shared for one meeting or one week automatically stops working afterward — this is a powerful habit for reducing lingering access you forget to revoke.

Think of it through the lens of **principle of least privilege**: give people exactly the access they need to accomplish the task, nothing more. This limits the damage if a link leaks, an account is compromised, or a collaborator accidentally changes something. Combined with your prior knowledge of shared document collaboration, access control is the permission layer that makes collaboration safe at scale — especially when documents contain sensitive information or are shared with people outside your organization.
