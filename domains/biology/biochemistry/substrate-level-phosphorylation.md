---
id: substrate-level-phosphorylation
title: Substrate-Level Phosphorylation
domain: biology
course: biochemistry
prerequisites:
- id: glycolysis-mechanism-and-regulation
  type: hard
- id: citric-acid-cycle-mechanism
  type: soft
- id: gibbs-free-energy-spontaneity
  type: soft
builds-toward:
- atp-synthesis
tags:
- ATP-synthesis
- phosphorylation
- glycolysis
stage: advanced
status: draft
---

# Substrate-Level Phosphorylation

## Core Idea
Substrate-level phosphorylation directly transfers a phosphoryl group from a high-energy substrate to ADP, forming ATP. In glycolysis, the 1,3-bisphosphoglycerate → 3-phosphoglycerate reaction couples oxidation to ATP synthesis. In the citric acid cycle, succinyl-CoA synthetase (GTP/ATP synthase) catalyzes the only substrate-level phosphorylation step.

## Explainer

From glycolysis and the citric acid cycle, you know that cells extract energy from fuel molecules through a series of enzyme-catalyzed reactions. From Gibbs free energy, you know that reactions proceed spontaneously when ΔG is negative, and that energy released by one reaction can be coupled to drive an otherwise unfavorable one. **Substrate-level phosphorylation** is the simplest and most direct way a cell makes ATP: an enzyme transfers a phosphoryl group straight from a high-energy substrate molecule onto ADP, producing ATP in a single catalytic step. No membrane, no proton gradient, no oxygen required.

The key requirement is a **high-energy phosphorylated intermediate** — a substrate whose phosphoryl group has a higher group-transfer potential than ATP itself. In glycolysis, the enzyme phosphoglycerate kinase catalyzes the transfer of the acyl-phosphate group from **1,3-bisphosphoglycerate** (1,3-BPG) to ADP, yielding ATP and 3-phosphoglycerate. This works because the preceding reaction (catalyzed by glyceraldehyde-3-phosphate dehydrogenase) oxidized an aldehyde to an acyl-phosphate, trapping the oxidation energy in that high-energy bond. A second substrate-level phosphorylation occurs later in glycolysis when **pyruvate kinase** transfers the phosphoryl group from phosphoenolpyruvate (PEP) — the highest-energy phosphorylated compound in common metabolism — to ADP. Together, these two steps account for all four ATP molecules produced in the payoff phase of glycolysis (two per step, since two three-carbon molecules pass through).

In the citric acid cycle, there is exactly one substrate-level phosphorylation: **succinyl-CoA synthetase** cleaves the high-energy thioester bond in succinyl-CoA and uses the released energy to phosphorylate GDP to GTP (or ADP to ATP, depending on the tissue-specific isoform). The GTP produced is energetically equivalent to ATP and can be converted to it by nucleoside diphosphate kinase.

It is important to contrast substrate-level phosphorylation with **oxidative phosphorylation**, which produces the vast majority of cellular ATP. Oxidative phosphorylation is indirect: electrons from NADH and FADH₂ flow through the electron transport chain, pumping protons across the inner mitochondrial membrane to create an electrochemical gradient, which ATP synthase then harnesses to drive ATP synthesis. Substrate-level phosphorylation, by contrast, is a direct, enzyme-catalyzed group transfer that works anywhere in the cell — in the cytoplasm during glycolysis or in the mitochondrial matrix during the citric acid cycle. This directness makes substrate-level phosphorylation essential for ATP production under anaerobic conditions, when the electron transport chain cannot operate and glycolysis becomes the cell's primary energy source.
