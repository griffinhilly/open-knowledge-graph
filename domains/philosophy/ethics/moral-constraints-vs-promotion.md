---
id: moral-constraints-vs-promotion
title: Moral Constraints vs Promotion
domain: philosophy
course: ethics
prerequisites:
- id: normative-ethics-overview
  type: hard
builds-toward:
- deontological-ethics
- consequentialism
- double-effect-doctrine
tags:
- normative-ethics
- constraints
- promotion
- structure
stage: abstract-reasoning
status: validated
---

# Moral Constraints vs Promotion

## Core Idea
Some ethical theories emphasize constraints—prohibitions against violating rights, using people as mere means, or harming innocents—while others emphasize promotion of good outcomes, virtues, or flourishing. Constraint-based theories restrict what we may do even to achieve good; promotion-based theories require maximizing value. This structural choice affects how to handle conflicts: a constraint prevents torturing innocents; a promotion framework might permit it to prevent greater harm.

## Questions

```yaml
- question: "A runaway trolley will kill five people unless diverted onto a side track where it will kill one person. According to a strict consequentialist promotion framework, what should a bystander with access to the lever do?"
  type: multiple-choice
  options:
    - "Not pull the lever — using a person as a means to save others is prohibited regardless of the numbers"
    - "Pull the lever — the outcome (one death instead of five) is better, and promotion requires bringing about the best available outcome"
    - "Not pull the lever — actively causing harm is always worse than allowing it to happen"
    - "Pull the lever only if the person on the side track would consent to being sacrificed"
  answer: 1
  explanation: "Pure consequentialist promotion views require the action that produces the best outcome. Five deaths are worse than one death, so pulling the lever produces the better outcome and is therefore not just permitted but obligatory. There are no absolute prohibitions on a strict promotion view — only better and worse outcomes. Option A reflects a constraint view, not a promotion view. Option C also reflects a constraint or agent-causation view. The trolley problem was designed to isolate exactly this structural difference."

- question: "According to a strict constraint-based framework, why might it be impermissible to torture one innocent person to prevent the torture of ten others?"
  type: multiple-choice
  options:
    - "Because the suffering of ten people is actually less severe in aggregate than one intense case of torture"
    - "Because the constraint against torturing an innocent person is agent-relative — it prohibits you from committing that act regardless of what others will do or what the net outcome is"
    - "Because consequentialist arithmetic is too unreliable to justify rights violations"
    - "Because you cannot know with sufficient certainty that torturing one will prevent the torture of ten"
  answer: 1
  explanation: "Agent-relative constraints focus on what *you* do, not on aggregate outcomes. The prohibition is against *you* being the agent of torture — it does not depend on what others might do or on the net number of tortures in the world. This is Nozick's 'side constraint' concept: the moral barrier is not a factor in a calculation but a limit on what kinds of actions you may take. A pure promoter would run the numbers and act; a constraint theorist says 'there are things I may not do, regardless of what good it would produce.'"

- question: "A promotion-based ethical framework permits some actions that a constraint-based framework prohibits, but never requires them — those actions remain merely optional on a promotion view."
  type: true-false
  answer: false
  explanation: "Pure promotion frameworks not only permit harm-causing actions when they maximize good outcomes — they *require* them. If redirecting the trolley produces the best outcome, a strict consequentialist is obligated to do it, not merely permitted to. On a pure promotion view, there are no supererogatory acts (doing more than morality demands) — only optimal actions and suboptimal ones. This is one of the most challenging features of strict consequentialism: it eliminates the category of 'going beyond what duty requires.'"

- question: "Moral constraints are agent-relative: the prohibition is against you taking a certain action, not simply against that action happening in the world."
  type: true-false
  answer: true
  explanation: "This is the defining structural feature of agent-relative constraints. It is prohibited for *me* to push the trolley victim, even if my doing so would prevent five identical pushings by others. The prohibition attaches to my agency, not to the outcome-state. This is why constraint views resist the 'numbers game': five unjust killings are worse than one in aggregate, but the constraint against me committing the one still holds. Promotion views, by contrast, care about outcomes in the world regardless of who causes them."

- question: "Explain the difference between a moral constraint and a moral consideration that can be outweighed by consequences. Why does this distinction matter for cases like trolley problems?"
  type: short-answer
  answer: "A moral consideration that can be outweighed by consequences is just a factor in the overall calculation — it counts against an action but can be overridden when consequences are good enough. A moral constraint, by contrast, is a side constraint that limits which actions are available regardless of consequences. The constraint doesn't figure in the calculation at all; it removes certain actions from the menu. This distinction matters for trolley problems because promotion views treat 'killing one' as a serious consideration that five deaths can outweigh, while constraint views treat 'killing one' as prohibited regardless of the count — making the two views reach opposite verdicts using the same factual description."
  explanation: "The practical difference: if killing one person to save five is just a very weighty consideration, then there will always be some number of people saved that makes it permissible. If it is a true constraint, no number of lives saved can make it permissible (or only a catastrophic threshold can override it, and only as a tragic exception). Trolley problems are useful precisely because they strip away uncertainty and enforce a clean choice, isolating whether the ethical structure is calculative (promotion) or limiting (constraint)."
```

## Explainer

Your prerequisite work on normative ethics introduced the landscape of ethical theories — consequentialism, deontology, virtue ethics, and others. The distinction between **moral constraints** and **moral promotion** cuts across these theories and identifies a fundamental structural choice every ethical framework must make: does morality tell you what you may not do, or what you must bring about?

A **promotion** framework says that morality is fundamentally about making the world better. You have an ongoing obligation to increase good outcomes — more welfare, more justice, more flourishing. Consequentialism is the clearest example: the right action is always the one that produces the best consequences. There are no actions that are prohibited *no matter what* on a pure promotion view; everything depends on what will produce the most good. If torturing one person prevents the torture of ten others, a strict promoter must say you should do it. The moral demand is open-ended: you are always obligated to do whatever maximizes value.

A **constraint** framework says that morality places limits on what you may do, regardless of outcomes. Some actions are prohibited — not because they usually lead to bad results, but because they violate a constraint that holds unconditionally or near-unconditionally. **Agent-relative constraints** are prohibitions on *you* taking certain actions, even when doing so would prevent more of the same bad thing from happening. The classic example: you may not push one person in front of a runaway trolley to save five, even though five deaths are worse than one. The constraint is against *you* killing the one person; it does not track net deaths. This structure is central to deontological ethics and to ordinary moral intuitions about rights.

The practical difference is sharpest in **dilemmas involving numbers**. Promotion views straightforwardly permit — and often require — violating individual welfare when the aggregate calculation favors it. Constraint views resist this: a right is a kind of fence around a person that cannot be crossed for aggregate benefit. Robert Nozick's phrase for why rights constrain rather than merely figure in a calculus is that they are **side constraints** — limits on action, not factors to be traded off. The moral landscape on a constraint view is not a surface to be maximized but a terrain full of barriers. This does not mean constraints can never be overridden — most deontologists allow that constraints can be **thresholds** beyond which catastrophic consequences override them. But the burden of justification is high and the override is described as a moral tragedy, not a clean calculation.

Understanding this distinction helps you map the internal debates within utilitarianism (act vs rule utilitarianism is partly a debate about whether rules can function as genuine constraints), interpret trolley problems (they are specifically designed to isolate the constraint structure by varying whether you are the agent of harm), and understand the debate about moral rights (whether rights are best understood as side constraints or as very weighty considerations that generally but not always override). The underlying question is one of moral architecture: is morality a goal-directed project of making things as good as possible, or is it a system of prohibitions and permissions that defines what kinds of agency are permissible, independent of what they produce?
