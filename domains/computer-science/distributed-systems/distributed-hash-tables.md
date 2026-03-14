---
id: distributed-hash-tables
title: Distributed Hash Tables and DHT
domain: computer-science
course: distributed-systems
prerequisites:
- id: hash-tables
  type: hard
- id: consistent-hashing
  type: hard
builds-toward:
- gossip-protocols
tags:
- dht
- peer-to-peer
- distributed-storage
stage: advanced
status: draft
---

# Distributed Hash Tables and DHT

## Core Idea
Distributed hash tables (DHTs) extend hash tables across many machines using consistent hashing: keys hash to positions on a ring, each node stores a range, and lookups route toward the responsible node. DHTs enable decentralized storage (Chord, Kademlia) with logarithmic lookup time and automatic load balancing as nodes join and leave.
