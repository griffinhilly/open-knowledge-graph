---
id: os-security-basics
title: OS Security Fundamentals
domain: computer-science
course: operating-systems
prerequisites:
- id: process-concept
  type: hard
- id: system-calls
  type: soft
builds-toward:
- access-control
tags:
- authentication
- authorization
- protection-rings
- privilege-escalation
- OS-security
stage: formal-systems
status: validated
---

# OS Security Fundamentals

## Core Idea
OS security encompasses the mechanisms and policies that protect system resources from unauthorized access. The hardware protection model uses privilege rings: ring 0 (kernel mode, full hardware access) and ring 3 (user mode, restricted) — user programs cannot directly access hardware or memory-mapped kernel structures. The OS enforces three security properties: authentication (verifying identity — who are you?), authorization (enforcing permissions — what are you allowed to do?), and auditing (logging activity). Security vulnerabilities often arise from privilege escalation bugs: a user-mode exploit that tricks the kernel into granting elevated access, or a buffer overflow in a privileged process that overwrites control data.

## How It's Best Learned
Study a classic privilege escalation CVE (e.g., a Linux kernel local privilege escalation). Identify which protection mechanism failed and what the attacker gained.

## Common Misconceptions
- Security is not solely about encryption; confidentiality, integrity, and availability are the three core goals (CIA triad).
- Running as root/Administrator to avoid permission errors is a major security mistake; the principle of least privilege states programs should run with the minimum permissions needed.
