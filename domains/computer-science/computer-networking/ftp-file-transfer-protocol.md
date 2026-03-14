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
