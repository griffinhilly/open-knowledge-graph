---
id: psychopharmacology-basics
title: Psychopharmacology Basics
domain: psychology
course: biological-psychology
prerequisites:
- id: neurotransmitter-systems
  type: hard
- id: receptor-types-and-signaling
  type: hard
- id: synaptic-transmission
  type: soft
- id: neuromuscular-junction
  type: soft
- id: glial-cells-and-support
  type: soft
- id: pain-and-somatosensory-processing
  type: soft
builds-toward:
- agonists-and-antagonists
- drug-classes-and-effects
tags:
- pharmacokinetics
- pharmacodynamics
- blood-brain-barrier
- dose-response
- tolerance
stage: formal-systems
status: validated
---
# Psychopharmacology Basics

## Core Idea
Psychopharmacology studies how drugs alter brain function and behavior by interacting with neurotransmitter systems. Pharmacokinetics describes how the body processes a drug — absorption, distribution, metabolism, and excretion (ADME). Pharmacodynamics describes how the drug affects neural systems — its mechanism of action at receptors or transporters. The dose-response curve captures the relationship between dose and effect, with therapeutic windows, ceiling effects, and lethal doses all clinically relevant. Repeated drug exposure leads to tolerance (reduced response) through receptor downregulation or desensitization.

## How It's Best Learned
Trace the journey of a drug from administration to effect: oral ingestion → absorption → blood-brain barrier crossing → receptor binding → downstream neural effects → behavior. The blood-brain barrier's lipid solubility requirement explains why many potential drugs fail to reach the CNS.

## Common Misconceptions
- Tolerance is not the same as addiction; physical dependence (tolerance + withdrawal) can occur without compulsive drug-seeking.
- More drug is not always better — dose-response curves often have inverted-U shapes where moderate doses are most effective.

## Questions

```yaml
- question: "A patient takes an opioid pain medication daily for six months following surgery. If the drug is abruptly stopped, she experiences nausea, sweating, and intense pain. Her doctor says she has developed physical dependence. Does this mean she is addicted?"
  type: multiple-choice
  options:
    - "Yes — physical dependence and addiction are the same thing; both involve needing the drug to function normally"
    - "Yes — withdrawal symptoms are the defining feature of addiction"
    - "No — physical dependence (tolerance + withdrawal) can exist without the compulsive drug-seeking that defines addiction"
    - "No — addiction only applies to recreational drugs, not prescribed medications"
  answer: 2
  explanation: "Physical dependence means the body has adapted to the drug's presence such that removal causes withdrawal — a predictable physiological response. Addiction involves compulsive drug-seeking behavior despite negative consequences, involving psychological craving and loss of control. A patient on prescribed opioids who takes them as directed may be physically dependent (tolerance + withdrawal risk) without showing any addictive behavior. Conflating the two leads to undertreating pain patients out of misplaced fear of creating 'addicts.'"

- question: "A researcher is testing a new anti-anxiety compound. At low doses (10 mg) it reduces anxiety. At moderate doses (30 mg) it is maximally effective. At high doses (100 mg) it paradoxically increases anxiety and causes seizures. This pattern is best described as:"
  type: multiple-choice
  options:
    - "A linear dose-response curve, where effect scales proportionally with dose"
    - "Evidence of receptor antagonism at high doses"
    - "An inverted-U shaped dose-response curve with a narrow therapeutic window"
    - "Pharmacokinetic failure — the drug is being cleared too quickly at high doses"
  answer: 2
  explanation: "Many psychoactive drugs produce inverted-U (or biphasic) dose-response curves where moderate doses are most effective, lower doses are subtherapeutic, and higher doses produce diminished or reversed effects. This is not unusual — it often reflects receptor saturation, activation of inhibitory pathways, or off-target effects at high concentrations. The clinical implication is that 'more is better' is false for such drugs; the therapeutic window (range between effective and toxic doses) demands precise dosing. Lithium shows this pattern: narrow window between therapeutic and toxic serum levels."

- question: "A drug that is highly lipid-soluble will generally cross the blood-brain barrier more readily than a drug that is water-soluble."
  type: true-false
  answer: true
  explanation: "The blood-brain barrier consists of tightly joined endothelial cells with a lipid-rich environment. Passive diffusion across this barrier strongly favors small, lipid-soluble molecules, which can dissolve into and traverse the lipid membranes. Highly water-soluble compounds are largely excluded unless they have specific transport mechanisms. This is why morphine (lipid-soluble) produces rapid CNS effects while many large, polar molecules (like most antibiotics) fail to reach therapeutic concentrations in the CNS despite adequate plasma levels."

- question: "Tolerance to a drug develops because the drug is metabolized more quickly in the liver over repeated exposures, so less reaches the brain."
  type: true-false
  answer: false
  explanation: "While increased metabolic clearance (metabolic tolerance) can contribute to tolerance in some cases, the primary mechanism described in psychopharmacology is pharmacodynamic tolerance — the brain's neural adaptation to repeated drug exposure. When a drug repeatedly activates receptors, neurons compensate by downregulating receptor density, reducing receptor sensitivity (desensitization), or decreasing neurotransmitter synthesis. The drug reaches the brain in similar concentrations but produces a diminished response because the target system has recalibrated. The withdrawal symptoms when the drug is removed reflect this recalibration."

- question: "What is the difference between pharmacokinetics and pharmacodynamics, and why do you need both frameworks to understand how a psychoactive drug affects behavior?"
  type: short-answer
  answer: "Pharmacokinetics describes what the body does to the drug — absorption into the bloodstream, distribution to tissues including the brain, metabolism (usually in the liver), and excretion (ADME). Pharmacodynamics describes what the drug does to the brain — its mechanism of action at receptors, transporters, or ion channels. Both are needed because a drug's behavioral effect depends on (1) whether it reaches the brain in sufficient concentration (pharmacokinetics) and (2) what it does once there (pharmacodynamics). A drug with excellent pharmacodynamics but poor CNS penetration may fail entirely; knowing only the mechanism of action tells you nothing about onset, duration, or dosing."
  explanation: "For example, morphine and codeine both act on opioid receptors (similar pharmacodynamics), but codeine must first be metabolized to morphine in the liver before it is active — a pharmacokinetic difference that makes codeine slower-acting and dependent on the CYP2D6 enzyme. Understanding both frameworks is essential for predicting drug effects, dosing intervals, and individual variation in response."
```

## Explainer

You already understand neurotransmitters, receptors, and synaptic transmission. Psychopharmacology is built on a simple question: what happens when an exogenous chemical enters this system? To answer it, you need two complementary frameworks — what the body does to the drug (**pharmacokinetics**) and what the drug does to the brain (**pharmacodynamics**).

Pharmacokinetics follows the ADME sequence. A drug is **absorbed** into the bloodstream, **distributed** to tissues including the brain, **metabolized** (chemically transformed, often in the liver) into active or inactive compounds, and **excreted** (typically via urine). The critical gateway for psychoactive drugs is the **blood-brain barrier** — a tight junction of specialized endothelial cells that surrounds brain capillaries. Unlike most of the body, the CNS is highly selective about what it admits. The barrier's lipid-rich environment means only small, lipid-soluble molecules cross freely. This is why morphine reaches the brain rapidly (highly lipid-soluble) while many antibiotics do not. Route of administration matters too: intravenous injection bypasses absorption entirely, reaching peak blood concentrations immediately; oral ingestion is slower because the drug must survive stomach acid and first-pass liver metabolism before entering circulation.

Pharmacodynamics describes how the drug alters neural signaling once it arrives. Building on your receptor knowledge: drugs can act as **agonists** (mimicking the endogenous ligand by binding and activating the receptor), **antagonists** (binding without activating, blocking the endogenous ligand), or **reuptake inhibitors** (blocking the transporter that clears neurotransmitter from the synapse, thereby prolonging its effect). The **dose-response curve** captures the relationship between drug concentration and effect, characterized by the EC50 (dose producing half-maximal effect), the maximum effect (ceiling), and the therapeutic window — the range between effective and toxic doses. Narrow therapeutic windows require careful dosing; lithium, used for bipolar disorder, is notorious for this.

Repeated exposure produces **tolerance**: the same dose produces a diminished effect over time. Tolerance reflects the brain's attempt to maintain homeostasis. When a drug repeatedly floods dopamine receptors, neurons compensate by downregulating receptor density or reducing neurotransmitter synthesis — the brain recalibrates around the drug's presence. Remove the drug and the system is now under-activated relative to baseline: this is **withdrawal**, a state opposite in quality to the drug's acute effects. Stimulant withdrawal causes fatigue and depression; opioid withdrawal causes pain and anxiety. Crucially, tolerance and withdrawal together constitute **physical dependence** — but dependence is not the same as addiction. A patient on long-term opioids for chronic pain may be physically dependent (would experience withdrawal if abruptly stopped) without showing the compulsive drug-seeking that defines addiction. The distinction matters clinically and morally.
