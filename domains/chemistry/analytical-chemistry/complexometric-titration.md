---
id: complexometric-titration
title: Complexometric Titrations (EDTA Methods)
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: titrimetric-analysis-intro
  type: hard
- id: chemical-equilibrium
  type: hard
- id: acid-base-chemistry
  type: soft
tags:
- EDTA
- chelate
- metal ion
- hardness
- conditional formation constant
stage: advanced
status: validated
---

# Complexometric Titrations (EDTA Methods)

## Core Idea
Complexometric titrations determine metal ion concentrations using chelating ligands, most commonly EDTA (ethylenediaminetetraacetic acid), which forms stable 1:1 complexes with nearly all metal ions. Because EDTA is a hexadentate ligand, complex stability depends strongly on pH; conditional formation constants (K′f) account for the fraction of EDTA in the uncomplexed form at a given pH. Metal ion indicators (e.g., Eriochrome Black T) form colored complexes with the analyte that are displaced by EDTA at the endpoint. Water hardness (total Ca²⁺ + Mg²⁺) is a classic application determined by EDTA titration.

## How It's Best Learned
Determine total water hardness and then individual calcium and magnesium concentrations by EDTA titration at different pH values. Constructing a pM titration curve analogous to a pH titration curve unifies complexometry with the general framework of titrimetric analysis.

## Common Misconceptions
- EDTA titrations must be buffered: pH control is not a minor detail but a thermodynamic requirement for the conditional formation constant to be favorable.
- Metal indicators that are themselves chelating agents can be blocked if metal concentrations are too high (indicator error).

## Explainer

From your study of titrimetric analysis, you know the basic architecture of a titration: a reagent of known concentration is added incrementally to an analyte until stoichiometric equivalence is reached, signaled by an indicator or instrument. Complexometric titrations apply this framework to metal ions, using a chelating agent — almost always **EDTA** — as the titrant. The key difference from acid-base or redox titrations is that the reaction here is complex formation: a metal ion and EDTA combine in a 1:1 molar ratio to form a stable, water-soluble chelate ring structure.

EDTA is uniquely suited to this role because it is a **hexadentate ligand** — it wraps around a metal ion using six donor atoms (four carboxylate oxygens and two amine nitrogens), forming an exceptionally stable complex in a single binding event. This 1:1 stoichiometry simplifies calculations enormously compared to ligands that form stepwise complexes at varying ratios. However, EDTA's six donor groups are also its complication: at low pH, the carboxylate and amine groups become protonated, reducing the fraction of EDTA available to bind metal ions. This is where your understanding of chemical equilibrium becomes essential.

The **conditional formation constant** (K′f) captures this pH dependence quantitatively. It equals the thermodynamic formation constant multiplied by αY⁴⁻, the fraction of EDTA in its fully deprotonated form at the working pH. At pH 10, nearly all EDTA is available for complexation and K′f is large; at pH 2, very little is deprotonated and K′f may be too small for a sharp endpoint. This means pH is not an incidental experimental condition — it is a thermodynamic lever that determines whether the titration works at all. Buffering the solution (typically with ammonia/ammonium chloride buffer at pH 10 for calcium and magnesium) is a fundamental requirement, not a convenience.

Endpoint detection uses **metallochromic indicators** like Eriochrome Black T (EBT), which are themselves weak chelating agents. Before the equivalence point, EBT binds free metal ions and displays one color (wine red for Mg²⁺). As EDTA is added, it strips metal from the indicator because the EDTA-metal complex is far more stable than the indicator-metal complex. At the endpoint, the last metal is pulled from the indicator, which reverts to its free color (blue for EBT). The classic application is **water hardness testing**: total hardness (Ca²⁺ + Mg²⁺) is determined by EDTA titration at pH 10, while calcium alone is measured at pH 12–13 where Mg(OH)₂ precipitates out of solution. The difference gives magnesium. This elegant use of pH to selectively mask one analyte while titrating another illustrates how equilibrium principles translate directly into analytical strategy.
