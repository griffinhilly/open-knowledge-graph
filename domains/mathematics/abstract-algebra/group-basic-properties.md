---
id: group-basic-properties
title: Basic Properties of Groups
domain: mathematics
course: abstract-algebra
prerequisites:
- id: group-definition-examples
  type: hard
builds-toward:
- subgroups-subgroup-test
- cyclic-groups
- group-homomorphisms
tags:
- group-properties
- identity
- inverse
- cancellation
stage: advanced
status: draft
---

# Basic Properties of Groups

## Core Idea
Every group has a unique identity element and every element has a unique inverse. The cancellation law holds: if ab = ac then b = c. These properties, derived from the group axioms, establish fundamental facts about group structure and behavior.

## Explainer

When you first learn the group axioms from your prerequisite study, the axioms assert that an identity exists and that inverses exist — but they don't immediately say those elements are *unique*. What if a group had two different identity elements? What if some element had two different inverses? The basic properties of groups prove that this cannot happen, and that proof is more instructive than the facts themselves.

The **uniqueness of the identity** is proved by contradiction: suppose e and e' are both identities. Then e = e·e' (since e' is an identity) = e' (since e is an identity). The argument is just two applications of the axiom, but it reveals something deep — the identity is pinned in place by its own definition. Similarly, **uniqueness of inverses** follows by multiplying on the left by a supposed second inverse: if both b and c satisfy ab = e and ba = e, then b = b·e = b·(ac) = (ba)·c = e·c = c. Both uniqueness proofs use the associativity axiom in an essential way.

The **cancellation law** — if ab = ac then b = c — is the group-theoretic analogue of cancelling common factors in arithmetic. Multiply both sides on the left by a⁻¹, and associativity does the rest: a⁻¹(ab) = a⁻¹(ac) gives (a⁻¹a)b = (a⁻¹a)c, then e·b = e·c, then b = c. Notice you need both the existence of inverses and associativity; neither alone suffices. Right-cancellation (ba = ca implies b = c) is proved symmetrically by multiplying on the right.

These properties may seem obvious — of course identity elements are unique, you say. But in abstract algebra, "obvious" is not a proof. A **monoid** (associative operation with identity, but no inverses) can have a unique identity but fail cancellation. A **quasigroup** (cancellation holds, but no identity required) is a different structure entirely. What makes a group powerful is precisely the interaction of all four axioms together. Learning to derive consequences from minimal hypotheses — rather than assuming what feels obvious — is the central intellectual habit that abstract algebra trains.
