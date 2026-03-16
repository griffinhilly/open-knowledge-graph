---
id: number-needed-to-treat
title: Number Needed to Treat and Number Needed to Harm
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: attributable-risk-calculation
  type: hard
builds-toward:
- screening-test-evaluation
tags:
- intervention-effectiveness
- clinical-significance
- decision-making
stage: advanced
status: draft
---

# Number Needed to Treat and Number Needed to Harm

## Core Idea
Number needed to treat (NNT) is the reciprocal of attributable risk in a trial: NNT = 1 / AR. It expresses how many people must receive an intervention to prevent one adverse outcome. Number needed to harm (NNH) applies the same logic to adverse effects. These metrics translate relative measures into absolute, clinically interpretable terms for individual patients.

## Explainer

From your study of attributable risk, you know that absolute risk measures — unlike relative ones — answer the question of how much a risk actually changes. A relative risk reduction of 50% sounds identical whether the risk drops from 20% to 10% or from 0.002% to 0.001%, but the public health and clinical significance of those two scenarios are vastly different. The **number needed to treat (NNT)** is the tool that makes this concreteness automatic, by converting the absolute risk difference into the language of individual patients: how many people must receive this treatment to prevent one adverse outcome?

The calculation flows directly from your attributable risk knowledge. In a randomized trial, the **absolute risk reduction (ARR)** is simply the event rate in the control group minus the event rate in the treatment group: ARR = Risk_control − Risk_treatment. NNT = 1 / ARR. A concrete example: a trial of a cholesterol-lowering drug finds that over 5 years, 8% of patients in the placebo group had a heart attack, compared to 5% in the treated group. ARR = 0.08 − 0.05 = 0.03. NNT = 1/0.03 ≈ 33. You must treat 33 patients for 5 years to prevent one heart attack. **Number needed to harm (NNH)** is calculated identically but for adverse events: if the drug causes a serious side effect in 2% of treated patients and 0.5% of controls, ARR_harm = 0.015, NNH = 67.

The clinical power of these metrics lies in enabling direct comparison between benefit and risk. The NNT of 33 and NNH of 67 in this example mean that for every two patients harmed by the drug, roughly four are protected from a heart attack — a favorable ratio. The formal version of this comparison is the **likelihood of being helped vs. harmed (LHH)**, calculated as NNH / NNT. Values above 1 favor treatment; below 1, the harm exceeds the benefit. For patient communication, framing as "1 in 33 patients benefits from this drug" is often more intuitive and honest than "the drug reduces your heart attack risk by 38%" — the relative measure that pharmaceutical marketing typically emphasizes because it sounds more impressive.

One critical limitation is that NNT is not a fixed property of a drug — it depends on the population's **baseline risk** and the time horizon of the trial. The NNT above applies only to patients with 8% five-year MI risk treated for five years. Applied to a lower-risk population (say, 2% five-year risk) with the same relative risk reduction, ARR would be approximately 0.008 and NNT would jump to 125. The treatment is three to four times less efficient in absolute terms, even though the same trial's relative risk reduction still applies. This is why applying published NNTs uncritically to patients who differ from the trial population can be systematically misleading — the absolute benefit scales with baseline risk, so the same drug can range from highly efficient prevention to marginal benefit depending entirely on who is receiving it.
