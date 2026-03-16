---
id: automorphism-groups-of-models
title: Automorphism Groups and Their Structure
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: model-theory-basics
  type: hard
- id: type-spaces-and-stone-topology
  type: soft
- id: group-definition-examples
  type: soft
- id: group-definition-and-examples
  type: soft
builds-toward:
- homogeneous-models-realization
- strongly-minimal-and-geometry
tags:
- automorphisms
- group-structure
- orbits
stage: advanced
status: draft
---

# Automorphism Groups and Their Structure

## Core Idea
The automorphism group Aut(M) of a model M consists of all bijections from M to itself that preserve the structure. The orbits of this group action on n-tuples partition the complete types realized in M. The structure of automorphism groups encodes information about types, definable subgroups, and stability properties of the model.

## Explainer

You already know from model theory basics that a model is a set equipped with interpretations for the function and relation symbols of a language. An **automorphism** of M is a bijection σ: M → M that preserves all of this structure: for every relation symbol R and every tuple ā, M ⊨ R(ā) if and only if M ⊨ R(σ(ā)). Automorphisms are exactly the symmetries of M — they rearrange elements while leaving all logical properties intact.

The collection of all automorphisms of M forms a group under composition, called **Aut(M)**. Composition is associative, the identity map is always an automorphism, and each automorphism has an inverse. From your optional prerequisite on group definitions, you know these are precisely the group axioms. What is new here is that Aut(M) is not just any abstract group — it is a group acting on M by permutation, and this action has deep logical content.

The key theorem connects automorphisms to types. Two elements a and b in M realize the **same complete type** (the same set of formulas they satisfy) if and only if there exists an automorphism σ ∈ Aut(M) such that σ(a) = b — at least in sufficiently homogeneous models. More generally, the **orbits** of the action of Aut(M) on n-tuples from M correspond exactly to the complete n-types realized in M. Elements in the same orbit are logically indistinguishable from the model's internal perspective; elements in different orbits are distinguished by some formula.

This orbit-type correspondence gives Aut(M) diagnostic power. If Aut(M) acts transitively on all pairs of realizations of a given type (every element can be mapped to every other), the model is called **homogeneous** in a strong sense. A model with a very small automorphism group (e.g., a rigid model with only the identity) has many distinct types and many definable singletons. Conversely, a rich automorphism group signals high symmetry and often stability: in the theory of algebraically closed fields, the automorphism group of the algebraic closure of Q is enormous, corresponding to the large number of types over Q that can be automorphically interchanged. Studying Aut(M) is thus studying the "degree of indistinguishability" baked into the model — a precise, algebraic measure of how much structure the first-order theory can pin down.
