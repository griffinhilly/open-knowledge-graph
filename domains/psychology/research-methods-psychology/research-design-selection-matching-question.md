---
id: research-design-selection-matching-question
title: Research Design Selection and Matching Design to Research Question
domain: psychology
course: research-methods-psychology
prerequisites:
- id: experimental-research-design
  type: soft
- id: correlational-research-design
  type: soft
- id: survey-research-methods
  type: soft
builds-toward:
- measurement-standardization-procedural-fidelity
- internal-validity-threats-experimental-control
tags:
- design
- research-questions
- design-selection
- tradeoffs
stage: formal-systems
status: validated
---

# Research Design Selection and Matching Design to Research Question

## Core Idea
Different research questions require different research designs, and no single design is universally superior; rather, designs differ in strengths regarding internal validity, external validity, practical feasibility, and cost. Experimental designs best answer questions about causation; correlational designs examine relationships and predictors; descriptive and qualitative designs explore phenomena. Researchers must consider fundamental trade-offs: experimental designs sacrifice external validity and ecological authenticity for internal validity and control; field studies gain external validity while losing control. Matching design to research question ensures the study can adequately address the question with appropriate evidence.

## How It's Best Learned
Select several different research questions and determine which design(s) would be most appropriate for each, justifying design choices based on the specific question.

## Common Misconceptions
Experimental designs are always superior to other designs (actually, experiments cannot answer all types of research questions). A poorly designed experiment is better than a well-designed correlational study (actually, design appropriateness depends on the research question).

## Questions

```yaml
- question: "A researcher wants to know whether a new mindfulness intervention reduces anxiety. Which research design is most appropriate, and why?"
  type: multiple-choice
  options:
    - "A correlational study measuring how often people meditate and their self-reported anxiety scores"
    - "A randomized controlled experiment assigning participants to mindfulness vs. control conditions"
    - "A nationally representative survey asking whether people who meditate feel less anxious"
    - "A qualitative interview study exploring participants' subjective experiences with mindfulness"
  answer: 1
  explanation: "The question asks whether the intervention *causes* reduced anxiety — a causal claim. Only a randomized experiment can establish causation, because random assignment equates the groups on everything except the treatment. A correlational study (option A) cannot rule out the possibility that less-anxious people are more likely to meditate. A survey (option C) has the same problem. Qualitative methods (option D) explore the structure of an experience but cannot test a causal hypothesis."

- question: "A researcher wants to understand the prevalence of depression among U.S. adults during economic recessions. Which design is most appropriate?"
  type: multiple-choice
  options:
    - "A randomized experiment exposing participants to simulated economic stress and measuring depression"
    - "A correlational study relating unemployment rates to depression scores in a convenience sample"
    - "A nationally representative survey measuring depression rates at multiple time points during a recession"
    - "A qualitative study interviewing a dozen unemployed workers about their mental health experiences"
  answer: 2
  explanation: "The question asks about *prevalence* — the distribution of depression in a population at a specific time. This is a descriptive question best answered by a representative survey with careful sampling. An experiment (option A) tests whether economic stress *causes* depression, which is a different question. A correlational study in a convenience sample (option B) cannot generalize to the U.S. population. A qualitative study (option D) generates depth of understanding in a small sample but cannot estimate prevalence."

- question: "Experimental designs are typically superior to correlational designs because they provide stronger causal evidence."
  type: true-false
  answer: false
  explanation: "This is the most common misconception in research methods. Design quality depends entirely on fit between design and research question. For causal questions, experiments are superior. But for questions about naturalistic relationships (e.g., how personality traits relate to job outcomes), relational prevalence (how common is depression?), or phenomena that cannot be experimentally manipulated (effects of childhood trauma, personality, neurological conditions), correlational or descriptive designs are not just adequate — they are the *only* appropriate choice. A well-designed correlational study beats a poorly designed experiment at answering a relational question."

- question: "A well-designed correlational study can provide stronger evidence for a naturalistic research question than a poorly designed experiment."
  type: true-false
  answer: true
  explanation: "Design quality and design type are independent. A correlational study with large representative samples, rigorous measurement, and appropriate statistical controls can provide robust, generalizable evidence about real-world relationships. A laboratory experiment with a non-representative sample, demand characteristics, and an artificial task may have strong internal validity but weak applicability to the phenomenon of interest. Appropriateness to the question, not the design label, determines evidential quality."

- question: "A researcher cannot ethically or practically randomly assign participants to experience childhood trauma in order to study its effects on adult mental health. What research design alternatives exist, and what validity trade-offs do they involve?"
  type: short-answer
  answer: "Alternatives include: (1) prospective longitudinal studies following children over time, measuring trauma exposure as it naturally occurs and tracking adult outcomes — this gains ecological validity but cannot control for confounders; (2) retrospective surveys asking adults to report past trauma — efficient but subject to recall bias; (3) quasi-experimental designs using natural experiments (e.g., comparing individuals who experienced a disaster to matched controls who did not) — these approximate experimental logic but cannot rule out all selection differences. All sacrifice some internal validity compared to a true experiment, trading causal certainty for ethical feasibility and naturalistic validity."
  explanation: "This question illustrates a fundamental constraint in psychological research: some of the most important questions (effects of trauma, poverty, early adversity) cannot be studied experimentally for ethical reasons. Recognizing the appropriate design given these constraints — and being transparent about the inferential limits — is the core skill in research design selection."
```

## Explainer

Your prerequisites on experimental, correlational, and survey designs each introduced a specific tool. This topic steps back to address the prior question: given a research question, how do you choose the right tool? The answer turns on two fundamental properties that every design trades off: **internal validity** — the degree to which you can attribute your findings to the variable you manipulated rather than to confounds — and **external validity** — the degree to which your findings generalize beyond the specific sample, setting, and conditions of your study.

Experimental designs maximize internal validity by randomly assigning participants to conditions and controlling all other variables. If you randomly assign people to read either fear-arousing or neutral health messages and then measure their intentions to exercise, you can confidently attribute any difference to the message content — random assignment equates the groups on everything else. But the lab setting may be artificial, your sample may be a convenience sample of undergraduates, and the measured intentions may not reflect real behavior. The tight internal control that makes the causal inference possible is often purchased at the cost of ecological realism. This isn't a flaw to apologize for — it's the correct tradeoff when your question is "does X cause Y?"

**Correlational designs** sacrifice causal claims but gain breadth and naturalism. Measuring conscientiousness and job performance in real employees at real organizations tells you something about how these variables co-occur in the world — that's external validity. But any observed correlation could reflect a third variable: maybe high-conscientiousness people also come from higher socioeconomic backgrounds that provide better jobs, and the SES is the actual driver. Correlational designs are the right choice when you want to characterize relationships in the natural world, when random assignment is impossible (you can't randomly assign people to be extroverted or to have experienced childhood trauma), or when you want to build predictive models rather than test causal theories.

**Survey and descriptive designs** are best when the research question asks "what is the distribution or prevalence of X in a population?" rather than "does X cause Y?" or "are X and Y related?" Prevalence of depression, distribution of political attitudes, frequency of health behaviors — these are answerable by surveys with careful sampling and not by experiments. Qualitative designs serve yet a different purpose: when you don't yet know what categories or variables matter, and need to discover the structure of a phenomenon before you can measure it, qualitative methods generate hypotheses rather than test them.

The practical skill is **translating a research question into design requirements**. Start by identifying the strongest form of your question: is it a causal claim, a relational claim, a prevalence claim, or an exploratory mapping? Then ask: what kind of evidence would definitively answer this question? What are the ethical and practical constraints on data collection? If a true experiment is feasible and the question is causal, run the experiment. If random assignment is impossible but causal inference is still needed, consider quasi-experimental designs with matched comparison groups. If the question is genuinely descriptive or exploratory, don't force an experimental frame onto it — you'll introduce constraints that produce artificial answers to a question nobody was asking. Good research design is the art of choosing the method that fits the question, not the method that sounds most rigorous in the abstract.
