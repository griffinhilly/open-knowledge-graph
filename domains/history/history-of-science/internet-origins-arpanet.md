---
id: internet-origins-arpanet
title: "The Internet Origins: ARPANET and Decentralized Networks"
domain: history
course: history-of-science
prerequisites:
- id: computing-revolution-turing-von-neumann
  type: hard

builds-toward:
- digital-economy-history
tags:
- history
- History Of Science
stage: advanced
status: validated
---

# The Internet Origins: ARPANET and Decentralized Networks

## Core Idea
The ARPANET, developed by the Advanced Research Projects Agency beginning in 1968, was designed to enable computer communication across geographically distributed research institutions. Its architects — Larry Roberts, Bob Taylor, Vint Cerf, Bob Kahn, and others — developed packet-switching protocols that allowed data to be broken into chunks, sent independently across heterogeneous networks, and reassembled at the destination. This architecture was radically decentralized: no single control point, no requirement for a central authority, resilient to partial failures. The TCP/IP protocol suite, developed in the 1970s, provided a standardized way for different networks to interconnect. The ARPANET evolved into the Internet, and the development of the World Wide Web in 1989 made it accessible to non-specialists. The Internet's history reveals how technological design embodies political assumptions: the decentralized architecture reflected Cold War concerns about survivability of command networks, yet it also enabled democratic communication structures. The Internet is a rare case where a transformative technology's origins are well-documented and traceable to specific decisions.

## Questions

```yaml

- question: "ARPANET was designed to survive a nuclear attack by routing packets around destroyed nodes. Is this account accurate?"
  type: short-answer
  answer: "The nuclear survivability narrative is largely a myth. Paul Baran at RAND did propose survivable distributed communication networks in 1962, and packet switching does have resilience properties — but ARPANET's actual designers (Larry Roberts, Bob Taylor) were primarily motivated by enabling resource sharing among research computers, not nuclear survivability. The confusion arose because Baran's survivability research and ARPANET's development were contemporaneous and overlapping in the same technical community, and the story was appealing as a Cold War justification for the project."
  explanation: "This is a well-documented historical misconception. Katie Hafner and Matthew Lyon's 'Where Wizards Stay Up Late' provides the definitive account of ARPANET's actual origins and motivations."

- question: "What was 'packet switching,' and why was it radical compared to the existing circuit-switched telephone network?"
  type: short-answer
  answer: "Circuit switching (used in telephone networks) establishes a dedicated physical connection between caller and receiver for the duration of a call — the circuit is reserved whether or not data is being sent, which is inefficient. Packet switching, developed by Paul Baran (RAND) and Donald Davies (NPL, UK) independently in the early 1960s, breaks messages into small chunks (packets), each of which travels independently through the network and is reassembled at the destination. This was radical because: packets share network capacity more efficiently (bandwidth is used only when needed); the network can route around failures (different packets take different paths); no central switching office is needed. TCP/IP is the protocol family implementing packet switching for internet communication."
  explanation: "Packet switching is the foundational design choice that makes the internet's decentralized architecture possible. All internet communication — web, email, video — is transmitted as packets."

- question: "Tim Berners-Lee invented the World Wide Web while working at CERN in 1989. How did the Web differ from the underlying Internet?"
  type: multiple-choice
  options:
    - "The Web replaced the Internet's packet-switching architecture with a more efficient content delivery system"
    - "The Internet is the underlying communication infrastructure; the Web is an application — a system of linked documents accessible via browsers using HTTP and HTML protocols — built on top of the Internet"
    - "The Web and the Internet are the same thing; Berners-Lee invented both"
    - "Berners-Lee invented the Web as a commercial competitor to the government-funded Internet"
  answer: 1
  explanation: "The Internet (physical infrastructure, TCP/IP protocol) and the World Wide Web (application built on top of it) are often conflated but are distinct. The Internet existed since 1969 as ARPANET and had email, FTP, and other applications before the Web existed. The Web — hypertext documents linked by URLs, accessed via browsers using HTTP — was invented by Berners-Lee at CERN in 1989-1991 and made the Internet accessible to non-specialists through a graphical interface. Other applications (email, streaming, peer-to-peer) also run on the Internet but are not the Web."

- question: "The Internet's decentralized architecture was a deliberate design choice that embeds political assumptions about how communication should be structured."
  type: true-false
  answer: true
  explanation: "The Internet's architecture reflects deliberate choices about where intelligence and control reside. The 'end-to-end principle' (Saltzer, Reed, Clark, 1984) holds that network functions should be implemented at the endpoints (computers) rather than in the network core, keeping the network simple and neutral. This embeds assumptions: no single node can control what others say; content decisions are made at the edges; the network is 'dumb' and content-agnostic. These are political choices, not technical necessities. Many authoritarian states have built architectures where the network core can filter, monitor, and block content — demonstrating that internet architecture is a choice with political consequences."

- question: "Mosaic, the first graphical Web browser, was released in 1993. What was its significance for Internet adoption?"
  type: short-answer
  answer: "Mosaic (developed by Marc Andreessen and Eric Bina at NCSA) made the Web accessible to non-technical users by displaying images inline with text and providing point-and-click navigation. Before Mosaic, Web browsers were text-only and used complex commands. Mosaic's graphical interface reduced the barrier to entry dramatically; Netscape Communications (founded by Andreessen) commercialized a successor browser, and rapid commercial adoption of the Web followed 1993-1995. The transition from 1 million to 100 million Internet users took roughly 7 years (1993-2000). Mosaic is often credited with triggering the commercialization of the Internet."

```

## Explainer

The Internet's history is among the best-documented cases of how a publicly-funded research project can produce a technology transforming every domain of human activity in ways its creators did not anticipate.

The ARPANET, established by the Department of Defense's Advanced Research Projects Agency beginning in 1968, had a specific and limited purpose: enabling researchers at different universities and government labs to share computing resources — expensive mainframe computers — without physically visiting each other's sites. The network was small: the first message was sent from UCLA to the Stanford Research Institute in October 1969. Larry Roberts (ARPA program manager), Bob Taylor (who pushed for the network's creation), and the contractor teams at Bolt Beranek and Newman built the first packet-switching network.

Packet switching — the fundamental architectural choice — was radical. Rather than establishing dedicated circuits (as in the telephone network), data was broken into packets that traveled independently through the network and were reassembled at the destination. This made the network more efficient and more resilient: packets could be rerouted if nodes were unavailable. The TCP/IP protocol suite, developed by Vint Cerf and Bob Kahn in the early 1970s, standardized how different networks communicated — enabling an 'internet of networks' (hence 'internet').

Through the 1970s and 1980s, the Internet was used primarily by researchers and academics for email, file transfer, and remote access. Acceptable use policies explicitly prohibited commercial activity. NSF took over civilian internet infrastructure from ARPA in the late 1980s and began transitioning toward commercial operation.

Tim Berners-Lee at CERN invented the World Wide Web in 1989 — a system of hypertext documents linked by URLs, accessed via a browser using HTTP. This was a particular application built on top of the Internet, not the Internet itself. The Web made the Internet accessible to non-specialists: point-and-click navigation through linked information spaces. Mosaic (1993), the first graphical browser, triggered rapid adoption; Netscape commercialized the Web and sparked the dot-com boom. The Internet's user base grew from roughly 1 million (1993) to over 100 million (2000).

The Internet's political dimensions were evident from the start. The network's end-to-end architecture — intelligence at the edges, dumb network core — embeds assumptions about decentralized control that contrasted with the telephone company's centralized architecture. These choices are not technically inevitable: authoritarian states have built internet architectures that filter and monitor content at the network core. The architecture of communication systems is a political choice.
