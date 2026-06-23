---
id: consequentialism
title: Consequentialism
domain: philosophy
course: ethics
prerequisites:
- id: metaethics-intro
  type: soft
- id: argument-structure
  type: hard
- id: agent-centered-vs-patient-centered-ethics
  type: soft
- id: consequences-in-moral-evaluation
  type: hard
- id: intrinsic-vs-extrinsic-value
  type: soft
- id: moral-constraints-vs-promotion
  type: soft
- id: normative-ethics-overview
  type: soft
builds-toward:
- utilitarianism
- act-vs-rule-utilitarianism
- trolley-problem
- applied-ethics-intro
tags:
- normative-ethics
- consequentialism
- outcomes
- welfare
stage: formal-systems
status: validated
---
# Consequentialism

## Core Idea
Consequentialism is the family of normative ethical theories holding that the moral rightness of an action is determined entirely by its consequences. What matters morally is the state of the world an action brings about—its effects on well-being, preference satisfaction, knowledge, or other valued outcomes. Different versions disagree about what counts as a good outcome (hedonism, preference satisfaction, objective list theories) and whose outcomes count (all sentient beings, all persons, only those affected). Consequentialism faces objections about integrity, rights violations, and demandingness: it can appear to justify sacrificing individuals for aggregate gain.

## How It's Best Learned
Work through classic cases: does it justify lying to save lives? Sacrificing one to save five? Contrast consequentialist answers with deontological and virtue-based answers. Reading Mill's Utilitarianism and then Bernard Williams's critique in Utilitarianism: For and Against is a productive pairing.

## Common Misconceptions
- Consequentialism does not necessarily mean 'the ends justify the means' in a naive way; sophisticated versions incorporate rules or constraints that tend to maximize good outcomes.
- Not all consequentialists are hedonists; some focus on preferences, capabilities, or objective goods.

## Questions

```yaml
- question: "A surgeon has five patients who will die without organ transplants and one perfectly healthy patient whose organs would save all five. What would a strict act-consequentialist analysis conclude?"
  type: multiple-choice
  options:
    - "Forbid harvesting the organs — individual rights cannot be overridden regardless of outcome"
    - "Permit or require harvesting the organs, since five lives saved outweighs one life lost"
    - "Abstain from judgment — consequentialism applies only to voluntary actions, not medical decisions"
    - "Permit it only if the healthy patient consents or is otherwise less socially valuable"
  answer: 1
  explanation: "This is the classic 'transplant problem.' If the right action is determined entirely by outcomes and five lives > one life, strict act-consequentialism follows the arithmetic: harvest the organs. Most people's strong intuition that this is wrong — that killing an innocent person for aggregate benefit violates something important — is precisely what Bernard Williams used to argue against bare act-consequentialism via the integrity objection. The question tests whether students understand that consequentialism genuinely follows its logic, not intuition."

- question: "A consequentialist argues that keeping promises is generally morally required. Which of the following best explains the consequentialist basis for this claim?"
  type: multiple-choice
  options:
    - "Promises are intrinsically binding — breaking them is wrong regardless of outcome"
    - "Keeping promises tends to produce better outcomes overall by sustaining trust and social cooperation"
    - "Consequentialism forbids promise-breaking because it violates a universal moral duty"
    - "A strict act-consequentialist must evaluate each promise individually; no general claim about promises is possible"
  answer: 1
  explanation: "Option D is actually correct for act-consequentialism — each promise is evaluated case-by-case. But rule-consequentialists argue that adopting the rule 'keep promises' maximizes good outcomes because trust and cooperation are highly valuable. This shows how consequentialism can ground familiar moral rules — but justifies them by outcomes, not by intrinsic rightness. This also illustrates the common misconception that consequentialism cannot generate stable moral rules."

- question: "According to consequentialism, lying can be morally required if it produces better consequences than telling the truth."
  type: true-false
  answer: true
  explanation: "This directly tests the core consequentialist claim: moral evaluation belongs to outcomes, not to intrinsic features of acts. The explainer states: 'Lying is not intrinsically wrong; it is wrong when and because it produces bad consequences... When lying would save lives, that same act becomes permissible or even required.' No act is categorically forbidden — rightness or wrongness is always contingent on the actual consequences in the specific situation."

- question: "'The ends justify the means' is an accurate and complete summary of consequentialist reasoning."
  type: true-false
  answer: false
  explanation: "The Common Misconceptions section explicitly addresses this. While naive act-consequentialism might seem to license any means for good ends, sophisticated versions — rule-consequentialism, indirect consequentialism — incorporate constraints and rules precisely because following them tends to produce better outcomes than case-by-case calculation. Additionally, 'the ends justify the means' ignores the rich disagreement about what counts as a good end (hedonism vs. preference satisfaction vs. objective list theories). The slogan oversimplifies a family of nuanced theories."

- question: "What is Bernard Williams's 'integrity' objection to consequentialism, and why does it challenge the theory at its core?"
  type: short-answer
  answer: "Williams argued that consequentialism erases the morally significant distinction between what you do and what you merely allow — it treats your causal contribution to an outcome as equivalent to anyone else's. This requires agents to perform acts violating their deepest moral commitments whenever aggregate arithmetic demands it, destroying the agent's integrity. It challenges consequentialism at its core because it suggests the theory's defining feature — evaluating acts solely by outcomes — fails to capture something essential about moral agency: that there is a difference between being an agent and being an instrument."
  explanation: "Williams's critique is not just squeamishness. It's that consequentialism turns the moral agent into a mere calculator for outcome production, with no special relationship to their own actions. You have no more reason to refrain from killing one to save five than you have to prevent a stranger from doing so — which conflicts with deep intuitions about personal responsibility. This is why the trolley problem's two versions (divert vs. push) feel morally different even with identical arithmetic."
```

## Explainer

You have studied argument structure — the ability to identify premises, inferences, and conclusions — and have some background in metaethics. **Consequentialism** is the moral theory that applies the most straightforward-seeming logic to ethics: the right action is the one that produces the best outcome. What makes it a family of theories rather than a single theory is that "best outcome" can be defined in many ways — and reasonable consequentialists disagree about both what counts as good and whose good counts.

The foundational claim is that **moral evaluation belongs to outcomes, not to intrinsic features of acts**. Lying is not intrinsically wrong; it is wrong when and because it produces bad consequences — harm, distrust, diminished well-being. When lying would save lives, that same act becomes permissible or even required. This is the move that distinguishes consequentialism from **deontological** theories, which hold that some acts (lying, killing an innocent person) are wrong regardless of outcomes. For a consequentialist, no act is categorically forbidden — only acts that reliably produce bad outcomes are prohibited, and that prohibition is contingent on the facts, not absolute.

The most historically influential consequentialist theory is **utilitarianism** (Mill, Bentham), which defines the good in terms of well-being or happiness and holds that we should maximize the total or average happiness of all affected parties. But consequentialism is broader: some versions value **preference satisfaction** (what people want, not just what feels good), others adopt **objective list theories** (knowledge, friendship, and achievement are good independently of whether they are wanted or felt as pleasant), and some extend moral consideration to all sentient beings, not just persons. The choice among these accounts matters practically: a hedonistic utilitarian might endorse policies that a preference-satisfaction consequentialist would reject, because the two accounts can come apart in real cases.

The most serious objections concern consequentialism's apparent willingness to violate individual rights for aggregate gain. The **trolley problem** tests your intuitions here: most people accept diverting a trolley to kill one rather than five (apparently consequentialist), but fewer accept pushing a large man off a bridge to stop it (same arithmetic, more visceral). Bernard Williams argued that consequentialism violates **integrity**: it treats your own causal contribution to an outcome as morally equivalent to another person's, erasing the morally significant distinction between what you do and what you merely allow. Sophisticated consequentialists — **rule consequentialists**, **indirect consequentialists** — respond by arguing that adopting rules that protect rights tends to produce better outcomes than case-by-case calculation, so rights-respecting behavior is itself consequentially justified. This is the live debate: is a rights-respecting consequentialism still genuinely consequentialist, or has it imported deontological constraints through the back door?
