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
status: draft
---

# Quasi-Experimental Designs with Nonequivalent Groups

## Core Idea
Quasi-experimental designs test causal hypotheses without random assignment to conditions, using nonequivalent control groups or other designs that provide partial control over confounds but less internal validity than true experiments. Nonequivalent control group designs compare naturally occurring groups assigned to interventions, but groups may differ systematically before intervention, making causal inference difficult. Regression discontinuity designs exploit sharp cutoffs in assignment to improve causal inference; interrupted time-series designs use temporal patterns to strengthen conclusions. Quasi-experiments sacrifice internal validity compared to randomized experiments but may gain external validity and feasibility when random assignment is infeasible or unethical.

## Explainer

From your study of experimental research design, you know that random assignment is the gold standard for causal inference: it distributes all confounding variables — measured and unmeasured — evenly across conditions in expectation, allowing any difference in outcomes to be attributed to the treatment. But random assignment is often impossible. You can't randomly assign children to be raised in poverty or affluence. You can't randomly assign communities to receive a new public health intervention. You can't randomize which classrooms get a new curriculum when the school has already decided who teaches where. **Quasi-experimental designs** are the toolkit for drawing causal inferences when randomization isn't available, and understanding them requires internalizing what exactly goes wrong when groups are not randomly assigned.

The core threat in a **nonequivalent control group design** is **selection bias**: the treatment and comparison groups differ systematically before the intervention begins, and any post-intervention difference might reflect those pre-existing differences rather than the treatment itself. Suppose a researcher studies whether a job training program reduces unemployment by comparing participants (who chose to enroll) to non-participants (who didn't). Even if participants are less likely to be unemployed afterward, we can't conclude the program worked — people who voluntarily enroll in job training may have more motivation, better support networks, or higher baseline skills than those who didn't. The groups were never equivalent, so the comparison is confounded by selection.

**Regression discontinuity (RD) designs** exploit a specific feature of assignment that makes causal inference credible: a sharp cutoff score that determines treatment. If students scoring below 70 on a placement test are assigned to a remedial reading program and those above 70 are not, students just below and just above the cutoff are likely very similar to each other — they were nearly identical on the assignment variable but ended up in different conditions by a small margin. Comparing outcomes for these near-cutoff students provides clean causal evidence about the program's effect, because near the threshold, assignment is effectively quasi-random. The tradeoff: the estimate is local — it tells you the effect for students at the threshold, not for all students.

**Interrupted time-series (ITS) designs** use the pre-intervention temporal trend as the counterfactual. If a city implements a seatbelt law and you have monthly traffic fatality data for many years before and after, you can ask: did the fatality rate change more sharply at the intervention point than the pre-existing trend would predict? The pre-intervention trend serves as the control condition. This is compelling when the trend is stable and the intervention is clearly defined in time. The key threat is **history**: something else might have changed at the same moment as the intervention (a new road safety campaign, an economic downturn affecting driving) and be the real cause of any observed change. The design improves substantially when you have a comparison series — a similar city that did not implement the law — to control for concurrent historical events. These designs don't achieve the clean causal logic of a randomized experiment, but with careful threat analysis they can produce credible and consequential evidence in real-world settings where experiments are impossible.

## How It's Best Learned
Compare a nonequivalent groups design with a randomized experiment addressing the same question; note how potential confounds differ between designs.

## Common Misconceptions
Quasi-experiments provide no causal evidence (actually, quasi-experiments can provide credible causal evidence if confounds are carefully considered). Nonequivalent groups designs are simply correlational studies (actually, they are distinct from pure correlational studies and can provide stronger evidence).
