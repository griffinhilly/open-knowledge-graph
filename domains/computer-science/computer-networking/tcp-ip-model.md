---
id: tcp-ip-model
title: TCP/IP Model and Protocol Stack
domain: computer-science
course: computer-networking
prerequisites:
- id: osi-model-layers
  type: soft
builds-toward:
- ipv4-addressing
- tcp-transmission-control-protocol
- udp-user-datagram-protocol
tags:
- tcp-ip
- protocol-stack
- network-architecture
- internet
stage: advanced
status: draft
---

# TCP/IP Model and Protocol Stack

## Core Idea
The TCP/IP model is a four-layer framework (Link, Internet, Transport, Application) that describes how the Internet actually works, in contrast to the theoretical seven-layer OSI model. It combines OSI's bottom two layers into a single Link layer and merges OSI's top three layers into Application, making it simpler and more practical for understanding real networks.

## How It's Best Learned
Map TCP/IP layers to OSI layers, then identify which major protocols (IP, TCP, UDP, HTTP, DNS) belong to each TCP/IP layer.

## Common Misconceptions
- TCP/IP model and OSI model are competing standards; they coexist, with TCP/IP being more practical and widely used.
- TCP/IP requires TCP; UDP is equally valid for many applications (DNS, video streaming, VoIP).
