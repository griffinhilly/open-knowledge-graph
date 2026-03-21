---
id: dnssec-dns-security-extensions
title: 'DNSSEC: DNS Security Extensions'
domain: computer-science
course: computer-networking
prerequisites:
- id: dns-domain-name-system
  type: hard
- id: network-security-fundamentals
  type: hard
builds-toward:
- network-security-fundamentals
- network-standards-and-ietf
tags:
- security
- dns
- dnssec
- cryptography
stage: advanced
status: draft
---

# DNSSEC: DNS Security Extensions

## Core Idea
DNSSEC (DNS Security Extensions) adds cryptographic signatures to DNS records, enabling recipients to verify origin and integrity. ZONESK (Zone-Signing Keys) and KSKs (Key-Signing Keys) form a signing hierarchy. Chain of trust extends from the root through TLDs to authoritative nameservers, with RRSIG records providing signatures and DS records delegating validation.

## How It's Best Learned
Set up a DNSSEC-signed zone using BIND or NSD. Observe RRSIG, DNSKEY, and DS records in DNS responses. Perform DNSSEC validation chain verification using dig +dnssec. Simulate DNSSEC validation failures and observe resolver behavior.

## Common Misconceptions
DNSSEC does not encrypt DNS queries; it only authenticates responses. Deploying DNSSEC requires careful key management and chain-of-trust setup. DNSSEC validation failures can occur due to misconfiguration, not just attacks.

## Questions

```yaml
- question: "After deploying DNSSEC for example.com, users of DNSSEC-validating resolvers report they cannot reach the site at all. Users of non-validating resolvers have no problem. What is the most likely cause?"
  type: multiple-choice
  options:
    - "The chain of trust is broken — for example, the DS record in the .com parent zone was not updated to match the zone's KSK, so validators cannot complete the validation chain and return SERVFAIL"
    - "DNSSEC encrypted the DNS responses in a format that validating resolvers cannot decrypt without the private key"
    - "The zone's A records were inadvertently deleted when DNSSEC signing was enabled"
    - "Non-validating resolvers are performing a DNS cache poisoning attack, making the site appear reachable to them"
  answer: 0
  explanation: "DNSSEC validation requires an unbroken chain of trust from the root through parent zones to the signed zone. If the DS record in the .com zone doesn't match the zone's KSK — a common error during deployment or key rollover — validating resolvers cannot verify the zone's DNSKEY, causing them to reject all responses with SERVFAIL. Non-validating resolvers simply ignore signatures and accept whatever answer they receive. DNSSEC does not encrypt responses; it signs them — so decryption is not involved. The broken chain failure mode is why DNSSEC deployments require careful coordination between the zone operator and the parent zone registry."

- question: "A network administrator deploys DNSSEC for their company's domain. A colleague says: 'Great — now no one can see what websites our employees are visiting.' Is the colleague correct?"
  type: multiple-choice
  options:
    - "Yes — DNSSEC cryptographically encrypts DNS queries and responses, hiding domain lookups from observers"
    - "No — DNSSEC authenticates DNS responses to prevent tampering, but queries and responses still travel in plaintext; observers can still see which domains are being looked up"
    - "Yes — the chain of trust prevents third parties from intercepting DNS traffic at any point in the network"
    - "No — DNSSEC only protects the path from authoritative nameservers to resolvers, not from clients to resolvers"
  answer: 1
  explanation: "DNSSEC provides authentication and integrity, not confidentiality. DNS queries and responses remain unencrypted plaintext — anyone who can observe the network traffic can still see which domains are being resolved. DNSSEC's signatures allow a receiver to verify that a response genuinely came from the authoritative source and was not modified in transit, but they reveal nothing about the content. Hiding DNS queries requires separate protocols like DNS-over-HTTPS (DoH) or DNS-over-TLS (DoT), which encrypt the entire DNS conversation."

- question: "DNSSEC validation chains trust from the root zone through parent zones via DS records down to the target zone, so a validating resolver must trust the root zone's public keys as its starting point."
  type: true-false
  answer: true
  explanation: "The root zone's DNSKEY records are the trust anchors: their public keys are hardcoded into validating resolvers. From there, each parent zone publishes a DS (Delegation Signer) record containing a hash of the child zone's KSK. The resolver verifies the child's DNSKEY against the parent's DS record, which was itself verified using the grandparent's keys, and so on up to the root. This hierarchical chain means that trusting the root is both the starting assumption and the point of maximum leverage — if a root key were compromised, the entire DNSSEC system would be undermined."

- question: "DNSSEC protects DNS responses from eavesdropping because all DNS records are encrypted with the Zone-Signing Key before transmission."
  type: true-false
  answer: false
  explanation: "DNSSEC does not encrypt DNS records — it signs them. The Zone-Signing Key is used to create RRSIG signatures that prove a record is authentic and unmodified, but the records themselves are transmitted in plaintext, just as in ordinary DNS. An observer watching the network can read every DNS response, including DNSSEC-signed ones. Encryption of DNS traffic requires DNS-over-HTTPS (DoH) or DNS-over-TLS (DoT), which wrap DNS messages in TLS sessions. DNSSEC's goal is authentication (did this response come from the legitimate authoritative server?), not confidentiality (can observers see the response?)."

- question: "Explain why a break in the DNSSEC chain of trust causes a domain to become completely unreachable for DNSSEC-validating resolvers, even if the domain's DNS records are technically correct."
  type: short-answer
  answer: "A validating resolver must verify every link in the chain from the root trust anchor to the zone's actual records: root DNSKEY → .com DS record → .com DNSKEY → example.com DS record → example.com DNSKEY → RRSIG signatures on the A record. If any link fails — an expired RRSIG, a DS record that doesn't match the zone's KSK, or a missing DNSKEY — the resolver cannot complete the validation chain. Rather than accept an unvalidated response (which could be a forgery), it returns SERVFAIL, making the domain unreachable. The resolver treats a broken chain identically to a detected attack, because it has no way to distinguish misconfiguration from tampering."
  explanation: "This 'fail closed' design is intentional: the security model assumes that an inability to verify authenticity is as dangerous as a detected attack. The operational consequence is that DNSSEC misconfigurations look exactly like outages to end users with validating resolvers."
```

## Explainer

Standard DNS, as you learned it, has a critical vulnerability: nothing in the protocol verifies that a DNS response actually came from the authoritative server. An attacker positioned between you and a DNS resolver can forge responses, redirecting "bank.com" to a malicious IP address. This is **DNS cache poisoning**, and it works because vanilla DNS responses are unsigned plain text — a resolver has no way to distinguish a legitimate answer from a forged one. **DNSSEC** solves this by adding cryptographic signatures to DNS records, allowing resolvers to verify that responses are authentic and unmodified.

The mechanism uses public-key cryptography, which you know from your network security prerequisites. Each DNS zone (like example.com) generates two key pairs. The **Zone-Signing Key (ZSK)** signs the actual DNS records — A records, MX records, and so on. Each signed record gets an accompanying **RRSIG record** containing the signature. When a resolver receives an answer, it retrieves the zone's DNSKEY record (containing the ZSK's public key) and verifies the RRSIG signature. If the signature checks out, the data is authentic. But this raises a bootstrapping problem: how does the resolver know the DNSKEY itself is legitimate?

This is where the **Key-Signing Key (KSK)** and the **chain of trust** come in. The KSK signs the DNSKEY record set (including the ZSK). A hash of the KSK is published as a **DS (Delegation Signer) record** in the parent zone. So example.com's DS record lives in the .com zone, and .com's DS record lives in the root zone. The root zone's keys are the **trust anchors** — their public keys are hardcoded into validating resolvers. Validation follows this chain: the resolver trusts the root keys, uses them to validate .com's keys via the DS record, then uses .com's validated keys to validate example.com's keys, and finally uses example.com's validated ZSK to verify the actual DNS record signatures.

A crucial distinction: DNSSEC provides **authentication and integrity**, not **confidentiality**. DNS queries and responses still travel in plaintext — anyone watching the network can see what domains you are looking up. DNSSEC only guarantees that the answers you receive genuinely came from the authoritative source and were not tampered with in transit. Encrypting DNS traffic is a separate concern, addressed by protocols like DNS-over-HTTPS (DoH) and DNS-over-TLS (DoT). The practical deployment challenge of DNSSEC is key management: zones must periodically rotate their ZSKs, DS records must be updated in parent zones during KSK rollovers, and any break in the chain of trust causes validation failures that make the domain unreachable for DNSSEC-validating resolvers — a failure mode that looks identical to an outage.
