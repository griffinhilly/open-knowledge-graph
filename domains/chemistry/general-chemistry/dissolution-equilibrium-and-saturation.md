---
id: dissolution-equilibrium-and-saturation
title: Saturated, Unsaturated, and Supersaturated Solutions
domain: chemistry
course: general-chemistry
prerequisites:
- id: solute-solvent-interactions-solvation
  type: hard
- id: chemical-equilibrium
  type: soft
builds-toward:
- solubility-product-constant-ksp-calculations
tags:
- saturation
- solubility
- equilibrium
- concentration
stage: formal-systems
status: validated
---

# Saturated, Unsaturated, and Supersaturated Solutions

## Core Idea
A saturated solution contains the maximum dissolved solute at a given temperature; the dissolution process and crystallization are in dynamic equilibrium. An unsaturated solution contains less solute and can dissolve more. A supersaturated solution temporarily contains more dissolved solute than saturation but is unstable and will crystallize when disturbed.

## Questions

```yaml
- question: "You add table salt to water until no more dissolves, then drop a small NaCl seed crystal into the saturated solution. What happens to the seed crystal?"
  type: multiple-choice
  options:
    - "It dissolves immediately — saturated solutions can still dissolve small additional amounts of solute"
    - "It remains unchanged — dynamic equilibrium means no net change occurs at the solid-solution interface"
    - "It grows rapidly — the excess dissolved NaCl crystallizes onto its surface until a new equilibrium is reached"
    - "The solution becomes supersaturated, storing the extra NaCl without visible change"
  answer: 1
  explanation: "In a saturated solution at equilibrium, dissolution and crystallization occur at equal rates — no net change in concentration. A seed crystal simply participates in this dynamic exchange: ions leave and rejoin the crystal constantly, but the crystal neither grows nor shrinks on net. Option A is wrong because the solution is already saturated — no additional dissolving can occur. Option C applies to supersaturated solutions, where excess solute crystallizes rapidly onto a seed. Option D describes how supersaturation is sustained, not what happens in a saturated solution."

- question: "A supersaturated sodium acetate solution sits undisturbed until a seed crystal is dropped in, triggering rapid crystallization. This happens because:"
  type: multiple-choice
  options:
    - "The seed crystal raises the local temperature, pushing the solubility curve below the current concentration"
    - "The seed crystal provides a nucleation site, removing the kinetic barrier that was preventing crystallization"
    - "The seed crystal chemically reacts with excess sodium acetate, converting it to solid form"
    - "The mechanical disturbance of adding the crystal releases thermal energy that drives crystallization"
  answer: 1
  explanation: "Supersaturation is a metastable state: the solution thermodynamically wants to crystallize (ion product exceeds Ksp) but lacks a nucleation site — a surface where the first crystal lattice can form. The seed crystal provides exactly this surface, unlocking the kinetic barrier. Once crystallization begins, it propagates rapidly as dissolved ions join the growing lattice, often releasing heat in the process. The system was not in equilibrium; it was trapped above equilibrium by the absence of nucleation sites."

- question: "In a saturated solution, dissolution has stopped because all the solute that can dissolve has already dissolved."
  type: true-false
  answer: false
  explanation: "This is the central misconception about saturated solutions. Saturation represents dynamic equilibrium: dissolution and crystallization are both occurring continuously at equal rates. Ions constantly leave the solid surface and enter solution, and ions from solution constantly rejoin the solid — the net concentration stays constant because the two processes balance, not because dissolution has stopped. If you isotopically labeled the solid, you would find labeled ions entering solution continuously even in a fully saturated system."

- question: "A supersaturated solution contains more dissolved solute than a saturated solution at the same temperature."
  type: true-false
  answer: true
  explanation: "By definition, a supersaturated solution temporarily holds more dissolved solute than the equilibrium (saturation) concentration at that temperature. This state is achieved by dissolving solute at high temperature (where solubility is greater) and cooling carefully without providing nucleation sites. The solution is metastable — thermodynamically unstable (ion product exceeds Ksp) but kinetically persistent because crystallization requires a nucleation site to begin."

- question: "Explain what 'dynamic equilibrium' means in a saturated solution, and why calling a saturated solution simply 'full' misses something important about what is happening at the molecular level."
  type: short-answer
  answer: "In a saturated solution, both dissolution (ions leaving the solid and entering solution) and crystallization (dissolved ions rejoining the solid) are occurring continuously — just at equal rates. The concentration stays constant not because nothing is happening, but because the two processes exactly balance. 'Full' implies a static state where dissolution has ceased; dynamic equilibrium means the system is actively exchanging ions between solid and dissolved phases at all times. This distinction explains supersaturation: the system can be driven above its equilibrium concentration if crystallization is kinetically blocked (no nucleation sites), something impossible to understand from a static 'full container' picture."
  explanation: "Dynamic equilibrium is the same concept as chemical equilibrium applied to a physical process, captured quantitatively by Ksp. A saturated solution is at Ksp; a supersaturated one has an ion product exceeding Ksp, making crystallization thermodynamically favorable. The static 'full' picture also cannot explain why solubility changes with temperature — because it misses that the equilibrium balance point between dissolution and crystallization rates shifts as temperature changes."
```

## Explainer

When you drop a spoonful of salt into water, the solute-solvent interactions you studied previously go to work: water molecules surround and pull apart the ions on the crystal surface, carrying them into solution. At first, dissolution is a one-way street — ions leave the solid and enter the liquid. But as more ions accumulate in solution, something else starts happening: dissolved ions occasionally collide with the surface of the remaining solid and reattach. This reverse process is **crystallization**, and its rate increases as the solution becomes more concentrated.

Eventually, the rate of dissolution equals the rate of crystallization. Ions are still leaving and rejoining the solid constantly, but the net concentration no longer changes. This is **dynamic equilibrium** — the same concept you encountered in chemical equilibrium, now applied to the physical process of dissolving. A solution at this point is called **saturated**: it holds the maximum amount of dissolved solute that the solvent can support at that temperature. If you add more solid to a saturated solution, it simply sits at the bottom undissolved, because every ion that enters the solution is matched by one that crystallizes out.

An **unsaturated** solution contains less dissolved solute than the equilibrium amount. There is still "room" for more solute, and if you add solid, it will dissolve. Most solutions you work with in the lab are unsaturated. A **supersaturated** solution, by contrast, contains *more* dissolved solute than the equilibrium concentration — a seemingly impossible state that arises when you dissolve solute at a high temperature (where solubility is greater) and then cool slowly and carefully. The excess solute stays dissolved because crystallization needs a nucleation site — a seed crystal or surface imperfection — to begin. The solution is metastable: thermodynamically it "wants" to crystallize, but kinetically it is trapped.

The dramatic nature of supersaturation becomes clear when you disturb it. Dropping a single seed crystal into a supersaturated sodium acetate solution triggers an explosive chain of crystallization as the excess solute crashes out all at once, often releasing heat in the process. This is not a chemical reaction — it is the system snapping from a metastable state to equilibrium. Understanding the distinction among these three states is essential for predicting when precipitation will occur, which connects directly to solubility product calculations and the quantitative treatment of dissolution equilibria.
