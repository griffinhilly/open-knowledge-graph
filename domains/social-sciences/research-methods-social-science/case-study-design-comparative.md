---
id: case-study-design-comparative
title: Case Study Design and Comparative Methods
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: research-design-advanced
  type: soft
- id: process-tracing-comparative
  type: soft
builds-toward:
- qualitative-comparative-analysis
- natural-experiments-design
tags:
- case-study
- comparative
- bounded-system
- within-case-analysis
stage: advanced
status: validated
---
# Case Study Design and Comparative Methods

## Core Idea
Examines case studies as research strategy and analysis method, covering instrumental, intrinsic, and collective designs. Develops within-case and cross-case analytic strategies, addresses case selection and comparison logic, and explores how case studies enable causal process tracing and generalization.

## How It's Best Learned
Design a multi-case study with explicit comparison logic, conduct within-case analysis with causal process tracing, write cross-case comparative findings.

## Common Misconceptions
- Case studies cannot test theories
- You cannot generalize from cases
- Comparing two cases is not comparative method

## Questions

```yaml
- question: "A researcher studying why revolutions succeed selects only five countries where a successful revolution occurred and compares them to identify common causal conditions. What fundamental design problem does this create?"
  type: multiple-choice
  options:
    - "Five cases is too small a sample for any meaningful comparison"
    - "Selecting only cases where the outcome occurred prevents the researcher from assessing what distinguishes success from failure"
    - "Revolutions cannot be studied with case study methods because they are politically sensitive"
    - "The researcher should use surveys to study revolutions instead of case studies"
  answer: 1
  explanation: "This is selecting on the dependent variable — one of the most fundamental errors in case study design. When all selected cases share the outcome (revolution succeeds), the researcher cannot determine which causal conditions are genuinely responsible versus which are merely common background features that also appear in cases where the revolution failed. A sound comparative design requires variation in the outcome: cases where revolution succeeded AND cases where it failed, allowing the researcher to identify what distinguishes them. Even with a small N, that comparison is possible; without it, the design cannot support causal inference."

- question: "A researcher uses a single well-documented case to test whether a specific causal mechanism predicted by a theory actually operated in the way the theory describes. Which statement best characterizes the logic of this inference?"
  type: multiple-choice
  options:
    - "This is statistical generalization: the case represents the broader population of similar situations"
    - "This is analytical generalization: the case provides evidence about whether a theoretical proposition holds, not about a population"
    - "Single-case studies cannot support any form of generalization and should only be used for description"
    - "The inference is valid only if the researcher has studied at least 50 cases using process tracing"
  answer: 1
  explanation: "Analytical generalization extends findings to a theory, not to a population. Statistical generalization — the kind a survey supports — requires a representative sample and allows claims about population prevalence. Case studies do something different: they test whether a proposed causal mechanism operates under specified conditions. A single case that rigorously traces the mechanism's operation (or absence) is analogous to a single well-designed experiment — it doesn't prove the law but it tests a theoretical proposition. The misconception that case studies 'can't generalize' conflates these two logically distinct forms of inference."

- question: "Process tracing within a single case can test causal claims by documenting intermediate steps and mechanisms between a cause and an outcome."
  type: true-false
  answer: true
  explanation: "Process tracing is the methodological workhorse of within-case analysis. Rather than just observing that variable A precedes outcome B, the researcher follows the chain of events, actors, and mechanisms connecting them — asking whether each predicted intermediate step actually occurred and whether an alternative explanation could account for the same sequence. A causal account that predicts three intermediate steps, all of which are documented, is substantially confirmed; an alternative that predicts a different sequence of steps that are absent is disconfirmed. This is stronger causal evidence than correlation alone, even from one case."

- question: "An intrinsic case study design is better suited for theory testing than an instrumental case study design, because intrinsic studies examine the case in greater depth."
  type: true-false
  answer: false
  explanation: "The distinction between intrinsic and instrumental is about purpose, not depth. An intrinsic case study examines the case because the case itself is inherently interesting — the goal is understanding this specific instance, not building or testing broader theory. An instrumental case study uses the case as a vehicle to illuminate a theoretical question; the case is selected because it can shed light on something beyond itself. Theory testing requires instrumental logic — the case is chosen because it allows a theoretical proposition to be examined, confirmed, or disconfirmed. Intrinsic studies are not better suited for this; they are designed for a different purpose."

- question: "What is the logical difference between a most-similar and a most-different case design, and when should each be used?"
  type: short-answer
  answer: "A most-similar case design selects cases that are alike on many background conditions but differ on the key causal variable and outcome — holding context constant to isolate the causal variable's effect (analogous to controlled comparison). A most-different case design selects cases that vary widely on background conditions but share the key causal variable and outcome — demonstrating that the causal relationship holds across diverse contexts. Most-similar designs are suited for testing whether a specific cause produces an outcome by minimizing confounds. Most-different designs are suited for demonstrating robustness: if the same cause-outcome relationship appears despite very different contexts, the relationship is more likely to be genuine and not an artifact of a specific background condition."
  explanation: "Case selection strategy is not arbitrary — it follows from the researcher's inferential goal. A researcher who wants to isolate the effect of a single variable should maximize similarity on everything else. A researcher who wants to show that a finding is not parochial should maximize contextual diversity while preserving the key causal relationship. Deviant cases (those that don't fit an established pattern) serve yet another purpose: they can expose the limits or boundary conditions of a theory by showing where the predicted mechanism fails to operate."
```

## Explainer

A **case study** is not simply a detailed description of one instance — it is a research strategy built around the logic of a bounded system. You already know from advanced research design that the choice of design should be driven by your research question. Case studies are best suited to questions that ask "how" or "why" something happened in a specific context, and where the boundary between phenomenon and context is not cleanly separable. A country, an organization, a policy episode, or a social movement can each constitute a case, but only when you have defined what makes it a coherent unit of analysis with meaningful boundaries.

The most important distinction in case study design is between **intrinsic**, **instrumental**, and **collective** designs. An intrinsic case study examines a case because the case itself is inherently interesting — you want to understand this specific school, this specific conflict. An instrumental case study uses the case as a vehicle to illuminate a broader theoretical question — the particular case is selected because it will shed light on something beyond itself. Collective designs extend this by examining multiple cases together, comparing them to build or test theory. Most scholarly case studies are instrumental: the case is a means, not an end.

**Within-case analysis** and **cross-case analysis** are the two analytical moves available to you. Within a single case, you use **causal process tracing** — following the chain of events, mechanisms, and conditions that connect a cause to an outcome. This is analogous to watching dominoes fall: you are not just correlating the first tile and the last, but documenting each intermediate step and asking whether an alternative explanation could account for the observed sequence. Process tracing can confirm or disconfirm a causal account in ways that correlational analysis cannot. When you have multiple cases, cross-case analysis compares patterns — looking for what cases that share an outcome also share in their causal conditions, and what cases with different outcomes differ in.

**Case selection** is where comparative logic becomes most powerful and most fraught. Selecting on the dependent variable — choosing only cases where the outcome occurred — is a design error that prevents you from assessing what conditions lead to different outcomes. Strategic designs include most-similar cases (holding many conditions constant while varying the key cause), most-different cases (varying many background conditions while sharing the key cause and outcome), and deviant cases (cases that don't fit a general pattern, which are analytically valuable precisely because they are anomalous). Each selection strategy is appropriate for different inferential goals.

The misconception that case studies cannot test theories or support generalization confuses statistical generalization with **analytical generalization**. You do not generalize from a case to a population the way a survey would; you generalize to a theory. If your theory predicts that a specific mechanism will operate under certain conditions, a single well-chosen case that either confirms or disconfirms the predicted mechanism is evidence. Robert Yin's framing is useful here: think of case studies as analogous to experiments — a single experiment does not prove a law, but it can decisively test a theoretical proposition when designed correctly. The strength of case study inference comes from the depth and rigor of within-case analysis, not from a large N.
