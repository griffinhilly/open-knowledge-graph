---
id: urea-cycle
title: The Urea Cycle
domain: biology
course: biochemistry
prerequisites:
- id: ammonia-metabolism
  type: hard
- id: citric-acid-cycle-mechanism
  type: soft
- id: organic-chemistry-intro
  type: soft
builds-toward:
- nitrogen-metabolism-integration
tags:
- urea
- nitrogen-disposal
- liver-metabolism
stage: advanced
status: draft
---

# The Urea Cycle

## Core Idea
The urea cycle is the primary pathway for nitrogen disposal, converting ammonia to urea in the liver. Five enzymes catalyze five reactions: carbamoyl phosphate synthetase I, ornithine transcarbamoylase, argininosuccinate synthetase, argininosuccinate lyase, and arginase. The cycle consumes 3 ATP and links to the citric acid cycle through fumarate.

## Explainer

From your study of ammonia metabolism, you know that amino acid degradation releases amino groups, which are ultimately converted to free ammonia (NH₃/NH₄⁺). Ammonia is toxic to the central nervous system — even modest elevations cause confusion and coma — so it must be disposed of rapidly. The **urea cycle**, operating exclusively in liver hepatocytes, solves this problem by packaging two nitrogen atoms into one molecule of **urea** (H₂N-CO-NH₂), a non-toxic, water-soluble compound that the kidneys excrete in urine.

The cycle spans two cellular compartments. It begins in the **mitochondrial matrix**, where **carbamoyl phosphate synthetase I** (CPS I) combines free ammonia with CO₂ and 2 ATP to form **carbamoyl phosphate**. This is the committed, rate-limiting step, and CPS I requires the allosteric activator **N-acetylglutamate** (NAG), which is synthesized when amino acid levels are high — a logical signal that nitrogen disposal is needed. Next, **ornithine transcarbamoylase** transfers the carbamoyl group to **ornithine**, producing **citrulline**, which is exported to the cytoplasm. From here, the remaining three reactions occur in the **cytoplasm**: argininosuccinate synthetase condenses citrulline with aspartate (consuming 1 ATP → AMP + PPᵢ, equivalent to 2 ATP equivalents) to form argininosuccinate; argininosuccinate lyase cleaves it into arginine and fumarate; and finally, **arginase** hydrolyzes arginine to produce urea and regenerate ornithine, which re-enters the mitochondria to begin another turn.

Notice two key features of the cycle's design. First, the two nitrogen atoms in urea come from different sources: one from free ammonia (via CPS I) and one from **aspartate** (via argininosuccinate synthetase). Aspartate is produced by transamination of oxaloacetate with glutamate, so the cycle is tightly linked to amino acid metabolism at multiple points. Second, the fumarate released by argininosuccinate lyase is a citric acid cycle intermediate — it can be converted to malate and then to oxaloacetate, which can be transaminated back to aspartate, creating the **aspartate-argininosuccinate shunt** that connects the urea cycle and citric acid cycle. This linkage means the two cycles share intermediates and are sometimes described as a "bicycle" that turns together.

The net energy cost of one turn of the urea cycle is **3 ATP** (2 consumed by CPS I, 1 consumed by argininosuccinate synthetase — though the latter yields AMP, so it costs the equivalent of 2 phosphoanhydride bonds, making the true cost 4 high-energy phosphate bonds). This is a significant expense, but it is the price of preventing ammonia toxicity. Clinical deficiencies in any of the five urea cycle enzymes result in **hyperammonemia**, which presents in neonates as lethargy, vomiting, and seizures. The most common inherited deficiency is ornithine transcarbamoylase deficiency (X-linked), which causes citrulline to be low and orotic acid to be elevated (because accumulated carbamoyl phosphate spills into the pyrimidine synthesis pathway). Understanding these biochemical signatures is how urea cycle defects are diagnosed.
