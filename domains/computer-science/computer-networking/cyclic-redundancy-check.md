---
id: cyclic-redundancy-check
title: Cyclic Redundancy Check (CRC)
domain: computer-science
course: computer-networking
prerequisites:
- id: error-detection-and-correction
  type: hard
builds-toward:
- ethernet-protocol
tags:
- crc
- error-detection
- polynomial
- checksum
stage: advanced
status: draft
---

# Cyclic Redundancy Check (CRC)

## Core Idea
CRC treats data as a polynomial and computes a remainder when divided by a fixed generator polynomial, appending this remainder to detect bit errors. CRC is computationally efficient, catches single and burst errors effectively, and is widely used in Ethernet and other link-layer protocols. The choice of generator polynomial determines the error-detection capability.
