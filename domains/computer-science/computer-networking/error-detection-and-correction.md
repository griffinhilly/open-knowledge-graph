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

## Explainer

From your study of network fundamentals, you know that data travels across physical links — copper wires, fiber optic cables, radio waves — that are inherently noisy. Electromagnetic interference, signal attenuation, and crosstalk can flip bits during transmission. Without some mechanism to detect these errors, corrupted data would silently propagate through the network and eventually reach applications, causing anything from garbled text to corrupted files to system crashes. **Error detection and correction** is the set of techniques that networks use to maintain data integrity despite unreliable physical media.

The simplest error-detection scheme is the **parity bit**. You count the number of 1-bits in a data block and append a single bit that makes the total count even (even parity) or odd (odd parity). If a single bit flips during transmission, the parity check fails and the receiver knows the data is corrupted. But parity has a fatal weakness: if two bits flip, the parity is restored and the error goes undetected. **Checksums** improve on this by summing the data in larger chunks (typically 16-bit words) and appending the result; they catch more error patterns but still miss some systematic corruptions like byte reordering. More sophisticated schemes like CRC (cyclic redundancy check) use polynomial mathematics to detect virtually all burst errors up to a certain length.

**Error correction** goes a step further — instead of just detecting that something went wrong, it encodes enough redundancy to figure out what the original data was and fix it without retransmission. The classic example is the **Hamming code**, which strategically places parity bits at power-of-two positions so that the pattern of parity failures (called the **syndrome**) directly identifies the corrupted bit's position. More advanced codes like Reed-Solomon can correct multi-byte errors and are used in CDs, QR codes, and deep-space communication where retransmission is impractical or impossible.

The choice between detection and correction is a tradeoff between **overhead and latency**. Error correction codes add more redundant bits to every message, consuming bandwidth even when no errors occur. Error detection codes are leaner — they add minimal overhead and simply request retransmission when corruption is detected. For networks like Ethernet and the Internet, where error rates are low and retransmission is fast, detection plus retransmission (ARQ protocols) is the dominant strategy. For satellite links, storage media, and real-time systems where retransmission is expensive or impossible, forward error correction (FEC) is worth the overhead. Most real networks use both: detection at the link layer (CRC in Ethernet frames), detection at the transport layer (TCP checksums), and correction where latency matters (FEC in wireless protocols).
