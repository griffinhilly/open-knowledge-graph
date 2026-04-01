---
id: session-types
title: Session Types
domain: computer-science
course: formal-methods
prerequisites:
- id: type-systems-overview
  type: hard
- id: process-calculi
  type: soft
builds-toward: []
tags:
- session-type
- communication-protocol
- channel-type
- deadlock-freedom
- protocol-compliance
stage: expert
status: validated
---
# Session Types

## Core Idea
Session types are a type discipline for communication-centric programs that assigns types to communication channels, specifying the sequence, direction, and payload types of messages exchanged between processes. A session type like !Int.?Bool.end describes a channel that first sends an integer, then receives a Boolean, then closes. The type system statically guarantees that communicating processes follow their protocols: messages are sent and received in the correct order with the correct types, and every session is properly completed. Violations — sending when the protocol expects receiving, sending the wrong type, or abandoning a session — are caught at compile time.

## Questions

```yaml
- question: "The session type !Int.?String.end describes a channel endpoint. What does a process holding this endpoint do?"
  type: multiple-choice
  options:
    - "It receives an Int, then sends a String, then closes"
    - "It sends an Int, then receives a String, then closes"
    - "It sends both an Int and a String simultaneously"
    - "It either sends an Int or receives a String"
  answer: 1
  explanation: "The ! prefix means 'send' and ? means 'receive.' The dot sequences the operations. So !Int.?String.end means: first send an integer on the channel, then receive a string from the channel, then the session is complete. The dual endpoint (held by the other process) has the complementary type ?Int.!String.end — it receives the Int and sends the String. Session types enforce that both endpoints agree on the protocol."

- question: "If one endpoint has session type S, the other endpoint must have the dual type S-bar (complement). For !Int.?Bool.end, what is the dual?"
  type: short-answer
  answer: "?Int.!Bool.end — every send becomes a receive and vice versa. The dual ensures that when one process sends, the other receives, and the message types match at each step."
  explanation: "Duality is the fundamental mechanism ensuring communication safety. If process A has type !Int.?Bool.end and process B has the dual ?Int.!Bool.end, then: A sends an Int while B receives an Int (types match), then A receives a Bool while B sends a Bool (types match), then both close. Any mismatch in the protocol would result in a type error. This duality requirement is checked statically, guaranteeing protocol compliance without runtime verification."

- question: "Session types can guarantee deadlock freedom in concurrent programs."
  type: true-false
  answer: true
  explanation: "Advanced session type systems guarantee deadlock freedom by imposing structural constraints on how sessions are composed. Linear session types ensure each channel is used exactly once (preventing interference), and session type systems with progress guarantees ensure that well-typed programs always advance — no set of processes can be mutually waiting for each other. This is achieved by requiring certain orderings on channel usage or by restricting the topology of communication. The guarantee is not universal (some systems only ensure type safety, not deadlock freedom), but it is a major research achievement in session type theory."

- question: "Why do session type systems typically require linearity — that each channel endpoint is used exactly once?"
  type: short-answer
  answer: "Linearity ensures that a channel endpoint is not shared between multiple processes or used at different protocol stages simultaneously. If two processes could both hold the same endpoint, one might send when the protocol expects only one send, corrupting the session. Linearity also prevents a process from using an endpoint after closing it or abandoning it mid-session. These constraints are essential for the type system to track the channel's protocol state accurately."
  explanation: "This connects session types to linear types more broadly. A linear channel endpoint is a resource that must be used exactly once: you send/receive on it according to the session type, and you eventually close it. You cannot duplicate it (that would create two senders where the protocol expects one), and you cannot discard it (that would abandon the session). This resource discipline is what makes static protocol verification possible."
```

## Explainer

Concurrent and distributed programs communicate by sending messages over channels. A pervasive source of bugs is **protocol violations**: a process sends a message when the other side expects silence, sends data of the wrong type, or closes a connection before the protocol is complete. Testing catches some of these, but the combinatorial space of interleavings makes thorough testing nearly impossible. **Session types** bring the power of static type checking to communication protocols, catching protocol violations at compile time.

A session type describes the communication behavior of a channel endpoint as a sequence of operations. **!T** means "send a value of type T." **?T** means "receive a value of type T." The dot **.** sequences operations: `!Int.?Bool.end` means "send an Int, then receive a Bool, then close." **Branching** (&{label1: S1, label2: S2}) offers a choice to the other process, and **selection** (choose{label1: S1, label2: S2}) makes a choice. Recursion (rec X. !Int.X) models repeating protocols. The key invariant is **duality**: if one endpoint has type S, the other must have the dual type, obtained by swapping every ! with ? and every & with choose. This ensures that whenever one process sends, the other receives, and vice versa.

**Linearity** is the enforcement mechanism. Each channel endpoint must be used exactly once — you cannot duplicate an endpoint (which would create two processes trying to follow the same protocol step) or discard one (which would abandon the session mid-protocol). Linear type systems track this ownership: when a process sends on an endpoint of type !Int.S, the endpoint's type advances to S (the remaining protocol), and the old type !Int.S is consumed. This progression through the session type mirrors the progression through the communication protocol, and the type system verifies that every step is followed correctly.

Session types were introduced by Honda (1993) and extended by Honda, Vasconcelos, and Kubo. The theory has matured significantly: **multiparty session types** (Yoshida, Honda, and others) extend the framework from two-party to n-party protocols, specifying each participant's role in a global protocol description. Advanced systems guarantee not just type safety but **deadlock freedom** and **progress** — well-typed programs always advance and never reach a state where all processes are stuck waiting. These properties are checked statically through structural constraints on how sessions are composed.

Practical adoption is growing. Languages like **Links** and frameworks for **Scala**, **Go**, **Rust**, and **TypeScript** incorporate session types or session-type-inspired discipline. In microservice architectures, where services communicate via structured protocols, session types offer a way to verify at compile time that all services conform to the agreed-upon API contract. The connection to process calculi is deep: session types were originally formulated for the pi-calculus, and the duality/linearity discipline directly reflects the resource-sensitive nature of communication channels in concurrent computation.
