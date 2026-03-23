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
status: validated
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

## Questions

```yaml
- question: "You believe it is 3:00 PM because you glanced at a clock that happens to be stopped at 3:00. The time really is 3:00 PM. Is your belief sensitive?"
  type: multiple-choice
  options:
    - "Yes — the belief is true and the clock gave the right answer, so it tracks the truth"
    - "No — if it were not 3:00 PM, the stopped clock would still read 3:00, and you would still believe it is 3:00 PM"
    - "Yes — sensitivity only requires that your belief-forming method is reliable over time"
    - "No — because you have no independent justification for trusting the clock"
  answer: 1
  explanation: "The sensitivity test asks: if P were false, would you still believe P? If it were not 3:00 PM, the stopped clock would still display 3:00, and you would still form the belief that it is 3:00 PM. Your belief does not track the truth — it would not vary with reality. This is the classic Gettier-adjacent case that the sensitivity condition is designed to capture. Option A confuses being accidentally right (which happened) with tracking the truth (which requires counterfactual covariance). Option C conflates sensitivity (a modal/subjunctive condition) with reliability (a statistical condition)."

- question: "What distinguishes sensitivity from reliability as conditions on knowledge?"
  type: multiple-choice
  options:
    - "Sensitivity requires true belief; reliability does not"
    - "Sensitivity asks about what you would believe in the closest possible world where P is false; reliability asks how often your belief-forming method produces true beliefs across many cases"
    - "Sensitivity is a necessary condition for knowledge; reliability is only sufficient"
    - "Sensitivity applies to perceptual beliefs; reliability applies to testimonial beliefs"
  answer: 1
  explanation: "Sensitivity is a modal/counterfactual condition: it concerns a specific nearby possible world — the closest world where P is false — and asks whether you would believe P there. Reliability is a statistical claim about the track record of a belief-forming method across many actual or possible cases. A belief-forming method can be statistically reliable (right 95% of the time) yet insensitive if the 5% of errors are concentrated in the worlds closest to the actual one — that is, the belief fails precisely when it is most at risk of failing. These are orthogonal properties."

- question: "A belief can be statistically reliable — produced by a method that is correct 95% of the time — and yet fail the sensitivity condition."
  type: true-false
  answer: true
  explanation: "Sensitivity is not about frequency of success but about whether your belief would covary with reality in the nearest possible world where reality is different. A stopped clock that happens to be right twice a day is reliable in a trivial sense (it is right twice daily) but completely insensitive (it would display the same time even if the time were different). More seriously: a clairvoyant who is usually right might still form beliefs that would not change if the facts changed, failing sensitivity despite high reliability. The two conditions measure different things."

- question: "The sensitivity condition applies straightforwardly to mathematical knowledge, such as the belief that 2 + 2 = 4."
  type: true-false
  answer: false
  explanation: "Mathematical truths are necessarily true — there is no coherent possible world in which 2 + 2 ≠ 4. The sensitivity condition asks: 'If P were false, would you still believe P?' But if P is necessarily true, there is no 'closest world where P is false' to evaluate. The counterfactual has a necessarily false antecedent, making it vacuously true or inapplicable. This is a well-known limitation of the sensitivity condition: it works naturally for contingent empirical knowledge but struggles with necessary truths, motivating alternative conditions like safety that handle this case more gracefully."

- question: "Explain why the stopped-clock belief fails the sensitivity condition, using the counterfactual formulation. What does this show about the relationship between accidental truth and genuine knowledge?"
  type: short-answer
  answer: "The sensitivity condition requires: if P were false, S would not believe P. For the stopped-clock belief: if it were not 3:00 PM, the clock would still show 3:00, and the believer would still form the belief that it is 3:00 PM. The belief would not vary with the facts — it is decoupled from reality. This shows that being accidentally right (true belief by coincidence) is insufficient for knowledge: genuine knowledge requires the belief to track the truth, i.e., to be counterfactually responsive to whether P is actually true. The sensitivity condition captures this 'tracking' requirement."
  explanation: "This is precisely the kind of case Nozick's sensitivity condition was designed to exclude. Gettier cases generally involve beliefs that are true 'by accident' — where the justification and the truth are accidentally aligned. Sensitivity gives a precise modal criterion for what it means to be non-accidentally true: your belief-forming mechanism must be sensitive to the fact in question, so that if the fact changed, your belief would change with it."
```

## Explainer

You already understand Gettier cases: situations where you have justified true belief but intuitively lack knowledge, because your belief is true "by accident." Various responses have attempted to add conditions that rule out such accidents. The sensitivity condition, developed most influentially by Robert Nozick, approaches this by asking a counterfactual question: **would you still believe it if it were false?**

The formulation uses a **subjunctive conditional**: S's belief that P is *sensitive* if and only if, were P false, S would not believe P. This tests whether your belief tracks the truth — whether your belief-forming mechanism is genuinely responsive to how things actually are. Consider a simple case: you see your cat on the mat and believe the cat is there. If the cat were not on the mat, you would look, see no cat, and not believe it. Your belief tracks the truth. Now contrast a Gettier-style case: you correctly believe it is 3:00 PM because you glance at a stopped clock that happens to read 3:00. If it were not 3:00 PM, the clock would still read 3:00, and you would still believe it is 3:00 PM. Your belief does not track the truth — it fails the sensitivity condition.

Your background in modal logic is directly relevant here. The sensitivity condition checks what happens in the **closest possible world** where P is false — the scenario minimally different from ours where the proposition doesn't hold. This is fundamentally different from asking about reliability across many actual cases (a statistical question). Sensitivity is a modal claim: it asks about what you *would* believe in a nearby counterfactual scenario. A belief can be statistically reliable and yet insensitive — if, for example, you're right 95% of the time but the 5% of errors are clustered in exactly the worlds closest to the actual one.

The sensitivity condition runs into a well-known problem with logical and mathematical knowledge. Consider your belief that 2 + 2 = 4. Were 2 + 2 not to equal 4 — which is arguably incoherent, since mathematical truths hold necessarily — what would you believe? Because there is no coherent closest world where the proposition is false, the sensitivity test becomes inapplicable. This suggests sensitivity works well for empirical knowledge (perceptual beliefs, contingent testimony) but struggles with necessary truths. That limitation motivates comparing sensitivity with alternative tracking conditions: **safety** (your belief couldn't easily have been false — a subtly different modal claim) and **proper function** (your belief-forming faculties are working as they were designed to). Together, these conditions map out the space of what it might mean for a true belief to be non-accidentally connected to the facts it represents.
