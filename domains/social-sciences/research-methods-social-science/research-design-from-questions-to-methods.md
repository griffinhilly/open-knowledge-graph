---
id: research-design-from-questions-to-methods
title: 'Research Design: From Questions to Methods'
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: philosophy-of-social-science-epistemology
  type: hard
builds-toward:
- operationalization-construct-validity
- validity-construct-internal-external
tags:
- research-design
- planning
- logic
stage: expert
status: draft
---

# Research Design: From Questions to Methods

## Core Idea
Sound research design bridges theory and evidence by specifying research questions, hypotheses, populations, and methods. Strong designs anticipate validity threats and clarify how data collection and analysis answer the research question. Design choices made early constrain and enable later analytic options.

## Questions

```yaml
- question: "A researcher collects data on police presence and crime rates across 50 cities, then decides — after observing a correlation — to frame the project as a causal study of whether police reduce crime. What is the primary design problem?"
  type: multiple-choice
  options:
    - "50 cities is too small a sample for any statistical analysis of this kind"
    - "The design was not structured to support causal inference; confounders and reverse causality cannot be ruled out post hoc"
    - "City-level analysis is always invalid because cities are too heterogeneous to compare"
    - "The researcher should have used a survey instrument rather than observational administrative data"
  answer: 1
  explanation: "The core problem is that causal inference requires a data structure designed to rule out alternative explanations — confounders, reverse causality, selection bias. Rich cities may have both more police and less crime for unrelated reasons (confounding); high-crime cities may hire more police in response (reverse causality). A design capable of supporting causal claims must anticipate these threats before data collection — through random assignment, instrumental variables, difference-in-differences, etc. Retrofitting a causal claim onto an observational dataset collected without those features is not a design flaw in the data; it is a fundamental mismatch between the inferential goal and the data structure."

- question: "A hypothesis is formulated after the researcher has already examined the data and observed the pattern it predicts. Why is this a methodological problem?"
  type: multiple-choice
  options:
    - "It violates the assumption of random sampling required for statistical inference"
    - "It commits the researcher to a conclusion before the analysis is complete, biasing interpretation"
    - "It is not falsifiable — the hypothesis was constructed to fit the data already observed, so no data could disconfirm it"
    - "It is always causally invalid because no experiment was conducted to test the prediction"
  answer: 2
  explanation: "A hypothesis must specify in advance what evidence would disconfirm it — that is what makes it a hypothesis rather than a post-hoc story. When a hypothesis is formulated after observing the data it 'predicts,' it cannot be disconfirmed by that data, because it was designed to fit it. This is HARKing (Hypothesizing After Results are Known) and produces apparent confirmation that is actually circular. The methodological requirement is that hypotheses commit you before collection to what counts as disconfirming evidence — which is only possible if they precede the data."

- question: "A randomized controlled experiment that carefully eliminates confounders automatically produces results that generalize to real-world populations and settings."
  type: true-false
  answer: false
  explanation: "Internal validity (the degree to which the design supports causal claims within the study) and external validity (the degree to which findings generalize beyond the study) are distinct and often in tension. A highly controlled laboratory experiment may eliminate confounders effectively (high internal validity) while using an unrepresentative sample, artificial conditions, or a constrained intervention that does not resemble real-world implementation (low external validity). Randomization addresses internal validity threats; generalizability requires deliberate attention to sampling, setting, and population representativeness."

- question: "The choice between qualitative and quantitative methods should be guided primarily by the researcher's epistemological commitments and the nature of the research question, not by convention or disciplinary default."
  type: true-false
  answer: true
  explanation: "Method choice flows from epistemology and research question. A researcher who wants to estimate a causal effect of a policy needs a design capable of causal inference — surveys and quantitative modeling. A researcher who wants to understand how participants construct meaning around an event needs interpretive depth — interviews, ethnography, discourse analysis. Using qualitative methods because 'that's what my field does' without asking whether they can answer the research question produces studies that are methodologically consistent but inferentially hollow."

- question: "What does it mean to 'work backward from your inferential goal' in research design, and why must this analysis happen before data collection rather than after?"
  type: short-answer
  answer: "Working backward means starting from the conclusion you want to be able to draw — for example, a causal claim that X causes Y — and then identifying what data structure would actually license that inference. For a causal claim, that typically means asking: what assignment mechanism (random, natural experiment, instrumental variable) would isolate the effect of X? What comparison group is needed? What measurements at what time points? You then design data collection to produce that structure. This must happen before collection because the inferential power of a study is determined by how data are collected, not by how they are analyzed afterward. You cannot add random assignment, create a comparison group, or introduce an instrument retroactively — those features must be built in from the start."
  explanation: "The discipline of working backward prevents the common error of designing convenient data collection and then asking what can be inferred from it. The question 'what data would let me answer this?' is more productive than 'what can I do with data I have?' The former leads to strong designs; the latter often leads to overstated conclusions from under-powered data structures."
```

## Explainer

From your study of the philosophy of social science and epistemology, you understand that there are deep disagreements about what counts as knowledge, how causal claims can be justified, and what the appropriate relationship is between theory and evidence. Research design is where those epistemological commitments become methodological choices. A positivist believes that social phenomena can be measured objectively and that causal relationships can be estimated from data; they tend toward surveys, experiments, and quantitative models. An interpretive researcher believes that social meaning is constructed and that understanding requires grasping actors' perspectives from the inside; they tend toward interviews, ethnography, and discourse analysis. Your design must be coherent with your epistemological stance — a mismatch produces studies that answer a different question than intended.

The starting point is a well-formed **research question**. A useful research question has three properties: it is specific enough to be answerable (not "why is inequality bad?" but "does income inequality increase political polarization?"), it is empirically tractable (there exists evidence that could bear on it), and it is non-obvious (if the answer is already known, you're doing description, not research). From the research question, you derive **hypotheses** — specific, falsifiable predictions about what you expect to find and why. Hypotheses do two things: they focus data collection, and they commit you in advance to what would count as disconfirming evidence. A hypothesis stated after seeing the data is not a hypothesis — it is a post-hoc story.

The next step is specifying the **population** and **unit of analysis**. Who or what are you studying? If you're studying whether police presence reduces crime, is your unit a city, a neighborhood, a precinct, a time-period? The answer shapes everything: what data you need, what comparisons make sense, and to whom your findings can be generalized. This is the question of **external validity** — whether your findings travel beyond your specific sample and setting. It is easy to get a clean, technically rigorous result that answers your question for a narrow population with no obvious relevance elsewhere. External validity requires deliberate design, not accidental luck.

Equally important is **internal validity** — whether your design supports the causal claim you want to make. If you observe that cities with more police have less crime, does that mean police reduce crime, or that rich cities (which have both) drive the relationship? Threats to internal validity include **confounding** (unmeasured third variables that cause both X and Y), **reverse causality** (Y causing X), and **selection bias** (non-random sorting into conditions). Strong designs anticipate these threats and build in defenses: random assignment eliminates many confounders; difference-in-differences designs control for stable unmeasured confounders; instrumental variables address reverse causality. No design eliminates all threats, but strong designs name the threats explicitly and argue why residual concerns are manageable.

The key insight — that design choices made early constrain analytic options later — means that the time to think about analysis is before data collection, not after. If you want to estimate a causal effect, you need to design the study so that causal estimation is possible. You cannot randomize after the fact. You cannot add a comparison group after collecting only treatment data. The discipline of research design is the discipline of working backward from your inferential goal to the data structure required to support it, and then asking whether you can actually collect that data.


