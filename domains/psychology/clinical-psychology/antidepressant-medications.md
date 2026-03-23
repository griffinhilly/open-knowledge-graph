---
id: antidepressant-medications
title: Antidepressant Medications
domain: psychology
course: clinical-psychology
prerequisites:
- id: mood-disorder-neurobiology
  type: hard
- id: psychopharmacology-basics
  type: hard
- id: serotonin-system
  type: hard
- id: monoamine-synthesis-and-catabolism
  type: hard
tags:
- antidepressants
- medication
- ssri
- snri
- psychopharmacology
stage: expert
status: validated
---

# Antidepressant Medications

## Core Idea
Antidepressants include SSRIs, SNRIs, tricyclics, MAOIs, and atypical agents, all targeting monoamine systems (serotonin, norepinephrine, dopamine). Despite mechanistic diversity, they show similar efficacy (~60% response rate) in MDD and anxiety disorders. They require 4-6 weeks for clinical effect; relapse risk is high upon discontinuation. Individual variation in response, side effects (sexual dysfunction, weight gain, activation), and drug interactions require individualized selection and monitoring.

## Questions

```yaml
- question: "An SSRI begins blocking serotonin reuptake within hours of the first dose, yet a patient shows no improvement in depression for 4–6 weeks. What best explains this delay?"
  type: multiple-choice
  options:
    - "SSRIs have poor bioavailability and require weeks of accumulation before reaching therapeutic plasma levels"
    - "Serotonin reuptake blockade alone is insufficient — clinical improvement requires gradual neuroadaptation: autoreceptor desensitization, changes in receptor expression, and BDNF-mediated neuroplasticity that accumulate over weeks of sustained elevated signaling"
    - "The delay is a placebo effect; the medication itself works immediately but patients take time to notice"
    - "The liver needs several weeks to convert SSRIs into their active metabolites"
  answer: 1
  explanation: "Reuptake blockade increases synaptic serotonin within hours — this is pharmacologically confirmed. But autoreceptors (especially 5-HT1A) initially dampen this effect by reducing neuronal firing. Over weeks, these autoreceptors desensitize, and downstream changes in receptor expression and neuroplasticity markers like BDNF accumulate. Clinical antidepressant effect correlates with these longer-timescale neuroadaptations, not with the initial reuptake block. This is why stopping medication prematurely is a major cause of treatment failure."

- question: "A patient with major depressive disorder is prescribed a standard SSRI at therapeutic dose. After 6 weeks of consistent use, they report no improvement. What does this most likely reflect?"
  type: multiple-choice
  options:
    - "The patient has not been taking the medication correctly — non-compliance is the only reason SSRIs fail"
    - "SSRIs are effective for anxiety but not for depression — a different drug class is needed"
    - "Non-response is expected in roughly 40% of patients on first-line treatment; individual variation in biology, genetics, and depression subtype means not everyone responds to any given agent"
    - "The dose is certainly too low — first-line SSRIs always work if the dose is sufficient"
  answer: 2
  explanation: "The ~60% response rate for antidepressants means approximately 40% of patients do not respond to a first-line agent. This non-response is not primarily explained by non-compliance or insufficient dosing — it reflects genuine biological heterogeneity: variation in which monoamine systems are dysregulated, in CYP450 enzyme genetics that affects drug metabolism, and in depression subtypes. Treatment-resistant depression requires escalating strategies including medication switches, augmentation, or non-pharmacological interventions."

- question: "Despite differing greatly in mechanism — SSRIs block SERT selectively, MAOIs prevent monoamine degradation entirely, and tricyclics block multiple transporters and receptors — all major antidepressant classes show roughly comparable overall efficacy in treating MDD."
  type: true-false
  answer: true
  explanation: "True — this is one of the most clinically important and theoretically puzzling findings in psychopharmacology. Across controlled trials, all major antidepressant classes achieve response rates of approximately 60% in MDD, despite targeting monoamine systems through very different mechanisms. This convergent efficacy suggests that what matters for antidepressant effect is sustained upregulation of monoaminergic tone and resulting neuroadaptation, rather than the specific mechanism by which monoamine levels are increased."

- question: "SSRIs work by increasing serotonin production in the presynaptic neuron."
  type: true-false
  answer: false
  explanation: "False — SSRIs do not affect serotonin synthesis or production. They block the serotonin transporter (SERT), which is responsible for reuptaking serotonin from the synapse back into the presynaptic neuron. Blocking SERT leaves more serotonin in the synapse for longer, increasing its availability for postsynaptic receptors. Serotonin is still synthesized from tryptophan via the same pathway as before; the SSRI only affects how quickly it is removed from the synaptic cleft."

- question: "Explain why the 4–6 week delay in antidepressant effect is clinically important and what it implies about the mechanism by which antidepressants relieve depression."
  type: short-answer
  answer: "Clinically, the delay matters because patients and clinicians need to know that early absence of improvement does not mean the medication isn't working — stopping too soon is a leading cause of treatment failure. It also means patients need monitoring for side effects or worsening during the lag period. Mechanistically, the delay implies that simple reuptake blockade (which happens within hours) is not the final therapeutic step. Instead, the antidepressant effect depends on slower neuroadaptive processes: autoreceptors that initially blunt the serotonergic increase gradually desensitize, receptor expression changes, and neuroplasticity-related proteins like BDNF require weeks of sustained elevated signaling to accumulate to therapeutically meaningful levels."
  explanation: "The 4–6 week timeline aligns with the time course of synaptic plasticity and receptor regulation, not pharmacokinetics. This has driven theories that depression involves impaired neuroplasticity (not just monoamine deficiency), and it is why newer fast-acting treatments like ketamine (which works within hours through NMDA receptor antagonism and rapid BDNF release) are so significant — they decouple antidepressant effect from the slow neuroadaptation timeline."
```

## Explainer

From your study of monoamine synthesis and catabolism, you know that serotonin, norepinephrine, and dopamine are inactivated primarily by two mechanisms: reuptake via transporter proteins (SERT, NET, DAT) and enzymatic degradation by monoamine oxidase (MAO). Every major antidepressant class targets one or more points in this system. The diversity of drug classes reflects different historical discoveries—often accidental—rather than a principled hierarchy of treatments.

**SSRIs** (selective serotonin reuptake inhibitors: fluoxetine, sertraline, escitalopram) block SERT, increasing synaptic serotonin availability with minimal effects on other transporters or receptors. Their selectivity produces a cleaner side-effect profile than older drugs. **SNRIs** (venlafaxine, duloxetine) block both SERT and NET, adding noradrenergic effects and showing some efficacy in chronic pain conditions. Older **tricyclic antidepressants** (amitriptyline, imipramine) block multiple transporters plus muscarinic, histaminergic, and adrenergic receptors—broadening efficacy but producing anticholinergic side effects (dry mouth, constipation, cognitive blunting) and dangerous cardiac effects in overdose. **MAOIs** (phenelzine, tranylcypromine) prevent degradation of all three monoamines simultaneously, making them potent but requiring strict dietary restriction to avoid hypertensive crises from dietary tyramine.

The 4–6 week lag to clinical effect is among the most clinically important and theoretically puzzling features of antidepressants. Reuptake blockade begins within hours of the first dose—monoamine levels rise almost immediately—yet depressive symptoms persist for weeks. The leading explanation involves **neuroadaptation**: autoreceptors that initially blunt the effect of increased monoamine availability (by reducing neuron firing) gradually desensitize; downstream receptor expression, synaptic structure, and neuroplasticity markers like **BDNF** (brain-derived neurotrophic factor) require sustained elevated signaling over weeks before meaningful change accumulates. This lag explains why stopping medication too soon (before the response has fully developed) is a common reason for treatment failure.

Individual variation in treatment response is large, and its sources are still incompletely understood. A patient whose depression involves primarily serotonergic dysregulation may respond to an SSRI; one with noradrenergic or dopaminergic involvement may not. Genetic variants in CYP450 enzymes (CYP2D6, CYP2C19) determine how quickly patients metabolize many antidepressants, producing wildly different effective doses at the same prescription level. The ~60% response rate also means that for 40% of patients, the first-line medication does not work—treatment-resistant depression requires escalating strategies: medication switches, augmentation with atypical antipsychotics or lithium, combination pharmacotherapy, or non-pharmacological interventions like electroconvulsive therapy (ECT) or TMS.
