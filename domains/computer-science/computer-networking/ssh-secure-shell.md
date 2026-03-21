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

## Questions

```yaml
- question: "An attacker with a full packet capture of an SSH session between a client and server can read which of the following?"
  type: multiple-choice
  options:
    - "Passwords and commands, but not the server's responses"
    - "Nothing useful — the entire session payload is encrypted after the handshake"
    - "Only the initial handshake, which is sent in plaintext before encryption is established"
    - "Commands typed by the user but not files transferred via SCP"
  answer: 1
  explanation: "SSH encrypts the entire session — not just the password, but every command, every response, every file transferred, and every byte of data moving through the connection. After the transport layer negotiates encryption during the handshake, all subsequent traffic flows through an encrypted channel. An attacker with packet capture sees only ciphertext. This contrasts sharply with Telnet, which transmitted everything in plaintext. The common misconception (represented by option A) is that SSH only protects the password; in fact, the session channel provides end-to-end encryption for all traffic."

- question: "How does SSH verify the identity of a server, and how does this differ from how TLS/HTTPS verifies a web server's identity?"
  type: multiple-choice
  options:
    - "SSH uses certificate authorities (CAs) to sign host keys, just like TLS uses CAs for certificates"
    - "SSH uses trust-on-first-use: the client accepts and stores the server's key on first connection, then verifies it matches on all subsequent connections"
    - "SSH does not verify server identity — only the user's identity is verified"
    - "SSH requires the server to present a certificate signed by a trusted CA before any connection is allowed"
  answer: 1
  explanation: "SSH uses a 'trust-on-first-use' (TOFU) model by default, not a certificate authority hierarchy. On first connection, SSH asks you to verify the server's host key fingerprint manually and stores it in `~/.ssh/known_hosts`. On subsequent connections, SSH checks the presented key against the stored copy — a mismatch triggers a warning (possible man-in-the-middle attack). TLS relies on CAs to pre-establish trust through signed certificates. SSH's TOFU model is simpler but shifts responsibility to the user to verify the fingerprint on first contact. Enterprise environments can configure SSH with CAs for automated trust, but TOFU is the default."

- question: "SSH encrypts the authentication phase (login) but transmits commands and responses in plaintext once the session is established."
  type: true-false
  answer: false
  explanation: "This is one of the most common misconceptions about SSH. The encryption established during the transport layer phase covers the entire session — authentication, commands, responses, and all data. The session channel is a continuously encrypted tunnel, not a single-use authentication wrapper. This is precisely why SSH replaced Telnet: Telnet encrypted nothing, while SSH encrypts everything. The only part that might be considered 'outside' the session channel is the initial key exchange negotiation itself, which uses public-key cryptography and does not require prior secrecy."

- question: "In SSH key-based authentication, the private key never leaves the client machine — the server verifies the client's identity through a cryptographic challenge that the client answers using the private key."
  type: true-false
  answer: true
  explanation: "This is the security advantage of key-based authentication over password authentication. The server knows the client's public key (stored in `~/.ssh/authorized_keys`). During authentication, the server sends a challenge encrypted with the client's public key. Only the holder of the matching private key can decrypt the challenge and produce the correct response. The private key is never transmitted — the server only sees the response. This is why key-based auth is immune to brute-force and password-guessing attacks, and why it is essential for automated systems that cannot type passwords interactively."

- question: "Why is key-based SSH authentication strongly preferred over password authentication for automated systems and CI/CD pipelines?"
  type: short-answer
  answer: "Automated systems cannot interactively type passwords, but they can use key files stored on disk. More importantly, key-based authentication is fundamentally more secure: the private key never travels over the network (only the response to a challenge does), so it cannot be captured by packet sniffing. Passwords, even over an encrypted channel, can be leaked through logs, brute-forced, or stolen from the server's authentication database. SSH keys with passphrases add a second factor. Additionally, fine-grained access control is easier with keys — a compromised key can be revoked by removing it from `authorized_keys` without changing credentials shared across systems."
  explanation: "For CI/CD pipelines specifically, the use of dedicated deploy keys (key pairs generated for a specific pipeline with minimal permissions) follows the principle of least privilege. If the pipeline is compromised, only that key needs to be revoked. With password authentication, shared credentials would need to be changed everywhere they are used. The combination of network security (key never transmitted), auditability (each key is a distinct identity), and revocability makes key-based auth the default for serious infrastructure automation."
```

## Explainer

You already understand TCP's reliable byte stream and TLS's encryption handshake from your prerequisites. SSH combines ideas from both: it runs over a TCP connection (typically port 22) and establishes its own encrypted channel, but it was designed specifically for interactive remote access rather than general-purpose web security. Before SSH existed, administrators used Telnet to manage remote servers — sending usernames, passwords, and every command in plaintext over the network. Anyone with a packet sniffer on the same network segment could read everything. SSH was created to solve exactly this problem.

The SSH connection proceeds in three phases. First, the **transport layer** negotiates encryption. The client connects to the server and they agree on algorithms for key exchange, encryption, and message authentication. The server presents its **host key** — a public key that identifies the server. The first time you connect, your SSH client asks you to verify this key's fingerprint (the familiar "Are you sure you want to continue connecting?" prompt). On subsequent connections, the client checks the server's key against its stored copy; a mismatch warns you that something has changed — possibly a man-in-the-middle attack. This host verification uses the same public-key cryptography concepts you learned with TLS certificates, but SSH manages trust through a simpler model: trust-on-first-use rather than certificate authorities.

Second, the **authentication layer** verifies the user's identity. Password authentication sends the password over the already-encrypted channel — secure in transit, but still vulnerable to brute-force attacks. **Key-based authentication** is stronger: you generate a public/private key pair, place the public key on the server, and during login the server challenges the client to prove it holds the matching private key without ever transmitting it. The private key never leaves your machine. This is why key-based auth is preferred for automated systems — scripts and CI/CD pipelines cannot type passwords, but they can use key files.

Third, the **connection layer** multiplexes the encrypted tunnel into **channels**. A single SSH connection can carry an interactive shell session, file transfers (via SCP or SFTP), and multiple **port forwards** simultaneously. **Local port forwarding** tunnels traffic from your machine through the SSH server to a destination behind it — useful for accessing a database that only accepts connections from the server's network. **Remote port forwarding** does the reverse, exposing a local service through the remote server. **Dynamic forwarding** turns the SSH connection into a SOCKS proxy. All of this traffic flows through the single encrypted TCP connection, making SSH not just a remote shell tool but a general-purpose secure tunnel for any TCP-based protocol.
