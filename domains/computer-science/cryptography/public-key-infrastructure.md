---
id: public-key-infrastructure
title: Public Key Infrastructure
domain: computer-science
course: cryptography
prerequisites:
- id: digital-signatures
  type: hard
- id: diffie-hellman-key-exchange
  type: hard
tags:
- pki
- certificate-authority
- x509
- certificate-revocation
- trust-model
stage: advanced
status: validated
---

# Public Key Infrastructure

## Core Idea
PKI solves the key distribution problem for public-key cryptography: how do you know that a public key actually belongs to the claimed entity? Certificate Authorities (CAs) sign X.509 certificates binding identities to public keys. Trust flows hierarchically from root CAs (pre-installed in browsers/OSes) through intermediate CAs to end-entity certificates. Revocation (CRL, OCSP) handles key compromise. Certificate Transparency logs provide public auditability. PKI is the trust backbone of HTTPS, code signing, and email encryption, but its security depends on every CA in the chain being trustworthy — a single compromised CA can forge certificates for any domain.

## Questions

```yaml
- question: "Your browser trusts hundreds of root CAs from dozens of countries. Why is this a security concern, and what mitigation does Certificate Transparency provide?"
  type: short-answer
  answer: "Any single root CA can issue a valid certificate for any domain — a compromised or coerced CA in any country can create a certificate for google.com that your browser will accept. Certificate Transparency (CT) requires CAs to log all issued certificates in public, append-only logs. Domain owners and monitors can detect unauthorized certificates by watching these logs. CT doesn't prevent mis-issuance but makes it publicly visible, enabling rapid detection and revocation."
  explanation: "The fundamental problem is that PKI trust is as strong as its weakest CA. CT shifts the security model from 'trust all CAs to behave' to 'detect and respond when they don't.' Since Chrome requires CT for all new certificates, any secretly issued certificate is detectable. The DigiNotar (2011) and Symantec (2017) incidents demonstrated that CA misbehavior is not hypothetical."

- question: "A website's certificate has expired. A user argues that since the cryptographic key hasn't changed, the connection is still secure. What does the user miss?"
  type: multiple-choice
  options:
    - "Expired certificates use weaker encryption algorithms"
    - "Certificate expiration serves multiple purposes: it limits the window of exposure if a private key is compromised without detection, forces regular re-validation of domain ownership, and ensures the certificate's cryptographic algorithms stay current. An unexpired certificate provides assurance that these checks were recent"
    - "The encryption key automatically weakens over time due to mathematical properties"
    - "Expired certificates cannot perform the TLS handshake at all"
  answer: 1
  explanation: "Expiration is a time-bounded trust assertion. Without it, a certificate for a domain you sold years ago, signed with a key that may have been stolen, using obsolete algorithms, would remain valid forever. Short certificate lifetimes (Let's Encrypt uses 90 days) reduce the blast radius of compromise and ensure certificates stay aligned with current security practices. The cryptographic strength doesn't change, but the trust context does."

- question: "The chain of trust in PKI is: root CA signs intermediate CA certificate, intermediate CA signs end-entity certificate. Why use intermediate CAs instead of having root CAs sign all certificates directly?"
  type: multiple-choice
  options:
    - "Intermediate CAs encrypt the certificates while root CAs only sign them"
    - "Root CA private keys are stored offline in hardware security modules and used rarely. Intermediate CAs handle day-to-day signing. If an intermediate CA is compromised, the root can revoke it without replacing the root key, which would require updating every browser and OS trust store"
    - "Root CAs can only sign a limited number of certificates due to mathematical constraints"
    - "Intermediate CAs provide faster signature verification"
  answer: 1
  explanation: "The root key is the ultimate anchor of trust — its compromise would be catastrophic. Keeping it offline (in an HSM, used only to sign intermediate certificates) dramatically reduces its attack surface. Intermediate CAs are more exposed but more replaceable: revoking an intermediate CA and issuing a new one is operationally feasible, while replacing a root CA requires coordinated updates across all browsers and operating systems worldwide."

- question: "OCSP stapling improves certificate revocation checking by having the web server include a recent, CA-signed OCSP response in the TLS handshake, rather than requiring the client to contact the CA directly."
  type: true-false
  answer: true
  explanation: "Without stapling, the client must contact the CA's OCSP responder to check revocation status, which adds latency, creates a privacy leak (the CA learns which sites you visit), and fails if the OCSP responder is unreachable (most browsers then accept the certificate anyway, defeating the purpose). With stapling, the server periodically fetches its own OCSP response and includes it in the TLS handshake. The response is signed by the CA, so the server cannot forge a 'good' status for a revoked certificate. This is faster, more private, and more reliable."

- question: "Let's Encrypt revolutionized PKI by offering free, automated certificates. How did this change the HTTPS adoption landscape?"
  type: short-answer
  answer: "Before Let's Encrypt (2015), certificates cost money and required manual installation, so HTTPS was mainly used for login pages and e-commerce. Let's Encrypt provided free certificates with automated issuance and renewal (via the ACME protocol), removing both cost and complexity barriers. HTTPS adoption went from ~40% of web traffic to >90% within a few years. The tradeoff is that Let's Encrypt only validates domain control (DV certificates), not organizational identity — it proves you control the domain but not who you are."
  explanation: "Let's Encrypt's contribution was making the operational barrier to HTTPS near zero. The 90-day certificate lifetime (requiring automated renewal) also pushed the ecosystem toward better certificate management practices. The shift to ubiquitous HTTPS means network-level surveillance and content injection are significantly harder, though phishing sites can also get certificates just as easily."
```

## Explainer

Public-key cryptography solves the key distribution problem — anyone can encrypt to you using your public key without a pre-shared secret. But this introduces a new problem: **how do you know a public key belongs to who it claims?** If an attacker substitutes their own public key for your bank's, they can intercept all your encrypted communications. **Public Key Infrastructure (PKI)** solves this through a hierarchy of trust anchored in **Certificate Authorities (CAs)**.

A CA is a trusted entity that verifies identities and issues **X.509 certificates** — digitally signed documents binding a public key to an identity (typically a domain name). Your browser or operating system ships with a set of **root CA certificates** pre-installed in its trust store. When you visit https://example.com, the server presents a certificate chain: the site's certificate (signed by an intermediate CA) and the intermediate CA's certificate (signed by a root CA). Your browser verifies each signature up the chain. If the root CA is in the trust store and all signatures are valid, the browser trusts the site's public key and proceeds with the TLS handshake. This chain of trust is what puts the padlock icon in your address bar.

The system has important fragilities. **Any trusted root CA can issue a certificate for any domain.** Since browsers trust hundreds of root CAs operated by organizations in dozens of countries, a single compromised or coerced CA can forge certificates for any website, enabling man-in-the-middle attacks. The DigiNotar breach (2011) demonstrated this: attackers obtained fraudulent certificates for google.com and used them to intercept Iranian users' Gmail. **Certificate Transparency (CT)** mitigates this by requiring CAs to log all issued certificates in public, cryptographically verifiable logs. Domain owners can monitor these logs and detect unauthorized certificates. Chrome now requires CT for all certificates, making secret certificate issuance detectable.

**Certificate revocation** handles key compromise after issuance. Two mechanisms exist: **CRLs (Certificate Revocation Lists)** are periodically published lists of revoked certificates (bulky, often stale), and **OCSP (Online Certificate Status Protocol)** allows real-time status checks (but adds latency and leaks browsing data). **OCSP stapling** improves this by having the server fetch and include a CA-signed OCSP response in the TLS handshake, eliminating the client's need to contact the CA. Despite these mechanisms, revocation remains PKI's weakest link — many browsers soft-fail (accept the certificate if revocation status cannot be checked), and revocation information propagates slowly. Short certificate lifetimes (Let's Encrypt's 90-day certificates) partially compensate by limiting the window during which a compromised certificate can be misused.
