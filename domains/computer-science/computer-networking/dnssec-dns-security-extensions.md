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

## Explainer

Standard DNS, as you learned it, has a critical vulnerability: nothing in the protocol verifies that a DNS response actually came from the authoritative server. An attacker positioned between you and a DNS resolver can forge responses, redirecting "bank.com" to a malicious IP address. This is **DNS cache poisoning**, and it works because vanilla DNS responses are unsigned plain text — a resolver has no way to distinguish a legitimate answer from a forged one. **DNSSEC** solves this by adding cryptographic signatures to DNS records, allowing resolvers to verify that responses are authentic and unmodified.

The mechanism uses public-key cryptography, which you know from your network security prerequisites. Each DNS zone (like example.com) generates two key pairs. The **Zone-Signing Key (ZSK)** signs the actual DNS records — A records, MX records, and so on. Each signed record gets an accompanying **RRSIG record** containing the signature. When a resolver receives an answer, it retrieves the zone's DNSKEY record (containing the ZSK's public key) and verifies the RRSIG signature. If the signature checks out, the data is authentic. But this raises a bootstrapping problem: how does the resolver know the DNSKEY itself is legitimate?

This is where the **Key-Signing Key (KSK)** and the **chain of trust** come in. The KSK signs the DNSKEY record set (including the ZSK). A hash of the KSK is published as a **DS (Delegation Signer) record** in the parent zone. So example.com's DS record lives in the .com zone, and .com's DS record lives in the root zone. The root zone's keys are the **trust anchors** — their public keys are hardcoded into validating resolvers. Validation follows this chain: the resolver trusts the root keys, uses them to validate .com's keys via the DS record, then uses .com's validated keys to validate example.com's keys, and finally uses example.com's validated ZSK to verify the actual DNS record signatures.

A crucial distinction: DNSSEC provides **authentication and integrity**, not **confidentiality**. DNS queries and responses still travel in plaintext — anyone watching the network can see what domains you are looking up. DNSSEC only guarantees that the answers you receive genuinely came from the authoritative source and were not tampered with in transit. Encrypting DNS traffic is a separate concern, addressed by protocols like DNS-over-HTTPS (DoH) and DNS-over-TLS (DoT). The practical deployment challenge of DNSSEC is key management: zones must periodically rotate their ZSKs, DS records must be updated in parent zones during KSK rollovers, and any break in the chain of trust causes validation failures that make the domain unreachable for DNSSEC-validating resolvers — a failure mode that looks identical to an outage.
