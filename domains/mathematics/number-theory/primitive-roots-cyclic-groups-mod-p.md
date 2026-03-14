---
id: primitive-roots-cyclic-groups-mod-p
title: Primitive Roots and Cyclic Groups Mod p
domain: mathematics
course: number-theory
prerequisites:
- id: fermats-little-theorem
  type: hard
- id: eulers-totient-function
  type: hard
- id: group-definition-and-examples
  type: soft
builds-toward:
- discrete-logarithms
tags:
- primitive-roots
- cyclic-groups
- generators
stage: advanced
status: draft
---

# Primitive Roots and Cyclic Groups Mod p

## Core Idea
A primitive root mod p is an integer g whose powers g^1, g^2, ..., g^(p-1) exhaust all nonzero residues mod p. Equivalently, g has order p-1. Every prime p has primitive roots, making (Z/pZ)* cyclic of order p-1.
