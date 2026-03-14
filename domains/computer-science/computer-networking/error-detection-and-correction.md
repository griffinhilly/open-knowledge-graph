---
id: error-detection-and-correction
title: Error Detection and Correction
domain: computer-science
course: computer-networking
prerequisites:
- id: network-fundamentals
  type: hard
builds-toward:
- cyclic-redundancy-check
- automatic-repeat-request
tags:
- error-handling
- reliability
- checksums
- integrity
stage: advanced
status: draft
---

# Error Detection and Correction

## Core Idea
Error detection techniques use redundant information (checksums, parity bits, or cryptographic hashes) to identify corrupted data, while error correction codes can reconstruct lost or damaged data without retransmission. Detection is cheaper but requires retransmission; correction adds overhead but improves efficiency in high-loss environments. Networks typically use error detection at multiple layers combined with retransmission protocols.
