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

## Explainer

You already know that a process is an abstraction the OS uses to isolate running programs, and that system calls provide the controlled gateway between user code and kernel services. OS security builds directly on these concepts: the entire security model depends on the hardware and OS enforcing a boundary between what user processes can do and what the kernel can do, and then carefully controlling how processes cross that boundary.

The foundation is **hardware privilege levels**, often called protection rings. Modern CPUs operate in at least two modes: **kernel mode** (ring 0), where code has unrestricted access to hardware, memory, and privileged instructions, and **user mode** (ring 3), where code is restricted. Your process runs in user mode. It cannot directly access another process's memory, touch hardware registers, or modify page tables. When it needs a privileged operation — opening a file, sending a network packet, allocating memory — it makes a system call, which triggers a controlled transition to kernel mode. The kernel validates the request, checks permissions, performs the operation, and returns to user mode. This boundary is the single most important security mechanism in the OS: without it, any process could read any file, access any device, or overwrite the kernel itself.

On top of this hardware boundary, the OS implements three security functions. **Authentication** establishes identity: when you log in, the system verifies your credentials (password, SSH key, biometric) and associates your session with a user ID (UID). **Authorization** enforces what each identity is allowed to do: file permissions (read/write/execute for owner/group/others), process capabilities, and access control lists determine whether a given UID can access a given resource. **Auditing** logs security-relevant events so that administrators can detect and investigate breaches after the fact. These three functions — sometimes called AAA (authentication, authorization, auditing) — work together as layers of defense.

The **principle of least privilege** ties these mechanisms together into a design philosophy: every process should run with the minimum set of permissions needed for its task. A web server does not need root access; it needs permission to bind to port 80, read its document root, and write to its log directory. Running it as root means that a vulnerability in the web server grants the attacker full system control. Running it as a restricted user means the same vulnerability is contained — the attacker can only access what the web server could access. **Privilege escalation** — an attacker gaining higher privileges than intended — is the primary threat model. This can happen through kernel bugs (a system call handler that fails to validate input, letting user-mode code corrupt kernel memory), setuid misconfigurations (a program that runs with elevated privileges but can be tricked into executing attacker-controlled code), or buffer overflows in privileged processes. Every layer of the OS security model exists to make privilege escalation as difficult as possible.
