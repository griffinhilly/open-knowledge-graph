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
status: draft
---

# Network Fundamentals

## Core Idea
Networks connect multiple computers to share resources and communicate by forwarding data units (packets) across links. Modern networks use a layered protocol stack where each layer provides services to the layer above while consuming services from the layer below. Understanding nodes, links, packets, and protocol layering is foundational to studying any networking technology.

## Explainer

From your study of operating systems, you know that a single computer manages processes, memory, and I/O devices through layers of abstraction. Networking extends this idea across machines: instead of processes communicating through shared memory or pipes on one host, they communicate by sending structured data across physical links connecting separate computers. The fundamental components are **nodes** (any device that sends or receives data — computers, routers, switches, phones), **links** (the physical or wireless connections between nodes), and **packets** (the discrete chunks of data that travel across those links). Rather than sending data as one continuous stream, networks break messages into packets that can be routed independently, reassembled at the destination, and retransmitted if lost.

The most important organizing principle in networking is **protocol layering**. Just as an OS kernel provides system calls that applications use without knowing the hardware details, each network layer provides a clean interface to the layer above it. The standard model has roughly five layers: the physical layer moves raw bits over a wire or radio signal; the data-link layer frames those bits and handles communication between directly connected nodes; the network layer routes packets across multiple hops from source to destination; the transport layer provides end-to-end reliability or speed; and the application layer implements the protocols users interact with, like HTTP or DNS. Each layer adds its own header to the data — a process called **encapsulation** — so that the corresponding layer at the receiving end can strip off that header and process it.

This layered design is what makes the internet possible at scale. A web browser does not need to know whether packets travel over fiber optic cable, Wi-Fi, or a satellite link — the lower layers handle that. A router in the middle of the network does not need to understand whether it is forwarding a video stream or an email — it just reads the network-layer header and forwards the packet toward its destination. Each layer can be designed, updated, and debugged independently, as long as it honors the interface contract with its neighbors. When you encounter concepts like packet switching, error detection, or routing in later topics, you will be working within specific layers of this stack — and the layered model is what keeps the complexity manageable.

To build intuition, think of sending a letter through a postal system. You write the letter (application layer), put it in an envelope with a destination address (network layer), hand it to the mail carrier who knows the local route (data-link layer), and the carrier drives it on a road (physical layer). At each stage, a different agent handles the message using only the information relevant to their job. Networking works the same way — every layer does one job well and trusts the other layers to do theirs.
