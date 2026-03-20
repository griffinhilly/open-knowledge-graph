---
id: safety-condition-knowledge
title: The Safety Condition for Knowledge
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
- safety
- modal-conditions
- gettier
stage: advanced
status: draft
---

# The Safety Condition for Knowledge

## Core Idea
The safety condition requires that if one knows a proposition, one could not easily have believed that proposition falsely under similar circumstances. This attempts to rule out Gettier cases by imposing a modal constraint: knowledge requires that one's belief-forming method is sufficiently reliable that nearby possible worlds don't contain false instances of the same belief. Safety captures when true justified belief constitutes genuine knowledge rather than lucky guessing.

## How It's Best Learned
Apply the safety condition to Gettier cases and near-miss scenarios. For each case, determine whether the subject's belief-formation method was safe—could they easily have been wrong? Compare with sensitivity.

## Common Misconceptions
- Conflating safety with sensitivity (safety concerns possible false beliefs; sensitivity concerns whether actual belief tracks truth).
- Thinking safety requires logical impossibility of error.
- Assuming all reliable methods are safe.

## Explainer

From your study of Gettier problems, you know the central challenge: justified true belief is not sufficient for knowledge. Gettier showed that you can have all three — justification, truth, and belief — and still only be *lucky* that your belief is true. The safety condition is one of the most influential attempts to identify what's missing. It draws on the modal vocabulary you encountered in the introduction to modal logic, which talks about what could or could not easily happen in nearby possible worlds.

The **safety condition** says: S knows P only if, in nearby possible worlds where S forms the belief that P using the same method as in the actual world, S's belief is true. In other words, your belief is safe if you couldn't easily have been wrong. "Nearby" worlds are worlds that differ from the actual world only in small, easily-occurring ways — a slight change in circumstances, a small alteration in what happened a moment before. If your belief-forming method would have produced a false belief in many such nearby worlds, your belief is unsafe, and you don't have knowledge even if you happen to be right in the actual world.

Here is how safety handles the classic Gettier case of the stopped clock. You glance at a clock that reads 3:00. It is in fact 3:00, and you form the true belief that it's 3:00. But the clock stopped exactly 12 hours ago. In nearby possible worlds — say, you glance a few minutes earlier or later — the clock still reads 3:00 even though the actual time is different. Your belief-forming method (reading the stopped clock) would easily have produced a false belief. So your belief is unsafe, and you don't know the time despite having a justified true belief. Safety correctly diagnoses this as a case of knowledge failure.

Safety is often contrasted with **sensitivity**, a related modal condition associated with Nozick. Sensitivity says: if P were false, you would not believe P. Safety reverses the direction: if you were to believe P via the same method, P would be true. These sound similar but come apart in important cases. You are sensitive to your belief that you're not a brain in a vat (if you were, you'd believe it differently) but not safe (in nearby worlds where you're almost a brain in a vat, you'd falsely believe you aren't). Conversely, you can be safe about lottery propositions (your ticket almost certainly doesn't win) without being sensitive (if your ticket were the winner, you might still believe you lost). Most epistemologists now favor safety over sensitivity because safety tracks our intuitions about knowledge more reliably — it captures the idea that a knower is not just right by accident, but right in a way that is robust across the situations they might easily have found themselves in.
