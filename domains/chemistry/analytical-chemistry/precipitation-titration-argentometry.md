---
id: precipitation-titration-argentometry
title: 'Precipitation Titration: Argentometry and Related Methods'
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: precipitation-titration
  type: hard
- id: solubility-product-constant-ksp
  type: hard
- id: titrimetric-analysis-intro
  type: soft
builds-toward:
- analytical-method-validation-core-parameters
tags:
- precipitation
- argentometry
- halide
- silver-nitrate
- titration
stage: advanced
status: draft
---

# Precipitation Titration: Argentometry and Related Methods

## Core Idea
Precipitation titration quantifies halide ions and other anions through their reaction with silver ion. Advanced techniques include Mohr method (indicator coprecipitation), Volhard method (back-titration with mercuric ion masking), and Fajans method (adsorption indicators), each suited to different analytes and matrices.

## How It's Best Learned
Perform Mohr, Volhard, and Fajans methods on different halide samples and compare results.

## Common Misconceptions
Assuming all three methods give identical results (they have different selectivities). Thinking indicator dye behavior is independent of temperature and ionic strength.

## Explainer

From your precipitation titration prerequisite, you understand the basic principle: when a titrant reacts with an analyte to form an insoluble precipitate, the equivalence point occurs when stoichiometric amounts have been mixed. From your knowledge of solubility product constants (Ksp), you understand what drives precipitation — the product of ion concentrations exceeding Ksp triggers solid formation. Argentometry applies these principles specifically to reactions involving **silver nitrate (AgNO₃)** as the titrant, exploiting the very low solubility of silver halides (AgCl, AgBr, AgI) and silver thiocyanate (AgSCN) to quantify halide ions and other anions.

The three classical argentometric methods differ primarily in how they detect the equivalence point. The **Mohr method** adds potassium chromate (K₂CrO₄) as an indicator. Throughout the titration, silver reacts preferentially with chloride (Ksp of AgCl ≈ 1.8 × 10⁻¹⁰) because AgCl is less soluble than Ag₂CrO₄ (Ksp ≈ 1.1 × 10⁻¹²). Once virtually all chloride has precipitated, the next drop of silver reacts with chromate to form a brick-red Ag₂CrO₄ precipitate — this color change signals the endpoint. The Mohr method works well for chloride and bromide in neutral to slightly basic solution, but it cannot be used in acidic conditions (chromate converts to dichromate) or for iodide (the dark AgI precipitate obscures the color change).

The **Volhard method** takes a back-titration approach, making it versatile for situations where direct titration is impractical. You add excess silver nitrate to the sample, then back-titrate the unreacted silver with potassium thiocyanate (KSCN) using ferric ion (Fe³⁺) as the indicator. When all excess Ag⁺ has precipitated as AgSCN, the next drop of thiocyanate forms a soluble red complex with Fe³⁺, signaling the endpoint. Because it works in acidic solution, the Volhard method handles samples that would decompose chromate or that require acid digestion. For chloride determination by Volhard's method, you must filter off the AgCl precipitate before back-titrating, because AgCl is more soluble than AgSCN and would slowly dissolve during the back-titration, consuming thiocyanate and causing a positive error.

The **Fajans method** uses an entirely different endpoint detection mechanism — **adsorption indicators** like fluorescein or dichlorofluorescein. Before the equivalence point, excess halide ions adsorb on the AgCl precipitate surface, giving it a negative charge. After the equivalence point, excess Ag⁺ adsorbs instead, making the surface positive. The positively charged surface then attracts the anionic indicator, and the adsorbed indicator changes color (fluorescein goes from yellow-green to pink). This method requires the precipitate to be colloidal (not heavily coagulated), so you typically add dextrin to stabilize the colloid. Each method has its niche: Mohr for straightforward chloride in neutral water, Volhard for acidic matrices and indirect determination of anions that form insoluble silver salts, and Fajans for rapid, direct titration when colloidal conditions can be maintained.
