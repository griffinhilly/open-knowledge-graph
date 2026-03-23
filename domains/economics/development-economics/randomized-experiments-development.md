---
id: randomized-experiments-development
title: Randomized Experiments in Development Economics
domain: economics
course: development-economics
prerequisites:
- id: causal-inference-econometrics
  type: hard
- id: hypothesis-testing-regression
  type: soft
- id: probability-theory
  type: hard
- id: sampling-distributions-theory
  type: hard
builds-toward:
- conditional-cash-transfers-cct
tags:
- RCT
- experimental-design
stage: expert
status: validated
---

# Randomized Experiments in Development Economics

## Core Idea
Randomized Controlled Trials randomly assign treatment (a development program) to some communities and not others, generating credible causal impact estimates. Banerjee and Duflo pioneered this approach in development economics, studying microfinance, education, and health programs. RCTs address selection bias and reverse causality but raise questions about generalizability and policy scalability.

## Questions

```yaml
- question: "A deworming RCT in Kenya found a 25% increase in school attendance. A policymaker wants to immediately scale the program nationally in Guatemala. What is the most important methodological concern?"
  type: multiple-choice
  options:
    - "The study had selection bias because villages self-selected into the program"
    - "External validity — results from one context may not generalize to different health burdens, institutions, and incentive structures elsewhere"
    - "The control group was contaminated by exposure to the treatment villages"
    - "The RCT sample size was too small to achieve statistical significance"
  answer: 1
  explanation: "RCTs solve selection bias through randomization, so option A is incorrect. The key concern here is external validity: an RCT establishes a causal effect in a specific context, but that effect may not transfer to another country with different disease ecology, school systems, parental incentives, and implementation capacity. This is one of the principal limitations of RCTs in development economics — causal identification in one place is not the same as a universal finding."

- question: "Why does random assignment address selection bias in a way that controlling for observed confounders in observational studies cannot?"
  type: multiple-choice
  options:
    - "Randomization guarantees that the treatment and control groups have identical individual characteristics"
    - "Randomization makes treatment and control groups statistically equivalent in expectation across all confounders — observed and unobserved"
    - "Random assignment eliminates the need for statistical analysis because the groups are identical"
    - "Observational studies cannot control for any confounders, only RCTs can"
  answer: 1
  explanation: "Option A overstates the claim — randomization does not make individual groups identical, it makes them equivalent in expectation across the full distribution of characteristics. The critical advantage over observational methods is that randomization balances all confounders — including ones the researcher never measured or even thought of. Observational studies can control for observed confounders using matching or regression, but unmeasured confounders remain a threat. RCTs remove that threat by design."

- question: "RCTs in development economics eliminate ethical concerns about withholding beneficial programs, because the control group receives the program once the trial ends."
  type: true-false
  answer: false
  explanation: "This is false. Ethical concerns are a genuine limitation of RCTs. During the trial period, the control group does not receive the program — and if the program turns out to be beneficial, those individuals were denied a potentially valuable intervention. Researchers and IRBs must weigh the social value of rigorous evidence against the harm of withholding treatment. Ethical issues are not resolved simply by later rollout; they bear on the design and justification of the trial itself."

- question: "An RCT-tested development program that succeeded in a carefully managed research trial will work equally well when implemented at national scale by government agencies."
  type: true-false
  answer: false
  explanation: "This is the scalability problem, a major limitation of RCTs. Small pilots benefit from researcher oversight, motivated field staff, tight implementation protocols, and Hawthorne effects that a national rollout cannot replicate. Governments implement at scale with existing bureaucratic capacity, variable local conditions, and without the research team's intensive monitoring. The causal estimate from the trial may be correct for that context, but the magnitude of impact often shrinks substantially when programs scale."

- question: "What problem does random assignment solve that makes RCTs the gold standard for causal inference in development economics?"
  type: short-answer
  answer: "Random assignment solves the fundamental problem of selection bias — the fact that, in observational data, who receives a program is not random. Villages that receive aid may be wealthier, better-governed, or more motivated, so comparing treated and untreated villages confounds the program's effect with pre-existing differences. By randomly assigning treatment, RCTs ensure that treatment and control groups are statistically equivalent in expectation on all characteristics, so any observed difference in outcomes can be attributed causally to the program."
  explanation: "The deeper point is that random assignment balances not just the confounders researchers can measure (which regression or matching can also address) but also unobserved confounders — motivation, governance quality, historical context — that can never be fully measured. This is what makes the causal claim credible in a way that observational analysis cannot match, and why Banerjee and Duflo's RCT approach transformed the evidentiary standards of development economics."
```

## Explainer

From causal inference, you know the fundamental problem: we want to know what would have happened to treated individuals had they not been treated, but we can never observe both states for the same person. From probability theory and sampling distributions, you understand that random assignment across a large enough sample ensures that treatment and control groups are statistically equivalent in expectation — any difference in outcomes can be attributed to the treatment itself. **Randomized Controlled Trials** (RCTs) in development economics apply this experimental logic to real-world programs, bringing the rigor of clinical trials to questions like whether deworming pills improve school attendance or whether microloans reduce poverty.

The core mechanics are straightforward. Researchers identify a population — say, 200 villages eligible for a new school-feeding program. They randomly assign half the villages to receive the program (treatment group) and half to continue without it (control group). After a specified period, they measure outcomes in both groups: test scores, attendance rates, nutritional status. Because assignment was random, any systematic difference between the groups at the end is the **average treatment effect** of the program. This eliminates **selection bias**, the problem that plagues observational studies. Without randomization, villages that receive feeding programs might be wealthier, better-governed, or more motivated — and any improvement in outcomes could reflect those pre-existing advantages rather than the program itself.

Abhijit Banerjee and Esther Duflo, along with collaborators at the Abdul Latif Jameel Poverty Action Lab (J-PAL), pioneered the systematic use of RCTs in development economics, winning the 2019 Nobel Prize for this work. Their studies produced surprising and policy-relevant findings. Providing free bed nets for malaria prevention was more effective than charging even small amounts, overturning the intuition that cost-sharing increases usage. Adding a second teacher to a classroom had little effect on learning, but hiring a contract teacher accountable to parents did. These results challenged development orthodoxies and shifted billions of dollars in aid allocation toward evidence-backed programs.

RCTs are not without limitations, and understanding them is essential for interpreting results responsibly. **External validity** — whether findings from one context generalize to another — is a persistent concern. A deworming program that raised attendance in Kenya may not work the same way in a Bolivian highland community with different health burdens and school systems. **Scalability** is related: a small, carefully managed pilot may succeed because of intensive researcher oversight that a national rollout cannot replicate. There are also ethical questions — is it acceptable to withhold a potentially beneficial program from the control group? — and practical constraints, since randomization requires the cooperation of governments and NGOs willing to let a coin flip determine who receives services. Despite these limitations, RCTs have fundamentally raised the evidentiary standard in development economics, shifting the field from ideological debates about what should work toward empirical evidence about what actually does.
