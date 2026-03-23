---
id: email-protocols-smtp-pop3-imap
title: 'Email Protocols: SMTP, POP3, and IMAP'
domain: computer-science
course: computer-networking
prerequisites:
- id: tcp-transmission-control-protocol
  type: hard
- id: dns-domain-name-system
  type: hard
- id: network-security-fundamentals
  type: soft
builds-toward:
- https-and-tls
- network-security-fundamentals
tags:
- application-layer
- email
- protocols
- messaging
stage: advanced
status: validated
---

# Email Protocols: SMTP, POP3, and IMAP

## Core Idea
SMTP (Simple Mail Transfer Protocol) handles message transmission from clients to servers and between mail servers, using TCP port 25. POP3 (Post Office Protocol) and IMAP (Internet Message Access Protocol) enable clients to retrieve messages, with IMAP supporting folder hierarchies and server-side state while POP3 downloads locally. These protocols enable the distributed email system, with SMTP providing delivery, POP3 providing simple retrieval, and IMAP providing rich mailbox management.

## How It's Best Learned
Set up a local mail server (Postfix/Dovecot) and observe SMTP transactions using tcpdump. Use telnet to manually send SMTP commands and see protocol-level interactions. Configure email clients with both IMAP and POP3 to understand behavioral differences.

## Common Misconceptions
SMTP is bidirectional—it only sends. POP3 and IMAP are not interchangeable; POP3 is stateless (downloads delete from server) while IMAP maintains server state. Authentication credentials differ between sending (SMTP) and receiving (POP3/IMAP).

## Questions

```yaml
- question: "A user sends an email from Gmail to a Yahoo address. Which protocol transfers the message from Gmail's mail server to Yahoo's mail server?"
  type: multiple-choice
  options:
    - "IMAP, because Yahoo's server needs to retrieve the message from Gmail"
    - "SMTP, because mail transmission between servers uses SMTP"
    - "POP3, because POP3 handles server-to-server message transfer"
    - "DNS alone, because the MX record lookup delivers the message directly"
  answer: 1
  explanation: "SMTP handles all mail transmission — from client to server and between mail servers. Gmail's SMTP server looks up Yahoo's MX record via DNS, then opens a TCP connection to Yahoo's SMTP server and pushes the message. DNS resolves the destination address but does not deliver the message. IMAP and POP3 are only for clients retrieving messages from their own mail server."

- question: "A user configures their laptop with POP3, reads several emails, then checks the same account on their phone. The previously-read emails are absent from the phone. What explains this?"
  type: multiple-choice
  options:
    - "This is a server error; both devices should always see the same messages"
    - "This is expected POP3 behavior: messages were downloaded to the laptop and deleted from the server, so the phone has nothing to retrieve"
    - "IMAP was misconfigured on the phone, preventing synchronization"
    - "The emails were automatically archived by the server after 24 hours"
  answer: 1
  explanation: "POP3's default behavior is to download messages to the client and delete them from the server. Once the laptop downloaded the messages, they were removed — leaving nothing for the phone to retrieve. This 'download and delete' model was designed for single-device access. IMAP keeps messages on the server so all devices always see the same mailbox state."

- question: "SMTP can be used to retrieve email from a mail server, just as IMAP and POP3 can."
  type: true-false
  answer: false
  explanation: "SMTP is a push-only sending protocol — it moves email from client to server and between mail servers. It cannot retrieve messages. Retrieval always requires POP3 or IMAP. This separation of concerns is fundamental to email architecture: sending and receiving use entirely different protocols operating on different TCP ports."

- question: "An email client using IMAP stores the authoritative copy of messages on the local device, synchronizing back to the server."
  type: true-false
  answer: false
  explanation: "IMAP treats the server as the primary storage location. Messages remain on the server; the client views and manipulates them remotely. Any action — reading, deleting, organizing into folders — is recorded on the server and reflected across all devices. This is the opposite of POP3, where the downloaded local copy becomes the only copy once it's removed from the server."

- question: "Explain why someone who accesses email from multiple devices (phone, laptop, tablet) should prefer IMAP over POP3."
  type: short-answer
  answer: "IMAP stores messages on the server and synchronizes state (read/unread status, flags, folders) across all devices. Any action on one device is immediately reflected on all others. POP3 downloads messages to a single device and deletes them from the server by default, so other devices lose access to those messages and see no synchronized state."
  explanation: "The fundamental difference is where the master copy lives. POP3 was designed when people used a single desktop computer for email. IMAP was designed for multi-device access — the server is the source of truth, and every client is a synchronized view of that server state."
```

## Explainer

Email might seem like a single system, but it is actually built from multiple protocols that handle different stages of a message's journey. Since you understand TCP (which provides reliable, ordered byte streams) and DNS (which resolves names to addresses), you can see how email protocols layer on top of both. The core insight is that **sending** and **receiving** email are fundamentally different operations handled by different protocols — just as postal mail has separate systems for collection, sorting, and delivery.

**SMTP** (Simple Mail Transfer Protocol) is the sending protocol. When you click "Send," your email client opens a TCP connection to an SMTP server on port 25 (or 587 for authenticated submission). The conversation follows a rigid text-based command sequence: `HELO` (identify yourself), `MAIL FROM:` (specify sender), `RCPT TO:` (specify recipient), `DATA` (send the message body), and `QUIT`. The SMTP server then uses DNS to find the recipient's mail server by looking up the domain's **MX (Mail Exchanger) record** — this is why DNS is a prerequisite. If alice@example.com sends to bob@company.org, Alice's SMTP server queries DNS for company.org's MX record, gets `mail.company.org`, and opens a new SMTP connection to deliver the message there. SMTP is a push protocol: it only moves messages forward, never retrieves them.

**POP3** (Post Office Protocol version 3) and **IMAP** (Internet Message Access Protocol) are the retrieval protocols — they let your email client download messages that SMTP already delivered to your server. POP3 is the simpler of the two: it connects on TCP port 110, authenticates, downloads all new messages to the client, and typically deletes them from the server. This is a "download and delete" model, meaning your email lives on one device only. **IMAP**, on port 143, takes a fundamentally different approach. It treats the server as the primary storage location and lets the client view, search, organize, and manipulate messages that remain on the server. IMAP supports **folder hierarchies**, **message flags** (read, starred, deleted), and **partial fetching** (download just headers first, then bodies on demand).

The practical difference between POP3 and IMAP matters most when you access email from multiple devices. With POP3, a message downloaded to your phone disappears from the server, so your laptop never sees it. With IMAP, both devices see the same mailbox state because the server is the source of truth — reading a message on your phone marks it as read on your laptop too. This is why IMAP dominates modern email: it mirrors how people actually use email today, across phones, tablets, and desktops. Modern email also wraps all three protocols in **TLS encryption** (SMTPS on port 465, IMAPS on port 993, POP3S on port 995) to protect credentials and message content in transit.
