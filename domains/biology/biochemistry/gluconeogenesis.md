---
id: gluconeogenesis
title: Gluconeogenesis and Blood Glucose Homeostasis
domain: biology
course: biochemistry
prerequisites:
- id: glycolysis-mechanism-and-regulation
  type: hard
- id: pyruvate-oxidation
  type: soft
builds-toward:
- metabolic-integration-hormonal-regulation
tags:
- gluconeogenesis
- glucose synthesis
- Cori cycle
- glucose-6-phosphatase
stage: advanced
status: draft
---

# Gluconeogenesis and Blood Glucose Homeostasis

## Core Idea
Gluconeogenesis is the metabolic synthesis of glucose from non-carbohydrate precursors (pyruvate, lactate, amino acids, glycerol) and occurs primarily in the liver and kidney. It essentially reverses glycolysis but bypasses three irreversible steps, using different enzymes (pyruvate carboxylase, PEPCK, fructose-1,6-bisphosphatase, glucose-6-phosphatase) to produce free glucose released into the bloodstream. Gluconeogenesis is active during fasting and is antagonistic to glycolysis, carefully regulated by reciprocal allosteric control.

## How It's Best Learned
Map the gluconeogenic pathway and identify which glycolytic steps are bypassed and which new enzymes catalyze the bypass reactions. Study the Cori cycle (lactate → glucose via gluconeogenesis in liver) and trace glucose synthesis from various precursors.

## Explainer

You already know glycolysis as the pathway that breaks glucose down to pyruvate, harvesting ATP and NADH in the process. Gluconeogenesis is essentially glycolysis running in reverse — it builds glucose from small precursors — but it cannot simply reverse all ten glycolytic reactions. Three steps in glycolysis are thermodynamically irreversible under cellular conditions (catalyzed by hexokinase, phosphofructokinase-1, and pyruvate kinase), so gluconeogenesis must bypass each of these with different enzymes. Understanding gluconeogenesis means understanding these three bypass points and why they exist.

The first bypass begins at the bottom of the pathway. Pyruvate kinase's conversion of PEP to pyruvate is irreversible, so gluconeogenesis uses a two-step detour. First, **pyruvate carboxylase** in the mitochondrial matrix converts pyruvate to oxaloacetate (OAA), consuming one ATP and requiring biotin as a cofactor. OAA is then converted to phosphoenolpyruvate (PEP) by **PEPCK** (phosphoenolpyruvate carboxykinase), consuming one GTP. This two-enzyme bypass is the committed entry point of gluconeogenesis. The second bypass replaces PFK-1: **fructose-1,6-bisphosphatase** simply hydrolyzes the phosphate that PFK-1 added, converting fructose-1,6-bisphosphate back to fructose-6-phosphate. The third bypass replaces hexokinase: **glucose-6-phosphatase**, found only in liver and kidney, hydrolyzes glucose-6-phosphate to free glucose, which is then released into the blood.

The precursors for gluconeogenesis come from several sources, and tracing them reveals how the body mobilizes fuel during fasting. Lactate, produced by exercising muscle and red blood cells, is converted back to pyruvate by lactate dehydrogenase in the liver — this is the **Cori cycle**, a metabolic relay between muscle and liver. Glucogenic amino acids (most amino acids) are converted to pyruvate or citric acid cycle intermediates, which feed into gluconeogenesis via OAA. Glycerol, released from fat breakdown in adipose tissue, enters the pathway at the level of dihydroxyacetone phosphate. Notably, fatty acids cannot be net precursors for glucose in animals because acetyl-CoA (the product of β-oxidation) cannot be converted to OAA — the two carbons entering the citric acid cycle as acetyl-CoA are lost as CO₂.

The regulation of gluconeogenesis is tightly reciprocal with glycolysis — when one is active, the other is suppressed. The key regulatory molecule is **fructose-2,6-bisphosphate**, which activates PFK-1 (glycolysis) and inhibits fructose-1,6-bisphosphatase (gluconeogenesis). During fasting, glucagon signaling lowers fructose-2,6-bisphosphate levels, releasing the brake on gluconeogenesis while simultaneously slowing glycolysis. Acetyl-CoA activates pyruvate carboxylase, linking fat oxidation to glucose production: when fatty acids are being burned, the resulting acetyl-CoA signals the liver to make glucose rather than oxidize pyruvate. This reciprocal regulation ensures the liver never wastes energy running both pathways simultaneously — a futile cycle that would simply hydrolyze ATP.
