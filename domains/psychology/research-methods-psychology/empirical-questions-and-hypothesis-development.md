---
id: empirical-questions-and-hypothesis-development
title: Formulating Empirical Questions and Hypotheses
domain: psychology
course: research-methods-psychology
prerequisites:
- id: scientific-inquiry-empirical-cycles-psychology
  type: hard
builds-toward:
- variable-definition-and-operational-measurement
- research-design-selection-and-matching
tags:
- hypotheses
- research-questions
- testability
stage: formal-systems
status: validated
---

# Formulating Empirical Questions and Hypotheses

## Core Idea
Empirical questions are answerable through systematic observation or experiment; hypotheses are specific, testable predictions. Strong hypotheses specify predicted relationships between variables, are grounded in theory or prior evidence, and can be rejected by data. The difference between directional (one-tailed) and nondirectional (two-tailed) hypotheses has implications for statistical testing and study design.

## How It's Best Learned
Take broad interests (e.g., 'Does social media affect mood?') and iteratively refine into testable hypotheses. Practice stating hypotheses in 'If-then' form. Review published hypotheses and evaluate their clarity and testability.

## Common Misconceptions
- A hypothesis is just a guess; - Hypotheses must always be directional; - Questions are the same as hypotheses; - A hypothesis can never be fully proven true.

## Questions

```yaml
- question: "A researcher states: 'I hypothesize that stress affects sleep quality.' Why does this fail as a scientific hypothesis?"
  type: multiple-choice
  options:
    - "It uses the word 'hypothesize' incorrectly, which should only appear in formal academic writing"
    - "It does not specify the direction of the expected relationship, the measurable variables, or the mechanism linking stress to sleep"
    - "It is too broad to be tested in a single study and would need to be split into sub-hypotheses"
    - "Stress and sleep are correlated variables and cannot be tested experimentally for causal relationships"
  answer: 1
  explanation: "A well-formed hypothesis does three things this statement does not: (1) specifies direction (does more stress lead to worse sleep?), (2) names variables precisely enough to be measured (what is 'stress'? what is 'sleep quality'?), and (3) grounds the prediction in a mechanism (why would stress affect sleep?). 'Stress affects sleep quality' is a research question — it states what the researcher wants to know. A hypothesis commits to a specific, falsifiable prediction."

- question: "Which of the following is NOT falsifiable, and therefore fails as a scientific hypothesis?"
  type: multiple-choice
  options:
    - "Sleep-deprived participants will recall fewer words on a 20-item list than well-rested controls"
    - "Students who study in a quiet environment will score higher on exams than those in noisy environments"
    - "Human behavior is sometimes influenced by unconscious mental processes"
    - "Participants who receive CBT treatment will show a 10% greater reduction in anxiety scores than control participants"
  answer: 2
  explanation: "Option C is not falsifiable because 'sometimes' provides an escape from any disconfirming evidence. Any single observed instance of unconscious influence confirms it; no amount of evidence showing deliberate behavior could refute it, because the claim only requires the phenomenon to occur 'sometimes.' A falsifiable hypothesis must specify conditions under which data would contradict it. Options A, B, and D all predict specific, measurable effects — data showing the opposite would directly refute each of them."

- question: "A directional (one-tailed) hypothesis is always preferable to a nondirectional one because it provides more statistical power."
  type: true-false
  answer: false
  explanation: "Directional hypotheses are only appropriate when theory and prior evidence strongly support a specific direction. While it's true that a one-tailed test concentrates statistical power in one direction, using a directional hypothesis when the evidence doesn't warrant it introduces bias: you are predicting a direction for convenience or publication reasons rather than because theory demands it. The choice should be driven by the state of evidence, not statistical advantage. Using directional hypotheses simply for more power is a form of researcher bias baked in before data collection."

- question: "A hypothesis is only as falsifiable as its variables are precisely defined and measurable."
  type: true-false
  answer: true
  explanation: "Falsifiability requires specifying what would count as evidence against the hypothesis — and you cannot do that without knowing what you're measuring. If 'stress' is undefined, any measurement could be dismissed as not capturing the 'real' stress the hypothesis was about. Precise operational definitions convert a vague claim into a specific prediction that can be contradicted by data. This is why operational definitions and hypothesis quality are inseparable: vague constructs permit endless reinterpretation that evades falsification."

- question: "What distinguishes a research question from a well-formed hypothesis, and why does the distinction matter for empirical research?"
  type: short-answer
  answer: "A research question asks what you want to know ('Does social media use affect adolescent mood?'). A well-formed hypothesis is a specific, falsifiable prediction about what you expect to find and why — specifying direction, measurable variables, and a grounding mechanism. The distinction matters because only a hypothesis is testable in the scientific sense: it specifies what data would confirm or contradict it. A research question merely frames a curiosity; a hypothesis converts that curiosity into a commitment — and therefore into something that can be wrong. Being wrong is exactly what science requires, because that is how theories are tested and refined."
  explanation: "The key criterion is falsifiability: a hypothesis must stick its neck out far enough that data could come back and cut it off. Research questions don't do this. A question can be answered by any finding; a hypothesis is confirmed or refuted by specific outcomes. This is why hypothesis formulation is the gateway to the rest of the empirical research process."
```

## Explainer

From the empirical cycle, you know that science advances through iteration: observations raise questions, questions generate hypotheses, hypotheses generate predictions, predictions are tested, and results feed back into theory. The current skill is about one specific step — forming good hypotheses — which turns out to require considerably more precision than everyday language suggests. The difference between a vague curiosity and a testable hypothesis is the difference between something interesting and something scientifically useful.

A **research question** and a **hypothesis** are not the same thing. A research question states what you want to know: "Does social media use affect adolescent mood?" A hypothesis is a specific, directional prediction about what you expect to find and why: "Adolescents who spend more than three hours per day on social media will report lower mood scores than those who spend less than one hour, because passive consumption produces upward social comparison." The hypothesis does three things the question does not: it specifies the direction of the expected relationship, names the variables precisely enough to be measured, and grounds the prediction in a mechanism (upward social comparison) derived from prior theory. A hypothesis that cannot say *why* it predicts what it predicts is not well-grounded — it's a guess dressed up as a hypothesis.

The key quality criterion is **falsifiability**: a hypothesis must be stated in a form where specific data could contradict it. "People sometimes behave irrationally" is not falsifiable, because you would never specify what counts as evidence against it — any single example of irrational behavior confirms it, and no amount of rational behavior disproves it. "Sleep-deprived participants will recall fewer words on a 20-item list than control participants" is falsifiable: you operationalize "sleep-deprived," measure "words recalled," and the data can come back showing controls performed worse, or no difference — either would contradict the hypothesis. Falsifiability is why operational definitions are so tightly linked to hypothesis quality. A hypothesis is only as falsifiable as its variables are precisely defined.

The **directional versus nondirectional** distinction has real consequences for statistical analysis. A directional (one-tailed) hypothesis commits to the sign of the expected effect: "sleep-deprived will do *worse*, not better." This allows you to concentrate statistical power in one tail of the distribution, making it easier to detect an effect in the predicted direction. A nondirectional (two-tailed) hypothesis predicts only a difference without specifying direction. The choice should be determined by the strength of your prior evidence, not convenience: directional hypotheses are only appropriate when theory and prior results strongly support a specific direction. If you predict a direction because it's the only direction that would be publishable, not because the evidence warrants it, that is a form of bias baked in before data collection — which is exactly why preregistration (the next topic) exists to prevent it.
