---
id: oxidative-deamination
title: Oxidative Deamination
domain: biology
course: biochemistry
prerequisites:
- id: amino-acid-structure-and-properties
  type: hard
- id: enzyme-cofactors-and-coenzymes
  type: hard
- id: oxidation-reduction-basics
  type: soft
builds-toward:
- urea-cycle
- ammonia-metabolism
- amino-acid-degradation-overview
tags:
- amino-acids
- redox-chemistry
- nitrogen-metabolism
stage: advanced
status: draft
---

# Oxidative Deamination

## Core Idea
Oxidative deamination removes the amino group from glutamate (or other amino acids) while oxidizing the carbon skeleton, producing the corresponding α-keto acid and ammonia. The reaction is catalyzed by glutamate dehydrogenase in mitochondria and is reversible, linking amino acid catabolism to ammonia metabolism.

## Explainer

When the body breaks down amino acids — whether from dietary protein or recycling of damaged cellular proteins — it faces a unique challenge that carbohydrate and fat metabolism do not: amino acids contain nitrogen, and that nitrogen must be removed before the carbon skeleton can be fed into energy-producing pathways. **Oxidative deamination** is the primary reaction that strips nitrogen from the amino acid pool and releases it as free ammonia (NH₄⁺).

The central player is the enzyme **glutamate dehydrogenase (GDH)**, located in the mitochondrial matrix. This enzyme catalyzes the removal of the amino group from glutamate, producing **α-ketoglutarate** (a citric acid cycle intermediate) and free ammonia. The reaction is an oxidation — the carbon that bore the amino group is oxidized as the nitrogen leaves — and it uses either NAD⁺ or NADP⁺ as the electron acceptor. Glutamate is the focal point because, as you know from amino acid structure, most amino acids do not undergo oxidative deamination directly. Instead, they first transfer their amino group to α-ketoglutarate via **transamination** (catalyzed by aminotransferases), funneling nitrogen from many different amino acids into a single molecule — glutamate. Oxidative deamination of glutamate then liberates the nitrogen as ammonia in one centralized reaction.

The reversibility of glutamate dehydrogenase is biologically significant. When ammonia levels are high and α-ketoglutarate is available, the reaction runs in reverse — **reductive amination** — incorporating free ammonia back into glutamate. This means GDH sits at a metabolic crossroads: it can either release nitrogen for excretion (via the urea cycle, which you will study next) or recapture it for biosynthesis of new amino acids. The direction depends on the cell's needs and the relative concentrations of substrates and products. GDH is allosterically regulated accordingly: GTP inhibits it (signaling sufficient energy), while ADP and leucine activate it (signaling a need for carbon skeletons or energy from amino acid catabolism).

The ammonia released by oxidative deamination is toxic at even modest concentrations — it can disrupt brain function by depleting α-ketoglutarate and altering neurotransmitter balance. This is why the reaction occurs in the mitochondria of the liver, where ammonia is immediately channeled into the **urea cycle** for safe conversion to urea and excretion by the kidneys. Oxidative deamination is therefore not just a disposal reaction; it is the critical junction that connects amino acid degradation to nitrogen excretion and, through α-ketoglutarate, links protein catabolism to the central energy-producing pathways of the cell.
