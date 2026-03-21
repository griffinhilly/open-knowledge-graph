---
id: reflective-equilibrium-method
title: Reflective Equilibrium
domain: philosophy
course: ethics
prerequisites:
- id: moral-reasoning-methods
  type: hard
- id: logical-consistency-and-contradiction
  type: soft
tags:
- epistemology
- methodology
- coherence
- justification
stage: formal-systems
status: draft
---

# Reflective Equilibrium

## Core Idea
Reflective equilibrium is a method for ethical justification: revise and adjust moral judgments, principles, and background theory until they cohere into a stable, mutually supporting set. Unlike foundationalism (grounding ethics in basic intuitions) or simple coherentism (all beliefs must cohere), reflective equilibrium allows modification at any level to achieve fit. This models how moral thinking actually works—we shuttle between particular convictions and general theories, adjusting each in light of the other.

## Questions

```yaml
- question: "A philosopher applies a utilitarian principle and derives the conclusion that harvesting one person's organs without consent to save five is morally required. According to reflective equilibrium, what is the appropriate response?"
  type: multiple-choice
  options:
    - "Accept the conclusion — the principle was applied correctly, so the conclusion must be right"
    - "Reject the principle entirely and abandon utilitarian reasoning"
    - "Treat the monstrous conclusion as evidence against at least one premise, and revise the principle or background theory rather than accepting the conclusion"
    - "Suspend judgment — reflective equilibrium says we cannot adjudicate between principle and intuition"
  answer: 2
  explanation: "This is 'tollensing the ponens': when an argument leads to a conclusion that seems clearly monstrous, reflective equilibrium treats the strongly counterintuitive conclusion as evidence that something in the argument chain is wrong. Rather than accepting the conclusion because the logic is valid, you run the argument in reverse — the strong intuition that non-consensual organ harvesting is wrong becomes a premise that refutes or revises the utilitarian principle. Reflective equilibrium permits revision at any level; the intuition has evidential weight, not just the principle."

- question: "What distinguishes wide reflective equilibrium from narrow reflective equilibrium?"
  type: multiple-choice
  options:
    - "Wide RE applies to more people; narrow RE applies only to the individual philosopher"
    - "Wide RE incorporates background theories about the nature of morality, metaethics, and human psychology as a third level of adjustment; narrow RE only seeks coherence between particular judgments and moral principles"
    - "Wide RE requires more time; narrow RE can be done quickly"
    - "Wide RE starts from principles; narrow RE starts from intuitions"
  answer: 1
  explanation: "Narrow RE seeks coherence between two levels: considered moral judgments (intuitions about particular cases) and moral principles. Wide RE adds a third level: background theories about the nature and purpose of morality, metaethical commitments, empirical facts about human psychology, and broader philosophical commitments. Wide RE is more ambitious — it doesn't just ask 'do my moral beliefs cohere?' but 'does my entire moral worldview, including its metaethical foundations, hang together?' Rawls used wide RE to derive his principles of justice."

- question: "Reflective equilibrium is a foundationalist approach to moral epistemology because it treats considered moral judgments as the basic, unrevokable foundation from which all principles must be derived."
  type: true-false
  answer: false
  explanation: "Reflective equilibrium is a coherentist approach, not a foundationalist one. Foundationalism holds that some beliefs are basic and immune to revision — all other beliefs are justified by deriving from these foundations. RE explicitly rejects this: revision can happen at any level. Considered judgments can be revised in light of principles; principles can be revised in light of judgments; background theories can be revised in light of both. No level is foundational or unrevokable. This is precisely what distinguishes RE from simple intuitionism, which treats intuitions as basic and authoritative."

- question: "In reflective equilibrium, moral intuitions can sometimes be revised in light of moral principles, rather than always adjusting principles to fit intuitions."
  type: true-false
  answer: true
  explanation: "This is a crucial feature of RE that distinguishes it from pure intuitionism. The method allows revision in either direction: if a principle seems well-grounded and an intuition seems parochial, culturally contingent, or based on bias, the intuition can be revised. Historical moral progress often looks like this — widespread intuitions about who deserves moral consideration have been revised upward through moral argument. RE is iterative and bidirectional; the goal is a stable coherence across levels, achieved through mutual adjustment, not one-way accommodation."

- question: "What problem does 'tollensing the ponens' solve within reflective equilibrium, and why can't pure principle-application handle it?"
  type: short-answer
  answer: "'Tollensing the ponens' handles the problem of arguments with valid form but monstrous conclusions. Pure principle-application runs arguments forward: if the premises are true and the logic is valid, accept the conclusion. But sometimes this produces conclusions that seem clearly wrong — conclusions strong enough that we are more confident they are wrong than we are confident in the premises. Reflective equilibrium treats the strong intuition against the conclusion as evidence against one of the premises, allowing us to run the argument backwards: 'not-C, and P2, therefore not-P1.' Pure deductivism has no mechanism for this — it cannot let the conclusion's wrongness count against the premises."
  explanation: "This capacity is what makes reflective equilibrium a realistic model of moral reasoning rather than a formal machine. Moral knowledge doesn't come from infallible axioms applied mechanically; it comes from building coherence across multiple levels, each of which has some evidential weight. When a valid argument produces a conclusion we are overwhelmingly confident is wrong, that confidence is data — and RE gives us a principled way to use it. The iterative, bidirectional character of RE is not a weakness but a feature that matches how careful moral thinking actually operates."
```

## Explainer

Think about how you already reason morally. You have **considered judgments** — strong, relatively confident intuitions about particular cases: torturing children for fun is wrong, keeping a promise matters, saving five lives is better than saving one. You also have moral principles that generalize across cases: maximize welfare, respect persons as ends, treat like cases alike. Reflective equilibrium is the method of making these two levels cohere. When they conflict, you face a choice: revise the principle to fit the intuition, revise the intuition in light of the principle, or revise both toward a stable middle ground.

The method comes in two strengths. **Narrow reflective equilibrium** just seeks coherence between your particular judgments and your general principles — no outside theory required. **Wide reflective equilibrium** brings in a third level: background theories about the nature of morality, the purpose of moral reasoning, facts about human psychology, and metaethical commitments. Wide equilibrium is harder to achieve but more philosophically ambitious: it doesn't just ask "do my moral beliefs cohere?" but "does my whole moral worldview hang together?"

From your prerequisite work in moral reasoning methods, you know that both intuitionism (just trust strong intuitions) and pure theorizing (just apply the principle mechanically) have problems. Reflective equilibrium is a response to both failures. Pure intuitionism leaves you with no way to adjudicate between conflicting intuitions or extend your judgments to new cases. Pure principle-application can produce monstrous conclusions from seemingly plausible premises — the classic problem of **tollensing the ponens**: when an argument leads to a conclusion that seems clearly wrong, the right move is often to reject a premise rather than accept the conclusion.

The process is iterative, not algorithmic. Rawls, who developed the method most systematically, used it to derive the principles of justice: he started from considered judgments (slavery is wrong, fair procedures matter), extracted principles that would generate those judgments, checked them against other cases, revised, and repeated until reaching stable principles. The stability is not mere consistency — it requires coherence across levels and robustness against counterexamples. The method concedes that moral knowledge is not derived from unshakeable foundations but built up through disciplined mutual adjustment. This is what makes it a coherentist rather than foundationalist approach to moral epistemology.
