---
id: complexometric-titration-edta-methods
title: 'Complexometric Titration: EDTA and Related Methods'
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: complexometric-titration
  type: hard
- id: complex-ions-and-stability
  type: hard
- id: titrimetric-analysis-intro
  type: soft
builds-toward:
- analytical-method-validation-core-parameters
tags:
- complexometry
- EDTA
- metal-ion
- titration
- chelation
stage: advanced
status: draft
---

# Complexometric Titration: EDTA and Related Methods

## Core Idea
Complexometric titration with EDTA enables direct determination of metal ions (Ca²⁺, Mg²⁺, Zn²⁺, etc.) by chelation with high selectivity. Advanced applications include masking interfering ions with complexing agents, adjusting pH to control selectivity, using metallochromic indicators, and applying displacement titrations for individual metals in mixtures.

## How It's Best Learned
Determine individual metal ions in mixtures using selective masking agents and appropriate pH buffers.

## Common Misconceptions
Assuming EDTA is equally selective for all metal ions at any pH (selectivity depends heavily on pH and masking agents). Thinking metal ion order of addition doesn't matter in EDTA titrations.

## Explainer

From your work with complexometric titrations, you already know that EDTA is a hexadentate ligand — it wraps around a metal ion using six donor atoms (four carboxylate oxygens and two amine nitrogens) to form an extraordinarily stable 1:1 chelate complex. What makes EDTA the workhorse of quantitative metal analysis is this combination of high stability, consistent 1:1 stoichiometry regardless of the metal's charge, and the ability to titrate dozens of different metal ions with the same reagent. But the real analytical power emerges when you learn to control *which* metal EDTA reacts with, and that control comes primarily through pH.

The key concept is the **conditional formation constant**. EDTA exists in multiple protonation states depending on pH, and only the fully deprotonated form (Y⁴⁻) binds metals most effectively. At low pH, most of the EDTA is protonated and unavailable for chelation, so the effective formation constant drops dramatically. Different metals have different absolute formation constants with EDTA, so lowering the pH selectively weakens the weaker complexes first. For example, at pH 10, EDTA binds both Ca²⁺ and Mg²⁺ tightly enough to titrate them together (this gives you total water hardness). But at pH 12–13, the Mg(OH)₂ precipitates out of solution and the conditional constant for Mg-EDTA drops, allowing you to titrate Ca²⁺ alone. This pH-dependent selectivity is what transforms a single reagent into a versatile analytical tool.

**Metallochromic indicators** — compounds like Eriochrome Black T (EBT) and Calmagite — signal the endpoint by changing color when they release their bound metal ion to EDTA. Before the endpoint, the indicator is complexed with excess metal and shows one color (typically wine-red for EBT with Mg²⁺). At the endpoint, EDTA strips the last metal ions from the indicator, which reverts to its free form and changes color (blue for EBT). The indicator must bind the metal less tightly than EDTA does, or the color change never occurs — this is why indicator selection depends on which metal you are titrating and at what pH.

When a sample contains multiple metals, **masking agents** provide an additional layer of selectivity. Cyanide masks transition metals like Ni²⁺, Co²⁺, and Zn²⁺ by forming stable cyanide complexes that EDTA cannot displace, leaving alkaline earth metals free for titration. Fluoride masks Al³⁺ and Fe³⁺. **Displacement titrations** offer yet another approach: you can add excess Mg-EDTA to a sample containing a metal that forms a stronger EDTA complex, and that metal displaces the Mg²⁺, which you then titrate. These techniques — pH control, masking, displacement — combine to let you determine individual metals in complex mixtures with nothing more than a buret, a buffer, and carefully chosen reagents.
