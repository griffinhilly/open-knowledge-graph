---
id: time-hierarchy-theorem
title: Time Hierarchy Theorem
domain: computer-science
course: theory-of-computation
prerequisites:
- id: time-complexity-classes
  type: hard
- id: turing-machines
  type: hard
builds-toward:
- exptime-expspace-classes
tags:
- complexity-theory
- hierarchy
- provable-separation
stage: advanced
status: draft
---

# Time Hierarchy Theorem

## Core Idea
The time hierarchy theorem states that for time-constructible f(n) > n log n, DTIME(f(n)) ⊂ DTIME(f(n) log f(n))—more time strictly enables computing harder problems. Using diagonal arguments with universal Turing machines, the theorem guarantees languages exist computable in quadratic but not linear time, providing rare provable separations in complexity theory. The log factor stems from the overhead of simulating one machine by another while verifying time bounds.

## Explainer

From your work with time complexity classes and Turing machines, you know that DTIME(f(n)) is the set of languages decidable by a deterministic Turing machine in O(f(n)) steps. An intuitive question arises: does giving a machine more time genuinely let it solve harder problems, or could clever algorithms always compensate? The **time hierarchy theorem** answers definitively: more time means strictly more computational power, and this can be proved.

The proof uses a **diagonalization** argument reminiscent of how Cantor proved the reals are uncountable, adapted to the computational setting. The idea is to construct a language L that a machine with the larger time bound can decide but no machine with the smaller bound can. Here is the intuition: a **universal Turing machine** U can simulate any other Turing machine M given M's description as input, but this simulation incurs overhead — roughly a logarithmic factor. You build a machine D that, on input x, interprets x as the encoding of some machine M_x, simulates M_x on x for f(n) steps using U, and then does the opposite of what M_x does (accepts if M_x rejects, rejects if M_x accepts). This diagonal machine D decides a language that differs from the language of every f(n)-bounded machine on at least one input. Because D itself runs in time O(f(n) log f(n)) — the extra log factor comes from the simulation overhead — the language D decides lives in DTIME(f(n) log f(n)) but provably not in DTIME(f(n)).

The requirement that f(n) be **time-constructible** — meaning a Turing machine can compute f(n) in O(f(n)) time — is a technical but necessary condition. The diagonal machine D needs to know when to stop simulating M_x, so it must be able to compute the time bound. Virtually all natural functions (polynomials, exponentials, n log n) are time-constructible, so this condition rarely matters in practice, but it prevents pathological edge cases involving functions whose values cannot be efficiently determined.

What makes the time hierarchy theorem remarkable is how rare provable separations are in complexity theory. We believe P ≠ NP but cannot prove it. We believe NP ≠ PSPACE but cannot prove it. Yet the time hierarchy theorem gives us unconditional, proven separations: DTIME(n) ⊊ DTIME(n²), DTIME(n²) ⊊ DTIME(n⁴), and P ⊊ EXP. These separations confirm that the complexity landscape has genuine structure — faster machines really do solve strictly fewer problems — even though we cannot yet locate where specific boundaries like P versus NP fall within that landscape. The theorem also has a space analogue (the space hierarchy theorem), which proves the same strict containment for space-bounded computation, but without the logarithmic overhead.
