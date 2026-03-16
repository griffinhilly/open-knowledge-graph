---
id: ftp-file-transfer-protocol
title: 'FTP: File Transfer Protocol and SFTP'
domain: computer-science
course: computer-networking
prerequisites:
- id: tcp-transmission-control-protocol
  type: hard
- id: port-addressing-sockets
  type: hard
builds-toward:
- network-security-fundamentals
- ssh-secure-shell
tags:
- application-layer
- file-transfer
- protocols
- data-transfer
stage: advanced
status: draft
---

# FTP: File Transfer Protocol and SFTP

## Core Idea
FTP (File Transfer Protocol) uses separate control (port 21) and data (port 20 or ephemeral) connections to transfer files. Active mode requires the server to initiate data connections, while passive mode has the client initiate both connections, making it firewall-friendly. SFTP (SSH File Transfer Protocol) wraps file transfer in SSH for encryption, replacing FTP in modern deployments due to security concerns.

## How It's Best Learned
Deploy a vsftpd server and observe both active and passive mode transfers using Wireshark. Monitor firewall rule impacts on passive mode. Configure an SFTP server and compare performance and security characteristics.

## Common Misconceptions
FTP is not secure; credentials are sent in plaintext on the control channel. Active mode is not inherently more secure or faster than passive mode. SFTP is not FTPS; FTPS wraps FTP in SSL/TLS while SFTP runs over SSH.

## Explainer

From your knowledge of TCP and port addressing, you understand that applications communicate through socket connections identified by IP addresses and port numbers. FTP is unusual among application-layer protocols because it uses **two separate TCP connections** simultaneously: a **control connection** for commands and responses, and a **data connection** for actual file transfers. This dual-connection design made sense in the 1970s when it was designed — separating control from data allowed users to issue commands (list directory, change directory, rename files) while a large transfer was in progress — but it creates complications in modern firewalled networks.

The control connection is straightforward: the client connects to the server on **port 21** and exchanges text commands like `USER`, `PASS`, `LIST`, `RETR` (download), and `STOR` (upload). This connection stays open for the entire session. The data connection is where things get interesting. In **active mode**, the client tells the server "I'm listening on port X — connect to me there." The server then initiates a TCP connection from its port 20 to the client's specified port. This is problematic because firewalls and NAT devices typically block incoming connections to clients. In **passive mode**, the roles reverse: the client asks the server to listen on a random high-numbered port, and the client initiates the data connection. Since the client initiates both connections in passive mode, it works much better through firewalls and NAT — which is why passive mode is the default in virtually all modern FTP clients.

FTP's fatal flaw is **security**. Usernames, passwords, and all data travel in plaintext over both connections. Anyone able to observe network traffic — through packet sniffing on a shared network or a compromised router — can capture credentials and file contents. Two solutions emerged. **FTPS** (FTP over SSL/TLS) wraps the existing FTP protocol in encryption, preserving the dual-connection architecture but encrypting both channels. **SFTP** (SSH File Transfer Protocol) takes a completely different approach: it runs as a subsystem within an SSH session, using a single encrypted connection for both commands and data. Despite the similar names, FTPS and SFTP are entirely different protocols. SFTP has largely won in practice because it uses a single connection (simpler for firewalls), inherits SSH's strong authentication, and is available everywhere SSH is installed.

Understanding FTP remains valuable even as it fades from active use because its design illustrates fundamental tradeoffs in protocol architecture: the tension between in-band and out-of-band control, the complications that NAT and firewalls introduce for protocols that were designed for end-to-end connectivity, and the evolution from plaintext to encrypted protocols as security requirements changed.
