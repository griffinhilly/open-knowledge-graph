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

## Questions

```yaml
- question: "Consider replacing TCP's three-way handshake with a two-way handshake: the client sends SYN, and the server responds with SYN-ACK — after which the connection is considered established. What critical problem would this create?"
  type: multiple-choice
  options:
    - "The server would not receive the client's initial sequence number"
    - "The client would have no way to send data without a third message"
    - "The server's initial sequence number would be unacknowledged — the server has no confirmation that the client received the SYN-ACK and is ready to communicate"
    - "Two-way handshakes require more retransmissions and are therefore slower"
  answer: 2
  explanation: "The handshake must be mutual: each side proposes a sequence number AND receives confirmation that the other side received it. In a two-way handshake, the server sends SYN-ACK (confirming the client's ISN and proposing its own) but never hears back. The server has no guarantee the client received the SYN-ACK, knows the server's ISN, or is still present. Three messages are the minimum required for both sides to know both ISNs have been acknowledged. Option A is wrong: the client's SYN carries the client's ISN, so the server does receive it — the problem is the server's ISN going unconfirmed."

- question: "A server receives a SYN segment, sends SYN-ACK, and then receives RST from the client instead of ACK. What most likely happened?"
  type: multiple-choice
  options:
    - "The client intentionally aborted a new connection request"
    - "A stale SYN segment from a previous, long-closed connection arrived at the server after a network delay"
    - "The server's SYN-ACK contained an incorrect sequence number"
    - "The client ran out of ports before completing the connection"
  answer: 1
  explanation: "This is the stale duplicate SYN scenario the three-way handshake is designed to handle. A SYN from a previous connection may arrive late due to network delays. The server cannot know it is stale and responds with SYN-ACK. But the client has no matching connection state and sends RST to clean up the ghost connection. Without this third message, the server might maintain a half-open connection indefinitely. This protection against network ghosts is a key reason the handshake uses three steps rather than two."

- question: "The third message in TCP's three-way handshake — the client's final ACK — can carry application data at the same time."
  type: true-false
  answer: true
  explanation: "TCP allows the third message (client ACK) to be combined with the first data segment. Once both sides have agreed on sequence numbers and confirmed receipt, there is no protocol requirement to wait for a separate data-only segment. Many TCP implementations do send data in the third message, reducing latency by one round-trip time. This is valid because the connection is fully established at the moment the third message is sent."

- question: "TCP uses a three-way handshake (rather than two) primarily because it is a full-duplex protocol and each direction of communication requires a separate setup phase."
  type: true-false
  answer: false
  explanation: "The three-way handshake is not fundamentally about full-duplex operation — it is about mutual acknowledgment of initial sequence numbers. Each side must both propose an ISN and receive confirmation that the other side received it. This requires a minimum of three messages regardless of duplex operation. A two-way handshake would fail even for unidirectional communication because the initiating side would have no confirmation its SYN was received. Connection teardown (the four-way FIN exchange) is the mechanism that separately closes each direction of data flow."

- question: "Why must TCP's connection setup use exactly three messages rather than two? What would go wrong with a two-way handshake?"
  type: short-answer
  answer: "Both sides must synchronize initial sequence numbers, and each side must confirm receipt of the other's ISN. In two messages (SYN, SYN-ACK), the client's ISN is acknowledged but the server's is not — the server cannot know the client received its SYN-ACK and is ready to communicate. Three messages are the minimum for mutual confirmation of both ISNs."
  explanation: "Without the third message, the server also cannot distinguish an active new connection from a delayed stale SYN from a long-dead previous connection. The three steps are: (1) client proposes its ISN, (2) server acknowledges client's ISN and proposes its own, (3) client acknowledges server's ISN — only then is mutual synchronization confirmed. This ensures both sides are actively participating right now, not reacting to old network segments."
```

## Explainer

From your understanding of TCP as a reliable, connection-oriented protocol, you know it must establish shared state between two hosts before data can flow. But why does this require exactly three messages? The answer comes down to a fundamental problem: both sides need to agree on **initial sequence numbers (ISNs)**, and each side must confirm that it received the other's ISN. This mutual agreement cannot happen in fewer than three exchanges.

The process begins when the client sends a **SYN** (synchronize) segment to the server. This segment contains no application data — its purpose is to propose a connection and declare the client's initial sequence number. Think of it as saying, "I want to talk, and I'll start counting my bytes from sequence number X." The server, if it is listening on the requested port, responds with a **SYN-ACK** segment. This single message does two things simultaneously: it acknowledges the client's ISN (by setting the ACK number to X+1, meaning "I received your byte X and expect X+1 next") and declares the server's own initial sequence number Y. Finally, the client sends an **ACK** acknowledging the server's ISN (ACK number Y+1). At this point, both sides have proposed a sequence number and received confirmation that the other side heard it. The connection is established, and data transfer can begin — in fact, the third ACK can already carry application data.

The choice of initial sequence numbers is deliberately unpredictable. Early TCP implementations used simple incrementing counters, which made it possible for an attacker to guess the next ISN and inject forged packets into a connection (a **sequence prediction attack**). Modern implementations randomize ISNs to make this infeasible. The three-way handshake also protects against a subtler problem: **stale duplicate SYNs**. Imagine a SYN segment from a previous, long-closed connection arrives at the server after a delay. Without the handshake, the server might establish a ghost connection. With the handshake, the server replies with SYN-ACK, and when the client receives it, the client does not recognize the connection and sends a RST (reset), cleaning up the stale state. The three-step exchange ensures that both sides are actively participating right now, not reacting to network ghosts.

Connection teardown is conceptually similar but uses a **four-way handshake** (FIN, ACK, FIN, ACK) because each direction of data flow is closed independently. The connection also passes through several well-defined **TCP states** — LISTEN, SYN-SENT, SYN-RECEIVED, ESTABLISHED, and eventually TIME-WAIT — each representing a step in the negotiation. The TIME-WAIT state, where a closed connection lingers for twice the maximum segment lifetime, exists precisely to absorb any stale segments still floating in the network. Understanding these states is essential for diagnosing real-world issues like port exhaustion under heavy connection churn.
