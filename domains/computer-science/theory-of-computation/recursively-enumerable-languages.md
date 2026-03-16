---
id: recursively-enumerable-languages
title: Recursively Enumerable Languages
domain: computer-science
course: theory-of-computation
prerequisites:
- id: turing-machines
  type: hard
- id: decidability
  type: hard
builds-toward:
- recognizability-vs-decidability
- halting-problem
tags:
- computability
- formal-languages
- turing-completeness
stage: advanced
status: draft
---

# Recursively Enumerable Languages

## Core Idea
A language is recursively enumerable (RE) if a Turing machine exists that halts-and-accepts every string in the language; for strings outside the language, the machine may never halt. RE languages equal Type 0 languages in the Chomsky hierarchy. They represent the boundary of mechanical computation: problems whose solutions can be systematically generated (enumerated) but not necessarily verified in finite time characterize this class.

## Explainer

From your study of Turing machines and decidability, you know that a **decidable** (recursive) language has a Turing machine that always halts — it says "yes" for strings in the language and "no" for strings outside it. A **recursively enumerable** language relaxes this guarantee in a crucial way: the machine must still halt and accept every string that belongs to the language, but for strings that do not belong, it is allowed to run forever. You get a definitive "yes" but never a guaranteed "no."

Think of it like a search process. Imagine you are looking for a proof that a mathematical statement is true. If a proof exists, a systematic search will eventually find it — you can enumerate all possible proof strings in order of length and check each one. If the statement is provable, your search halts with the proof. But if the statement is not provable, your search continues indefinitely; you never reach a point where you can confidently declare "no proof exists," because there is always a longer candidate you haven't tried yet. This asymmetry between confirmation and refutation is the defining feature of recursively enumerable languages.

The name "recursively enumerable" comes from an equivalent characterization: a language is RE if and only if there exists a Turing machine that **enumerates** (lists) all strings in the language, one by one, possibly with repetitions and in no particular order. If you wait long enough, every member of the language will eventually appear on the list. But if a string is not in the language, it simply never shows up — and you can never be sure it won't appear later. This enumeration perspective connects to the idea of a **semi-decision procedure**: a process that can confirm membership but cannot confirm non-membership.

The gap between RE and decidable languages has profound consequences. The **halting problem** — does a given Turing machine halt on a given input? — is the classic example of a language that is RE but not decidable. You can confirm halting by simply running the machine and waiting for it to stop, but you cannot confirm non-halting because the machine might halt after any number of steps. This means the complement of an RE language is not necessarily RE; in fact, a language is decidable if and only if both it and its complement are recursively enumerable. When one side of this pair breaks — when you can enumerate the "yes" instances but not the "no" instances — you have crossed from decidability into the territory of undecidability, and recursively enumerable languages mark exactly that frontier.
