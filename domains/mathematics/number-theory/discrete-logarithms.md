---
id: discrete-logarithms
title: Discrete Logarithms
domain: mathematics
course: number-theory
prerequisites:
- id: primitive-roots-and-cyclic-groups-mod-p
  type: hard
tags:
- discrete-logarithm
- cyclic-groups
- cryptography
stage: advanced
status: draft
---

# Discrete Logarithms

## Core Idea
The discrete logarithm problem is: given g, h in a cyclic group, find x such that g^x = h. This problem is believed to be hard for large finite fields and underpins the security of Diffie-Hellman key exchange, ElGamal encryption, and elliptic-curve cryptography.
