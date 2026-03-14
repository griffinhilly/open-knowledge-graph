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
