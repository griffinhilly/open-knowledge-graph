---
id: quasi-experimental-designs-nonequivalent-groups
title: Quasi-Experimental Designs with Nonequivalent Groups
domain: psychology
course: research-methods-psychology
prerequisites:
- id: experimental-research-design
  type: hard
- id: confounding-variables
  type: hard
- id: internal-validity-threats-experimental-control
  type: soft
builds-toward:
- research-design-selection-matching-question
tags:
- design
- quasi-experimental
- causal-inference
- non-equivalent-groups
stage: formal-systems
status: validated
---

# Quasi-Experimental Designs with Nonequivalent Groups

## Core Idea
Quasi-experimental designs test causal hypotheses without random assignment to conditions, using nonequivalent control groups or other designs that provide partial control over confounds but less internal validity than true experiments. Nonequivalent control group designs compare naturally occurring groups assigned to interventions, but groups may differ systematically before intervention, making causal inference difficult. Regression discontinuity designs exploit sharp cutoffs in assignment to improve causal inference; interrupted time-series designs use temporal patterns to strengthen conclusions. Quasi-experiments sacrifice internal validity compared to randomized experiments but may gain external validity and feasibility when random assignment is infeasible or unethical.

## Questions

```yaml
- question: "A researcher compares job outcomes for people who voluntarily enrolled in a job training program versus people who did not enroll. Program participants show better employment outcomes. What is the strongest threat to concluding the program caused this improvement?"
  type: multiple-choice
  options:
    - "Demand characteristics — participants knew they were being evaluated and worked harder as a result"
    - "Selection bias — people who chose to enroll may have had higher motivation, better social support, or stronger baseline skills before the program began"
    - "History — a regional economic boom may have happened to coincide with the program period"
    - "Attrition — some participants may have dropped out of the program before completion"
  answer: 1
  explanation: "Selection bias is the central threat in any nonequivalent control group design. Because enrollment was voluntary, the two groups were not equivalent from the start — people who enroll in job training programs likely differ systematically from those who don't in ways that predict employment success (motivation, conscientiousness, social resources). Any post-program difference might simply reflect those pre-existing differences rather than the program's causal effect. History and attrition are real threats, but they are secondary to this fundamental nonequivalence. The only way to rule out selection bias is random assignment — which this design lacks."

- question: "A school assigns students scoring below 70 on a placement test to a tutoring program; those scoring 71+ are not assigned. A researcher compares outcomes for students scoring 68–69 versus students scoring 71–72. Why does this comparison provide relatively strong causal evidence compared to comparing all participants to all non-participants?"
  type: multiple-choice
  options:
    - "Because the cutoff score is arbitrary, it effectively randomizes assignment for all students in the study"
    - "Because students near the cutoff are likely very similar to each other on all relevant characteristics — they nearly received the same score — making near-threshold assignment quasi-random"
    - "Because the standardized test score fully controls for all pre-existing differences between students"
    - "Because regression discontinuity designs eliminate all threats to internal validity just as randomized experiments do"
  answer: 1
  explanation: "The power of regression discontinuity (RD) designs rests on the local quasi-randomness near the threshold. A student scoring 69 and a student scoring 71 were very similar — one or two items on a test — yet ended up in different conditions. Their pre-existing characteristics (ability, motivation, background) are likely nearly identical near this boundary, unlike the full treatment and control groups which may differ broadly. This makes the comparison near the cutoff credible. However, RD estimates are local: they tell you the effect for students near the threshold, not for all students. And RD does not eliminate all threats — it only improves causal inference for the near-cutoff comparison."

- question: "Quasi-experimental designs can never provide credible causal evidence because they lack random assignment."
  type: true-false
  answer: false
  explanation: "This is the key misconception the topic addresses. While quasi-experiments do have weaker internal validity than randomized experiments, they can still provide credible causal evidence when designed and analyzed carefully. Regression discontinuity designs exploit near-random assignment at sharp cutoffs. Interrupted time-series designs use stable pre-intervention trends as counterfactuals. Difference-in-differences approaches control for baseline group differences. Quasi-experiments have produced influential and credible findings in economics, public health, and psychology precisely because researchers can analyze and address known confounds, even without randomization."

- question: "In an interrupted time-series design, the history threat refers to the possibility that some other event occurred at the same time as the intervention and was the actual cause of any observed outcome change."
  type: true-false
  answer: true
  explanation: "History is the primary internal validity threat in ITS designs. The design uses the pre-intervention trend as the counterfactual: if outcomes were stable before and then changed sharply at the intervention point, the intervention seems causal. But if something else also changed at that moment — a concurrent policy, an economic event, a media campaign — the design cannot distinguish between them. This threat is why adding a comparison time series (a similar unit that did NOT receive the intervention) greatly strengthens ITS evidence: if the comparison series shows no change while the treatment series does, concurrent historical events become less plausible as alternative explanations."

- question: "What is selection bias in a nonequivalent control group design, and why does it make causal inference difficult?"
  type: short-answer
  answer: "Selection bias occurs when the treatment and comparison groups differ systematically on characteristics related to the outcome before the intervention begins. Because there was no random assignment, pre-existing differences between groups can produce outcome differences that look like treatment effects but actually reflect who was selected into each group."
  explanation: "The core logic of causal inference is: if two groups are identical before treatment and then differ afterward, the treatment likely caused the difference. Random assignment creates that pre-treatment equivalence in expectation. Without it, the groups may differ at baseline on motivation, resources, health, ability, or countless other variables. Any post-treatment difference is then ambiguous: was it the treatment, or those pre-existing differences? Quasi-experimental methods like matching, covariate adjustment, and regression discontinuity all attempt to approximate pre-treatment equivalence, but none fully replicate the guarantee that randomization provides."
```

## Explainer

From your study of experimental research design, you know that random assignment is the gold standard for causal inference: it distributes all confounding variables — measured and unmeasured — evenly across conditions in expectation, allowing any difference in outcomes to be attributed to the treatment. But random assignment is often impossible. You can't randomly assign children to be raised in poverty or affluence. You can't randomly assign communities to receive a new public health intervention. You can't randomize which classrooms get a new curriculum when the school has already decided who teaches where. **Quasi-experimental designs** are the toolkit for drawing causal inferences when randomization isn't available, and understanding them requires internalizing what exactly goes wrong when groups are not randomly assigned.

The core threat in a **nonequivalent control group design** is **selection bias**: the treatment and comparison groups differ systematically before the intervention begins, and any post-intervention difference might reflect those pre-existing differences rather than the treatment itself. Suppose a researcher studies whether a job training program reduces unemployment by comparing participants (who chose to enroll) to non-participants (who didn't). Even if participants are less likely to be unemployed afterward, we can't conclude the program worked — people who voluntarily enroll in job training may have more motivation, better support networks, or higher baseline skills than those who didn't. The groups were never equivalent, so the comparison is confounded by selection.

**Regression discontinuity (RD) designs** exploit a specific feature of assignment that makes causal inference credible: a sharp cutoff score that determines treatment. If students scoring below 70 on a placement test are assigned to a remedial reading program and those above 70 are not, students just below and just above the cutoff are likely very similar to each other — they were nearly identical on the assignment variable but ended up in different conditions by a small margin. Comparing outcomes for these near-cutoff students provides clean causal evidence about the program's effect, because near the threshold, assignment is effectively quasi-random. The tradeoff: the estimate is local — it tells you the effect for students at the threshold, not for all students.

**Interrupted time-series (ITS) designs** use the pre-intervention temporal trend as the counterfactual. If a city implements a seatbelt law and you have monthly traffic fatality data for many years before and after, you can ask: did the fatality rate change more sharply at the intervention point than the pre-existing trend would predict? The pre-intervention trend serves as the control condition. This is compelling when the trend is stable and the intervention is clearly defined in time. The key threat is **history**: something else might have changed at the same moment as the intervention (a new road safety campaign, an economic downturn affecting driving) and be the real cause of any observed change. The design improves substantially when you have a comparison series — a similar city that did not implement the law — to control for concurrent historical events. These designs don't achieve the clean causal logic of a randomized experiment, but with careful threat analysis they can produce credible and consequential evidence in real-world settings where experiments are impossible.

## How It's Best Learned
Compare a nonequivalent groups design with a randomized experiment addressing the same question; note how potential confounds differ between designs.

## Common Misconceptions
Quasi-experiments provide no causal evidence (actually, quasi-experiments can provide credible causal evidence if confounds are carefully considered). Nonequivalent groups designs are simply correlational studies (actually, they are distinct from pure correlational studies and can provide stronger evidence).
