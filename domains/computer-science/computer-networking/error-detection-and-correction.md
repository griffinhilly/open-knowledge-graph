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

## Questions

```yaml
- question: "A satellite communicating with a deep-space probe has a 40-minute round-trip signal delay. When bit errors occur, the best error-handling strategy is:"
  type: multiple-choice
  options:
    - "Parity bits with retransmission requested on every detected error"
    - "Forward error correction codes that let the receiver reconstruct corrupted data without retransmission"
    - "CRC checksums combined with TCP-style ARQ retransmission"
    - "No redundancy — deep-space links are clean enough that error handling is unnecessary"
  answer: 1
  explanation: "With a 40-minute round-trip delay, retransmitting on every error would mean waiting 40 minutes per correction — completely impractical. Forward error correction (FEC) encodes enough redundancy into the original transmission that the receiver can reconstruct corrupted bits locally. The overhead of extra bits is worth it when retransmission is impossibly slow. Detection + retransmission strategies (ARQ) are ideal for low-latency networks like Ethernet, not deep-space links."

- question: "A network engineer adds a single parity bit to each 8-bit data byte. If two bits are flipped by noise during transmission, what happens?"
  type: multiple-choice
  options:
    - "The error is detected — parity bits catch all errors regardless of how many bits flip"
    - "The error goes undetected — two flipped bits restore the parity to its expected value"
    - "The error is corrected — the parity bit identifies which two bits were flipped"
    - "The error is partially detected — parity catches the first flipped bit but ignores the second"
  answer: 1
  explanation: "Parity works by making the count of 1-bits even (or odd). One flipped bit changes the count and is detected. But two flipped bits change the count by 2, restoring the original parity — the error is invisible to the receiver. This is parity's fundamental weakness: it reliably detects odd numbers of bit errors but misses all even-numbered errors. This limitation motivates stronger schemes like CRC for real networking."

- question: "Error correction codes require more redundant bits than error detection codes because they must encode enough information to identify the specific location of corrupted bits, not just whether corruption occurred."
  type: true-false
  answer: true
  explanation: "Detection only needs to signal 'something went wrong' — a single bit change suffices to indicate corruption. Correction must pinpoint *which* bit(s) need flipping, which requires enough redundancy to uniquely identify the error position. Hamming codes, for example, use parity bits at power-of-two positions so the syndrome (pattern of parity failures) directly encodes the error location. More correction capability = more redundant bits per message."

- question: "Because modern error correction codes can fix corrupted data automatically, they have replaced error detection protocols in all layers of modern networks."
  type: true-false
  answer: false
  explanation: "Real networks use both, at different layers, based on tradeoffs. Ethernet uses CRC (detection) at the link layer; TCP uses checksums (detection) at the transport layer; 5G wireless uses FEC (correction) where retransmission adds too much latency. Detection + retransmission dominates when error rates are low and retransmission is fast. Correction dominates where retransmission is impractical. The two approaches are complementary, not substitutes."

- question: "Explain why 'forward error correction' is preferred over 'detection + retransmission' in some communication environments. What property of the environment makes correction worth the extra bandwidth overhead?"
  type: short-answer
  answer: "FEC is preferred when retransmission is impractical or prohibitively expensive — either because round-trip latency is very high (deep-space, satellite links) or because the channel cannot support bidirectional signaling (broadcast media, one-way streaming). In these environments, the cost of waiting for a retransmission exceeds the cost of sending extra redundant bits upfront. The extra bandwidth overhead of FEC becomes worthwhile when the alternative is unacceptable delay or failed correction."
  explanation: "The tradeoff is overhead vs. latency. FEC burns bandwidth on every transmission, even when no errors occur. ARQ only pays when errors happen, but its cost is delay proportional to round-trip time. For Ethernet (microseconds RTT, rare errors), ARQ wins. For satellite (hundreds of milliseconds RTT, moderate error rates), FEC wins. Real systems combine both: FEC handles most errors proactively, ARQ handles the rare cases FEC can't fix."
```

## Explainer

From your study of network fundamentals, you know that data travels across physical links — copper wires, fiber optic cables, radio waves — that are inherently noisy. Electromagnetic interference, signal attenuation, and crosstalk can flip bits during transmission. Without some mechanism to detect these errors, corrupted data would silently propagate through the network and eventually reach applications, causing anything from garbled text to corrupted files to system crashes. **Error detection and correction** is the set of techniques that networks use to maintain data integrity despite unreliable physical media.

The simplest error-detection scheme is the **parity bit**. You count the number of 1-bits in a data block and append a single bit that makes the total count even (even parity) or odd (odd parity). If a single bit flips during transmission, the parity check fails and the receiver knows the data is corrupted. But parity has a fatal weakness: if two bits flip, the parity is restored and the error goes undetected. **Checksums** improve on this by summing the data in larger chunks (typically 16-bit words) and appending the result; they catch more error patterns but still miss some systematic corruptions like byte reordering. More sophisticated schemes like CRC (cyclic redundancy check) use polynomial mathematics to detect virtually all burst errors up to a certain length.

**Error correction** goes a step further — instead of just detecting that something went wrong, it encodes enough redundancy to figure out what the original data was and fix it without retransmission. The classic example is the **Hamming code**, which strategically places parity bits at power-of-two positions so that the pattern of parity failures (called the **syndrome**) directly identifies the corrupted bit's position. More advanced codes like Reed-Solomon can correct multi-byte errors and are used in CDs, QR codes, and deep-space communication where retransmission is impractical or impossible.

The choice between detection and correction is a tradeoff between **overhead and latency**. Error correction codes add more redundant bits to every message, consuming bandwidth even when no errors occur. Error detection codes are leaner — they add minimal overhead and simply request retransmission when corruption is detected. For networks like Ethernet and the Internet, where error rates are low and retransmission is fast, detection plus retransmission (ARQ protocols) is the dominant strategy. For satellite links, storage media, and real-time systems where retransmission is expensive or impossible, forward error correction (FEC) is worth the overhead. Most real networks use both: detection at the link layer (CRC in Ethernet frames), detection at the transport layer (TCP checksums), and correction where latency matters (FEC in wireless protocols).
