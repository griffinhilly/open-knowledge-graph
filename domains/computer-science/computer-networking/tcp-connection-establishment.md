---
id: tcp-connection-establishment
title: TCP Connection Establishment (Three-Way Handshake)
domain: computer-science
course: computer-networking
prerequisites:
- id: tcp-transmission-control-protocol
  type: hard
builds-toward:
- tcp-flow-control-and-congestion-control
tags:
- three-way-handshake
- syn
- ack
- connection-setup
- tcp-states
stage: advanced
status: draft
---

# TCP Connection Establishment (Three-Way Handshake)

## Core Idea
TCP connections are established via a three-way handshake: the client sends SYN, the server responds with SYN-ACK, and the client replies with ACK. This exchange initializes sequence numbers and ensures both sides are ready to communicate, preventing connection issues due to stale segments from past connections.
