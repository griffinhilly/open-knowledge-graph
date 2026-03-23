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
stage: formal-systems
status: validated
---

# Precipitation Titration: Argentometry and Related Methods

## Core Idea
Precipitation titration quantifies halide ions and other anions through their reaction with silver ion. Advanced techniques include Mohr method (indicator coprecipitation), Volhard method (back-titration with mercuric ion masking), and Fajans method (adsorption indicators), each suited to different analytes and matrices.

## How It's Best Learned
Perform Mohr, Volhard, and Fajans methods on different halide samples and compare results.

## Common Misconceptions
Assuming all three methods give identical results (they have different selectivities). Thinking indicator dye behavior is independent of temperature and ionic strength.

## Questions

```yaml
- question: "A student uses the Volhard back-titration method to determine chloride content but skips the filtration step (leaving AgCl in solution during the back-titration with KSCN). What error does this introduce?"
  type: multiple-choice
  options:
    - "A negative error — extra AgCl consumes the silver titrant"
    - "A positive error — AgCl dissolves during back-titration, consuming extra thiocyanate"
    - "No error — AgCl is insoluble and does not participate in the back-titration"
    - "A negative error — AgCl adsorbs the ferric indicator, masking the endpoint"
  answer: 1
  explanation: "AgCl (Ksp ≈ 1.8 × 10⁻¹⁰) is more soluble than AgSCN (Ksp ≈ 1.1 × 10⁻¹²). As KSCN is added during the back-titration, it drives the dissolution of AgCl by consuming Ag⁺ and shifting the equilibrium. This dissolved Ag⁺ reacts with additional thiocyanate, causing the endpoint to come later than it should — a positive error in the chloride determination. This is why filtering or adding nitrobenzene to coat the AgCl is essential before back-titrating."

- question: "Why cannot the Mohr method (chromate indicator) be used in strongly acidic solution?"
  type: multiple-choice
  options:
    - "AgCl becomes more soluble in acid, preventing precipitation"
    - "Silver nitrate reacts with the acid instead of the halide"
    - "Chromate converts to dichromate in acid, making the indicator ineffective"
    - "The endpoint color change is masked by the acid's own color"
  answer: 2
  explanation: "Chromate (CrO₄²⁻) is in equilibrium with dichromate (Cr₂O₇²⁻) at lower pH. In acidic conditions, the equilibrium shifts toward dichromate, dramatically reducing the free [CrO₄²⁻]. Ag₂CrO₄ therefore requires much more excess Ag⁺ before it precipitates, making the endpoint come far too late and producing a large positive error. The Mohr method requires near-neutral to slightly basic conditions (pH 6.5–10)."

- question: "In the Fajans method, the adsorption indicator changes color because the precipitate surface charge reverses at the equivalence point."
  type: true-false
  answer: true
  explanation: "This is precisely the mechanism. Before the equivalence point, excess Cl⁻ ions adsorb on the AgCl precipitate surface, giving it a net negative charge that repels the anionic indicator dye. After the equivalence point, excess Ag⁺ adsorbs instead, making the surface positive. The positively charged surface now attracts the anionic indicator (e.g., fluorescein anion), and the adsorbed indicator changes color (yellow-green to pink). The color change is not due to a soluble complex forming in solution but to adsorption on the solid surface."

- question: "The Volhard method cannot be used in acidic solutions because the indicator decomposes under acidic conditions."
  type: true-false
  answer: false
  explanation: "This is the opposite of the truth — the Volhard method works specifically *because* it operates in acidic solution. It uses ferric ion (Fe³⁺) as the indicator, which is stable in acid, and the back-titration with KSCN proceeds cleanly. This acid compatibility is actually the Volhard method's key advantage over the Mohr method (which requires neutral pH). Acidic conditions also prevent the precipitation of Fe(OH)₃ and allow acid digestion of complex matrices before titration."

- question: "Why must the AgCl precipitate be filtered off before the thiocyanate back-titration in the Volhard determination of chloride, but this step is not necessary for iodide or bromide?"
  type: short-answer
  answer: "AgCl is more soluble than AgSCN (Ksp of AgCl > Ksp of AgSCN), so AgCl slowly dissolves as KSCN is added, consuming extra thiocyanate and causing a positive error. AgBr and AgI are less soluble than AgSCN, so they don't dissolve during the back-titration — they are stable to thiocyanate addition and the back-titration proceeds without interference."
  explanation: "The key is comparing Ksp values: AgI < AgBr < AgSCN < AgCl. For AgCl determination, AgCl dissolves in the presence of thiocyanate because AgSCN is less soluble — the more stable solid forms at the expense of the less stable one. For AgBr and AgI, the precipitate is already more stable than AgSCN, so no dissolution occurs. This solubility ordering is fundamental to understanding when the filtration step is required."
```

## Explainer

From your precipitation titration prerequisite, you understand the basic principle: when a titrant reacts with an analyte to form an insoluble precipitate, the equivalence point occurs when stoichiometric amounts have been mixed. From your knowledge of solubility product constants (Ksp), you understand what drives precipitation — the product of ion concentrations exceeding Ksp triggers solid formation. Argentometry applies these principles specifically to reactions involving **silver nitrate (AgNO₃)** as the titrant, exploiting the very low solubility of silver halides (AgCl, AgBr, AgI) and silver thiocyanate (AgSCN) to quantify halide ions and other anions.

The three classical argentometric methods differ primarily in how they detect the equivalence point. The **Mohr method** adds potassium chromate (K₂CrO₄) as an indicator. Throughout the titration, silver reacts preferentially with chloride (Ksp of AgCl ≈ 1.8 × 10⁻¹⁰) because AgCl is less soluble than Ag₂CrO₄ (Ksp ≈ 1.1 × 10⁻¹²). Once virtually all chloride has precipitated, the next drop of silver reacts with chromate to form a brick-red Ag₂CrO₄ precipitate — this color change signals the endpoint. The Mohr method works well for chloride and bromide in neutral to slightly basic solution, but it cannot be used in acidic conditions (chromate converts to dichromate) or for iodide (the dark AgI precipitate obscures the color change).

The **Volhard method** takes a back-titration approach, making it versatile for situations where direct titration is impractical. You add excess silver nitrate to the sample, then back-titrate the unreacted silver with potassium thiocyanate (KSCN) using ferric ion (Fe³⁺) as the indicator. When all excess Ag⁺ has precipitated as AgSCN, the next drop of thiocyanate forms a soluble red complex with Fe³⁺, signaling the endpoint. Because it works in acidic solution, the Volhard method handles samples that would decompose chromate or that require acid digestion. For chloride determination by Volhard's method, you must filter off the AgCl precipitate before back-titrating, because AgCl is more soluble than AgSCN and would slowly dissolve during the back-titration, consuming thiocyanate and causing a positive error.

The **Fajans method** uses an entirely different endpoint detection mechanism — **adsorption indicators** like fluorescein or dichlorofluorescein. Before the equivalence point, excess halide ions adsorb on the AgCl precipitate surface, giving it a negative charge. After the equivalence point, excess Ag⁺ adsorbs instead, making the surface positive. The positively charged surface then attracts the anionic indicator, and the adsorbed indicator changes color (fluorescein goes from yellow-green to pink). This method requires the precipitate to be colloidal (not heavily coagulated), so you typically add dextrin to stabilize the colloid. Each method has its niche: Mohr for straightforward chloride in neutral water, Volhard for acidic matrices and indirect determination of anions that form insoluble silver salts, and Fajans for rapid, direct titration when colloidal conditions can be maintained.
