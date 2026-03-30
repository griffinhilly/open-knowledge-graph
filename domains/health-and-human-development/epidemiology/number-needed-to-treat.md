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
status: validated
---

# Number Needed to Treat and Number Needed to Harm

## Core Idea
Number needed to treat (NNT) is the reciprocal of attributable risk in a trial: NNT = 1 / AR. It expresses how many people must receive an intervention to prevent one adverse outcome. Number needed to harm (NNH) applies the same logic to adverse effects. These metrics translate relative measures into absolute, clinically interpretable terms for individual patients.

## Questions

```yaml
- question: "A statin trial shows the same 50% relative risk reduction in two populations. In Population A, the 5-year MI rate in the control group is 20%; in Population B it is 4%. What are the approximate NNTs for each population?"
  type: multiple-choice
  options:
    - "Both are NNT = 2, because the relative risk reduction is the same"
    - "Population A: NNT ≈ 10; Population B: NNT ≈ 50"
    - "Population A: NNT ≈ 50; Population B: NNT ≈ 10"
    - "NNT cannot be calculated without knowing absolute event counts"
  answer: 1
  explanation: "NNT = 1/ARR. For Population A: ARR = 0.20 − 0.10 = 0.10, NNT = 10. For Population B: ARR = 0.04 − 0.02 = 0.02, NNT = 50. The same relative risk reduction produces wildly different NNTs depending on baseline risk. This is the central insight: relative measures look identical across populations, but absolute measures reveal that treating Population A is five times more efficient than treating Population B. Pharmaceutical marketing emphasizes relative risk reduction partly because it sounds more impressive than the NNT."

- question: "A clinician reads a published NNT of 25 for a blood pressure drug, derived from a trial of high-risk patients over 10 years. She applies it to a low-risk patient population with roughly half the baseline event rate. What is the most appropriate expectation for the NNT in her patients?"
  type: multiple-choice
  options:
    - "The NNT remains 25, because NNT is a fixed property of the drug"
    - "The NNT drops to around 12, because lower risk means the drug works harder"
    - "The NNT approximately doubles to around 50, because absolute risk reduction scales with baseline risk"
    - "The NNT is irrelevant in lower-risk patients because relative risk reduction doesn't apply"
  answer: 2
  explanation: "NNT scales inversely with baseline risk. If the trial population had twice the event rate of her patients, the ARR will be roughly half as large, and NNT will roughly double. The drug's relative risk reduction may be identical, but the absolute benefit — how many patients you must treat to prevent one event — is far less efficient at lower baseline risk. Applying a published NNT uncritically to a different population is a systematic error in clinical reasoning."

- question: "An NNT of 5 is typically more clinically significant than an NNT of 50."
  type: true-false
  answer: false
  explanation: "NNT must be interpreted in context: it depends on the severity of the outcome prevented, the duration of treatment, and the NNH for adverse effects. An NNT of 5 for preventing mild indigestion is far less significant than an NNT of 50 for preventing fatal stroke. Additionally, comparing NNT to NNH — the likelihood of being helped vs. harmed (LHH = NNH/NNT) — is the relevant clinical calculation, not the NNT alone."

- question: "If a drug reduces relative risk by 50%, halving the baseline event rate in the treated population, then halving the baseline risk of the target population will approximately double the NNT."
  type: true-false
  answer: true
  explanation: "NNT = 1/ARR, and ARR = baseline risk × relative risk reduction. If baseline risk halves (and relative risk reduction stays constant), ARR halves, and NNT doubles. This mathematical relationship is why NNT is not a drug property but a population-and-drug property — it depends on who is being treated."

- question: "Why can't you directly apply an NNT derived from a clinical trial to a patient population with different baseline risk, and what calculation would you need to adjust?"
  type: short-answer
  answer: "Because NNT = 1/ARR, and ARR depends on the baseline event rate in the control group. A published NNT embeds a specific baseline risk. For a patient with different baseline risk, you must recalculate: estimate the expected ARR for your patient (baseline risk × relative risk reduction from the trial), then compute NNT = 1/new ARR. Without this adjustment, you will systematically underestimate NNT (overestimate benefit) for lower-risk patients and overestimate NNT for higher-risk patients."
  explanation: "This is the most clinically important limitation of published NNTs. The relative risk reduction from a trial may generalize to different populations, but the absolute risk reduction — and therefore the NNT — is population-specific. Clinicians must either apply the relative risk reduction to their patient's estimated baseline risk, or use a population-specific NNT from a subgroup analysis matching their patient's risk profile."
```

## Explainer

From your study of attributable risk, you know that absolute risk measures — unlike relative ones — answer the question of how much a risk actually changes. A relative risk reduction of 50% sounds identical whether the risk drops from 20% to 10% or from 0.002% to 0.001%, but the public health and clinical significance of those two scenarios are vastly different. The **number needed to treat (NNT)** is the tool that makes this concreteness automatic, by converting the absolute risk difference into the language of individual patients: how many people must receive this treatment to prevent one adverse outcome?

The calculation flows directly from your attributable risk knowledge. In a randomized trial, the **absolute risk reduction (ARR)** is simply the event rate in the control group minus the event rate in the treatment group: ARR = Risk_control − Risk_treatment. NNT = 1 / ARR. A concrete example: a trial of a cholesterol-lowering drug finds that over 5 years, 8% of patients in the placebo group had a heart attack, compared to 5% in the treated group. ARR = 0.08 − 0.05 = 0.03. NNT = 1/0.03 ≈ 33. You must treat 33 patients for 5 years to prevent one heart attack. **Number needed to harm (NNH)** is calculated identically but for adverse events: if the drug causes a serious side effect in 2% of treated patients and 0.5% of controls, ARR_harm = 0.015, NNH = 67.

The clinical power of these metrics lies in enabling direct comparison between benefit and risk. The NNT of 33 and NNH of 67 in this example mean that for every two patients harmed by the drug, roughly four are protected from a heart attack — a favorable ratio. The formal version of this comparison is the **likelihood of being helped vs. harmed (LHH)**, calculated as NNH / NNT. Values above 1 favor treatment; below 1, the harm exceeds the benefit. For patient communication, framing as "1 in 33 patients benefits from this drug" is often more intuitive and honest than "the drug reduces your heart attack risk by 38%" — the relative measure that pharmaceutical marketing typically emphasizes because it sounds more impressive.

One critical limitation is that NNT is not a fixed property of a drug — it depends on the population's **baseline risk** and the time horizon of the trial. The NNT above applies only to patients with 8% five-year MI risk treated for five years. Applied to a lower-risk population (say, 2% five-year risk) with the same relative risk reduction, ARR would be approximately 0.008 and NNT would jump to 125. The treatment is three to four times less efficient in absolute terms, even though the same trial's relative risk reduction still applies. This is why applying published NNTs uncritically to patients who differ from the trial population can be systematically misleading — the absolute benefit scales with baseline risk, so the same drug can range from highly efficient prevention to marginal benefit depending entirely on who is receiving it.
