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

## Explainer

You already understand TCP's reliable byte stream and TLS's encryption handshake from your prerequisites. SSH combines ideas from both: it runs over a TCP connection (typically port 22) and establishes its own encrypted channel, but it was designed specifically for interactive remote access rather than general-purpose web security. Before SSH existed, administrators used Telnet to manage remote servers — sending usernames, passwords, and every command in plaintext over the network. Anyone with a packet sniffer on the same network segment could read everything. SSH was created to solve exactly this problem.

The SSH connection proceeds in three phases. First, the **transport layer** negotiates encryption. The client connects to the server and they agree on algorithms for key exchange, encryption, and message authentication. The server presents its **host key** — a public key that identifies the server. The first time you connect, your SSH client asks you to verify this key's fingerprint (the familiar "Are you sure you want to continue connecting?" prompt). On subsequent connections, the client checks the server's key against its stored copy; a mismatch warns you that something has changed — possibly a man-in-the-middle attack. This host verification uses the same public-key cryptography concepts you learned with TLS certificates, but SSH manages trust through a simpler model: trust-on-first-use rather than certificate authorities.

Second, the **authentication layer** verifies the user's identity. Password authentication sends the password over the already-encrypted channel — secure in transit, but still vulnerable to brute-force attacks. **Key-based authentication** is stronger: you generate a public/private key pair, place the public key on the server, and during login the server challenges the client to prove it holds the matching private key without ever transmitting it. The private key never leaves your machine. This is why key-based auth is preferred for automated systems — scripts and CI/CD pipelines cannot type passwords, but they can use key files.

Third, the **connection layer** multiplexes the encrypted tunnel into **channels**. A single SSH connection can carry an interactive shell session, file transfers (via SCP or SFTP), and multiple **port forwards** simultaneously. **Local port forwarding** tunnels traffic from your machine through the SSH server to a destination behind it — useful for accessing a database that only accepts connections from the server's network. **Remote port forwarding** does the reverse, exposing a local service through the remote server. **Dynamic forwarding** turns the SSH connection into a SOCKS proxy. All of this traffic flows through the single encrypted TCP connection, making SSH not just a remote shell tool but a general-purpose secure tunnel for any TCP-based protocol.
