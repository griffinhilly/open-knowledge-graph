---
id: ssh-secure-shell
title: 'SSH: Secure Shell and Remote Access'
domain: computer-science
course: computer-networking
prerequisites:
- id: tcp-transmission-control-protocol
  type: hard
- id: https-and-tls
  type: hard
- id: network-security-fundamentals
  type: hard
builds-toward:
- vpn-virtual-private-networks
- network-security-fundamentals
tags:
- application-layer
- security
- remote-access
- encryption
stage: advanced
status: draft
---

# SSH: Secure Shell and Remote Access

## Core Idea
SSH (Secure Shell) provides encrypted remote login and command execution over TCP port 22, replacing the insecure Telnet protocol. It uses public-key cryptography for host authentication and establishes an encrypted tunnel for all transmitted data. SSH supports both password and key-based authentication, with key-based methods preferred for automated systems and security-critical environments.

## How It's Best Learned
Generate SSH key pairs and configure key-based authentication on a remote server. Monitor SSH handshakes using tcpdump and observe the key exchange process. Set up SSH tunneling (local and remote port forwarding) to proxy traffic through a remote host.

## Common Misconceptions
SSH only encrypts passwords, not all traffic—it encrypts the entire session. Port 22 is configurable and should be changed for exposed servers. SSH keys are not passwords and should not be treated as such; key passphrases are optional but recommended.
