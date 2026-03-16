---
id: sensitivity-condition-knowledge
title: The Sensitivity Condition and Tracking Truth
domain: philosophy
course: epistemology
prerequisites:
- id: gettier-problems
  type: hard
- id: what-is-knowledge
  type: soft
- id: modal-logic-intro
  type: soft
tags:
- knowledge
- sensitivity
- tracking
- gettier
stage: formal-systems
status: draft
---

# The Sensitivity Condition and Tracking Truth

## Core Idea
The sensitivity requirement states that if the proposition known were false, the believer would not believe it—the belief appropriately tracks the truth. Unlike safety, which asks about false beliefs one could have made, sensitivity focuses on whether one's actual belief would vary with the truth-value of the proposition. Together with safety, sensitivity attempts to capture when true justified belief constitutes genuine knowledge rather than lucky guessing.

## How It's Best Learned
Practice checking whether a belief would vanish if the proposition were false. Apply to perceptual knowledge, testimony, and inference. Note cases where sensitivity fails even with true justified belief (like normal logical deduction).

## Common Misconceptions
- Confusing sensitivity with reliability (sensitivity is subjunctive; reliability is statistical).
- Thinking sensitivity alone is sufficient for knowledge.
- Assuming true beliefs are automatically sensitive to their truth-conditions.

## Explainer

You already understand Gettier cases: situations where you have justified true belief but intuitively lack knowledge, because your belief is true "by accident." Various responses have attempted to add conditions that rule out such accidents. The sensitivity condition, developed most influentially by Robert Nozick, approaches this by asking a counterfactual question: **would you still believe it if it were false?**

The formulation uses a **subjunctive conditional**: S's belief that P is *sensitive* if and only if, were P false, S would not believe P. This tests whether your belief tracks the truth — whether your belief-forming mechanism is genuinely responsive to how things actually are. Consider a simple case: you see your cat on the mat and believe the cat is there. If the cat were not on the mat, you would look, see no cat, and not believe it. Your belief tracks the truth. Now contrast a Gettier-style case: you correctly believe it is 3:00 PM because you glance at a stopped clock that happens to read 3:00. If it were not 3:00 PM, the clock would still read 3:00, and you would still believe it is 3:00 PM. Your belief does not track the truth — it fails the sensitivity condition.

Your background in modal logic is directly relevant here. The sensitivity condition checks what happens in the **closest possible world** where P is false — the scenario minimally different from ours where the proposition doesn't hold. This is fundamentally different from asking about reliability across many actual cases (a statistical question). Sensitivity is a modal claim: it asks about what you *would* believe in a nearby counterfactual scenario. A belief can be statistically reliable and yet insensitive — if, for example, you're right 95% of the time but the 5% of errors are clustered in exactly the worlds closest to the actual one.

The sensitivity condition runs into a well-known problem with logical and mathematical knowledge. Consider your belief that 2 + 2 = 4. Were 2 + 2 not to equal 4 — which is arguably incoherent, since mathematical truths hold necessarily — what would you believe? Because there is no coherent closest world where the proposition is false, the sensitivity test becomes inapplicable. This suggests sensitivity works well for empirical knowledge (perceptual beliefs, contingent testimony) but struggles with necessary truths. That limitation motivates comparing sensitivity with alternative tracking conditions: **safety** (your belief couldn't easily have been false — a subtly different modal claim) and **proper function** (your belief-forming faculties are working as they were designed to). Together, these conditions map out the space of what it might mean for a true belief to be non-accidentally connected to the facts it represents.
