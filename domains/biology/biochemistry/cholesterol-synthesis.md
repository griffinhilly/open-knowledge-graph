---
id: cholesterol-synthesis
title: Cholesterol Synthesis and Regulation
domain: biology
course: biochemistry
prerequisites:
- id: fatty-acid-synthesis
  type: soft
- id: enzyme-cofactors-and-coenzymes
  type: soft
- id: electrophilic-aromatic-substitution
  type: soft
builds-toward:
- membrane-lipids-and-lipoproteins
- metabolic-integration-hormonal-regulation
tags:
- cholesterol
- steroid synthesis
- HMG-CoA reductase
- mevalonate pathway
stage: advanced
status: draft
---

# Cholesterol Synthesis and Regulation

## Core Idea
Cholesterol is synthesized primarily in the liver from acetyl-CoA through a 30+ step pathway. The rate-limiting and irreversible step is catalyzed by HMG-CoA reductase, which converts HMG-CoA to mevalonate; this step is the target of statin drugs. Cholesterol synthesis is tightly regulated by allosteric feedback inhibition (cholesterol inhibits HMG-CoA reductase), by SREBP (sterol regulatory element binding protein), a transcription factor controlling gene expression, and by covalent modification of HMG-CoA reductase. Cholesterol is essential for cell membranes, steroid hormone synthesis, and bile acid synthesis.

## How It's Best Learned
Outline the cholesterol synthesis pathway from acetyl-CoA to mevalonate to cholesterol, highlighting the major branches (squalene synthesis, steroid nucleus formation). Understand why statins are so effective at lowering cholesterol and cardiovascular disease risk.

## Explainer

From your study of fatty acid synthesis, you know that the cell can build complex lipid molecules from the simple two-carbon building block acetyl-CoA, using NADPH as a reducing agent. Cholesterol synthesis follows the same logic but aims at a very different product: instead of a long hydrocarbon chain, the pathway constructs a rigid four-ring **steroid nucleus** — a flat, hydrophobic scaffold that is essential for membrane structure, steroid hormone production, and bile acid synthesis.

The pathway begins in the cytoplasm when two molecules of acetyl-CoA condense to form acetoacetyl-CoA, which then combines with a third acetyl-CoA to produce **HMG-CoA** (3-hydroxy-3-methylglutaryl-CoA). The next step is the one that matters most: **HMG-CoA reductase** converts HMG-CoA to **mevalonate**, consuming two molecules of NADPH. This is the **rate-limiting step** — the slowest reaction in the pathway and the point where regulation is concentrated. Everything downstream of mevalonate proceeds through a series of phosphorylation, decarboxylation, and condensation reactions that build isoprene units (five-carbon building blocks), join them into the 30-carbon linear molecule squalene, and then cyclize squalene into the four-ring steroid structure that, after further modifications, becomes cholesterol.

The regulation of this pathway is remarkably tight and operates at multiple levels, all converging on HMG-CoA reductase. First, cholesterol itself acts as a **feedback inhibitor**: when cholesterol levels in the cell are high, it directly suppresses HMG-CoA reductase activity. Second, the cell controls how much of the enzyme it makes through **SREBP** (sterol regulatory element-binding protein), a transcription factor embedded in the endoplasmic reticulum membrane. When cholesterol is abundant, SREBP stays trapped in the membrane and the gene for HMG-CoA reductase is not transcribed. When cholesterol drops, SREBP is cleaved and released, travels to the nucleus, and turns on transcription of the reductase gene. Third, the enzyme is regulated by **covalent modification** — phosphorylation inactivates it, dephosphorylation activates it — linking cholesterol synthesis to the cell's broader energy-sensing machinery.

This layered regulation explains why **statins** are such effective drugs. Statins are structural analogs of HMG-CoA that competitively inhibit HMG-CoA reductase, blocking the rate-limiting step. With less cholesterol being synthesized in liver cells, SREBP senses the deficit and upregulates LDL receptors on the cell surface, pulling more LDL cholesterol out of the bloodstream. The net effect — lower circulating LDL — is one of the most successful pharmacological interventions in modern medicine, and it follows directly from understanding where the pathway's control point sits and how the cell's feedback systems respond when that point is blocked.
