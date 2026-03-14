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
tags:
- discrete-log
- cryptography
- cyclic-groups
stage: advanced
status: draft
---

# Discrete Logarithms

## Core Idea
Given a primitive root g mod p and nonzero residue a, the discrete logarithm is the unique k (mod p-1) such that g^k ≡ a (mod p). Computing discrete logs is believed hard; this one-way function underpins Diffie-Hellman and elliptic-curve cryptography.
