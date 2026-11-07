---
id: discrete-logarithms
title: Discrete Logarithms
domain: mathematics
course: number-theory
prerequisites:
- id: primitive-roots-cyclic-groups-mod-p
  type: hard
- id: order-element-modulo-n
  type: hard
- id: primitive-roots-and-cyclic-groups-mod-p
  type: hard
tags:
- discrete-log
- cryptography
- cyclic-groups
stage: advanced
status: validated
---

# Discrete Logarithms

## Core Idea
Given a primitive root g mod p and nonzero residue a, the discrete logarithm is the unique k (mod p-1) such that g^k ≡ a (mod p). Computing discrete logs is believed hard; this one-way function underpins Diffie-Hellman and elliptic-curve cryptography.

## How It's Best Learned
Build the full log table for p = 11 and g = 2 from the powers 1, 2, 4, 8, 5, 10, 9, 7, 3, 6. Check one law: log 3 + log 4 = 8 + 2 ≡ 0 (mod 10), and 3 · 4 ≡ 1. Then solve 2ᵏ ≡ 7 by baby-step giant-step with m = 4. Here 7 · 2⁻⁴ ≡ 7 · 9 ≡ 8 = 2³, so k = 4 + 3 = 7.

## Common Misconceptions
- Discrete logs add modulo p, because the residues live mod p. (The exponents live mod p − 1, since g^(p−1) ≡ 1. With p = 11 and g = 2, log 3 + log 4 = 10, which reduces to 0 mod 10.)
- Any nonzero residue can serve as the base. (A base that is not a primitive root misses some residues. Mod 11, the powers of 3 are only 3, 9, 5, 4, 1, so 2 has no logarithm base 3.)
- Since the problem is hard, checking every power of g is the best known method. (Baby-step giant-step needs about √p steps, and index calculus is subexponential in (ℤ/pℤ)*. Security depends on p being large enough to defeat these.)

## Questions

```yaml
- question: "Alice knows a prime p, a primitive root g, and an exponent k, and wants to compute g^k mod p. Bob knows p, g, and the value a = g^k mod p, and wants to find k. Whose problem is computationally harder?"
  type: multiple-choice
  options:
    - "Alice's — exponentiation mod p requires inspecting every power of g"
    - "Bob's — finding k from g^k mod p is believed to be computationally infeasible for large p"
    - "Both are equally hard — modular arithmetic is always expensive"
    - "Neither — both problems reduce to prime factorization"
  answer: 1
  explanation: "Alice's problem (computing g^k mod p given k) is easy: repeated squaring solves it in O(log k) multiplications regardless of how large p is. Bob's problem (recovering k from g^k mod p) is the discrete logarithm problem, believed to require time exponential in the size of p for the best known algorithms on general groups. This asymmetry — fast forward, slow reverse — is precisely what Diffie-Hellman and elliptic-curve cryptography exploit. Option D is wrong: discrete logs are not believed to reduce to factoring, which is why breaking one cryptosystem does not break the other."

- question: "In the group (Z/pZ)*, we have log_g(ab) ≡ log_g(a) + log_g(b) (mod p-1). Which of the following best explains why this law holds?"
  type: multiple-choice
  options:
    - "It holds because multiplication distributes over addition in modular arithmetic"
    - "It mirrors ordinary logarithm laws because the group is cyclic of order p-1 and g is a generator"
    - "It is a coincidence that only applies when p is prime"
    - "It follows from the fact that g^k is always greater than g^j when k > j"
  answer: 1
  explanation: "The discrete log law is a direct consequence of the group structure. Since g generates (Z/pZ)*, we have g^k · g^j = g^(k+j). Taking the discrete log of both sides: log_g(g^k · g^j) = k + j = log_g(g^k) + log_g(g^j). The exponents live in Z/(p-1)Z (because g^(p-1) ≡ 1), so addition is mod p-1 — exactly the same reason ordinary logs have log(xy) = log(x) + log(y): in both cases the underlying operation on exponents is addition in a suitable group."

- question: "The discrete logarithm obeys additive laws that mirror ordinary logarithms: log_g(ab) ≡ log_g(a) + log_g(b) (mod p-1)."
  type: true-false
  answer: true
  explanation: "True. Because g is a generator of the cyclic group (Z/pZ)* of order p-1, every nonzero residue is a unique power of g. Multiplying two residues g^j and g^k gives g^(j+k), so the discrete log of a product equals the sum of the individual discrete logs — exactly as with ordinary logarithms. The addition takes place mod p-1 because the exponents cycle with period p-1."

- question: "Using a larger prime p makes the forward computation g^k mod p slower, which is why large primes improve cryptographic security."
  type: true-false
  answer: false
  explanation: "False — this reverses the relevant asymmetry. The forward computation g^k mod p uses repeated squaring and costs O(log k · log²p) bit operations, which grows very slowly as p increases. It is the *inverse* computation (finding k from g^k mod p) that becomes harder as p grows, because the best algorithms (baby-step giant-step, index calculus) have running times that grow with p. Cryptographic security comes from making the *reverse* problem hard, not the forward problem."

- question: "What makes the discrete logarithm problem a 'one-way function,' and why is this property essential for cryptographic key exchange?"
  type: short-answer
  answer: "Computing g^k mod p given g, k, and p is fast (O(log k) multiplications via repeated squaring), but recovering k given g, p, and g^k mod p is believed to require time exponential in the bit-length of p. This asymmetry means two parties can publicly exchange values derived from discrete exponentiation without an eavesdropper being able to recover the secret exponents — the basis of Diffie-Hellman."
  explanation: "The one-way property is not proved but is a widely believed computational hardness assumption. Diffie-Hellman works because Alice can publish g^a mod p and Bob can publish g^b mod p; Alice computes (g^b)^a = g^ab and Bob computes (g^a)^b = g^ab — the same shared secret — while an eavesdropper would need to solve the discrete log problem to recover a or b from the public values."
```

## Explainer

You already know that a **primitive root** g modulo p generates every nonzero residue as successive powers: g¹, g², g³, … cycle through all p-1 nonzero residues mod p before repeating. This means for any nonzero a mod p, there is exactly one exponent k in {0, 1, …, p-2} with g^k ≡ a (mod p). That exponent k is called the **discrete logarithm** of a to the base g, written log_g(a) mod (p-1). It is the modular analogue of the ordinary logarithm: just as log_b(x) asks "to what power must I raise b to get x?", the discrete log asks the same question inside Z/pZ.

The crucial asymmetry is computational. Given g, k, and p, computing g^k mod p is fast — repeated squaring does it in O(log k) multiplications. But given g, a, and p, finding k requires examining (in the naive case) each power of g until you hit a. For a prime p with hundreds of digits, this is astronomically slow. This **one-way function** property — easy in one direction, hard to reverse — is precisely what cryptographic protocols exploit. Diffie-Hellman key exchange works because two parties can combine public values derived from g^k mod p without an eavesdropper being able to recover k.

The discrete log obeys algebraic laws that mirror ordinary logarithms. From your knowledge of the order of elements, you know g^k has order (p-1)/gcd(k, p-1), so log_g(ab) ≡ log_g(a) + log_g(b) (mod p-1). This is the discrete analogue of log(xy) = log(x) + log(y). The exponents add in Z/(p-1)Z in the same way that ordinary logs add in the reals, because the group (Z/pZ)* is cyclic of order p-1, and g is a generator.

There are algorithms faster than brute force — **baby-step giant-step** runs in O(√p) time and space, and the **index calculus** method is subexponential for integers. This is why modern cryptographic systems use primes with thousands of bits, or move to elliptic curves where no index calculus analogue is known. The hardness assumption for discrete logs in carefully chosen groups remains one of the cornerstones of public-key cryptography.
