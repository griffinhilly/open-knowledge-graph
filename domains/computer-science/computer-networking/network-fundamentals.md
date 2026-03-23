---
id: network-fundamentals
title: Network Fundamentals
domain: computer-science
course: computer-networking
prerequisites:
- id: operating-systems
  type: hard
builds-toward:
- packet-switching-circuit-switching
- encapsulation-and-protocol-layers
- error-detection-and-correction
tags:
- networking
- foundations
- basics
stage: advanced
status: validated
---

# Network Fundamentals

## Core Idea
Networks connect multiple computers to share resources and communicate by forwarding data units (packets) across links. Modern networks use a layered protocol stack where each layer provides services to the layer above while consuming services from the layer below. Understanding nodes, links, packets, and protocol layering is foundational to studying any networking technology.

## Questions

```yaml
- question: "A YouTube video streams over a cellular network. Which layer is responsible for ensuring that video data packets are delivered reliably and in order to the viewer's device?"
  type: multiple-choice
  options:
    - "Physical layer — it controls the radio signals that carry the data"
    - "Network layer — it routes packets across the internet from YouTube's servers to the viewer"
    - "Transport layer — it provides end-to-end reliability between the communicating applications"
    - "Application layer — HTTP handles reliable delivery of video data directly"
  answer: 2
  explanation: "End-to-end reliability is the job of the transport layer (TCP in this case). The physical layer handles raw bit transmission over the radio link between adjacent nodes; the network layer routes packets hop by hop across the internet; the application layer (HTTP) operates in terms of requests and responses, relying on lower layers for delivery guarantees. The critical point is that 'end-to-end' means across the entire path from source to destination — spanning multiple physical links and routers — which is precisely the transport layer's scope. This is one of the most useful mental models in networking: different guarantees live at different layers."

- question: "An engineer wants to replace the physical transmission medium from fiber optic cable to a new quantum communication link, without changing how IP routing, TCP connections, or web applications work. Is this possible under the layered model?"
  type: multiple-choice
  options:
    - "No — changing the physical medium requires updating all higher layers since they depend on implementation details of the physical transmission"
    - "Yes — each layer only interacts with its immediate neighbor through a defined service interface; higher layers don't know or care about the physical medium"
    - "Only if the quantum link supports the same bandwidth as fiber, since higher layers assume specific throughput"
    - "Only if IP and TCP are redesigned to take advantage of quantum properties"
  answer: 1
  explanation: "This is the central benefit of protocol layering: as long as a new physical medium implements the same service interface to the data-link layer above it (the ability to transfer frames between directly connected nodes), everything higher in the stack works unchanged. This is how Ethernet, Wi-Fi, fiber, 5G, and satellite links all run under the same IP stack — they all implement the same interface. The layers above don't know what medium is below them, and by design, they don't need to."

- question: "For the transport layer to send data correctly, it must know whether the physical layer is using fiber optic cable, Wi-Fi, or a cellular radio link."
  type: true-false
  answer: false
  explanation: "This is exactly what protocol layering prevents. Each layer interacts only with its immediate neighbors through defined interfaces: the transport layer calls on the network layer, which calls on the data-link layer, which calls on the physical layer. The physical medium is completely invisible to the transport layer — this independence is the key architectural property. It is why the internet can work across such diverse physical infrastructure without every application needing to be redesigned for each new medium."

- question: "Encapsulation in a protocol stack means that as data passes down the sending stack, each layer adds its own header, creating a nested structure that each corresponding layer at the receiving end strips off."
  type: true-false
  answer: true
  explanation: "As data passes from application → transport → network → data-link → physical, each layer prepends its own header (and sometimes a trailer) to the payload, wrapping it like nested envelopes. The receiving end unwraps in reverse: the physical layer passes bits up; the data-link layer strips its frame header; the network layer strips the IP header; the transport layer strips the TCP/UDP header; the application receives the original data. Each header contains information only that layer needs to do its job — port numbers for transport, IP addresses for network, MAC addresses for data-link. This structure is what lets each layer operate independently."

- question: "Why does breaking a message into small packets (rather than transmitting it as one continuous stream) improve network performance and reliability?"
  type: short-answer
  answer: "Packets enable multiple sources to share the same links simultaneously through statistical multiplexing: different packets from different users interleave on the same wire, so no user monopolizes a dedicated connection. If transmission fails, only the lost packet needs retransmission, not the entire message. Packets can take different routes through the network if a path becomes congested or fails, increasing resilience. Smaller packets also reduce head-of-line blocking: a large continuous stream would delay all other traffic until it finishes, while short packets allow other users' packets to interleave. These properties together make packet-switched networks far more efficient and robust than circuit-switched networks that dedicate a fixed path for each communication."
  explanation: "The contrast with circuit switching clarifies the advantage: in a circuit-switched network (like traditional telephone), a dedicated path is reserved for the duration of the call, wasting capacity whenever there's silence. Packet switching shares capacity dynamically — links carry packets from whoever has something to send. The internet's scalability to billions of simultaneous users depends fundamentally on this sharing."
```

## Explainer

From your study of operating systems, you know that a single computer manages processes, memory, and I/O devices through layers of abstraction. Networking extends this idea across machines: instead of processes communicating through shared memory or pipes on one host, they communicate by sending structured data across physical links connecting separate computers. The fundamental components are **nodes** (any device that sends or receives data — computers, routers, switches, phones), **links** (the physical or wireless connections between nodes), and **packets** (the discrete chunks of data that travel across those links). Rather than sending data as one continuous stream, networks break messages into packets that can be routed independently, reassembled at the destination, and retransmitted if lost.

The most important organizing principle in networking is **protocol layering**. Just as an OS kernel provides system calls that applications use without knowing the hardware details, each network layer provides a clean interface to the layer above it. The standard model has roughly five layers: the physical layer moves raw bits over a wire or radio signal; the data-link layer frames those bits and handles communication between directly connected nodes; the network layer routes packets across multiple hops from source to destination; the transport layer provides end-to-end reliability or speed; and the application layer implements the protocols users interact with, like HTTP or DNS. Each layer adds its own header to the data — a process called **encapsulation** — so that the corresponding layer at the receiving end can strip off that header and process it.

This layered design is what makes the internet possible at scale. A web browser does not need to know whether packets travel over fiber optic cable, Wi-Fi, or a satellite link — the lower layers handle that. A router in the middle of the network does not need to understand whether it is forwarding a video stream or an email — it just reads the network-layer header and forwards the packet toward its destination. Each layer can be designed, updated, and debugged independently, as long as it honors the interface contract with its neighbors. When you encounter concepts like packet switching, error detection, or routing in later topics, you will be working within specific layers of this stack — and the layered model is what keeps the complexity manageable.

To build intuition, think of sending a letter through a postal system. You write the letter (application layer), put it in an envelope with a destination address (network layer), hand it to the mail carrier who knows the local route (data-link layer), and the carrier drives it on a road (physical layer). At each stage, a different agent handles the message using only the information relevant to their job. Networking works the same way — every layer does one job well and trusts the other layers to do theirs.
