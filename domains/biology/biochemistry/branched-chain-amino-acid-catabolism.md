---
id: branched-chain-amino-acid-catabolism
title: Branched-Chain Amino Acid Metabolism
domain: biology
course: biochemistry
prerequisites:
- id: amino-acid-degradation-overview
  type: hard
- id: enzyme-cofactors-and-coenzymes
  type: soft
- id: functional-groups-overview
  type: soft
builds-toward:
- maple-syrup-urine-disease
tags:
- amino-acids
- leucine
- isoleucine
- valine
stage: advanced
status: draft
---

# Branched-Chain Amino Acid Metabolism

## Core Idea
Branched-chain amino acids (leucine, isoleucine, valine) are catabolized primarily in muscle, not liver, via transamination and oxidative decarboxylation by the branched-chain α-keto acid dehydrogenase complex. Leucine is purely ketogenic and a powerful activator of mTOR signaling; isoleucine and valine are glucogenic.

## Explainer

From your study of amino acid degradation, you know that each amino acid's carbon skeleton must be converted into a metabolic intermediate — either a citric acid cycle intermediate (glucogenic) or acetyl-CoA/acetoacetate (ketogenic) — before its energy can be harvested. The **branched-chain amino acids (BCAAs)** — leucine, isoleucine, and valine — are a special group because of two distinguishing features: their side chains branch rather than extending in a straight line, and their catabolism occurs primarily in skeletal muscle rather than in the liver where most other amino acids are degraded.

The first step in BCAA catabolism is **transamination** by branched-chain aminotransferase (BCAT), which transfers the amino group to α-ketoglutarate, producing glutamate and the corresponding **branched-chain α-keto acid**. This step is reversible and occurs in muscle and other peripheral tissues. The second step is the committed, irreversible reaction: **oxidative decarboxylation** by the **branched-chain α-keto acid dehydrogenase complex (BCKDH)**. If this enzyme complex sounds familiar from your cofactor studies, it should — BCKDH is structurally and mechanistically analogous to the pyruvate dehydrogenase complex and the α-ketoglutarate dehydrogenase complex. Like those enzymes, it requires five cofactors: thiamine pyrophosphate (TPP), lipoic acid, CoA, FAD, and NAD⁺. It removes CO₂ and generates an acyl-CoA product. BCKDH is regulated by phosphorylation (inactivation) and dephosphorylation (activation), providing fine control over the rate of BCAA breakdown.

After the BCKDH reaction, the three pathways diverge. **Leucine** is purely ketogenic: its carbon skeleton is ultimately converted to acetoacetate and acetyl-CoA, which can enter the citric acid cycle for energy but cannot be used for net glucose synthesis. This makes leucine unique among the common amino acids and particularly important during fasting, when its carbons contribute to ketone body production. **Valine** is purely glucogenic, yielding succinyl-CoA — a citric acid cycle intermediate that can feed into gluconeogenesis. **Isoleucine** is both glucogenic and ketogenic, producing both succinyl-CoA and acetyl-CoA.

The clinical significance of this pathway is dramatic. A deficiency in the BCKDH complex causes **maple syrup urine disease** (MSUD), named for the characteristic sweet odor of the accumulated branched-chain α-keto acids in urine. Without functional BCKDH, these keto acids accumulate to toxic levels, causing severe neurological damage if untreated. Beyond pathology, BCAAs — especially leucine — play a signaling role that extends beyond their caloric value. Leucine is a potent activator of the **mTOR pathway**, which stimulates muscle protein synthesis. This is why BCAAs are heavily marketed as exercise supplements: leucine directly signals muscle cells to build protein, independent of its role as a metabolic fuel. Understanding the BCAA pathway thus connects enzymology, metabolic logic, clinical medicine, and the molecular basis of muscle growth.
