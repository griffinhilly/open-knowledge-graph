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
stage: formal-systems
status: validated
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

## Questions

```yaml
- question: "Anna glances at a clock that reads 3:00. It is actually 3:00, but the clock stopped exactly 12 hours ago. Does Anna know it is 3:00, according to the safety condition?"
  type: multiple-choice
  options:
    - "Yes — she has a justified true belief, and the safety condition only adds that the method must be reliable in general, which clocks usually are"
    - "Yes — she is right, and the safety condition only requires that she couldn't have been wrong given exactly these circumstances"
    - "No — in nearby possible worlds (she glances slightly earlier or later), her clock-reading method produces a false belief, so her belief is unsafe"
    - "No — the safety condition requires logical certainty, and it is logically possible the clock stopped recently"
  answer: 2
  explanation: "The safety condition asks whether Anna could *easily* have been wrong — whether there are nearby possible worlds where her same belief-forming method (reading this clock) yields a false belief. There are: if she glanced a minute earlier or later, the clock would still read 3:00 but the actual time would be different. Her belief is unsafe, so safety correctly withholds the status of knowledge. Option A is the classical JTB analysis that Gettier showed to be insufficient; option D confuses safety with infallibilism."

- question: "Consider a fair lottery with one million tickets. You hold ticket #452,891 and have not yet heard the results. You believe 'my ticket will lose.' Is this belief safe, according to the safety condition?"
  type: multiple-choice
  options:
    - "No — if your ticket were the winner, you would still believe it will lose, so you are sensitive but not safe"
    - "Yes — in nearly all nearby possible worlds you do lose, so your belief is true in nearly all nearby worlds where you form it"
    - "No — safety requires that you couldn't be wrong even in slightly different circumstances, and there exists a circumstance (your ticket winning) where you would be wrong"
    - "Yes — but only because lotteries are randomly determined, which makes nearby worlds all equally probable"
  answer: 1
  explanation: "Safety asks: in nearby worlds where you form this belief by the same method, is it true? 'Nearby' means small changes — you still hold ticket #452,891, the draw hasn't happened yet. In the vast majority of nearby worlds, your ticket does lose (probability 999,999/1,000,000). So your belief is safe. Note that safety and sensitivity come apart here: sensitivity asks 'if my ticket were the winner, would I still believe I'll lose?' — and the answer is yes, making the belief *insensitive*. This case illustrates why safety and sensitivity are distinct modal conditions."

- question: "The safety condition is sensitive to the specific belief-forming method used, not just to whether the resulting belief happens to be true."
  type: true-false
  answer: true
  explanation: "Safety evaluates whether the method could easily produce a false belief in nearby worlds. Two people can form the same true belief 'It is 3:00' — one by reading a working clock, one by reading a stopped clock — and only the first has a safe belief because the methods differ in their reliability across nearby worlds. A belief can be accidentally true (like reading the stopped clock at exactly the right moment) but still unsafe, because the method would easily mislead in nearby circumstances. This is precisely why safety improves on the simple JTB account."

- question: "The safety condition and the sensitivity condition give identical verdicts on whether a belief constitutes knowledge, since both are modal conditions relating belief and truth."
  type: true-false
  answer: false
  explanation: "Safety and sensitivity are both modal conditions but in different directions, and they come apart in important cases. Sensitivity says: if P were false, you wouldn't believe P. Safety says: if you believe P via this method, P is true in nearby worlds. Lottery beliefs are safe (you almost certainly will lose) but insensitive (if you were the winner, you'd still believe you'd lose). Brain-in-vat beliefs are insensitive (if you were a brain in a vat, you'd still believe you have hands) but safe (in nearly all nearby worlds you are not in a vat). Most epistemologists favor safety for tracking knowledge intuitions more reliably."

- question: "Explain how the safety condition handles a standard Gettier case, and why this represents an improvement over the classical justified true belief analysis."
  type: short-answer
  answer: "In a Gettier case — like reading a stopped clock that coincidentally displays the correct time — the subject has a justified true belief but lacks knowledge because the truth is accidental. The JTB analysis cannot explain this: all three conditions are satisfied. Safety explains it: the belief-forming method (reading a stopped clock) would easily produce a false belief in nearby worlds (one minute earlier or later, the clock still reads 3:00 but the actual time is wrong). The belief is unsafe — the subject 'got lucky' in the actual world, but luck is precisely what safety rules out. A belief counts as knowledge only if the method that produced it is reliably truth-tracking in nearby circumstances, not just accidentally true in this one."
  explanation: "The safety condition essentially says: you know P only if your being right about P is not a matter of luck in the relevant sense. Gettier cases are paradigm cases of epistemic luck — you are right, but you could very easily have been wrong using the very same method. Safety captures this by looking at nearby possible worlds and asking whether the method is reliable there. The JTB analysis has no modal component and so cannot distinguish knowledge from lucky true belief."
```

## Explainer

From your study of Gettier problems, you know the central challenge: justified true belief is not sufficient for knowledge. Gettier showed that you can have all three — justification, truth, and belief — and still only be *lucky* that your belief is true. The safety condition is one of the most influential attempts to identify what's missing. It draws on the modal vocabulary you encountered in the introduction to modal logic, which talks about what could or could not easily happen in nearby possible worlds.

The **safety condition** says: S knows P only if, in nearby possible worlds where S forms the belief that P using the same method as in the actual world, S's belief is true. In other words, your belief is safe if you couldn't easily have been wrong. "Nearby" worlds are worlds that differ from the actual world only in small, easily-occurring ways — a slight change in circumstances, a small alteration in what happened a moment before. If your belief-forming method would have produced a false belief in many such nearby worlds, your belief is unsafe, and you don't have knowledge even if you happen to be right in the actual world.

Here is how safety handles the classic Gettier case of the stopped clock. You glance at a clock that reads 3:00. It is in fact 3:00, and you form the true belief that it's 3:00. But the clock stopped exactly 12 hours ago. In nearby possible worlds — say, you glance a few minutes earlier or later — the clock still reads 3:00 even though the actual time is different. Your belief-forming method (reading the stopped clock) would easily have produced a false belief. So your belief is unsafe, and you don't know the time despite having a justified true belief. Safety correctly diagnoses this as a case of knowledge failure.

Safety is often contrasted with **sensitivity**, a related modal condition associated with Nozick. Sensitivity says: if P were false, you would not believe P. Safety reverses the direction: if you were to believe P via the same method, P would be true. These sound similar but come apart in important cases. You are sensitive to your belief that you're not a brain in a vat (if you were, you'd believe it differently) but not safe (in nearby worlds where you're almost a brain in a vat, you'd falsely believe you aren't). Conversely, you can be safe about lottery propositions (your ticket almost certainly doesn't win) without being sensitive (if your ticket were the winner, you might still believe you lost). Most epistemologists now favor safety over sensitivity because safety tracks our intuitions about knowledge more reliably — it captures the idea that a knower is not just right by accident, but right in a way that is robust across the situations they might easily have found themselves in.
