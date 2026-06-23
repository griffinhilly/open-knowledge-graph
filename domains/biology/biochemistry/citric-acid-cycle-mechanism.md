---
id: citric-acid-cycle-mechanism
title: 'Citric Acid Cycle: Mechanism and Stoichiometry'
domain: biology
course: biochemistry
prerequisites:
- id: krebs-cycle
  type: hard
- id: pyruvate-dehydrogenase-complex
  type: soft
- id: reaction-mechanisms-overview
  type: soft
- id: equilibrium-expression-kc-kp-constants
  type: soft
- id: oxidation-reduction-reactions
  type: hard
- id: organic-chemistry-intro
  type: soft
- id: oxidation-reduction-basics
  type: soft
- id: reduction-reactions-organic
  type: soft
- id: glycolysis-mechanism-and-regulation
  type: soft
- id: nad-nadh-structure-and-function
  type: soft
builds-toward:
- citric-acid-cycle-regulation
- oxidative-phosphorylation-and-chemiosmosis
tags:
- citric acid cycle
- Krebs cycle
- TCA cycle
- acetyl-CoA
- NADH
- FADH2
stage: formal-systems
status: validated
---

# Citric Acid Cycle: Mechanism and Stoichiometry

## Core Idea
The citric acid cycle (Krebs cycle) is an eight-step cycle that oxidizes the acetyl group of acetyl-CoA to 2 CO₂, generating 3 NADH, 1 FADH₂, and 1 GTP per acetyl-CoA. The cycle is catalytic (oxaloacetate is regenerated) and occurs in the mitochondrial matrix. Each step involves the chemistry of C=C addition (citrate synthase), isomerization (aconitase), oxidative decarboxylation (isocitrate and α-ketoglutarate dehydrogenases), substrate-level phosphorylation (succinyl-CoA synthetase), and oxidation (succinate and malate dehydrogenases).

## How It's Best Learned
Draw out all eight reactions of the citric acid cycle, noting the cofactors, substrates, and products. Calculate the total ATP yield when one acetyl-CoA is oxidized, accounting for NADH (2.5 ATP each) and FADH₂ (1.5 ATP each). Identify which intermediates are anaplerotic (replenish the cycle).

## Questions

```yaml
- question: "How many NADH molecules are produced per single turn of the citric acid cycle (per acetyl-CoA oxidized)?"
  type: multiple-choice
  options: ["1", "2", "3", "4"]
  answer: 2
  explanation: "Three NADH are produced per turn: one at isocitrate dehydrogenase, one at α-ketoglutarate dehydrogenase, and one at malate dehydrogenase. A common error is confusing the yield per acetyl-CoA (3 NADH) with the yield per glucose, which requires two turns (6 NADH total from the cycle)."

- question: "The two carbon atoms that enter the citric acid cycle as acetyl-CoA are the same two carbons that are released as CO₂ in the same turn of the cycle."
  type: true-false
  answer: false
  explanation: "This is a key misconception. The two carbons of acetyl-CoA are incorporated into citrate but are NOT the ones released as CO₂ in that same turn. CO₂ is released from the carbon skeleton of oxaloacetate at the isocitrate and α-ketoglutarate dehydrogenase steps. The newly added acetyl carbons are only lost as CO₂ in a subsequent turn."

- question: "Why is the citric acid cycle described as 'catalytic' with respect to oxaloacetate?"
  type: short-answer
  answer: "Oxaloacetate is consumed at the start of the cycle (by condensing with acetyl-CoA to form citrate) and regenerated at the end (by malate dehydrogenase). It is not net consumed — it acts as a molecular carrier that is continuously recycled, meaning a small amount can drive many rounds of oxidation."
  explanation: "This catalytic regeneration is what makes the cycle a cycle rather than a linear pathway. It also means that if oxaloacetate levels fall (e.g., during gluconeogenesis), the cycle slows — which is why anaplerotic reactions that replenish oxaloacetate (like the pyruvate carboxylase reaction) are essential for cycle flux."
```

## Explainer

The citric acid cycle is the cell's central hub for extracting chemical energy from carbon compounds. By the time a glucose molecule reaches this cycle, glycolysis has already broken it into two pyruvate molecules and pyruvate dehydrogenase has converted each into a two-carbon acetyl group attached to Coenzyme A. The cycle's job is to completely oxidize those two carbons — meaning it strips their electrons and hands them off to electron carriers (NAD⁺ and FAD) for use in the downstream electron transport chain.

The mechanism is cleverly catalytic. Oxaloacetate, a four-carbon molecule, condenses with the two-carbon acetyl group to form the six-carbon citrate. Over eight enzymatic steps, two carbons are released as CO₂, and the original oxaloacetate is regenerated. This means the cycle never "uses up" its oxaloacetate — a single molecule can shuttle through indefinitely. The actual fuel (acetyl carbons) is destroyed; the carrier (oxaloacetate) is preserved. This is exactly analogous to a catalyst in organic chemistry: it participates in the reaction without being net consumed.

The energy yield per turn is 3 NADH, 1 FADH₂, and 1 GTP (or ATP). On their own, these are modest. The power lies in the NADH and FADH₂: these are electron carriers that will donate electrons to the electron transport chain, where the enormous majority of ATP is generated via oxidative phosphorylation. Using current estimates (2.5 ATP per NADH, 1.5 ATP per FADH₂), each turn yields roughly 10 ATP equivalents — and glucose drives two turns.

A critical nuance about the CO₂: the two carbons released as CO₂ in any given turn are not the newly entered acetyl carbons — they come from the oxaloacetate skeleton. The acetyl carbons are incorporated into the cycle's intermediates and only emerge as CO₂ in a subsequent turn. This has been confirmed experimentally using isotopically labeled acetyl-CoA. It does not change the stoichiometry, but it matters for understanding flux and for interpreting tracer studies in metabolic research.

## Common Misconceptions

- One turn of the cycle processes one glucose molecule — false. One glucose yields two acetyl-CoA, so two full turns are required.
- The CO₂ released comes directly from the acetyl group — false (see above).
- GTP and ATP are equivalent in energy terms — essentially true, but GTP is produced here and can be interconverted with ATP via nucleoside diphosphate kinase.
