---
id: rice-theorem
title: Rice's Theorem and Non-Trivial Turing Machine Properties
domain: computer-science
course: theory-of-computation
prerequisites:
- id: reductions-and-undecidability
  type: hard
tags:
- rice-theorem
- undecidability
- machine-properties
stage: abstract-reasoning
status: draft
---

# Rice's Theorem and Non-Trivial Turing Machine Properties

## Core Idea
Rice's theorem states that any non-trivial property of the language recognized by a Turing machine is undecidable. Non-trivial means the property holds for some languages but not others. This powerful result implies that properties like 'Is the language empty?', 'Is it finite?', or 'Is it regular?' are all undecidable.

## Explainer

You have already seen specific undecidability results — the halting problem, and likely several others proved via reduction. Each time, you constructed a custom reduction showing that deciding some property of Turing machines would let you decide the halting problem. Rice's theorem is the grand generalization that makes most of those individual proofs unnecessary: it tells you that **every non-trivial property of the language recognized by a Turing machine is undecidable**, in one sweeping result.

The key word is **non-trivial**. A property of RE languages is trivial if it holds for all RE languages or for none. "Does this Turing machine recognize some language?" is trivially true — every machine recognizes something (even if it's the empty set). "Does this machine recognize a language that is also a valid Java program?" could go either way depending on the machine, so it's non-trivial. Rice's theorem says that any question of this second kind — any question that is true for some machines' languages and false for others — cannot be decided by an algorithm.

The proof works by reduction from the halting problem, but the construction is elegant and general. Suppose you had a decider D for some non-trivial language property P. Since P is non-trivial, there exists some Turing machine M_yes whose language has property P and some machine M_no whose language does not. Given an arbitrary machine M and input w, you construct a new machine M' that first simulates M on w; if M halts, M' then behaves like M_yes. If M never halts on w, M' never gets past the simulation, so its language is empty (which either has P or doesn't). By comparing M''s behavior to whether P holds, you can determine whether M halts on w — solving the halting problem. Since the halting problem is undecidable, D cannot exist.

Notice what Rice's theorem does and does not cover. It applies to **properties of the language** a machine recognizes — semantic questions about what the machine computes. It does not apply to **properties of the machine itself** — syntactic questions about the machine's description. "Does this Turing machine have more than 100 states?" is decidable because you can just count the states in the description. "Does this Turing machine accept more than 100 strings?" is undecidable because it's a question about the language. The dividing line is between inspecting the code (decidable) and predicting the behavior (undecidable). This distinction is deeply relevant to software engineering: Rice's theorem is the formal reason why no algorithm can perfectly detect all viruses, verify all program properties, or decide whether two programs compute the same function.
