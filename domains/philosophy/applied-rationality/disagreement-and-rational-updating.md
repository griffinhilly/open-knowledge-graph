---
id: disagreement-and-rational-updating
title: "Disagreement and Rational Updating"
domain: philosophy
course: applied-rationality
prerequisites:
  - id: steelmanning
    type: hard
  - id: intellectual-humility-and-calibrated-uncertainty
    type: hard
  - id: epistemology-of-disagreement
    type: soft
tags: ["epistemics", "disagreement", "aumann", "updating", "social-epistemology"]
stage: advanced
status: draft
---

## Core Idea

Aumann's agreement theorem proves that two rational agents with common knowledge of each other's beliefs cannot agree to disagree — if they share the same priors and each knows the other's posterior, they must converge. In practice, persistent disagreement signals that at least one party has different priors, different evidence, or is reasoning incorrectly. The Rationalist approach to disagreement: take the other person's belief as evidence (their brain processed information you have not seen), update toward them proportional to your assessment of their reliability, and investigate the crux — the specific factual or inferential disagreement that drives the difference. Productive disagreement requires identifying cruxes rather than repeating arguments.

## How It's Best Learned

In your next substantive disagreement, try to identify the crux: what is the specific factual claim or inference where you and the other person diverge? State it explicitly and check whether resolving that point would change both your minds. Practice taking the other person's confidence as evidence — if a domain expert disagrees with you, how much should you update?

## Common Misconceptions

- Aumann's theorem does not mean you should always split the difference with anyone who disagrees — it applies to rational agents with common priors and common knowledge, which is rarely fully satisfied.
- Rational updating on disagreement does not mean deferring to the loudest or most confident person — it means weighting by assessed reliability and relevant expertise.

## Questions

```yaml
- question: "You estimate hypothesis H has 70% probability. A well-calibrated domain expert tells you she thinks it's 30%. Assuming you have no reason to think your evidence is superior to hers, the rational response is:"
  type: multiple-choice
  options:
    - "Stand firm at 70% — your reasoning is your own and shouldn't be overridden by another's opinion"
    - "Average the two estimates and settle on 50%"
    - "Update toward her estimate, with the degree proportional to your assessment of her reliability as a reasoner"
    - "Defer entirely to her estimate because domain expertise always outweighs personal probability assessments"
  answer: 2
  explanation: "The key insight is that her belief is evidence: her brain processed information and inferences you may not have seen. The rational response is to update toward her estimate by an amount proportional to your assessment of her reliability — not to blindly average (option B ignores differing expertise weights) and not to fully defer (option D ignores that you also have information). Refusing to update at all (option A) treats your prior probability as immune to new evidence, which is epistemically unjustified."

- question: "Aumann's agreement theorem most precisely establishes that:"
  type: multiple-choice
  options:
    - "Experts in the same field who share data will eventually converge on the same probability estimate"
    - "Two rational agents with common priors who have common knowledge of each other's posteriors cannot have different posteriors"
    - "Any two honest people who discuss a disagreement openly will eventually agree"
    - "The long-run accumulation of shared evidence will cause rational agents to converge regardless of prior differences"
  answer: 1
  explanation: "Aumann's theorem is a precise mathematical result with strict conditions: *common priors* (same prior probability distribution) and *common knowledge* of each other's posteriors (each knows the other knows the other knows… their posterior, infinitely). This is rarely fully satisfied in practice. The theorem does not say that any two communicating people will converge — it applies only to idealized rational agents meeting the technical conditions. Persistent real-world disagreement can arise from differing priors, differing evidence, or reasoning errors."

- question: "When a rational person encounters persistent disagreement from a peer, the primary reason to update their beliefs is that the peer's belief is itself evidence — it reflects information and reasoning the peer has processed."
  type: true-false
  answer: true
  explanation: "This is the core Rationalist insight about disagreement: a reasoning agent's posterior probability encodes all the information they have processed. If a peer disagrees, their brain arrived at that conclusion through some chain of evidence and inference, even if they cannot fully articulate it. Their credence is thus a signal about the world. The appropriate response is to treat it as evidence and update accordingly, not to ignore it as merely their opinion."

- question: "Rational updating on disagreement means you should update your beliefs toward whoever expresses the most confidence or argues most persistently."
  type: true-false
  answer: false
  explanation: "Rational updating weights the other person's view by their assessed reliability and relevant expertise — not by their expressed confidence or persistence. The loudest or most tenacious arguer is not necessarily better calibrated or better informed. Deferring to rhetorical force rather than epistemic track record is a form of social capitulation, not rational updating. Aumann's framework weights by the quality of the reasoning process, which is orthogonal to how confidently it is expressed."

- question: "What is a 'crux' in a disagreement, and why is identifying one more productive than repeating your main arguments?"
  type: short-answer
  answer: "A crux is the specific factual claim, inference, or value judgment that actually drives the disagreement — if it were resolved, both parties would converge on the same conclusion. Identifying it focuses the debate on the real source of divergence rather than restating downstream positions that both parties already know are in conflict."
  explanation: "Repeating arguments in a disagreement typically rehearses the conclusions each side has already reached, not the premises generating the divergence. A crux-finding approach asks: 'What would have to be true for you to update toward my view?' and 'What would have to be true for me to update toward yours?' This locates the actual factual or inferential gap, where progress is possible. Without this, debate cycles indefinitely around conclusions rather than converging on evidence."
```
