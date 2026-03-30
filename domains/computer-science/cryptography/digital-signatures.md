---
id: digital-signatures
title: Digital Signatures
domain: computer-science
course: cryptography
prerequisites:
- id: rsa-cryptosystem
  type: hard
- id: hash-functions-and-collision-resistance
  type: hard
tags:
- digital-signature
- non-repudiation
- rsa-pss
- dsa
- euf-cma
stage: advanced
status: validated
---

# Digital Signatures

## Core Idea
A digital signature scheme lets a signer with a private key produce a signature on a message that anyone with the corresponding public key can verify. Unlike MACs, signatures provide non-repudiation: the signer cannot deny having signed because only they possess the private key. Security requires existential unforgeability under chosen-message attack (EUF-CMA). RSA-PSS, DSA, and ECDSA are the main schemes. Signatures are applied to message hashes (not raw messages) for efficiency and to prevent algebraic attacks. They are foundational to PKI, code signing, certificates, and blockchain transactions.

## Questions

```yaml
- question: "A MAC and a digital signature both verify message integrity. What property does a digital signature provide that a MAC cannot, and why does this matter for legal and financial applications?"
  type: short-answer
  answer: "Digital signatures provide non-repudiation: only the holder of the private key can produce the signature, so the signer cannot later deny having signed. With a MAC, both parties share the same key, so either could have produced the tag — the receiver cannot prove to a third party that the sender specifically authored the message. Non-repudiation matters for contracts, financial transactions, and legal documents where accountability and proof of origin are required."
  explanation: "Non-repudiation transforms a two-party integrity check into a publicly verifiable proof of authorship. A judge, auditor, or any third party can verify the signature using the public key without accessing any secrets. This is why digital signatures are legally recognized in most jurisdictions as equivalent to handwritten signatures for electronic documents."

- question: "Why do signature schemes sign the hash of the message rather than the message itself?"
  type: multiple-choice
  options:
    - "Hashing reduces the message to a fixed size, making the signature operation efficient regardless of message length. It also prevents algebraic attacks (like RSA's multiplicative homomorphism) that exploit structure in the raw message space"
    - "Hashing makes the signature longer, providing more security"
    - "The hash function encrypts the message, providing confidentiality alongside authentication"
    - "Signature algorithms cannot operate on inputs larger than 256 bits"
  answer: 0
  explanation: "RSA and DSA operate on fixed-size inputs (the size of the modulus or group order). Hashing reduces any message to a fixed-size digest. More critically, hashing destroys algebraic structure. Without hashing, RSA signatures are multiplicatively homomorphic: s1 * s2 is a valid signature on m1 * m2. Hashing prevents this because H(m1 * m2) != H(m1) * H(m2). The hash function acts as a computational barrier between the message space and the algebraic domain where the signature is computed."

- question: "ECDSA (Elliptic Curve DSA) requires a fresh random nonce k for each signature. If the same k is used to sign two different messages, the private key can be recovered."
  type: true-false
  answer: true
  explanation: "This is not a theoretical concern — it destroyed real systems. In ECDSA, the signature component s = k^(-1)(H(m) + r*x) mod n, where x is the private key. With two signatures (s1, s2) using the same k, the attacker computes k from s1 - s2 = k^(-1)(H(m1) - H(m2)) and then recovers x. Sony's PlayStation 3 code signing was broken this way in 2010 (they used a constant k). Deterministic nonce generation (RFC 6979) eliminates this risk by deriving k from the private key and message."

- question: "A certificate authority signs a website's public key, creating a certificate. If the CA's signing key is compromised, what is the scope of the damage?"
  type: multiple-choice
  options:
    - "Only the specific website whose certificate was most recently signed is affected"
    - "Every certificate ever signed by that CA becomes untrustworthy — the attacker can forge new certificates for any domain, enabling man-in-the-middle attacks against all sites that browsers trusted via that CA"
    - "No damage occurs because the website's private key is separate from the CA's key"
    - "Only future certificates are affected; existing certificates remain valid"
  answer: 1
  explanation: "The CA's signing key is the root of trust for all certificates it has issued. An attacker with the CA's private key can create valid-looking certificates for any domain — google.com, your bank, anything — that browsers will accept without warning. This enables MITM attacks on any HTTPS connection. This catastrophic failure mode is why CA private keys are stored in hardware security modules, why certificate transparency logs exist, and why key compromise requires revoking the CA and all its certificates. The DigiNotar breach (2011) demonstrated this: a compromised CA led to real attacks on Iranian users."

- question: "RSA signatures and RSA encryption use the same mathematical operation (modular exponentiation) but with the roles of public and private keys swapped."
  type: true-false
  answer: true
  explanation: "In RSA encryption, the sender uses the public key (exponent e) and the receiver uses the private key (exponent d) to decrypt. In RSA signatures, the signer uses the private key (exponent d) to sign and the verifier uses the public key (exponent e) to verify. Signing is 'encryption with the private key' and verification is 'decryption with the public key.' However, this symmetry is specific to RSA — other signature schemes (DSA, ECDSA, Ed25519) use entirely different mathematical structures for signing and verification."
```

## Explainer

A **digital signature** is the public-key analog of a handwritten signature: it binds a message to the identity of the signer in a way that anyone can verify but only the signer can produce. A signature scheme consists of three algorithms: **key generation** (produce a public-private key pair), **signing** (use the private key to compute a signature on a message), and **verification** (use the public key to check whether a signature is valid). The security goal is **EUF-CMA** (existential unforgeability under chosen-message attack): an adversary who can obtain signatures on any messages of their choosing still cannot forge a valid signature on any new message.

The simplest conceptual scheme is RSA signatures. The signer computes s = H(m)^d mod n, where d is the private key and H is a cryptographic hash. The verifier checks that s^e mod n = H(m), where e is the public key. Hashing is essential for two reasons: it compresses the message to a fixed size for the RSA operation, and it prevents algebraic forgery attacks that exploit RSA's multiplicative homomorphism. In practice, RSA-PSS adds randomized padding to the hash before signing, providing a tighter security proof. **DSA** and **ECDSA** use a different approach based on discrete logarithms in a prime-order group (or elliptic curve group), where the signature is a pair (r, s) computed using the private key and a per-signature random nonce.

The nonce in DSA/ECDSA is a critical security parameter. If the same nonce is ever reused for two different messages, the private key can be algebraically recovered from the two signatures. This is not a theoretical curiosity — Sony's PlayStation 3 ECDSA implementation used a constant nonce, allowing hackers to recover the signing key and run unauthorized software. **Deterministic signatures** (Ed25519, or ECDSA with RFC 6979) eliminate nonce-related risks by deriving the nonce deterministically from the private key and the message, ensuring it is unique per message without relying on a random number generator.

The most transformative application of digital signatures is **Public Key Infrastructure (PKI)**, the trust system underlying HTTPS. A **certificate authority (CA)** signs a binding between a domain name and a public key, producing a **certificate**. When your browser connects to a website, it verifies the certificate's signature using the CA's public key (which is pre-installed in the browser's trust store). If the signature checks out, the browser trusts that the public key belongs to the claimed domain and proceeds with a DH key exchange. This chain of trust — from CA to certificate to session key — is what makes secure web browsing possible. It also creates a concentration of trust: a compromised CA can forge certificates for any domain, which is why the security of CAs is one of the most critical (and fragile) aspects of internet infrastructure.
