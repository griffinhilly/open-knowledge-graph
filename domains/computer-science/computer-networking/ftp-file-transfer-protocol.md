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
status: validated
---

# FTP: File Transfer Protocol and SFTP

## Core Idea
FTP (File Transfer Protocol) uses separate control (port 21) and data (port 20 or ephemeral) connections to transfer files. Active mode requires the server to initiate data connections, while passive mode has the client initiate both connections, making it firewall-friendly. SFTP (SSH File Transfer Protocol) wraps file transfer in SSH for encryption, replacing FTP in modern deployments due to security concerns.

## How It's Best Learned
Deploy a vsftpd server and observe both active and passive mode transfers using Wireshark. Monitor firewall rule impacts on passive mode. Configure an SFTP server and compare performance and security characteristics.

## Common Misconceptions
FTP is not secure; credentials are sent in plaintext on the control channel. Active mode is not inherently more secure or faster than passive mode. SFTP is not FTPS; FTPS wraps FTP in SSL/TLS while SFTP runs over SSH.

## Questions

```yaml
- question: "A client behind a firewall that blocks all unsolicited incoming TCP connections tries to download a file using FTP in active mode. The transfer fails. What is the direct cause?"
  type: multiple-choice
  options:
    - "Active mode uses UDP for data transfers, which firewalls always block"
    - "In active mode, the server initiates the data connection to the client's IP address and port — and the firewall blocks this incoming connection"
    - "Active mode requires the client to open port 21, but the firewall only allows outbound connections on port 80"
    - "The FTP control connection was not established because port 21 is also blocked for incoming connections"
  answer: 1
  explanation: "Active mode's defining characteristic is that the server initiates the data connection: the client tells the server 'I'm listening on port X,' and the server opens a TCP connection from its port 20 to the client's specified port. From the firewall's perspective, this is an unsolicited incoming connection — a server on the internet trying to connect to an internal host — which modern firewalls block by default. Passive mode solves this by reversing the roles: the client initiates both connections, so no incoming connections are required."

- question: "Why has SFTP largely replaced FTP in modern deployments rather than FTPS, despite FTPS also providing encryption?"
  type: multiple-choice
  options:
    - "SFTP uses faster encryption algorithms than FTPS, making file transfers significantly quicker"
    - "FTPS is not supported on Linux or Unix systems, limiting its deployment"
    - "SFTP runs over a single SSH connection (simpler for firewalls, strong authentication built in), while FTPS preserves FTP's dual-connection architecture with added TLS overhead"
    - "SFTP allows resuming interrupted transfers, while FTPS does not support this feature"
  answer: 2
  explanation: "FTPS adds TLS encryption to FTP's existing architecture, which means it still uses separate control and data connections — preserving all the firewall and NAT complications of FTP while adding certificate management overhead. SFTP, running as an SSH subsystem, uses a single encrypted connection for everything, inherits SSH's proven authentication (including public key auth), requires no special firewall configuration beyond the standard SSH port, and is available wherever SSH is installed. The single-connection architecture is the key practical advantage."

- question: "In FTP passive mode, the client initiates both the control connection to port 21 and the data connection to a server-provided high-numbered port."
  type: true-false
  answer: true
  explanation: "Passive mode was designed specifically to work through firewalls and NAT. The client opens the control connection to the server on port 21 (standard). When a data transfer is needed, the client sends a PASV command, and the server responds with an IP address and high-numbered port it is listening on. The client then opens the data connection outbound to that server port. Since the client initiates both connections, no incoming connections are needed on the client side — making passive mode work reliably through firewalls that block unsolicited inbound traffic."

- question: "SFTP (SSH File Transfer Protocol) is an encrypted version of FTP that adds SSL/TLS security to the existing FTP control and data channels."
  type: true-false
  answer: false
  explanation: "This describes FTPS, not SFTP. SFTP is an entirely different protocol that runs as a subsystem within SSH — it has no relationship to FTP beyond the name similarity and purpose. SFTP uses a single SSH-encrypted connection for all communication, while FTP (and FTPS) use separate control and data channels. FTPS (FTP over TLS/SSL) is the protocol that wraps FTP in encryption while preserving its dual-connection structure. The name confusion between SFTP and FTPS is one of the most common misconceptions in network administration."

- question: "Explain why FTP's active mode causes problems with firewalls and NAT, and why passive mode solves this problem."
  type: short-answer
  answer: "In active mode, the client tells the server its IP address and a listening port via the PORT command, and the server then initiates a TCP data connection from its port 20 to the client's specified port. Firewalls block this because it appears to be an unsolicited incoming connection from an external server to an internal client — exactly the type of traffic firewalls are designed to prevent. NAT compounds the problem because the internal IP address the client reports in the PORT command is private and unreachable from outside the NAT. In passive mode, the roles reverse: the server advertises a port it will listen on (via PASV response), and the client initiates the data connection outbound. Since the client initiates both connections, both look like normal outbound traffic to the firewall and NAT — no incoming connections are required."
  explanation: "The root cause is that FTP was designed in the 1970s when the internet had end-to-end connectivity and no firewalls or NAT. Active mode assumes the server can reach the client directly — an assumption that breaks in any modern network with firewall protection. Passive mode works around this by making the client always be the initiator, which is compatible with the client-initiates-outbound-connections model that firewalls expect."
```

## Explainer

From your knowledge of TCP and port addressing, you understand that applications communicate through socket connections identified by IP addresses and port numbers. FTP is unusual among application-layer protocols because it uses **two separate TCP connections** simultaneously: a **control connection** for commands and responses, and a **data connection** for actual file transfers. This dual-connection design made sense in the 1970s when it was designed — separating control from data allowed users to issue commands (list directory, change directory, rename files) while a large transfer was in progress — but it creates complications in modern firewalled networks.

The control connection is straightforward: the client connects to the server on **port 21** and exchanges text commands like `USER`, `PASS`, `LIST`, `RETR` (download), and `STOR` (upload). This connection stays open for the entire session. The data connection is where things get interesting. In **active mode**, the client tells the server "I'm listening on port X — connect to me there." The server then initiates a TCP connection from its port 20 to the client's specified port. This is problematic because firewalls and NAT devices typically block incoming connections to clients. In **passive mode**, the roles reverse: the client asks the server to listen on a random high-numbered port, and the client initiates the data connection. Since the client initiates both connections in passive mode, it works much better through firewalls and NAT — which is why passive mode is the default in virtually all modern FTP clients.

FTP's fatal flaw is **security**. Usernames, passwords, and all data travel in plaintext over both connections. Anyone able to observe network traffic — through packet sniffing on a shared network or a compromised router — can capture credentials and file contents. Two solutions emerged. **FTPS** (FTP over SSL/TLS) wraps the existing FTP protocol in encryption, preserving the dual-connection architecture but encrypting both channels. **SFTP** (SSH File Transfer Protocol) takes a completely different approach: it runs as a subsystem within an SSH session, using a single encrypted connection for both commands and data. Despite the similar names, FTPS and SFTP are entirely different protocols. SFTP has largely won in practice because it uses a single connection (simpler for firewalls), inherits SSH's strong authentication, and is available everywhere SSH is installed.

Understanding FTP remains valuable even as it fades from active use because its design illustrates fundamental tradeoffs in protocol architecture: the tension between in-band and out-of-band control, the complications that NAT and firewalls introduce for protocols that were designed for end-to-end connectivity, and the evolution from plaintext to encrypted protocols as security requirements changed.
