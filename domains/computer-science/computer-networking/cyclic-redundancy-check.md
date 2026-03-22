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

## Questions

```yaml
- question: "A sender transmits a data frame with its CRC appended. The receiver performs polynomial division on the entire received message and gets a remainder of zero. What can be concluded?"
  type: multiple-choice
  options:
    - "The data was received without any bit errors — the transmission was perfect"
    - "No errors were introduced that are detectable by the chosen generator polynomial"
    - "The CRC check passed, so the receiver should request a retransmission to confirm"
    - "A zero remainder means the CRC was lost in transit and must be re-requested"
  answer: 1
  explanation: "A zero remainder means the received message passed the CRC check — but CRC cannot detect every possible error pattern. If the pattern of bit flips happens to be divisible by the generator polynomial (an astronomically unlikely but nonzero probability), the remainder will still be zero despite corruption. So the correct statement is 'no detectable errors,' not 'no errors.' Option 0 overclaims the guarantee. CRC is error detection, not error correction, so retransmission is triggered only on a nonzero remainder, making options 2 and 3 incorrect."

- question: "Why does CRC catch burst errors far more reliably than a simple additive byte checksum?"
  type: multiple-choice
  options:
    - "CRC uses more bits than most checksums, so it has statistically more coverage"
    - "The algebraic properties of polynomial division over GF(2) guarantee detection of all burst errors shorter than the CRC degree, regardless of their position in the data"
    - "CRC recalculates a hash of the full message, while checksums only compare individual byte values"
    - "CRC can correct burst errors once detected, which is why it catches more than checksums"
  answer: 1
  explanation: "The advantage is mathematical, not just quantitative. Polynomial division over GF(2) (binary XOR arithmetic) has provable properties: any burst error shorter than the degree of the generator polynomial produces a nonzero remainder. This is a theorem about polynomial algebra, not a statistical approximation. A simple additive checksum can miss burst errors because reordering or swapping corrupted bytes can still sum to the same total. Option 0 is partially true but misses the algebraic guarantee. Option 3 is false — CRC is detection-only."

- question: "CRC is implemented efficiently in hardware using shift registers with XOR feedback taps, allowing it to process data at wire speed without requiring division circuits."
  type: true-false
  answer: true
  explanation: "Polynomial division over GF(2) maps directly onto a linear feedback shift register (LFSR): each incoming bit shifts through the register, and XOR operations at tap positions implement the modular reduction by the generator polynomial. This requires only shift and XOR operations — no multiplier or divider hardware. Ethernet NICs compute CRC-32 over every frame at full line rate using this hardware implementation. The mathematical description (polynomial division) sounds expensive but the hardware realization is extremely simple."

- question: "CRC detects all possible bit error patterns in a transmitted frame, making it a complete and sufficient error-detection scheme."
  type: true-false
  answer: false
  explanation: "No finite-length error-detection code can catch every possible error pattern. CRC has a residual undetected error probability: if the error pattern is itself divisible by the generator polynomial, the remainder is zero and the error goes undetected. For CRC-32 with well-chosen generators, this probability is approximately 1/2³² ≈ 2.3×10⁻¹⁰ per frame — negligibly small for most purposes, but not zero. CRC provides strong probabilistic error detection, not absolute detection. For critical applications, additional mechanisms (sequence numbers, higher-layer checksums, or cryptographic MACs) are used alongside CRC."

- question: "Why does the choice of generator polynomial matter for a CRC scheme's error-detection capability?"
  type: short-answer
  answer: "The generator polynomial's algebraic structure determines which error patterns CRC can guarantee to detect. A polynomial that includes (x+1) as a factor ensures all odd numbers of bit errors are detected. The polynomial's degree sets the maximum burst error length that is guaranteed to be caught. Different polynomials have different detection profiles for common error types (single-bit, double-bit, burst). Standardized polynomials like CRC-32 were chosen by exhaustive mathematical analysis to maximize detection probability across all error classes for the expected frame sizes and bit error rates of their target protocols — an arbitrary polynomial could systematically miss entire categories of common errors."
  explanation: "This is why you cannot simply pick any polynomial of the right degree. The mathematical properties — reducibility, primitive vs. non-primitive, presence of specific factors — directly translate into guarantees about which errors are detectable. Protocol designers invest significant effort in selecting generator polynomials that are optimally matched to the error statistics of their target physical medium."
```

## Explainer

From your study of error detection and correction, you know the basic idea: append redundant information to data so the receiver can detect if something changed in transit. A simple checksum adds up byte values, but it misses many common corruption patterns — for example, swapping two bytes produces the same sum. **Cyclic Redundancy Check (CRC)** is a far more powerful error-detection scheme that catches virtually all common bit-error patterns by treating the entire data stream as a mathematical object and performing polynomial division on it.

The core idea uses an analogy to ordinary long division, but over binary polynomials instead of decimal numbers. Think of your data bits as the coefficients of a polynomial: the bit string 1101 represents x³ + x² + 1. You also choose a fixed **generator polynomial** — for example, CRC-32 uses a specific 33-bit polynomial standardized for Ethernet. To compute the CRC, you divide the data polynomial by the generator polynomial using XOR-based binary division (no carries, no borrows — just XOR at each step). The **remainder** of this division is the CRC value, which you append to the data before transmission.

At the receiving end, the receiver performs the same polynomial division on the entire received message (data plus CRC). If no errors occurred, the remainder is exactly zero. If any bits were corrupted during transmission, the remainder will be nonzero, and the receiver knows to discard the frame. The mathematical properties of polynomial division guarantee that CRC detects all single-bit errors, all double-bit errors (for well-chosen generators), all odd numbers of bit errors, and all **burst errors** shorter than the CRC length. A burst error is a contiguous sequence of corrupted bits — exactly the kind of corruption that noisy communication links produce — and CRC's ability to catch these bursts is its main advantage over simple checksums.

In practice, CRC computation is implemented in hardware using **shift registers** with XOR feedback taps arranged to match the generator polynomial. Each incoming bit is shifted in and XOR'd with the feedback, producing the remainder one bit at a time with no multiplication or division hardware required. This makes CRC extremely fast — Ethernet NICs compute CRC-32 over every frame at wire speed. The choice of generator polynomial is not arbitrary; standardized polynomials like CRC-32 (used in Ethernet and ZIP files) and CRC-16 (used in USB and Modbus) have been mathematically analyzed to maximize error-detection probability for their target applications and data lengths.
