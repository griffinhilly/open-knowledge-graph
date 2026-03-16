---
id: fatty-acid-synthesis
title: Fatty Acid Synthesis and Regulation
domain: biology
course: biochemistry
prerequisites:
- id: fatty-acid-oxidation-beta-oxidation
  type: hard
- id: pentose-phosphate-pathway
  type: soft
builds-toward:
- cholesterol-synthesis
- metabolic-integration-hormonal-regulation
tags:
- fatty acid synthesis
- acetyl-CoA carboxylase
- fatty acid synthase
- NADPH
stage: advanced
status: draft
---

# Fatty Acid Synthesis and Regulation

## Core Idea
Fatty acid synthesis (lipogenesis) is an anabolic pathway that builds fatty acids from acetyl-CoA units, primarily in the liver, adipose tissue, and mammary glands. The process requires acetyl-CoA carboxylase (catalyzes the first committed step, forming malonyl-CoA) and fatty acid synthase (a large multienzymatic complex catalyzing the iterative condensation, reduction, and dehydration of malonyl units). Unlike β-oxidation, synthesis uses NADPH (from the pentose phosphate pathway and malic enzyme) rather than NAD⁺/FAD. Fatty acid synthesis is allosterically activated by citrate and inhibited by AMP, palmitoyl-CoA, and glucagon.

## Explainer

If β-oxidation is the process of chopping fatty acids into two-carbon acetyl-CoA units, fatty acid synthesis is essentially the reverse challenge: stitching two-carbon units back together into a long hydrocarbon chain. But cells do not simply run β-oxidation backwards. Instead, fatty acid synthesis uses a completely different set of enzymes, a different cellular compartment (the cytoplasm rather than the mitochondrial matrix), and a different electron carrier — **NADPH** instead of NADH and FADH₂. This separation is a recurring theme in metabolism: catabolic and anabolic pathways for the same molecule are kept distinct so the cell can regulate them independently.

The pathway begins with a critical problem: acetyl-CoA is produced inside mitochondria, but synthesis happens in the cytoplasm. Acetyl-CoA cannot cross the inner mitochondrial membrane directly, so it is shuttled out as citrate (via the citrate shuttle), then regenerated in the cytoplasm. Once there, **acetyl-CoA carboxylase (ACC)** catalyzes the first committed step: adding a CO₂ to acetyl-CoA to form **malonyl-CoA**, a three-carbon activated building block. This carboxylation is the key regulatory point of the entire pathway — ACC is activated by citrate (signaling energy abundance) and inhibited by palmitoyl-CoA (the end product, providing feedback inhibition) and by phosphorylation driven by AMP-activated protein kinase when cellular energy is low.

From malonyl-CoA, the heavy lifting is done by **fatty acid synthase (FAS)**, a large homodimeric enzyme complex that carries the growing chain on an acyl carrier protein domain. Each cycle adds two carbons: malonyl-CoA condenses with the growing chain (releasing the CO₂ that was added by ACC), then the resulting β-keto group is reduced, dehydrated, and reduced again — four reactions per cycle, each consuming NADPH. After seven cycles, the 16-carbon saturated fatty acid **palmitate** is released. The NADPH consumed at each reduction step comes from two sources you already know: the **pentose phosphate pathway** (which produces NADPH in its oxidative phase) and the malic enzyme reaction that converts malate to pyruvate in the cytoplasm.

The regulation of fatty acid synthesis reflects the cell's overall energy state. When glucose is plentiful and energy stores are full, citrate accumulates in mitochondria and is exported to the cytoplasm, where it both provides the carbon source (via acetyl-CoA) and allosterically activates ACC. Insulin stimulates lipogenesis by activating ACC phosphatase, while glucagon and epinephrine suppress it by promoting ACC phosphorylation. This hormonal control ensures that the body synthesizes fat only when energy intake exceeds immediate needs — the biochemical basis of why chronic caloric surplus leads to fat accumulation.
