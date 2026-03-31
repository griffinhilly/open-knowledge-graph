---
id: field-experiments
title: Field Experiments
domain: economics
course: behavioral-economics
prerequisites:
- id: experimental-economics-methods
  type: hard
tags:
- field-experiments
- RCT
- natural-experiments
- external-validity
stage: advanced
status: validated
---

# Field Experiments

## Core Idea
Field experiments are randomized controlled trials conducted in real-world settings with real participants making real decisions with real consequences. They address the primary limitation of laboratory experiments — external validity — by testing whether behavioral patterns observed in the lab persist in natural environments with experienced agents, actual stakes, and genuine institutional contexts. Pioneered in economics by researchers like John List, Esther Duflo, and Michael Kremer, field experiments have become the gold standard for evaluating policy interventions in development economics, education, health, and behavioral public policy. The 2019 Nobel Prize was awarded to Banerjee, Duflo, and Kremer for their experimental approach to alleviating global poverty.

## Questions

```yaml
- question: "A key advantage of field experiments over laboratory experiments is that..."
  type: multiple-choice
  options:
    - "They always have larger sample sizes"
    - "They test behavior in natural settings with real participants and stakes, increasing confidence that findings generalize beyond the laboratory"
    - "They eliminate the need for randomization"
    - "They are cheaper and easier to implement"
  answer: 1
  explanation: "The central advantage is external validity — behavior in real markets, workplaces, or policy contexts may differ from behavior in an artificial laboratory. Field experiments test whether lab findings hold when participants are experienced, stakes are genuine, and the institutional environment is complex. However, field experiments sacrifice some internal validity (less control over confounding variables) and are typically more expensive and logistically challenging than lab experiments — they are not easier to implement."

- question: "List's field experiments on the endowment effect found that the WTA-WTP gap disappears for experienced market traders, challenging the universal applicability of the laboratory finding."
  type: true-false
  answer: true
  explanation: "List (2003) conducted experiments at a sports card trading show and found that experienced traders showed no endowment effect — their WTA and WTP were approximately equal — while inexperienced traders showed the standard gap. This suggests that market experience can eliminate the endowment effect, possibly through learning, professional norms, or evolved decision rules for exchange goods. The finding illustrates the value of field experiments: a robust laboratory finding may have important boundary conditions that only appear in natural settings."

- question: "What are the main ethical and practical challenges of conducting field experiments in economics?"
  type: short-answer
  answer: "Ethical challenges include: randomization creates unequal treatment (some receive a beneficial intervention, others do not), informed consent may be difficult when participants are unaware they are in an experiment, and withholding effective treatments from control groups raises welfare concerns. Practical challenges include: maintaining randomization integrity in complex real-world settings, preventing spillover effects between treatment and control groups, ensuring adequate sample size, managing logistical complexity, and measuring outcomes accurately in uncontrolled environments."
  explanation: "The ethical tension is acute in development economics: if a program is believed to help, randomly denying it to a control group raises objections. Researchers address this through stepped-wedge designs (all groups eventually receive treatment), waitlist controls, and comparisons to 'business as usual' rather than active deprivation. The practical challenges explain why field experiments are expensive and time-consuming — a randomized evaluation of a microfinance program may require years of data collection, cooperation from governments and NGOs, and careful monitoring for implementation fidelity."
```

## Explainer

Laboratory experiments excel at internal validity — controlling everything except the variable of interest — but they raise a persistent question: does behavior in a university lab with student participants playing for modest stakes tell us anything about behavior in real markets with experienced agents and consequential outcomes? Field experiments answer this question by taking the randomized experiment out of the lab and into the world.

The taxonomy of field experiments distinguishes several types. "Artefactual" field experiments use standard lab protocols but with non-student participant pools (e.g., CEO's instead of undergraduates). "Framed" field experiments use a task that mimics a naturally occurring context. "Natural" field experiments occur in the normal decision environment of the subjects, who may not know they are in an experiment. The distinction matters because each level adds realism at the cost of control. A natural field experiment testing the effect of a charitable giving strategy (Karlan and List's work on matching donations) captures real donor behavior, real stakes, and real institutional context, but the researcher has less control over confounding factors than in a lab.

In development economics, randomized controlled trials have transformed how poverty interventions are evaluated. Before the experimental revolution, development policy was often guided by theoretical arguments, case studies, or cross-country correlations — methods that could not reliably identify causal effects. Duflo, Banerjee, and Kremer pioneered the application of RCTs to questions like: Do bed nets reduce malaria? Does microfinance reduce poverty? Does deworming improve school attendance? Their approach yielded precise, credible answers — sometimes confirming conventional wisdom (bed nets work), sometimes overturning it (microfinance effects on poverty are smaller than hoped).

In behavioral economics specifically, field experiments have tested whether lab findings survive contact with reality. List's work on the endowment effect showed that market experience attenuates or eliminates the WTA-WTP gap — a finding that would never emerge in a lab populated by inexperienced undergraduates. Gneezy and List's field experiment on gift exchange found that paying workers above-market wages increased effort temporarily but the effect dissipated within hours — a result weaker than lab findings had suggested. These findings do not invalidate the underlying behavioral phenomena but they calibrate effect sizes and identify boundary conditions that determine real-world relevance.

The policy applications of field experiments in behavioral economics have been transformative. Testing nudge-style interventions — default effects in retirement savings, social norm messages in tax compliance, simplified enrollment forms for social programs — in randomized field settings provides the causal evidence policymakers need to justify implementation at scale. The UK Behavioural Insights Team's practice of "test, learn, adapt" — piloting interventions through small-scale RCTs before scaling — represents the integration of field experimental methodology into routine governance. The limitation is that not everything can be experimentally tested (you cannot randomize monetary policy or tax codes), but for the wide range of interventions that can be tested, field experiments provide the most credible evidence available.
