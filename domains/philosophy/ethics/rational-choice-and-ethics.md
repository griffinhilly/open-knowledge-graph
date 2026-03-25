---
id: rational-choice-and-ethics
title: Rational Choice and Ethics
domain: philosophy
course: ethics
prerequisites:
- id: normative-ethics-overview
  type: hard
- id: probabilistic-reasoning
  type: soft
- id: agent-evaluation-vs-action-evaluation
  type: soft
- id: impartial-vs-partial-agents
  type: soft
- id: ought-implies-can
  type: soft
- id: care-ethics
  type: soft
builds-toward:
- preference-utilitarianism
- contractualism
tags:
- rationality
- choice
- preference
- normative-ethics
stage: formal-systems
status: validated
---
# Rational Choice and Ethics

## Core Idea
Rational choice theory analyzes decisions through preferences and utility maximization. Applied to ethics, it raises central questions: Are moral choices rational? Does rationality require morality? Can an agent prefer immoral outcomes rationally? Preference utilitarianism grounds ethics in rational preferences; contractualism justifies obligations through what rational agents would agree to. These approaches link morality to rationality, though they must address whether rational egoism can be moral.

## How It's Best Learned
Model an ethical scenario as a rational choice problem: identify agents, outcomes, preferences. How does rational choice theory evaluate the options? Where does it align with or diverge from moral intuition?

## Common Misconceptions
Assuming rationality guarantees morality. Treating preference satisfaction as the only rational goal. Confusing rational egoism with rational choice—they're not identical.

## Questions

```yaml
- question: "An investor consistently and coherently maximizes his own financial gain, caring nothing about the welfare of others affected by his decisions. Under standard rational choice theory, is this agent irrational?"
  type: multiple-choice
  options:
    - "Yes — genuine rationality requires impartial concern for all affected parties"
    - "Yes — rational agents must weigh long-term reputational costs, which include others' welfare"
    - "No — rational choice theory only requires consistent preference ordering, not any particular content of preferences"
    - "No — but only because rationality is instrumentally identical to morality in the long run"
  answer: 2
  explanation: "Rational choice theory's formal requirements are consistency (transitivity, completeness) and maximization of expected utility — not any specific content of preferences. An agent whose preferences are entirely self-regarding satisfies these requirements just as well as an altruistic one. This is the central tension: rationality, formally defined, does not entail morality. Option D describes a separate argument (that morality is instrumentally rational) — but that is a conclusion that must be argued for, not a feature of the formal framework."

- question: "According to contractualism in the Scanlonian tradition, what role does rationality play in generating moral principles?"
  type: multiple-choice
  options:
    - "Rationality requires maximizing total preference satisfaction across all agents"
    - "Rationality provides the procedure — principles are those no one could reasonably reject — even if it doesn't dictate their content"
    - "Rationality determines which outcomes are intrinsically valuable, from which moral rules are derived"
    - "Rationality is irrelevant to morality, which is grounded in sentiment rather than reason"
  answer: 1
  explanation: "For Scanlon, morality consists of principles that rational agents could not reasonably reject under conditions of fairness. Rationality here is procedural, not substantive: it governs how agreement is reached (consistency, non-arbitrariness), but the content of moral principles emerges from the outcome of the procedure. This contrasts with consequentialist approaches that use rationality to directly calculate optimal outcomes. The 'reasonable rejection' criterion is doing normative work that rationality alone cannot supply."

- question: "Preference utilitarianism and hedonic utilitarianism are equivalent because both maximize utility."
  type: true-false
  answer: false
  explanation: "Though both are consequentialist theories that maximize utility, they differ in what 'utility' means. Hedonic utilitarianism equates utility with pleasure and absence of pain — a fixed psychological measure. Preference utilitarianism equates utility with preference satisfaction — what agents actually want, regardless of whether it produces pleasure. An agent might prefer a challenging life over a comfortable one; preference utilitarianism respects that preference, while hedonic utilitarianism would favor the more pleasant life."

- question: "In rational choice theory, it is possible for an agent's utility function to assign positive weight to the welfare of others."
  type: true-false
  answer: true
  explanation: "Rational choice theory places no constraints on the content of preferences — only on their formal structure (consistency, transitivity, completeness). An agent whose utility increases when others flourish is fully accommodated by the framework. Altruism and moral concern can all be represented as preferences within a utility function. This means 'rationality requires self-interest' is false — rational egoism is one coherent position, but not the only one."

- question: "Why can't we simply derive morality from rationality using rational choice theory, even if rational agents can have other-regarding preferences?"
  type: short-answer
  answer: "Because rational choice theory permits both self-regarding and other-regarding preferences without privileging either. Rational egoism — consistently maximizing one's own interests — satisfies every formal requirement of rationality. The framework can represent moral preferences, but it cannot tell you which preferences you ought to have. To get from rationality to morality, you need an additional argument: that morality is instrumentally rational, that genuine rationality constitutively includes concern for others, or that the two normative domains must be related by a substantive philosophical argument."
  explanation: "This is the 'gap' that preference utilitarianism and contractualism attempt to bridge in different ways. Preference utilitarianism widens the utility function to include all affected parties; contractualism uses the rationality of fair agreement. Neither strategy is uncontested, which is why the relationship between rationality and morality remains a central open question in metaethics."
```

## Explainer

The connection between rationality and morality is one of the oldest puzzles in practical philosophy. You already know from normative ethics that different theories — consequentialism, deontology, virtue ethics — give different accounts of what we ought to do. Rational choice theory adds a sharper question: is there a formal framework, grounded in preference and utility, that can unify moral reasoning? The core claim is that a rational agent has a consistent ordering of preferences, and **utility** is simply a mathematical representation of those preferences. Nothing in this framework requires preferences to be selfish — an agent can rationally prefer that others flourish, that principles be honored, or that suffering be minimized.

The most direct application is **preference utilitarianism**, championed by Peter Singer. On this view, the right action is the one that best satisfies the preferences of all affected parties. This is more sophisticated than hedonic utilitarianism (maximizing pleasure) because it respects what agents actually want rather than imposing a fixed conception of well-being. Your probabilistic reasoning background is relevant here: satisfying preferences under uncertainty requires weighing outcomes by their probability, producing expected utility calculations that mirror the formal structure of decision theory. The moral question becomes a maximization problem with an unusually wide scope — your preferences count, but so does everyone else's.

**Contractualism** takes a different approach. Rather than aggregating preferences, it asks: what principles would rational agents agree to under conditions of fairness? Associated with Rawls and Scanlon, this view holds that morality consists of principles no one could reasonably reject. Rationality here is instrumental — if you want to live in a cooperative society, you must accept rules that others can also accept. The key insight is that rationality provides the *procedure* for generating moral principles, even if it doesn't directly dictate their content. What comes out of the agreement depends on what bargaining conditions you stipulate and what counts as "reasonable" rejection.

But the framework has a limit you must understand clearly. **Rational egoism** — the view that rationality requires maximizing your own preferences — is a coherent position within rational choice theory. The formal structure does not rule it out. This is the critical point: rationality and morality can come apart. An agent who consistently pursues self-interest is not irrational by the standard definition. Moral philosophy must therefore argue either that morality *is* instrumentally rational (you benefit from moral behavior in the long run through cooperation and reputation), that morality is constitutive of genuine rationality (properly understood preferences include concern for others), or that rationality and morality are simply different normative domains that don't reduce to each other. Each path has serious defenders — and serious critics — and working through them is the primary task of rational choice ethics.
