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
status: draft
---

# Email Protocols: SMTP, POP3, and IMAP

## Core Idea
SMTP (Simple Mail Transfer Protocol) handles message transmission from clients to servers and between mail servers, using TCP port 25. POP3 (Post Office Protocol) and IMAP (Internet Message Access Protocol) enable clients to retrieve messages, with IMAP supporting folder hierarchies and server-side state while POP3 downloads locally. These protocols enable the distributed email system, with SMTP providing delivery, POP3 providing simple retrieval, and IMAP providing rich mailbox management.

## How It's Best Learned
Set up a local mail server (Postfix/Dovecot) and observe SMTP transactions using tcpdump. Use telnet to manually send SMTP commands and see protocol-level interactions. Configure email clients with both IMAP and POP3 to understand behavioral differences.

## Common Misconceptions
SMTP is bidirectional—it only sends. POP3 and IMAP are not interchangeable; POP3 is stateless (downloads delete from server) while IMAP maintains server state. Authentication credentials differ between sending (SMTP) and receiving (POP3/IMAP).

## Explainer

Email might seem like a single system, but it is actually built from multiple protocols that handle different stages of a message's journey. Since you understand TCP (which provides reliable, ordered byte streams) and DNS (which resolves names to addresses), you can see how email protocols layer on top of both. The core insight is that **sending** and **receiving** email are fundamentally different operations handled by different protocols — just as postal mail has separate systems for collection, sorting, and delivery.

**SMTP** (Simple Mail Transfer Protocol) is the sending protocol. When you click "Send," your email client opens a TCP connection to an SMTP server on port 25 (or 587 for authenticated submission). The conversation follows a rigid text-based command sequence: `HELO` (identify yourself), `MAIL FROM:` (specify sender), `RCPT TO:` (specify recipient), `DATA` (send the message body), and `QUIT`. The SMTP server then uses DNS to find the recipient's mail server by looking up the domain's **MX (Mail Exchanger) record** — this is why DNS is a prerequisite. If alice@example.com sends to bob@company.org, Alice's SMTP server queries DNS for company.org's MX record, gets `mail.company.org`, and opens a new SMTP connection to deliver the message there. SMTP is a push protocol: it only moves messages forward, never retrieves them.

**POP3** (Post Office Protocol version 3) and **IMAP** (Internet Message Access Protocol) are the retrieval protocols — they let your email client download messages that SMTP already delivered to your server. POP3 is the simpler of the two: it connects on TCP port 110, authenticates, downloads all new messages to the client, and typically deletes them from the server. This is a "download and delete" model, meaning your email lives on one device only. **IMAP**, on port 143, takes a fundamentally different approach. It treats the server as the primary storage location and lets the client view, search, organize, and manipulate messages that remain on the server. IMAP supports **folder hierarchies**, **message flags** (read, starred, deleted), and **partial fetching** (download just headers first, then bodies on demand).

The practical difference between POP3 and IMAP matters most when you access email from multiple devices. With POP3, a message downloaded to your phone disappears from the server, so your laptop never sees it. With IMAP, both devices see the same mailbox state because the server is the source of truth — reading a message on your phone marks it as read on your laptop too. This is why IMAP dominates modern email: it mirrors how people actually use email today, across phones, tablets, and desktops. Modern email also wraps all three protocols in **TLS encryption** (SMTPS on port 465, IMAPS on port 993, POP3S on port 995) to protect credentials and message content in transit.
