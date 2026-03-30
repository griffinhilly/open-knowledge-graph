---
id: random-number-generation
title: Random Number Generation in Cryptography
domain: computer-science
course: cryptography
prerequisites:
- id: symmetric-encryption-block-ciphers
  type: hard
- id: hash-functions-and-collision-resistance
  type: soft
tags:
- csprng
- entropy
- prng
- dev-urandom
- dual-ec-drbg
stage: advanced
status: validated
---

# Random Number Generation in Cryptography

## Core Idea
Cryptographic security depends critically on high-quality randomness for key generation, nonces, IVs, and padding. A cryptographically secure pseudorandom number generator (CSPRNG) expands a short truly random seed into a long pseudorandom stream that is computationally indistinguishable from true randomness. Entropy — genuine physical unpredictability — must be harvested from hardware sources (timing jitter, thermal noise, etc.) and cannot be created algorithmically. Weak or predictable randomness has caused catastrophic real-world failures: the Debian OpenSSL bug (2008) reduced key entropy to 15 bits, and Dual_EC_DRBG contained an NSA backdoor. Using the OS-provided CSPRNG (/dev/urandom, CryptGenRandom) is the correct practice.

## Questions

```yaml
- question: "The Debian OpenSSL bug (2006-2008) commented out a line that mixed process memory into the random seed, reducing the effective entropy to the process ID (~15 bits). What was the practical impact?"
  type: short-answer
  answer: "With only ~32,768 possible seeds (2^15 process IDs), all SSH and TLS keys generated on affected Debian/Ubuntu systems came from a set of ~32,768 possible keys per key type and size. An attacker could pre-compute all possible keys and test each against any target server in seconds. Every key generated during the affected period had to be revoked and regenerated. This demonstrated that a single line of code affecting randomness can compromise millions of systems."
  explanation: "The bug persisted for nearly two years because the code change appeared to fix a Valgrind warning — it was a plausible maintenance commit. No one noticed the catastrophic security impact until a researcher generated all possible keys and found matches on production servers. The lesson: randomness is a single point of failure, and its correctness is not visible from the outside."

- question: "A developer seeds a PRNG with the current time in seconds. Why is this insecure even if the PRNG algorithm itself is cryptographically strong?"
  type: multiple-choice
  options:
    - "The current time changes too fast for the PRNG to process"
    - "Time in seconds provides at most ~20-30 bits of entropy (the attacker can estimate when the key was generated to within a plausible time window). A CSPRNG cannot create entropy — it can only expand existing entropy. If the seed has 30 bits of entropy, the output has 30 bits of entropy regardless of the PRNG quality"
    - "Time-based seeds cause the PRNG to produce negative numbers"
    - "The PRNG algorithm needs at least 256 bits of input to function"
  answer: 1
  explanation: "Entropy is a property of the seed, not the algorithm. A CSPRNG with a 128-bit truly random seed produces output that is computationally indistinguishable from random. The same CSPRNG with a predictable seed produces predictable output. If the attacker knows the key was generated sometime in 2024, that's about 31.5 million seconds — roughly 25 bits of entropy. They can try all possible seeds in seconds. This is why entropy sources must be genuinely unpredictable physical processes."

- question: "Why should developers use OS-provided CSPRNGs (/dev/urandom on Linux, BCryptGenRandom on Windows) rather than implementing their own?"
  type: multiple-choice
  options:
    - "OS CSPRNGs are faster than user-space implementations"
    - "OS CSPRNGs continuously mix entropy from multiple hardware sources, are maintained by security experts, are hardened against state compromise, and have been extensively audited. Custom implementations are likely to have entropy collection bugs, reseeding failures, or state leakage that the developer won't detect"
    - "User-space PRNGs are illegal in most jurisdictions"
    - "OS CSPRNGs use quantum random number generators"
  answer: 1
  explanation: "Randomness is one of the hardest things to get right in cryptography because failures are silent — weak randomness produces output that looks random to the developer but is predictable to an attacker. OS CSPRNGs have been battle-tested, receive continuous security patches, and integrate with hardware random number generators when available. The Dual_EC_DRBG scandal showed that even NIST-standardized PRNGs can contain backdoors, but OS-level implementations are the most scrutinized option available."

- question: "/dev/random and /dev/urandom on Linux differ in that /dev/random blocks when the entropy pool is estimated to be depleted, while /dev/urandom never blocks. For cryptographic key generation, /dev/urandom is the correct choice."
  type: true-false
  answer: true
  explanation: "This is counterintuitive — it seems like /dev/random should be 'more secure' because it waits for entropy. But the entropy estimation is unreliable, and once a CSPRNG is properly seeded (which happens early in boot), its output is computationally indistinguishable from true randomness regardless of the estimated entropy level. /dev/random's blocking causes availability issues (programs hang waiting for entropy) without providing meaningful additional security. The Linux kernel developers explicitly recommend /dev/urandom for all purposes except very early boot randomness."

- question: "Dual_EC_DRBG was standardized by NIST in 2006 and later revealed to contain a likely NSA backdoor. What made the backdoor possible?"
  type: short-answer
  answer: "Dual_EC_DRBG uses two elliptic curve points P and Q. If the relationship between P and Q is known (specifically, if someone knows the discrete logarithm e such that Q = eP), the holder of e can predict all future outputs from a short observation of the generator's output. NIST specified particular P and Q values without justifying their choice. If NSA generated Q = eP for a known e, they could predict any Dual_EC_DRBG output. The design also had an output truncation that was shorter than necessary, making the backdoor exploitable from observing just 32 bytes of output."
  explanation: "The mathematical backdoor was identified by Shumow and Ferguson in 2007, but NIST did not withdraw the standard. The Snowden leaks (2013) confirmed NSA had paid RSA Security $10 million to make Dual_EC_DRBG the default in their BSAFE library. This episode permanently damaged trust in government-standardized cryptographic algorithms and motivated the development of fully transparent standards processes."
```

## Explainer

Every cryptographic operation that generates keys, nonces, IVs, or random padding depends on a source of randomness that an adversary cannot predict. If an attacker can predict or narrow down the random values used in key generation, they can break the system regardless of how strong the algorithms are. **Entropy** — genuine physical unpredictability — is the foundation of cryptographic randomness, and it cannot be manufactured by computation. A deterministic algorithm, no matter how complex, produces a predictable output from a predictable input. Randomness must ultimately come from physical processes: hardware timing jitter, thermal noise, radioactive decay, or user input timing.

A **cryptographically secure pseudorandom number generator (CSPRNG)** bridges the gap between the small amount of entropy available from hardware sources and the large amount of randomness that cryptographic operations consume. It takes a short truly random seed (128-256 bits of entropy) and expands it into an arbitrarily long stream that is **computationally indistinguishable** from true randomness — no polynomial-time algorithm can tell the CSPRNG's output from a truly random string. Modern CSPRNGs (like ChaCha20-based designs in Linux) also provide **forward secrecy**: even if the internal state is compromised at some point, past outputs remain unpredictable, and the generator recovers security as new entropy is mixed in.

The critical principle is that **a CSPRNG cannot create entropy; it can only expand it**. If the seed has 30 bits of entropy (e.g., seeded with a timestamp), the output has 30 bits of entropy — the CSPRNG merely obscures which 30-bit value was used. Real-world catastrophes confirm this. The Debian OpenSSL bug (2006-2008) accidentally reduced entropy to the process ID (~15 bits), making every key generated on affected systems guessable from a set of ~32,768 possibilities. A developer who seeds a PRNG with time.time() provides perhaps 25-30 bits of entropy to an attacker who can estimate when the key was generated. These failures are invisible: the output looks random, passes statistical tests, and appears to work perfectly — until an attacker exploits the predictability.

The correct practice is simple: **use your operating system's CSPRNG**. On Linux, /dev/urandom (or the getrandom() system call) provides a CSPRNG seeded from hardware entropy sources, continuously reseeded, and maintained by security experts. On Windows, BCryptGenRandom serves the same role. These implementations handle entropy collection, pool management, and reseeding automatically. Rolling your own is almost always wrong — the Dual_EC_DRBG scandal (a NIST-standardized PRNG with a probable NSA backdoor exploiting the relationship between two elliptic curve points) showed that even standards bodies can get it wrong, but OS implementations receive the most scrutiny and the fastest patches. For application developers, the rule is absolute: never implement your own random number generation for cryptographic purposes.
