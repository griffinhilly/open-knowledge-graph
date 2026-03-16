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

## Explainer

From your understanding of TCP as a reliable, connection-oriented protocol, you know it must establish shared state between two hosts before data can flow. But why does this require exactly three messages? The answer comes down to a fundamental problem: both sides need to agree on **initial sequence numbers (ISNs)**, and each side must confirm that it received the other's ISN. This mutual agreement cannot happen in fewer than three exchanges.

The process begins when the client sends a **SYN** (synchronize) segment to the server. This segment contains no application data — its purpose is to propose a connection and declare the client's initial sequence number. Think of it as saying, "I want to talk, and I'll start counting my bytes from sequence number X." The server, if it is listening on the requested port, responds with a **SYN-ACK** segment. This single message does two things simultaneously: it acknowledges the client's ISN (by setting the ACK number to X+1, meaning "I received your byte X and expect X+1 next") and declares the server's own initial sequence number Y. Finally, the client sends an **ACK** acknowledging the server's ISN (ACK number Y+1). At this point, both sides have proposed a sequence number and received confirmation that the other side heard it. The connection is established, and data transfer can begin — in fact, the third ACK can already carry application data.

The choice of initial sequence numbers is deliberately unpredictable. Early TCP implementations used simple incrementing counters, which made it possible for an attacker to guess the next ISN and inject forged packets into a connection (a **sequence prediction attack**). Modern implementations randomize ISNs to make this infeasible. The three-way handshake also protects against a subtler problem: **stale duplicate SYNs**. Imagine a SYN segment from a previous, long-closed connection arrives at the server after a delay. Without the handshake, the server might establish a ghost connection. With the handshake, the server replies with SYN-ACK, and when the client receives it, the client does not recognize the connection and sends a RST (reset), cleaning up the stale state. The three-step exchange ensures that both sides are actively participating right now, not reacting to network ghosts.

Connection teardown is conceptually similar but uses a **four-way handshake** (FIN, ACK, FIN, ACK) because each direction of data flow is closed independently. The connection also passes through several well-defined **TCP states** — LISTEN, SYN-SENT, SYN-RECEIVED, ESTABLISHED, and eventually TIME-WAIT — each representing a step in the negotiation. The TIME-WAIT state, where a closed connection lingers for twice the maximum segment lifetime, exists precisely to absorb any stale segments still floating in the network. Understanding these states is essential for diagnosing real-world issues like port exhaustion under heavy connection churn.
