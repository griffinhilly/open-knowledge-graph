---
id: osmosis-and-tonicity
title: Osmosis and Tonicity
domain: biology
course: cell-biology
prerequisites:
- id: cell-membrane-structure
  type: hard
- id: osmotic-water-balance
  type: hard
- id: colligative-properties
  type: soft
builds-toward:
- active-transport
- cell-senescence-aging
tags:
- membrane-transport
- water-balance
- solutes
stage: formal-systems
status: validated
---

# Osmosis and Tonicity

## Core Idea
Osmosis is the movement of water across a semipermeable membrane toward regions of higher solute concentration. Tonicity describes a solution's osmotic potential: hypertonic solutions cause cells to shrink, isotonic solutions maintain equilibrium, and hypotonic solutions cause cells to swell. Understanding tonicity is essential for predicting cellular responses to environmental osmotic stress.

## How It's Best Learned
Start with simple solutions of known solute concentrations, predict water movement direction, then observe actual cell behavior (e.g., red blood cells in different media). Use water potential calculations to quantify driving forces.

## Common Misconceptions
- Osmosis is water 'flowing toward salt'; it flows toward higher solute concentration, which can be any dissolved particle. - Tonicity depends only on solute concentration; actually it depends on membrane permeability too.

## Questions

```yaml
- question: "A red blood cell is placed in a solution with a very high salt concentration. What happens to the cell?"
  type: multiple-choice
  options:
    - "It swells and may burst (lyse) as water rushes in"
    - "It shrinks (crenates) as water moves out of the cell"
    - "Nothing changes — the cell membrane blocks salt from affecting it"
    - "It divides rapidly to restore osmotic balance"
  answer: 1
  explanation: "A high-salt solution is hypertonic relative to the cell interior. The solute concentration outside exceeds that inside, so water moves by osmosis out of the cell toward the higher external solute concentration. This causes the cell to shrink and wrinkle (crenate). Lysis (option A) is the opposite scenario — it occurs in hypotonic solutions when water rushes into the cell."

- question: "Two solutions with identical total solute concentrations usually have identical tonicity effects on a cell."
  type: true-false
  answer: false
  explanation: "Tonicity depends not only on solute concentration but also on membrane permeability to each solute. A solute that freely crosses the membrane (like urea) equilibrates across it and therefore does not sustain an osmotic gradient — it contributes nothing to effective tonicity. A solute that cannot cross (like NaCl in most contexts) maintains the gradient and drives net water movement. Two solutions with equal total solute concentrations can differ dramatically in tonicity if their solutes have different permeabilities."

- question: "A cell has an internal solute concentration of 0.3 M. It is placed in a 0.1 M external solution. In which direction will water move, and what term describes the external solution relative to the cell?"
  type: short-answer
  answer: "Water moves into the cell. The external solution is hypotonic relative to the cell — it has a lower solute concentration, so the cell has a lower water potential, drawing water inward by osmosis."
  explanation: "Osmosis always moves water toward higher solute concentration (lower water potential). Here the cell interior has more solutes, so it 'pulls' water inward. The external solution is hypotonic, meaning it has less solute than the cell. This can cause the cell to swell and, if unchecked, lyse."
```

## Explainer

From your study of cell membrane structure, you know that the plasma membrane is selectively permeable — it allows some molecules through while blocking others. Water is small enough to cross through aquaporin channels and by direct diffusion through the lipid bilayer. Solutes, by contrast, are often too large or charged to cross freely. This asymmetry is exactly what makes osmosis possible.

Osmosis is simply water moving down its own concentration gradient. When one side of a membrane has more dissolved solutes, that side has fewer free water molecules — the solutes "take up space" in solution. Water therefore moves toward the side with more solutes, driven by this difference in water concentration. Notice that osmosis is not really about solutes moving toward water; it is water moving toward solutes. The direction is always from lower solute concentration (higher water potential) to higher solute concentration (lower water potential).

Tonicity is the term we use to describe what a given solution does to a cell. Place a cell in a *hypertonic* solution (more solutes outside than inside) and water leaves the cell — it shrinks. Place it in a *hypotonic* solution (fewer solutes outside) and water enters the cell — it swells, potentially to the point of bursting (lysis in animal cells; in plant cells, the rigid wall prevents lysis and the cell becomes turgid instead). In an *isotonic* solution, the concentrations are matched and there is no net water movement, so the cell maintains its normal shape.

A critical refinement: tonicity is not just about concentration. It depends on which solutes cannot cross the membrane. Some small uncharged molecules, like urea, permeate membranes freely — they equilibrate on both sides, so they create no sustained osmotic gradient and do not affect tonicity. Only membrane-impermeant solutes (those the membrane actually blocks) drive net water movement. This is why tonicity is sometimes called "effective osmolarity" — it measures only the osmotically active, membrane-impermeant fraction.

Understanding tonicity is foundational for the active transport topics ahead. Cells constantly work to maintain their internal osmotic environment against external changes. When passive osmosis would drive water out (as in a hypertonic environment), cells must actively pump solutes or use energy-dependent transporters to compensate. The interplay between passive osmosis and active regulation of solute concentrations defines how cells survive osmotic stress.
