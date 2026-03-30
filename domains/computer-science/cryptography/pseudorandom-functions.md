---
id: pseudorandom-functions
title: Pseudorandom Functions
domain: computer-science
course: cryptography
prerequisites:
- id: pseudorandom-generators
  type: hard
- id: symmetric-encryption-block-ciphers
  type: hard
tags:
- prf
- ggm-construction
- keyed-function
- indistinguishability
stage: expert
status: validated
---

# Pseudorandom Functions

## Core Idea
A pseudorandom function (PRF) family {F_k} maps inputs to outputs such that F_k (for a random key k) is computationally indistinguishable from a truly random function, even to an adversary with adaptive oracle access. PRFs are the theoretical model for block ciphers and the core building block for MACs, CPA-secure encryption, and key derivation. The GGM construction proves that PRGs imply PRFs, completing the chain: OWFs → PRGs → PRFs. A pseudorandom permutation (PRP) is a PRF that is also a bijection — the formal model for block ciphers like AES. The PRP/PRF switching lemma shows PRPs and PRFs are interchangeable for most applications when the domain is large.

## Questions

```yaml
- question: "A truly random function from {0,1}^n to {0,1}^n requires 2^n * n bits to specify (a lookup table). A PRF with an n-bit key specifies 2^n outputs using only n bits. Why doesn't this compression make PRFs trivially distinguishable?"
  type: short-answer
  answer: "A truly random function can produce 2^{n*2^n} possible input-output mappings, while a PRF with n-bit keys produces only 2^n mappings. An unbounded adversary could enumerate all 2^n PRF-generated functions and check membership. But an adversary with polynomial oracle access can query at most polynomially many points — far too few to detect the compression. The PRF guarantee is that no polynomial-time adversary, even with adaptive queries, can distinguish F_k from a random function with non-negligible advantage."
  explanation: "This parallels the PRG situation: computational indistinguishability allows a massive compression that would be statistically detectable but is computationally invisible. A polynomial-time adversary sees polynomially many input-output pairs, and the PRF guarantee says these look exactly like random input-output pairs."

- question: "The GGM construction builds a PRF from a PRG with expansion factor 2. The key is the PRG seed, and to evaluate F_k(x) for input x = x_1x_2...x_n, you start with k and iteratively apply G, choosing the left or right half based on each bit of x. Why does this work?"
  type: multiple-choice
  options:
    - "Each bit of x selects a random function from a pre-computed table"
    - "The construction builds a binary tree of depth n. The root is labeled with key k; each internal node's children are the two halves of the PRG applied to the node's label. The leaf reached by input x is F_k(x). A hybrid argument shows that replacing any single node's PRG output with truly random values is indistinguishable (by PRG security), and there are only polynomially many hybrids across the n levels"
    - "The XOR of all path nodes ensures output randomness"
    - "G is applied n times to create a hash chain"
  answer: 1
  explanation: "The GGM tree is a beautiful construction. At level 0, the root holds k. At level 1, G(k) = (k_0, k_1). At level 2, G(k_0) = (k_{00}, k_{01}) and G(k_1) = (k_{10}, k_{11}). Input x = x_1...x_n walks from root to leaf, turning left (first half) or right (second half) at each level based on x_i. The security proof replaces real PRG outputs with random values level by level, using the PRG security at each step. After n hybrid steps, all leaves are independent random values — exactly a random function."

- question: "AES is modeled as a pseudorandom permutation (PRP) rather than a pseudorandom function (PRF). The PRP/PRF switching lemma says the distinction doesn't matter when the number of queries q satisfies q^2 << 2^n."
  type: true-false
  answer: true
  explanation: "The switching lemma bounds the distinguishing advantage between a random permutation and a random function by q^2/2^{n+1}, where q is the number of queries and n is the block size. For AES with n = 128, this is negligible as long as q << 2^64. Since practical applications rarely process 2^64 blocks (that's 2^68 bytes ≈ 256 exabytes) with a single key, PRP and PRF are effectively interchangeable for AES. This is why AES can be used wherever a PRF is theoretically required."

- question: "CPA-secure symmetric encryption can be built from a PRF: to encrypt message m, choose random r and output (r, F_k(r) XOR m). Why does the PRF property make this secure?"
  type: multiple-choice
  options:
    - "The PRF encrypts the randomness r, hiding the key"
    - "If F_k is a PRF, then F_k(r) for a random r is indistinguishable from a random string. So F_k(r) XOR m looks like random XOR m = random. An adversary who can distinguish this from random can distinguish F_k from a random function, contradicting the PRF property. The fresh random r ensures different encryptions of the same message produce different ciphertexts (semantic security)"
    - "The XOR operation provides information-theoretic security like a one-time pad"
    - "The PRF ensures that r cannot be guessed by the adversary"
  answer: 1
  explanation: "This is essentially CTR mode for a single block. The security reduction is clean: assume adversary A breaks CPA security. Construct distinguisher D that simulates the encryption scheme using its oracle (either F_k or a random function). If the oracle is random, the scheme is a one-time pad and A has zero advantage. If the oracle is F_k and A has advantage epsilon, then D distinguishes with advantage epsilon. Since F_k is a PRF, epsilon must be negligible."

- question: "A PRF is a stronger primitive than a PRG: any PRF can be used to construct a PRG, but the GGM construction shows PRGs are sufficient to build PRFs."
  type: true-false
  answer: true
  explanation: "To build a PRG from a PRF, simply fix the input and vary the key: G(k) = F_k(0) || F_k(1) || ... || F_k(m). Since F_k for a random k produces outputs indistinguishable from random, this concatenation is indistinguishable from a random string. Combined with GGM (PRG → PRF), this shows PRGs and PRFs are equivalent — they can be built from each other. Both are equivalent to one-way functions, completing the circle of equivalences."
```

## Explainer

A **pseudorandom function (PRF)** family is a collection of keyed functions {F_k} such that when k is chosen randomly, the function F_k is computationally indistinguishable from a truly random function — even to an adversary who can adaptively choose inputs and observe outputs. This is a stronger guarantee than PRGs: the adversary has **oracle access**, meaning they can query F_k on any input of their choosing and see the corresponding output, yet they still cannot tell F_k apart from a genuinely random input-output mapping.

The formal definition captures the ideal behavior of a block cipher. AES with a random key should behave like a random permutation (a special case of a random function that is also a bijection). Every output should appear random given all previously observed input-output pairs, and no pattern in the outputs should reveal the key or predict future outputs. The **PRP/PRF switching lemma** shows that for large domains (like AES's 128-bit block space), random permutations and random functions are indistinguishable until the adversary has made close to 2^{n/2} queries, making the distinction irrelevant in practice.

The **GGM construction** (Goldreich, Goldwasser, Micali) builds a PRF from any PRG with expansion factor 2. Think of it as a binary tree: the root holds the key k. Applying the PRG to k produces two values (left and right children). Applying the PRG to each child produces four grandchildren, and so on. To evaluate F_k on an n-bit input x, walk from the root to a leaf, going left when the next input bit is 0 and right when it is 1. The leaf value is the output. The security proof uses a **hybrid argument**: replace the PRG output at each level with truly random values, one level at a time. Each replacement is undetectable by PRG security, and after n levels all leaves are independent random values — a truly random function. This construction, combined with the HILL theorem (OWFs → PRGs), proves that OWFs suffice for PRFs, completing the foundational chain of cryptographic primitives.

PRFs are the workhorse building block of modern cryptography. **CPA-secure encryption**: to encrypt message m, pick random r and output (r, F_k(r) XOR m) — this is essentially CTR mode, secure because F_k(r) is pseudorandom. **MACs**: F_k(m) is a secure MAC for fixed-length messages because forging a tag on a new message requires predicting a PRF output on an unqueried input. **Key derivation**: F_k(context) derives application-specific keys that are pseudorandom even if the adversary knows other derived keys. The universality of PRFs means that understanding this single primitive — a keyed function indistinguishable from random — unlocks the construction of most symmetric cryptographic tools.
