---
id: single-case-intensive-nof1-designs
title: Single-Case and Intensive Within-Subject Designs
domain: psychology
course: research-methods-psychology
prerequisites:
- id: research-design-selection-and-matching
  type: hard
- id: variable-definition-and-operational-measurement
  type: hard
builds-toward:
- internal-validity-confounds-and-control
tags:
- single-case
- within-subject
- ABAB
- N-of-1
stage: formal-systems
status: validated
---

# Single-Case and Intensive Within-Subject Designs

## Core Idea
Single-case designs (ABAB, multiple-baseline, changing-criterion) intensively study one individual across repeated measurements and condition changes. They establish causality by showing that behavior changes when treatment is introduced and reverts when withdrawn. Suitable for clinical practice, organizational consultancy, and understanding individual mechanisms when group designs are impractical.

## How It's Best Learned
Study a published single-case design and trace how repeated measurements reveal treatment effects. Design your own single-case study specifying baseline, treatment, and reversal phases. Discuss when individual-level evidence is clinically or theoretically crucial.

## Common Misconceptions
- Single-case designs are anecdotal; - Causality requires large group studies; - Single-case findings cannot be generalized; - Multiple-baseline designs require reversal.

## Questions

```yaml
- question: "A therapist uses an ABAB design to test a new anxiety-reduction technique with a single client. After the second A (withdrawal) phase, the client's anxiety levels drop unexpectedly without treatment. What is the most likely problem with concluding the technique caused the improvement?"
  type: multiple-choice
  options:
    - "The sample size is too small to draw any conclusions"
    - "The causal logic of the design requires behavior to revert during withdrawal; if it doesn't, the effect cannot be attributed to treatment"
    - "ABAB designs only work when treatment is applied continuously, not in phases"
    - "A single replication is insufficient; at least three full ABAB cycles are needed"
  answer: 1
  explanation: "The causal logic of ABAB depends on reversal: if behavior improves during B, reverts during the return to A, and improves again in the second B, each transition moves in the predicted direction and strongly implicates treatment. If anxiety drops during the second A phase without treatment, some other factor — natural remission, a life event — is a more plausible explanation. The design's causal power comes specifically from behavior tracking condition changes."

- question: "A researcher wants to test an intervention for self-injurious behavior but cannot ethically withdraw treatment once it works. Which design is most appropriate?"
  type: multiple-choice
  options:
    - "ABAB reversal design — it provides the strongest causal evidence even if ethically uncomfortable"
    - "Multiple-baseline design — it staggers intervention across behaviors or settings so no reversal is needed"
    - "Group randomized controlled trial — it avoids the need to study individuals at all"
    - "Changing-criterion design — it removes the need for any baseline phase"
  answer: 1
  explanation: "Multiple-baseline designs achieve causal inference without reversal by introducing treatment at staggered time points across different behaviors, settings, or individuals. If each target only changes when treatment is applied to it (not before), the staggered pattern rules out history and maturation as explanations. No individual ever has successful treatment withdrawn — the causal argument comes from timing, not reversal."

- question: "Single-case designs establish causality by comparing one individual to a matched control participant who receives no treatment."
  type: true-false
  answer: false
  explanation: "Single-case designs use the individual as their own control. In an ABAB design, the person's own stable baseline serves as the counterfactual — what the behavior would look like without intervention. There is no separate control group. The control condition is temporal (before vs. during treatment) rather than cross-sectional (treated vs. untreated group)."

- question: "A finding from a single ABAB study replicated across 20 individuals in five different settings by different clinicians provides meaningful evidence of generalizability."
  type: true-false
  answer: true
  explanation: "Systematic replication — applying the same protocol across multiple individuals, clinicians, and settings — can build external validity that rivals group RCTs. While a single case study cannot generalize, when the same effect appears across varied replications, the accumulation of evidence substantially increases confidence. This is why applied behavior analysis relies on single-case methods rather than viewing them as inherently non-generalizable."

- question: "Why does single-case research place such heavy emphasis on measurement quality and inter-rater reliability, compared to group designs?"
  type: short-answer
  answer: "In group designs, measurement error averages out across many participants. In single-case work, each data point represents the individual's behavior on a specific occasion — there is no averaging. A noisy or inconsistent measure creates artifactual trends that mimic or mask real treatment effects. The design's entire causal argument rests on detecting reliable changes across phases, so each observation must be trustworthy."
  explanation: "This is the core trade-off of single-case methodology: deep individual-level insight at the cost of losing the statistical averaging that absorbs measurement error in group designs. The solution is investing more in measurement precision — behavioral coding systems, operational definitions, inter-rater reliability checks. This is not a weakness of the method but a different quality-control strategy appropriate to its goals."
```

## Explainer

From your study of research design selection, you know that choosing a design depends on matching the research question to the appropriate unit of analysis, the available sample, and the causal claims you want to make. Most experimental designs achieve causal inference by averaging across many participants — random assignment distributes individual differences across conditions, so any systematic outcome difference is attributable to the manipulation. **Single-case designs** take a different route to the same destination: instead of averaging across people, they accumulate many observations *within* one person over time, using the person's own stable baseline as the counterfactual.

The foundational logic is reversal. In the simplest **ABAB design**, the researcher establishes a baseline phase (A) by measuring the target behavior repeatedly until it is stable. Then treatment is introduced (B), and the behavior is measured repeatedly again. If the behavior changes with the introduction of treatment, that's suggestive — but it could be coincidence or a natural trend. The critical move is withdrawal: the treatment is removed (returning to A), and if the behavior reverts toward baseline, the pattern strongly implicates treatment as the cause. Reintroducing treatment (second B) and seeing the behavior change again creates a replication within the single case, making chance explanations increasingly implausible. Four phase changes within one participant, each moving in the predicted direction, provide convincing causal evidence.

The **multiple-baseline design** is used when reversal is impractical or unethical — you wouldn't want to withdraw a successful intervention for self-injury just to prove a point. Multiple-baseline designs introduce treatment to different behaviors, settings, or individuals at staggered time points while keeping the others at baseline. If each target behavior changes only when treatment is introduced to it (and not before), this staggered replication rules out history, maturation, and other time-based confounds. The logic is "if it only moves when I push it, I must be doing the pushing." No reversal is needed; temporal coincidence of change and intervention across multiple baselines makes the causal argument.

Operational measurement — your other prerequisite — matters enormously here because inference depends entirely on the reliability and precision of the dependent variable across hundreds of repeated observations. Unlike group designs where measurement error averages out across participants, in single-case work each data point must be trustworthy. Poor operationalization introduces noise that masks true treatment effects; inconsistent measurement creates artifactual trends that mimic treatment responses. The design's causal power is proportional to measurement quality. This is why single-case researchers invest heavily in behavioral coding procedures, inter-rater reliability checks, and observer calibration.

Single-case designs are not purely local — they can support generalization through **systematic replication**: applying the same treatment protocol with the same design across a series of individuals, settings, and clinicians. When a therapeutic technique works in ABAB replications with 20 individuals across five different clinicians in three different settings, the accumulation of evidence rivals the external validity of many randomized controlled trials, while also providing mechanistic insight into how treatment works at the individual level. This is why single-case methodology dominates applied behavior analysis, clinical psychology for rare conditions, and educational interventions for individual students — contexts where understanding and helping the individual is both the practical and scientific goal.

