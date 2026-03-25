---
id: natural-experiments-design
title: Natural Experiments and Quasi-Experimental Design
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: causal-inference-observational-data
  type: hard
- id: research-design-advanced
  type: hard
tags:
- natural-experiments
- quasi-experiments
- policy-variation
- validity-threats
stage: formal-systems
status: validated
---

# Natural Experiments and Quasi-Experimental Design

## Core Idea
Examines research designs that exploit naturally occurring policy changes, discontinuities, or accidents as quasi-experiments. Covers identification assumptions, threats to internal validity, and methodological issues in leveraging natural experiments. Discusses examples from policy evaluation and organizational research.

## How It's Best Learned
Identify natural experiment variations in your research domain, evaluate whether identification assumptions are plausible, discuss alternative explanations for observed effects.

## Common Misconceptions
- Natural experiments are as good as randomization
- Timing of exposure automatically proves causation
- Natural experiments eliminate all confounding

## Questions

```yaml
- question: "A researcher uses cities that experienced an unexpected river flood as a natural experiment to study the effect of economic disruption on crime. What is the most critical question she must answer to establish causal identification?"
  type: multiple-choice
  options:
    - "Whether the flood was large enough in magnitude to produce measurable economic disruption"
    - "Whether she should use regression discontinuity or difference-in-differences as her estimation strategy"
    - "Whether flooded and non-flooded cities were on parallel trends before the flood, and whether flooding was truly unrelated to pre-existing differences in crime risk"
    - "Whether she collected a sufficiently large sample size to detect the effect"
  answer: 2
  explanation: "The critical issue is whether the identification assumption holds: the flooded cities must be a plausible counterfactual for the non-flooded cities — they would have followed the same trajectory absent the flood. If flooded cities differ from non-flooded ones in ways related to crime (e.g., poorer infrastructure, higher population density), the comparison is confounded. This is the parallel trends assumption for difference-in-differences. Establishing this assumption empirically and theoretically is what separates a credible natural experiment from a mere coincidence."

- question: "A researcher observes that earnings rose more in State A than State B after State A implemented a job training program. She concludes the program caused the increase. What critical assumption is being ignored?"
  type: multiple-choice
  options:
    - "That the sample size in State A might be too small to produce reliable estimates"
    - "That both states should have received the program to enable a valid comparison"
    - "That State A and State B must have been on parallel trends before the program — i.e., they would have diverged by the same amount absent the program — and this assumption must be defended, not assumed"
    - "That regression discontinuity design should have been used instead of difference-in-differences"
  answer: 2
  explanation: "The parallel trends assumption is the identification assumption for difference-in-differences: the treated and control units (here, states) would have followed the same trajectory absent the treatment. If State A was already growing faster than State B before the program — perhaps because it was attracting industry for unrelated reasons — the comparison attributes pre-existing trends to the program. This assumption cannot be verified for the post-treatment period, but researchers typically test it by checking whether trends were parallel in the pre-treatment period."

- question: "A natural experiment is equivalent to a randomized controlled trial because both eliminate confounding by making treatment assignment independent of individual characteristics."
  type: true-false
  answer: false
  explanation: "This is a common and dangerous misconception. Natural experiments approximate experimental logic but are not equivalent to true randomization. Even lottery-based natural experiments require checking that the lottery was genuinely random and that no sorting occurred. RDD requires that units can't precisely control which side of the cutoff they land on. Difference-in-differences requires parallel trends. Each design requires explicit identification assumptions that must be defended empirically and theoretically — they don't inherit the guarantees of true randomization."

- question: "Even when treatment is assigned by lottery (as in the Vietnam draft lottery), the natural experiment requires checking that the lottery was truly random and that no one could selectively avoid or obtain their assigned treatment."
  type: true-false
  answer: true
  explanation: "True. Angrist's Vietnam draft lottery study worked because birth dates were genuinely randomly assigned draft priority AND because 'lottery number' affected earnings mainly through its effect on actual military service. Both conditions had to be checked. If wealthy individuals could reliably obtain medical deferments regardless of lottery number, the lottery number would no longer be a valid instrument — treatment receipt would be selective. Verifying randomness and checking for 'compliance' are essential steps in any lottery-based natural experiment."

- question: "What is an 'identification assumption' in natural experiments, and why can't a researcher simply assume it is satisfied?"
  type: short-answer
  answer: "An identification assumption is a claim that must hold for the natural variation to isolate a causal effect rather than reflect confounding. For difference-in-differences it is parallel trends; for RDD it is that units can't precisely manipulate which side of the cutoff they fall on; for lottery instruments it is that lottery assignment is truly random and affects outcomes only through the treatment channel. Researchers can't simply assume these hold because they are empirical claims about the world — whether flooded cities had different pre-trends, whether medical deferments were selectively obtained, whether scores were manipulated near a cutoff. Each must be argued for using pre-treatment data, robustness checks, and theoretical reasoning about the institutional context."
  explanation: "The whole point of a natural experiment is that the variation is 'as-if' random — but 'as-if' requires justification, not assumption. Researchers defend identification assumptions through falsifiable pre-treatment tests (parallel trends plots, balance checks), placebo tests (does the 'treatment' affect outcomes that should be unaffected?), and institutional knowledge about the mechanism that created the variation. When identification assumptions fail, the natural experiment produces biased causal estimates — potentially worse than a transparent observational comparison that acknowledges its confounders."
```

## Explainer

You already know the core problem in causal inference from observational data: people and units do not randomly select into treatment, so observed differences between treated and untreated groups might reflect pre-existing differences rather than any effect of the treatment itself. **Natural experiments** are cases where some external process — a policy change, an administrative cutoff, a lottery, a natural disaster — creates variation in treatment that is effectively independent of the characteristics that would ordinarily confound it. The appeal is enormous: you get something approximating experimental logic without actually running an experiment.

The canonical example is the **Vietnam draft lottery**, used by Joshua Angrist to estimate the earnings effects of military service. The U.S. Selective Service assigned draft priority by a randomized lottery based on birth date. Men with low lottery numbers faced much higher probability of induction. Crucially, lottery number was unrelated to anything else about a young man's characteristics — it was literally random. This allows comparison of earnings outcomes between men with low and high lottery numbers as if they had been randomly assigned to serve, isolating the causal effect of military service from the selection effects that would plague any simple comparison of veterans and non-veterans.

**Regression discontinuity design (RDD)** exploits a different kind of natural experiment: an administrative cutoff that creates a sharp threshold. If you score 70 or above on an entrance exam, you get the scholarship; below 70, you don't. Students just above and just below the threshold are nearly identical in all respects except which side of the cutoff they fall on — this local comparison yields a valid estimate of the scholarship's effect. Card and Krueger's famous minimum wage study compared fast-food workers just across the New Jersey–Pennsylvania border, using geographic discontinuity as a natural control group. The logic is the same in every case: find a feature of the world that creates as-if random assignment.

The critical skill is evaluating **identification assumptions** — the claims that must hold for the natural experiment to actually identify a causal effect. For a lottery, there must be no sorting around the lottery. For RDD, units can't precisely control which side of the cutoff they land on. For **difference-in-differences** designs, the key assumption is parallel trends: treated and control groups would have followed the same trajectory absent the treatment. None of these assumptions are automatically satisfied; each requires empirical scrutiny and explicit defense. Natural experiments are not equivalent to true randomization — they get closer, but they require careful argument about why the specific variation at hand is plausibly exogenous to the outcome of interest.
