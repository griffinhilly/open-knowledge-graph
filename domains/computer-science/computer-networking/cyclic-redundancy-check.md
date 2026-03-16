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

## Explainer

From your study of error detection and correction, you know the basic idea: append redundant information to data so the receiver can detect if something changed in transit. A simple checksum adds up byte values, but it misses many common corruption patterns — for example, swapping two bytes produces the same sum. **Cyclic Redundancy Check (CRC)** is a far more powerful error-detection scheme that catches virtually all common bit-error patterns by treating the entire data stream as a mathematical object and performing polynomial division on it.

The core idea uses an analogy to ordinary long division, but over binary polynomials instead of decimal numbers. Think of your data bits as the coefficients of a polynomial: the bit string 1101 represents x³ + x² + 1. You also choose a fixed **generator polynomial** — for example, CRC-32 uses a specific 33-bit polynomial standardized for Ethernet. To compute the CRC, you divide the data polynomial by the generator polynomial using XOR-based binary division (no carries, no borrows — just XOR at each step). The **remainder** of this division is the CRC value, which you append to the data before transmission.

At the receiving end, the receiver performs the same polynomial division on the entire received message (data plus CRC). If no errors occurred, the remainder is exactly zero. If any bits were corrupted during transmission, the remainder will be nonzero, and the receiver knows to discard the frame. The mathematical properties of polynomial division guarantee that CRC detects all single-bit errors, all double-bit errors (for well-chosen generators), all odd numbers of bit errors, and all **burst errors** shorter than the CRC length. A burst error is a contiguous sequence of corrupted bits — exactly the kind of corruption that noisy communication links produce — and CRC's ability to catch these bursts is its main advantage over simple checksums.

In practice, CRC computation is implemented in hardware using **shift registers** with XOR feedback taps arranged to match the generator polynomial. Each incoming bit is shifted in and XOR'd with the feedback, producing the remainder one bit at a time with no multiplication or division hardware required. This makes CRC extremely fast — Ethernet NICs compute CRC-32 over every frame at wire speed. The choice of generator polynomial is not arbitrary; standardized polynomials like CRC-32 (used in Ethernet and ZIP files) and CRC-16 (used in USB and Modbus) have been mathematically analyzed to maximize error-detection probability for their target applications and data lengths.
