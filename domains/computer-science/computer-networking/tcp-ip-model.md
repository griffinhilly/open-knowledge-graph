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

## Questions

```yaml
- question: "A browser sends an HTTP request to a web server. Which layer of the TCP/IP model is responsible for adding the source and destination IP addresses?"
  type: multiple-choice
  options:
    - "Application layer, because HTTP defines the addresses"
    - "Transport layer, because TCP needs IP addresses to route segments"
    - "Internet layer, because IP is responsible for addressing and routing"
    - "Link layer, because MAC addresses are used for all addressing"
  answer: 2
  explanation: "The Internet layer is where IP lives. Its job is addressing and routing — it wraps the Transport layer segment in an IP packet containing source and destination IP addresses. The Transport layer handles port numbers (which application), not IP addresses. The Link layer adds MAC addresses for the next hop, not end-to-end IP addresses."

- question: "Why does the TCP/IP model combine the OSI Session, Presentation, and Application layers into a single Application layer?"
  type: multiple-choice
  options:
    - "To reduce the total number of layers to four for simplicity"
    - "Because application protocols like HTTP handle session management and data formatting themselves, making the OSI separation artificial"
    - "Because the Session and Presentation layers were never implemented by any real protocols"
    - "Because TCP handles session management at the Transport layer"
  answer: 1
  explanation: "HTTP manages its own sessions (via cookies and keep-alive), defines its own data format (headers, body encoding), and implements application logic — all within one protocol. The OSI distinction between Session, Presentation, and Application layers rarely corresponds to actual protocol boundaries in practice. TCP/IP's consolidation reflects how real protocols are built, not a simplification for its own sake."

- question: "The TCP/IP model requires all applications to use TCP as their transport protocol."
  type: true-false
  answer: false
  explanation: "Despite being named 'TCP/IP,' the model supports both TCP and UDP at the Transport layer. TCP provides reliable, ordered delivery; UDP provides lightweight, low-latency delivery without guarantees. Many important applications use UDP — DNS queries, video streaming, VoIP, and online gaming all benefit from UDP's speed over TCP's overhead. The model does not mandate TCP."

- question: "In TCP/IP encapsulation, the Transport and Application layer data passes through intermediate routers unchanged."
  type: true-false
  answer: true
  explanation: "Routers process the Link and Internet layers — they strip the incoming frame, examine the IP destination, and re-wrap in a new frame for the next hop — but the Transport and Application layer data passes through untouched. This is why end-to-end reliability (TCP) and application logic (HTTP) work correctly across a network of routers; only the outermost wrapping changes at each hop."

- question: "What is encapsulation in the TCP/IP model, and why does it allow each layer to operate independently of the layers above and below it?"
  type: short-answer
  answer: "Encapsulation is the process by which each layer wraps the data from the layer above it in its own header before passing it downward. The Application layer produces data; Transport wraps it in a segment with port numbers; Internet wraps that in a packet with IP addresses; Link wraps that in a frame with MAC addresses. Because each layer only inspects and modifies its own header, it does not need to understand the contents from other layers — the Internet layer does not know whether the payload is TCP or UDP, or what application is involved. It simply routes IP packets."
  explanation: "This independence is what makes the layered model powerful. You can change the Link layer technology (swap Ethernet for Wi-Fi) without touching TCP or HTTP. You can use a different application protocol (SMTP instead of HTTP) without changing IP or the physical layer. Each layer has a well-defined interface with its neighbors, and the internals of each layer are hidden from all others."
```

## Explainer

If you have studied the OSI model, you know that network communication can be described as a stack of layers, each handling a specific responsibility. The **TCP/IP model** is the practical counterpart — the layered architecture that the Internet actually uses. While the OSI model was designed as a theoretical reference with seven layers, TCP/IP was built alongside the real protocols that power the Internet, and its four layers reflect how those protocols actually group together in practice.

The four layers, from bottom to top, are **Link**, **Internet**, **Transport**, and **Application**. The Link layer handles the physical transmission of data between directly connected devices — Ethernet frames on a LAN, Wi-Fi signals over the air. It corresponds roughly to OSI layers 1 (Physical) and 2 (Data Link) combined, because in practice these concerns are tightly coupled in real hardware. The **Internet layer** is where IP lives. Its job is addressing and routing: given a destination IP address, figure out the next hop toward that destination. This maps directly to OSI layer 3. The **Transport layer** provides end-to-end communication between applications on different hosts. TCP gives you reliable, ordered delivery; UDP gives you fast, lightweight delivery without guarantees. This maps to OSI layer 4. Finally, the **Application layer** encompasses everything above transport — HTTP for web pages, SMTP for email, DNS for name resolution — collapsing OSI layers 5, 6, and 7 into a single layer.

The collapsing of layers is not arbitrary. The OSI model separates "session management," "data presentation," and "application" into three distinct layers, but in practice, these concerns are almost always handled together within a single application protocol. HTTP manages its own sessions (via cookies and keep-alive), defines its own data format (headers, body encoding), and implements the application logic — all within one protocol. Splitting these into separate layers creates distinctions that rarely correspond to actual protocol boundaries. TCP/IP's pragmatic consolidation reflects how engineers actually build and think about networked systems.

The model is best understood by tracing a real request. When your browser requests a webpage, the Application layer constructs an HTTP request. The Transport layer wraps this in a TCP segment, adding source and destination port numbers so the receiving host knows which application should get the data. The Internet layer wraps the segment in an IP packet, adding source and destination IP addresses for routing across networks. The Link layer wraps the packet in a frame appropriate for the local network (an Ethernet frame, for instance), adding MAC addresses for the next hop. At each router along the path, the Link and Internet layers are processed and re-wrapped, but the Transport and Application data pass through untouched. At the destination, the layers are unwrapped in reverse order until the HTTP request reaches the web server. This process of wrapping data at each layer is called **encapsulation**, and it is the mechanism that allows each layer to operate independently of the others.
