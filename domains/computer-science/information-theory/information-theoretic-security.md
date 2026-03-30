---
id: information-theoretic-security
title: Information-Theoretic Security
domain: computer-science
course: information-theory
prerequisites:
- id: mutual-information
  type: hard
- id: kl-divergence
  type: hard
- id: shannon-entropy
  type: hard
tags:
- perfect secrecy
- one-time pad
- Shannon secrecy
- wiretap channel
- security
stage: expert
status: validated
---

# Information-Theoretic Security

## Core Idea
Information-theoretic security provides secrecy guarantees that hold against adversaries with unlimited computational power, unlike computational security (which assumes hard problems remain hard). Shannon proved that perfect secrecy — I(M; C) = 0, where M is the message and C is the ciphertext — requires the key to be at least as long as the message (the one-time pad achieves this bound). Wyner's wiretap channel extends this to noisy channels: when the eavesdropper has a degraded channel compared to the legitimate receiver, positive secrecy rates are achievable without any shared key. Information-theoretic security is unconditional — it cannot be broken by future algorithmic advances, quantum computers, or increased computing power.

## Questions

```yaml
- question: "Shannon proved that any perfectly secret cipher must have a key at least as long as the message. Why does this make perfect secrecy impractical for most applications?"
  type: multiple-choice
  options:
    - "Long keys are computationally expensive to generate"
    - "The key distribution problem: securely sharing a key as long as the message is essentially as hard as securely sharing the message itself — you have not reduced the problem, only shifted it to key distribution"
    - "Long keys increase encryption latency"
    - "Perfect secrecy is only possible for binary messages"
  answer: 1
  explanation: "If you need a key as long as the message, and the key must be shared secretly between sender and receiver before communication, then the key distribution problem is as hard as the original communication problem. This is why most real systems use computational security (AES, RSA, etc.) with short keys: they are secure under complexity assumptions but could theoretically be broken with enough computation. The one-time pad remains used only in extreme cases (diplomatic hotlines, some military communications) where key pre-distribution is feasible."

- question: "In Wyner's wiretap channel, the eavesdropper receives a noisier version of the signal than the legitimate receiver. Positive secrecy rates are achievable even without a pre-shared key."
  type: true-false
  answer: true
  explanation: "This is Wyner's remarkable result: when the eavesdropper's channel is degraded relative to the legitimate receiver's, the sender can transmit at a positive rate that is perfectly secret from the eavesdropper — with NO pre-shared key. The secrecy capacity is C_s = C_main - C_eavesdropper (the difference in channel capacities). The sender uses random coding to create confusion at the eavesdropper while maintaining reliable communication with the legitimate receiver. The extra noise on the eavesdropper's channel is the source of secrecy."

- question: "Explain the fundamental difference between information-theoretic security and computational security, and why the distinction matters in the era of quantum computing."
  type: short-answer
  answer: "Information-theoretic security (like the one-time pad) guarantees I(M;C) = 0 — the ciphertext reveals literally no information about the message, regardless of the adversary's computational power. Computational security (like AES or RSA) guarantees that breaking the cipher requires solving a problem believed to be computationally hard (factoring, discrete log). If the hardness assumption fails — due to algorithmic breakthroughs or quantum computers — computational security breaks. Quantum computers threaten RSA and ECC via Shor's algorithm, making computational security time-limited. Information-theoretic security is immune to this: even a quantum adversary with unlimited resources cannot break it, because the security comes from information theory, not computational hardness."
  explanation: "This is why quantum key distribution (QKD) is valuable: it provides information-theoretically secure key distribution using quantum mechanics. Combined with the one-time pad, QKD provides end-to-end unconditional security. However, the practicality debate continues — QKD requires special hardware and has range limitations, while post-quantum cryptographic algorithms provide computational security that is believed (but not proved) to resist quantum attacks."
```

## Explainer

Most modern cryptography is computationally secure: AES, RSA, and elliptic curve cryptography rely on the assumption that certain problems (factoring, discrete logarithm) are computationally hard. If someone proved P = NP or built a sufficiently powerful quantum computer, these systems would break. Information-theoretic security eliminates this risk entirely by proving that the ciphertext contains zero information about the message, regardless of the adversary's capabilities.

Shannon formalized this in 1949. **Perfect secrecy** means I(M; C) = 0: the ciphertext C is statistically independent of the message M. Observing C does not change the adversary's beliefs about M at all — not even by one bit. Shannon proved that this requires H(K) >= H(M): the key must have at least as much entropy as the message. The **one-time pad** achieves this bound: C = M XOR K, where K is a uniformly random key the same length as M. Each ciphertext is equally likely under any message, providing perfect secrecy. But the key can never be reused (reuse leaks information via C_1 XOR C_2 = M_1 XOR M_2), making key management the central challenge.

Wyner's **wiretap channel** (1975) showed that physical-layer noise can provide secrecy without any key. If the sender communicates over a noisy channel to a legitimate receiver, and an eavesdropper observes a degraded version, the sender can encode messages so that the eavesdropper learns nothing while the legitimate receiver decodes correctly. The secrecy capacity C_s is the difference between the main channel capacity and the eavesdropper's channel capacity. The coding scheme uses stochastic encoding: the sender adds deliberate randomness that creates confusion for the eavesdropper but can be resolved by the legitimate receiver.

The modern relevance of information-theoretic security is growing. Quantum key distribution (QKD) provides information-theoretically secure key exchange using quantum physics. Physical-layer security extends the wiretap channel to practical wireless scenarios (fading, MIMO, cooperative jamming). Secret sharing and secure multi-party computation use information-theoretic tools to distribute secrets and compute functions without revealing private inputs. As quantum computing threatens computational security assumptions, unconditional security guarantees become increasingly valuable for applications where long-term secrecy is required — government communications, medical records, financial data with decades-long sensitivity.
