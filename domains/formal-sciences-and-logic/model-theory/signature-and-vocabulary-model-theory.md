---
id: signature-and-vocabulary-model-theory
title: Signature and Formal Vocabulary
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: first-order-logic-syntax
  type: hard
- id: structures-and-formal-languages
  type: hard
builds-toward:
- model-instantiation-structures
- embedding-and-preservation-properties
tags:
- signature
- vocabulary
- language
- formalization
stage: abstract-reasoning
status: draft
---

# Signature and Formal Vocabulary

## Core Idea
A signature consists of a set of constant symbols, function symbols, and relation symbols with specified arities. The signature defines the vocabulary through which we can express properties of structures. Every first-order theory is formulated in a particular signature, and different signatures can express different classes of mathematical objects.

## How It's Best Learned
Study signatures for familiar mathematical structures: the signature for groups (one binary operation, identity), fields (addition, multiplication), and ordered sets (a binary relation). Compare how the same underlying structure can be described in different signatures.

## Common Misconceptions
Signature is not the same as a theory—a signature is the vocabulary, while a theory makes statements in that vocabulary. The choice of signature can dramatically affect what is expressible.
