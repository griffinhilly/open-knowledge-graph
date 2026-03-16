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

## Explainer

If you have studied the OSI model, you know that network communication can be described as a stack of layers, each handling a specific responsibility. The **TCP/IP model** is the practical counterpart — the layered architecture that the Internet actually uses. While the OSI model was designed as a theoretical reference with seven layers, TCP/IP was built alongside the real protocols that power the Internet, and its four layers reflect how those protocols actually group together in practice.

The four layers, from bottom to top, are **Link**, **Internet**, **Transport**, and **Application**. The Link layer handles the physical transmission of data between directly connected devices — Ethernet frames on a LAN, Wi-Fi signals over the air. It corresponds roughly to OSI layers 1 (Physical) and 2 (Data Link) combined, because in practice these concerns are tightly coupled in real hardware. The **Internet layer** is where IP lives. Its job is addressing and routing: given a destination IP address, figure out the next hop toward that destination. This maps directly to OSI layer 3. The **Transport layer** provides end-to-end communication between applications on different hosts. TCP gives you reliable, ordered delivery; UDP gives you fast, lightweight delivery without guarantees. This maps to OSI layer 4. Finally, the **Application layer** encompasses everything above transport — HTTP for web pages, SMTP for email, DNS for name resolution — collapsing OSI layers 5, 6, and 7 into a single layer.

The collapsing of layers is not arbitrary. The OSI model separates "session management," "data presentation," and "application" into three distinct layers, but in practice, these concerns are almost always handled together within a single application protocol. HTTP manages its own sessions (via cookies and keep-alive), defines its own data format (headers, body encoding), and implements the application logic — all within one protocol. Splitting these into separate layers creates distinctions that rarely correspond to actual protocol boundaries. TCP/IP's pragmatic consolidation reflects how engineers actually build and think about networked systems.

The model is best understood by tracing a real request. When your browser requests a webpage, the Application layer constructs an HTTP request. The Transport layer wraps this in a TCP segment, adding source and destination port numbers so the receiving host knows which application should get the data. The Internet layer wraps the segment in an IP packet, adding source and destination IP addresses for routing across networks. The Link layer wraps the packet in a frame appropriate for the local network (an Ethernet frame, for instance), adding MAC addresses for the next hop. At each router along the path, the Link and Internet layers are processed and re-wrapped, but the Transport and Application data pass through untouched. At the destination, the layers are unwrapped in reverse order until the HTTP request reaches the web server. This process of wrapping data at each layer is called **encapsulation**, and it is the mechanism that allows each layer to operate independently of the others.
