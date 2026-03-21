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

## Questions

```yaml
- question: "In a monoid — a set with an associative operation and an identity element, but without guaranteed inverses — a student tries to prove cancellation: 'ab = ac implies b = c, by multiplying both sides on the left by a⁻¹.' Why does this argument fail in a monoid?"
  type: multiple-choice
  options:
    - "Monoids do not have an associative operation, so regrouping is invalid"
    - "There is no guarantee that a has an inverse in a monoid, so a⁻¹ may not exist"
    - "The identity element in a monoid might not be unique, making the manipulation ambiguous"
    - "Cancellation holds in all algebraic structures with an identity, so the argument succeeds"
  answer: 1
  explanation: "The cancellation proof in a group works precisely because every element has an inverse: multiply ab = ac on the left by a⁻¹, use associativity to regroup as (a⁻¹a)b = (a⁻¹a)c, use the inverse axiom to get eb = ec, then use the identity axiom to get b = c. Each step requires a specific axiom. In a monoid, inverses are not guaranteed — the element a may have no inverse at all. The argument breaks at the first step. This illustrates why abstract algebra distinguishes carefully between structures: monoids, groups, and quasigroups each have different subsets of the four group axioms, and each subset enables different theorems."

- question: "Suppose you find an element a in a group satisfying a² = a. What can you conclude about a?"
  type: multiple-choice
  options:
    - "a must be the identity element of the group"
    - "a must equal its own inverse"
    - "a = e only if the group is abelian (commutative)"
    - "Nothing certain — the axioms do not constrain elements satisfying a² = a"
  answer: 0
  explanation: "From a² = a, apply left-cancellation (which holds in any group): a·a = a·e (since a = a·e by the identity axiom). By left-cancellation (cancel the leading a from both sides), we get a = e. Alternatively: multiply both sides on the left by a⁻¹ to get a⁻¹(aa) = a⁻¹a, giving (a⁻¹a)a = e (by associativity and inverse), so ea = e, so a = e. The element satisfying a² = a in a group is uniquely the identity. This result holds in any group, abelian or not — it follows from the axioms alone."

- question: "The group axioms explicitly state that every group contains exactly one identity element."
  type: true-false
  answer: false
  explanation: "The group axioms assert only that AN identity EXISTS — that there is some element e such that ae = ea = a for all a. The axioms do not say it is unique. Uniqueness is a theorem that must be proved. The proof is: suppose e and e' are both identities. Then e = e·e' (applying e' as identity) = e' (applying e as identity). So e = e'. The distinction matters because it is a model for rigorous mathematics: you are allowed to use only what the axioms give you, not what feels obvious. A structure could conceivably satisfy 'an identity exists' without it being unique — the proof rules that out."

- question: "In any group, both left-cancellation (ab = ac implies b = c) and right-cancellation (ba = ca implies b = c) hold."
  type: true-false
  answer: true
  explanation: "Left-cancellation: multiply ab = ac on the left by a⁻¹, use associativity: (a⁻¹a)b = (a⁻¹a)c, then eb = ec, then b = c. Right-cancellation: multiply ba = ca on the right by a⁻¹, use associativity: b(aa⁻¹) = c(aa⁻¹), then be = ce, then b = c. Both proofs use inverses (to produce e from aa⁻¹) and associativity (to regroup), plus the identity axiom. Removing any one of these axioms breaks one or both cancellation laws — which is exactly why abstract algebra has separate names for structures without one or more axioms."

- question: "Why does proving the uniqueness of the identity and inverses in a group matter, when it seems 'obvious' there should only be one? What algebraic structure shows that uniqueness of identity doesn't automatically imply cancellation?"
  type: short-answer
  answer: "Uniqueness must be proved because the axioms only assert existence. An axiom system could be satisfied by structures where multiple identities coexist — the uniqueness proof rules this out by deriving a contradiction from the axioms. This matters because abstract algebra is about working from minimal hypotheses: if a result follows from the axioms, it holds in every structure satisfying those axioms; if it doesn't follow, some structures may lack it. A monoid (associative operation + unique identity, no inverses) has a unique identity but generally fails the cancellation law — cancellation requires inverses. Conversely, a quasigroup satisfies cancellation but need not have an identity at all. Groups are special because they have all four axioms, and each axiom is needed to prove the standard results."
  explanation: "The intellectual discipline is learning to ask: 'Which axioms did I actually use in this proof?' If you prove cancellation using only associativity and inverses (no commutativity), then cancellation holds in all groups including non-abelian ones. If your proof accidentally uses commutativity, you've only proved it for abelian groups — a weaker result. This axiom-tracking habit is the core skill that abstract algebra develops, and it carries into every area of mathematics where you work with general algebraic structures."
```

## Explainer

When you first learn the group axioms from your prerequisite study, the axioms assert that an identity exists and that inverses exist — but they don't immediately say those elements are *unique*. What if a group had two different identity elements? What if some element had two different inverses? The basic properties of groups prove that this cannot happen, and that proof is more instructive than the facts themselves.

The **uniqueness of the identity** is proved by contradiction: suppose e and e' are both identities. Then e = e·e' (since e' is an identity) = e' (since e is an identity). The argument is just two applications of the axiom, but it reveals something deep — the identity is pinned in place by its own definition. Similarly, **uniqueness of inverses** follows by multiplying on the left by a supposed second inverse: if both b and c satisfy ab = e and ba = e, then b = b·e = b·(ac) = (ba)·c = e·c = c. Both uniqueness proofs use the associativity axiom in an essential way.

The **cancellation law** — if ab = ac then b = c — is the group-theoretic analogue of cancelling common factors in arithmetic. Multiply both sides on the left by a⁻¹, and associativity does the rest: a⁻¹(ab) = a⁻¹(ac) gives (a⁻¹a)b = (a⁻¹a)c, then e·b = e·c, then b = c. Notice you need both the existence of inverses and associativity; neither alone suffices. Right-cancellation (ba = ca implies b = c) is proved symmetrically by multiplying on the right.

These properties may seem obvious — of course identity elements are unique, you say. But in abstract algebra, "obvious" is not a proof. A **monoid** (associative operation with identity, but no inverses) can have a unique identity but fail cancellation. A **quasigroup** (cancellation holds, but no identity required) is a different structure entirely. What makes a group powerful is precisely the interaction of all four axioms together. Learning to derive consequences from minimal hypotheses — rather than assuming what feels obvious — is the central intellectual habit that abstract algebra trains.
