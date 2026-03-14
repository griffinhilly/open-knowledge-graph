---
id: temporal-logic
title: Temporal Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: modal-logic-intro
  type: hard
builds-toward: []
tags:
- temporal-logic
- LTL
- CTL
- Kripke-structures
- model-checking
- program-verification
stage: formal-systems
status: draft
---

# Temporal Logic

## Core Idea
Temporal logic specializes modal logic to reason about time. Linear Temporal Logic (LTL) models time as a single infinite sequence of states, with operators G (always/globally), F (eventually/finally), X (next), and U (until). Computation Tree Logic (CTL) models time as a branching tree, adding path quantifiers A (on all paths) and E (on some path) before temporal operators. Both are interpreted over Kripke structures where the accessibility relation represents temporal succession. Temporal logic is the formal backbone of model checking — the automated verification technique that exhaustively tests whether a system satisfies its specification, used extensively in hardware and software verification.

## How It's Best Learned
Write LTL specifications for simple properties (e.g., "every request is eventually followed by a response" = G(request → F response)) and evaluate them on small transition systems drawn as labeled graphs. Then compare LTL and CTL expressiveness by finding properties expressible in one but not the other.

## Common Misconceptions
- LTL and CTL are not subsets of each other — they are incomparable in expressiveness. Some properties (e.g., fairness) are expressible in LTL but not CTL, and vice versa.
- The "always" operator G does not mean "at every time step from now" in CTL without a path quantifier — AG and EG mean very different things.
- Temporal logic model checking is decidable and efficient for finite-state systems, but undecidable for infinite-state systems in general.
