---
id: gossip-protocols
title: Gossip Protocols and Epidemic Algorithms
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-systems-overview
  type: hard
- id: eventual-consistency
  type: soft
tags:
- gossip
- epidemic
- information-dissemination
stage: advanced
status: draft
---

# Gossip Protocols and Epidemic Algorithms

## Core Idea
Gossip protocols spread information through a network by having each node periodically contact random peers and exchange state. Information propagates exponentially with logarithmic delay, and the protocol is robust to failures: if some nodes fail, information still reaches all healthy nodes. Gossip is used for failure detection, membership management, and database replication (Cassandra).
