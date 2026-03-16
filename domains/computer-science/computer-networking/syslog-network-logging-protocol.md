---
id: syslog-network-logging-protocol
title: 'Syslog: Network Logging and Log Aggregation'
domain: computer-science
course: computer-networking
prerequisites:
- id: network-management-and-monitoring
  type: hard
- id: udp-user-datagram-protocol
  type: soft
builds-toward:
- network-management-and-monitoring
- network-security-fundamentals
tags:
- monitoring
- logging
- syslog
- management
stage: advanced
status: draft
---

# Syslog: Network Logging and Log Aggregation

## Core Idea
Syslog (RFC 3164, RFC 5424) is a standard for transmitting log messages across networks, enabling centralized log collection from devices (routers, switches, firewalls, servers). Syslog servers aggregate logs for analysis, archival, and correlation. Priority levels (severity, facility) classify messages for filtering and retention.

## How It's Best Learned
Set up rsyslog on Linux and configure remote logging. Send syslog messages from network devices to a central collector. Parse structured syslog (RFC 5424) with CEE fields. Implement log rotation and retention policies.

## Common Misconceptions
Syslog does not guarantee delivery; it is connectionless (UDP). Log content is not encrypted by default; TLS-based syslog should be used for sensitive logs. Syslog timestamps are local to the sending device; clock skew can affect correlation.

## Explainer

From your study of network management and monitoring, you know that visibility into what is happening across a network requires collecting data from many devices. **Syslog** is the standard protocol for doing exactly this with log messages — it gives routers, switches, firewalls, servers, and applications a common language for reporting events to a central location where they can be stored, searched, and correlated.

Every syslog message carries two classification numbers: a **facility** code indicating what generated the message (kernel, mail system, authentication, local applications) and a **severity** level from 0 (Emergency — system is unusable) to 7 (Debug — verbose diagnostic output). Together, these form a **priority value** calculated as (facility × 8) + severity. This priority lets the receiving syslog server make fast decisions about routing: emergencies might trigger alerts and get written to persistent storage immediately, while debug messages might go to a separate file with aggressive rotation or be dropped entirely during normal operations.

The original syslog specification (RFC 3164, sometimes called "BSD syslog") was intentionally simple: a UDP datagram on port 514 containing a priority value, a timestamp, a hostname, and a free-text message. This simplicity is both syslog's strength and its weakness. Any device can emit syslog messages with minimal overhead — no connection setup, no acknowledgment, no negotiation. But UDP provides no delivery guarantee, so if the network is congested or the syslog server is down, messages are silently lost. The newer specification (RFC 5424) adds structured data fields, UTF-8 support, and precise timestamps with timezone information, addressing many of the original format's ambiguities while remaining backward-compatible.

In practice, centralized log collection is what makes syslog powerful. A single syslog server (or a modern log aggregation platform like rsyslog, syslog-ng, or an ELK stack) receives messages from hundreds or thousands of devices, enabling administrators to **correlate events** across the network. When a security incident occurs, the ability to search logs from the firewall, the authentication server, and the application server with a common timeline is invaluable. However, this correlation depends on synchronized clocks — since syslog timestamps come from each sending device, even small clock differences can make event ordering ambiguous. This is why NTP (Network Time Protocol) is a critical companion to any syslog deployment. For sensitive environments, syslog over TLS (RFC 5425) encrypts log traffic in transit, and TCP-based transport ensures reliable delivery at the cost of additional overhead.
