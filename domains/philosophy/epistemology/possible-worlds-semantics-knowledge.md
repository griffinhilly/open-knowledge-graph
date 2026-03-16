---
id: possible-worlds-semantics-knowledge
title: Possible Worlds Semantics for Knowledge
domain: philosophy
course: epistemology
prerequisites:
- id: epistemic-logic-basics
  type: hard
- id: possible-worlds-semantics
  type: soft
- id: modal-semantics-possible-worlds
  type: soft
- id: modal-logic-intro
  type: hard
builds-toward:
- epistemic-accessibility-relations
- closure-principles-formalized
tags:
- possible-worlds
- semantics
- knowledge
stage: formal-systems
status: draft
---

# Possible Worlds Semantics for Knowledge

## Core Idea
Knowledge is represented as truth across a restricted set of possible worlds—those compatible with the agent's evidence or cognitive state. An agent knows p if p is true in all worlds accessible to her; she merely believes p if it is true in some but not all accessible worlds. This model makes precise the intuition that knowledge requires ruling out certain error-possibilities.

## Explainer

You have already worked with modal logic and possible worlds semantics: you know that a proposition is necessarily true if it is true in all possible worlds, and possibly true if it is true in at least one. The semantics for knowledge takes this framework and adds a crucial relational structure — the **accessibility relation**. Rather than asking about all possible worlds, we ask about only those worlds that are **epistemically accessible** to a particular agent: worlds that are, from her perspective, compatible with everything she knows or has evidence for. This restricted set is called the agent's **epistemic range**.

The knowledge condition then becomes: an agent **knows** that p if and only if p is true in every world within her epistemic range. She **believes** p if p is true in at least some accessible worlds. The gap between these conditions captures the gap between belief and knowledge: a believer's accessible worlds include some in which p is true and some in which it is false; a knower's accessible worlds are all p-worlds. To know p is to have **ruled out** all the accessible worlds in which p is false. This is not just a formal trick — it makes vivid what knowledge requires: you must have evidence or justification that eliminates the relevant error possibilities.

Consider the standard example. You are looking at a barn in good light, and you believe there is a barn there. But suppose (without your knowing) that you are in "Fake Barn County," where the countryside is full of barn facades that look exactly like barns from the road. In the actual world, you are facing a real barn. But in nearby accessible worlds — ones compatible with your visual evidence — you might be facing a facade. Your evidence does not rule out those worlds. So even though your belief is true, it is not knowledge: your epistemic range contains worlds in which p is false. This is the famous Gettier-style problem made geometrically precise in the possible worlds model.

The accessibility relation does more than locate the agent's evidence. Different constraints on the relation generate different **epistemic logics**. If the relation is **reflexive** (every world is accessible to itself), then knowledge is **veridical**: if you know p, p is true (axiom T). If the relation is also **transitive** (knowing implies knowing that you know — axiom 4), you get the S4 system; add symmetry and you get S5. Each axiom corresponds to an intuitive principle about knowledge, and the possible worlds framework lets you see exactly what structural commitments are required to validate each principle. This is the power of the formal approach: epistemological choices become geometrical choices about the shape of the accessibility relation, visible and testable in a way that purely verbal formulations often obscure.
