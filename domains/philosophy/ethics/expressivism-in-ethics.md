---
id: expressivism-in-ethics
title: Expressivism in Ethics
domain: philosophy
course: ethics
prerequisites:
- id: metaethics-intro
  type: hard
- id: moral-realism
  type: soft
- id: moral-relativism
  type: soft
- id: moral-non-cognitivism
  type: soft
- id: expressivism-and-noncognitivism
  type: soft
builds-toward:
- error-theory
tags:
- metaethics
- non-cognitivism
- expressivism
- emotivism
stage: formal-systems
status: validated
---
# Expressivism in Ethics

## Core Idea
Expressivism holds that moral utterances do not express beliefs or state facts, but rather express non-cognitive mental states such as emotions, attitudes, or prescriptions. Early emotivism (Ayer, Stevenson) said 'murder is wrong' means roughly 'boo to murder.' More sophisticated versions, such as Blackburn's quasi-realism and Gibbard's norm-expressivism, try to explain how moral discourse can mimic truth-apt language without positing moral facts. Expressivism faces the Frege–Geach problem: if moral terms in assertions are non-descriptive, what do they contribute when embedded in conditionals ('if lying is wrong, then getting children to lie is wrong')?

## Questions

```yaml
- question: "A committed emotivist is confronted with the argument: (1) Lying is wrong. (2) Getting your children to lie is getting them to do something wrong. (3) Therefore, getting your children to lie is wrong. Which response best captures the problem this argument creates for emotivism?"
  type: multiple-choice
  options:
    - "The argument is invalid because the conclusion does not follow from the premises"
    - "'Lying is wrong' in premise 1 expresses an attitude, but in premise 2 it appears inside a conditional where no attitude is being expressed — emotivism cannot explain this consistency of meaning"
    - "Emotivism accepts this argument because expressing disapproval of lying implies disapproval of teaching children to lie"
    - "The problem is that premise 2 is not a moral statement and should not appear in a moral argument"
  answer: 1
  explanation: "This is the Frege-Geach problem. For an argument to be logically valid, the same term must mean the same thing in every premise. If 'lying is wrong' in premise 1 expresses an emotion (not a proposition), then it cannot function as a premise — emotions don't have truth values and can't be combined logically. But in premise 2, 'wrong' appears inside a conditional where no emotion is being expressed. Emotivism has no account of what 'wrong' contributes in that embedded position, which seems to require it to have a stable descriptive meaning that emotivism denies it has."

- question: "According to expressivism, what is someone doing when they say 'Torturing animals for fun is wrong'?"
  type: multiple-choice
  options:
    - "Stating a fact about the objective moral property of wrongness that the action instantiates"
    - "Reporting their own psychological state of feeling disgusted by animal torture"
    - "Expressing a non-cognitive attitude of disapproval toward animal torture, not stating a fact"
    - "Issuing a legal prohibition that carries normative force within their community"
  answer: 2
  explanation: "Expressivism holds that moral utterances express non-cognitive attitudes (approval, disapproval, norms) rather than stating facts — either about the world (moral realism's view) or about the speaker's psychology (option B). The difference between B and C is crucial: option B is a form of subjectivism (moral sentences report inner states), which makes them factual claims that can be true or false. Expressivism denies even this — moral sentences do not report anything; they express, like 'hooray!' or 'boo!'. The sentence has no truth conditions in the standard sense."

- question: "According to expressivism, moral disagreements are fundamentally disputes about facts — specifically, facts about which attitudes are objectively correct."
  type: true-false
  answer: false
  explanation: "Expressivism specifically rejects this. If moral sentences express attitudes rather than state facts, moral disagreements are contests between opposing attitudes, not disputes about who has the correct factual belief. Two people who disagree about whether capital punishment is wrong are, on the expressivist view, expressing conflicting attitudes toward capital punishment — not asserting incompatible propositions about a moral reality. This is one of expressivism's attractive features for those skeptical of moral facts: it explains why moral disagreements feel so persistent and heated (they involve deep attitude differences) without positing disputed moral facts."

- question: "The Frege-Geach problem arises because moral terms embedded in conditionals and logical arguments appear to require stable, proposition-like meaning that early emotivism cannot provide."
  type: true-false
  answer: true
  explanation: "This is precisely the problem. Valid logical arguments require that terms mean the same thing in every position — in assertions and in embedded clauses. If 'wrong' in 'lying is wrong' just means 'boo, lying!', then 'wrong' in 'if lying is wrong, then X' cannot be expressing an attitude (you are not booing lying when you say 'if'). The term needs a constant semantic contribution across both uses, but emotivism's account of moral terms as attitude expressions provides no such stable content. Quasi-realism and norm-expressivism are attempts to solve exactly this problem."

- question: "Explain the Frege-Geach problem in your own words. What does it challenge expressivists to explain?"
  type: short-answer
  answer: "The Frege-Geach problem points out that moral terms appear inside logical structures — conditionals, arguments, inferences — where they cannot be expressing attitudes. If 'lying is wrong' just expresses disapproval of lying, then in the conditional 'if lying is wrong, then teaching children to lie is wrong,' the antecedent is not expressing disapproval; it is serving as a hypothetical premise. But for the argument to be logically valid, 'lying is wrong' must mean the same thing in both positions. Expressivism challenges: what stable meaning do moral terms have that makes them function consistently across assertoric and embedded contexts?"
  explanation: "The Frege-Geach problem is often considered the most serious objection to simple emotivism, which is why it motivated the development of more sophisticated positions like Blackburn's quasi-realism and Gibbard's norm-expressivism. Both try to show that expressivist language can mimic the logical behavior of truth-apt language without positing moral facts — but whether they fully succeed remains contested."
```

## Explainer

From your introduction to metaethics, you know the central divide: moral realism holds that moral sentences express beliefs about mind-independent moral facts, while **non-cognitivism** holds that moral sentences do something other than state facts. Expressivism is the most developed non-cognitivist position, and its central claim is deceptively simple: when you say "cruelty is wrong," you are not describing the world — you are expressing an attitude of disapproval toward cruelty. On this view, moral language is more like saying "boo to cruelty!" than like saying "cruelty causes suffering." No moral facts are needed, no moral perception faculty is required, and no difficult metaphysics about the nature of goodness is necessary.

Early **emotivism** (A.J. Ayer in *Language, Truth and Logic*, 1936; C.L. Stevenson in *Ethics and Language*, 1944) made this claim in its bluntest form: moral utterances are expressions of emotion and attempts to influence others' emotions, with no descriptive content at all. This position has obvious appeal for anyone attracted to a scientifically austere worldview — it eliminates mysterious moral facts while explaining why moral disagreement feels so persistent and heated (we are expressing and contesting attitudes, not discovering facts). But it faces an immediate objection: we do not *talk* as though we are merely venting emotions. We argue, reason, change our minds, call each other right and wrong, and use moral terms inside complex logical structures. If "lying is wrong" just means "boo, lying!", what does it mean embedded in a conditional?

This is the **Frege-Geach problem**, named for philosopher Peter Geach (building on Frege's logic). Consider the valid argument: (1) Lying is wrong. (2) Getting your children to lie is getting them to do something wrong. (3) Therefore, getting your children to lie is wrong. This looks logically valid. But if "lying is wrong" in premise 1 just expresses an attitude (rather than asserting a proposition), it cannot serve as a premise in a logical argument — the same expression in premise 2 appears inside a conditional, where no emotion is being expressed. The logical structure requires that "lying is wrong" mean the *same thing* in both positions, but emotivism has no account of what that constant meaning could be.

Simon Blackburn's **quasi-realism** and Allan Gibbard's **norm-expressivism** are sophisticated responses to this problem. Blackburn argues that we can "earn the right" to talk as if there are moral facts — including using truth-apt language, making inferences, and claiming objectivity — without actually positing moral facts. We project our attitudes onto the world and then regulate them through social norms of rational coherence, producing discourse that mimics factual language. Gibbard analyzes moral judgments as expressions of *norms* for governing action and reactive attitudes: to say an act is wrong is to express acceptance of norms that forbid it. Both approaches try to show that the logical and epistemic features of moral discourse (inference, revision, testimony, disagreement) can be explained in purely expressivist terms, without invoking moral facts. Whether they fully succeed — whether quasi-realism "earns the right" to moral truth-talk without quietly smuggling in realism — remains the central contested question in contemporary metaethics.
