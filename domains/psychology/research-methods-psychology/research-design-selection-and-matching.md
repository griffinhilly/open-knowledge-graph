---
id: research-design-selection-and-matching
title: Selecting and Matching Research Designs to Questions
domain: psychology
course: research-methods-psychology
prerequisites:
- id: empirical-questions-and-hypothesis-development
  type: hard
- id: variable-definition-and-operational-measurement
  type: hard
builds-toward:
- true-experimental-randomized-designs
- quasi-experimental-non-randomized-designs
- correlational-and-observational-research
- qualitative-research-interview-methods
tags:
- research-design
- design-selection
- methodology
stage: formal-systems
status: draft
---

# Selecting and Matching Research Designs to Questions

## Core Idea
Different research questions require different designs. Experiments test causality through manipulation and random assignment; quasi-experiments approximate causal inference without full randomization; correlational studies examine relationships without manipulation; qualitative studies explore mechanisms and experiences. The logic of each design—what it can and cannot conclude—flows from its structure.

## How It's Best Learned
Map research questions to designs: 'Does X cause Y?' (experiment); 'Are X and Y related?' (correlational); 'How do people experience X?' (qualitative). Compare how the same question answered via different designs yields different insights.

## Common Misconceptions
- More complex designs are always better; - Experiments are the only way to understand causality; - Observational and correlational designs cannot inform theory; - Design choice is primarily about preference rather than question logic.

## Questions

```yaml
- question: "A researcher wants to test whether a new tutoring program causes improvements in student test scores. Which design feature is logically necessary — not just helpful — to support a causal conclusion?"
  type: multiple-choice
  options:
    - "A large sample size to increase statistical power"
    - "Longitudinal follow-up to track students over multiple years"
    - "Random assignment of students to tutoring versus control conditions"
    - "Measuring both tutoring attendance and test scores in every student"
  answer: 2
  explanation: "Random assignment is logically necessary for causal inference because it makes the groups equivalent before the manipulation, ruling out the possibility that pre-existing differences explain the outcome. Without it, students who received tutoring might have been more motivated or better-resourced to begin with. Large sample size improves statistical precision but does not close the confound. Longitudinal follow-up and measuring both variables are useful but do not replace randomization as the mechanism that supports causality."

- question: "A study finds that people who drink coffee daily have lower rates of Parkinson's disease. A journalist concludes that coffee prevents Parkinson's. What is the primary logical problem with this conclusion?"
  type: multiple-choice
  options:
    - "The study did not measure Parkinson's disease accurately"
    - "A third variable — such as overall lifestyle or genetic factors — might cause both higher coffee consumption and lower Parkinson's risk, explaining the correlation without any causal link"
    - "The study did not follow participants long enough to observe Parkinson's onset"
    - "The sample of coffee drinkers was probably too small to generalize"
  answer: 1
  explanation: "Correlational designs cannot rule out third-variable confounds. A lurking variable like an active lifestyle or genetic predisposition could independently predict both coffee drinking and Parkinson's risk, producing the observed correlation without any causal mechanism. The journalist's error is treating a correlational finding as causal — the study design simply cannot support that conclusion without manipulation and random assignment."

- question: "A qualitative interview study cannot contribute to scientific understanding of causal mechanisms because it produces no quantifiable data."
  type: true-false
  answer: false
  explanation: "Qualitative designs are well-suited for generating and refining causal theories by revealing the mechanisms and experiences underlying a phenomenon. While they cannot establish causation in the quantitative sense, they can surface plausible causal pathways that experiments can later test. The misconception conflates 'quantifiable' with 'scientific' — qualitative research can be rigorous, theory-informing, and essential for questions that quantitative designs would oversimplify."

- question: "The right research design is determined primarily by the logical requirements of the research question — specifically, which alternative explanations must be closed to support the intended inference."
  type: true-false
  answer: true
  explanation: "This is the core principle of design selection. A causal question requires closing third-variable confounds through manipulation and random assignment. A correlational question requires measuring both variables but not manipulating either. A phenomenological question requires rich qualitative data. The question type determines the design, not researcher preference, resource availability, or a general preference for complexity."

- question: "Why is choosing the simplest design that logically supports the inference — rather than the most sophisticated one available — the correct standard for research design selection?"
  type: short-answer
  answer: "More complex designs add cost, analytic difficulty, and ethical challenges without improving validity if they exceed what the question requires. The goal is to close the alternative explanations most relevant to the specific inference, not to close every possible alternative. A design should be matched to what the question logically demands: a correlational question does not benefit from random assignment because manipulation is not needed; a causal question cannot be answered by a correlational design regardless of its sophistication. Complexity beyond the minimum required actually reduces clarity and introduces unnecessary sources of error."
  explanation: "The key insight is that validity comes from the match between design logic and question type, not from complexity per se. Applying a randomized experiment to a 'how do people experience X?' question would suppress the rich, contextual data needed to answer it. Applying a correlational design to 'does X cause Y?' leaves confounds open that the question requires closing. The skill is identifying the minimum logical requirements of the question and selecting the simplest feasible design that meets them."
```

## Explainer

You know from your prerequisites that empirical questions are formulated with measurable variables, and that operationalization defines how those variables will be captured. But having a well-formed question and well-defined variables doesn't specify the design — it only opens the door. **Research design selection** is the process of asking: given what I want to conclude, what logical structure does the study need to support that conclusion? The answer flows from the type of question, not from preference or habit.

The key insight is that different question types have different minimum logical requirements. **"Does X cause Y?"** requires manipulation — you must assign participants to X versus not-X conditions — and random assignment, which ensures the groups are equivalent before the manipulation. Without both, you cannot rule out that some third variable explains any observed relationship. **"Are X and Y related, and how strongly?"** requires measuring both variables in the same participants but doesn't require manipulating either; correlational designs serve this question. **"How do people experience X?"** calls for rich qualitative data — open-ended interviews, narrative description — that quantitative measurement would suppress. Each design type is the right tool for its corresponding question and the wrong tool for others.

The practical skill is **ruling out alternative explanations**. When a design is selected, the question becomes: what confounds remain open? Correlational designs leave third-variable confounds open — maybe a lurking variable causes both X and Y. Experimental designs close those confounds via random assignment but cannot be used to study variables that cannot be ethically or practically manipulated (you cannot randomly assign people to poverty, abuse, or genetic conditions). Quasi-experimental designs (with a comparison group but without random assignment) partially address confounds but leave some open. Qualitative designs produce deep mechanistic understanding but not quantifiable generalizations. No design closes every alternative explanation; the task is choosing the one that closes the alternatives most relevant to the specific inference you want to draw.

**Matching design to question** also requires practical judgment: available sample size, feasibility of manipulation, time, resources, and ethical constraints. A researcher studying long-term effects of early adversity cannot run a controlled experiment; they work with longitudinal observational data, natural experiments, or quasi-experimental comparisons — the strongest design that is actually feasible. The goal is not the most sophisticated design, but the simplest design that logically supports the intended inference given real-world constraints. Applying a more complex design than necessary doesn't improve validity; it adds cost and analytic complexity without corresponding gain. Starting from the question, identifying what it requires logically, and then working within constraints is the sequence that leads to well-matched designs.
