---
id: linear-bounded-automata
title: Linear Bounded Automata
domain: computer-science
course: theory-of-computation
prerequisites:
- id: turing-machine-model-and-definition
  type: hard
- id: context-sensitive-languages
  type: hard
builds-toward:
- pspace-complexity-class
tags:
- automata
- resource-bounds
- complexity
stage: advanced
status: draft
---

# Linear Bounded Automata

## Core Idea
A linear bounded automaton (LBA) is a Turing machine whose read-write head cannot move beyond O(n) cells, bounding working memory linearly in input size. LBAs recognize exactly context-sensitive languages. Unlike Turing machines, it is unknown whether deterministic and nondeterministic LBAs recognize the same classes—a fundamental open problem. This contrasts with finite automata (where DFA = NFA) and suggests LBAs occupy an intermediate level of computational universality.

## Explainer

You already know that a Turing machine has an infinite tape, giving it unbounded memory to work with. A **linear bounded automaton (LBA)** is what you get when you take that infinite tape away and replace it with a strict constraint: the machine can only use the portion of tape occupied by the input, plus at most a constant factor more. If the input has n symbols, the LBA gets O(n) tape cells — no more. It can still read, write, and move left or right within that bounded region, and it has the full power of a Turing machine's state-based control. The only limitation is memory.

This memory restriction has a precise correspondence in the Chomsky hierarchy: LBAs recognize exactly the **context-sensitive languages**. Recall that context-sensitive grammars have the property that productions never shrink the string — the right side is always at least as long as the left side. This non-shrinking property is the grammatical reflection of bounded memory: if a derivation never shortens intermediate strings, then the entire derivation stays within O(n) space, which is exactly what an LBA can track. The equivalence between LBAs and context-sensitive grammars is the third level of the automata-grammar correspondence, sitting between pushdown automata / context-free grammars below and Turing machines / unrestricted grammars above.

What makes LBAs theoretically fascinating is an open question that has resisted resolution for decades: **does nondeterminism help?** For finite automata, the answer is no — every NFA can be converted to a DFA recognizing the same language. For Turing machines, the answer is also no — a deterministic TM can simulate any nondeterministic TM (though possibly with exponential slowdown). But for LBAs, it is unknown whether deterministic LBAs (DLBAs) recognize the same class of languages as nondeterministic LBAs (NLBAs). This is the **LBA problem**, and its resolution would have profound implications for complexity theory, particularly the relationship between DSPACE(n) and NSPACE(n).

The LBA occupies a unique position in the computational hierarchy. It is powerful enough to decide properties that context-free languages cannot express — like whether a string has the form ww (a word repeated twice), or whether three numbers encoded in a string satisfy a × b = c. Yet its bounded memory means every LBA computation is guaranteed to halt, unlike a general Turing machine that might loop forever. This guaranteed termination makes the membership problem for context-sensitive languages decidable — in contrast to the undecidable membership problem for recursively enumerable languages. LBAs thus represent a sweet spot: substantially more expressive than pushdown automata, yet tame enough that fundamental questions about their languages remain answerable.
