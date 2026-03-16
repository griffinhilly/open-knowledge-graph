---
id: decidability
title: Decidable Languages
domain: computer-science
course: theory-of-computation
prerequisites:
- id: turing-machines
  type: hard
- id: set-theory-basics
  type: soft
- id: cardinality-and-countability
  type: soft
- id: mathematical-induction
  type: soft
- id: church-turing-thesis
  type: soft
- id: turing-machine-variants
  type: soft
builds-toward:
- halting-problem
- recognizability-vs-decidability
- undecidability-reductions
tags:
- decidable
- Turing-decidable
- recognizable
- algorithms
stage: advanced
status: validated
---
# Decidable Languages

## Core Idea
A language is *Turing-decidable* (or just decidable) if some Turing machine halts on every input and correctly accepts or rejects. A language is *Turing-recognizable* if some TM halts and accepts on every string in the language, but may loop on strings outside it. Decidable languages are a proper subset of recognizable languages. Examples of decidable languages include all regular and context-free languages. The distinction between recognizable and decidable becomes crucial when studying the limits of computation: some problems can be semi-solved (recognized) but not fully solved (decided).

## How It's Best Learned
Build TMs that decide specific languages (e.g., ATM for the same-length palindrome) and contrast with TMs that only recognize. Understanding why a decider must *halt on rejection* — not just loop — is the key conceptual bridge to undecidability.

## Common Misconceptions
- Thinking 'recognizable' and 'decidable' are synonyms — a recognizer may loop forever on non-members.
- Assuming all natural computational problems are decidable — the halting problem proves this false.

## Explainer

From your study of Turing machines, you know that a TM can read, write, and move along an infinite tape, giving it the power to simulate any algorithm. But here is the critical question: when you run a Turing machine on an input, does it always eventually stop and give you an answer? The distinction between machines that always halt and machines that might run forever is the heart of **decidability**.

A **decider** is a Turing machine that halts on *every* input — it always reaches either an accept state or a reject state in finite time. A language is **decidable** if some decider exists for it. By contrast, a **recognizer** is a Turing machine that halts and accepts every string in the language but might loop forever on strings not in the language. A language is **Turing-recognizable** if some recognizer exists for it. The difference is subtle but profound: with a decider, you are guaranteed an answer (yes or no) in finite time. With a mere recognizer, a "yes" answer comes in finite time, but a "no" answer might never come — the machine just keeps running, and you can never be sure whether it will eventually halt or loop forever.

Every decidable language is automatically recognizable (a decider is a recognizer that happens to always halt), but the converse is false — some recognizable languages are not decidable. Where do familiar languages fall? All **regular languages** are decidable: you can simulate a DFA, which always halts after reading the input. All **context-free languages** are decidable: the CYK algorithm always terminates with a yes-or-no answer. So for the language classes you have studied so far, decidability comes for free. The interesting territory begins with questions *about* Turing machines themselves — like "does this TM accept this input?" — where recognizability and decidability diverge.

The reason decidability matters is that it draws a sharp, provable boundary around what algorithms can accomplish. It is not a matter of cleverness or computing power: some problems have no algorithm that always halts with a correct answer, and this can be *proven* — no future hardware or software breakthrough will change it. The **halting problem**, which you will study next, is the canonical example. Understanding the decidable/recognizable distinction equips you to ask the right question about any computational problem: not just "can I solve it?" but "can I *always* solve it and know when I am done?"
