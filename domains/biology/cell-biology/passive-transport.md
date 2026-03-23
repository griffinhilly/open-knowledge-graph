---
id: passive-transport
title: Passive Transport
domain: biology
course: cell-biology
prerequisites:
- id: cell-membrane-structure
  type: hard
builds-toward:
- active-transport
- cell-signaling-intro
tags:
- diffusion
- osmosis
- facilitated-diffusion
- transport
stage: formal-systems
status: validated
---

# Passive Transport

## Core Idea
Passive transport moves substances across the cell membrane down their concentration gradient without requiring cellular energy (ATP). Simple diffusion allows small nonpolar molecules (O₂, CO₂) to pass directly through the bilayer. Facilitated diffusion uses channel or carrier proteins for ions and polar molecules. Osmosis is the diffusion of water through a selectively permeable membrane toward regions of lower water potential (higher solute concentration).

## How It's Best Learned
Work through quantitative osmosis problems using the concepts of isotonic, hypotonic, and hypertonic solutions. Predict what happens to a red blood cell or plant cell in each environment and explain using water potential reasoning.

## Common Misconceptions
- Osmosis does not require aquaporins (it can occur through the bilayer itself), though aquaporins greatly accelerate it.
- Facilitated diffusion still moves molecules down their gradient — it's passive, just protein-assisted.

## Questions

```yaml
- question: "A red blood cell is placed in a solution with a much higher solute concentration than its cytoplasm (hypertonic). What will happen and why?"
  type: multiple-choice
  options: ["The cell will swell as water moves in by osmosis down its concentration gradient", "The cell will shrink as water moves out by osmosis toward lower water potential outside", "Solutes will rush into the cell through the membrane by simple diffusion", "Nothing will happen because the cell membrane blocks all movement"]
  answer: 1
  explanation: "In a hypertonic environment, the solute concentration is higher outside than inside the cell, which means water potential is lower outside. Water moves by osmosis from high water potential (inside) to low water potential (outside), causing the cell to lose water and shrink (crenate). This is a direct application of osmosis — water always moves toward higher solute concentration across a semipermeable membrane."

- question: "Facilitated diffusion requires the cell to expend ATP because transport proteins need energy to move molecules across the membrane."
  type: true-false
  answer: false
  explanation: "Facilitated diffusion is passive — no ATP is consumed. Transport proteins (channels or carriers) provide a pathway that lowers the energy barrier for crossing the membrane, but the driving force is still the concentration gradient. Molecules still move from high to low concentration spontaneously. ATP is only required for active transport, which moves substances *against* their gradient."

- question: "Explain why oxygen (O₂) can cross the cell membrane by simple diffusion, but glucose requires a transport protein (facilitated diffusion)."
  type: short-answer
  answer: "O₂ is a small, nonpolar molecule that dissolves readily in the lipid bilayer and passes directly through. Glucose is a large, polar molecule that cannot dissolve in the hydrophobic core of the membrane, so it requires a protein channel or carrier to provide a hydrophilic pathway."
  explanation: "The cell membrane's core is a nonpolar lipid bilayer. Small nonpolar molecules (O₂, CO₂, lipid-soluble vitamins) dissolve in this layer and cross freely. Large or polar molecules face a steep energy barrier because inserting them into the hydrophobic core is thermodynamically unfavorable. Membrane proteins solve this by creating hydrophilic tunnels or shuttling mechanisms — but crucially, these proteins do not add energy to the process, they just lower the barrier."
```

## Explainer

You already know from studying the cell membrane that the phospholipid bilayer is a selective barrier — hydrophobic in its core, hydrophilic at its surfaces. This structure is what makes passive transport possible: certain substances can cross it without any energy input from the cell, driven purely by concentration gradients.

The simplest form is **simple diffusion**: small, nonpolar molecules like O₂ and CO₂ dissolve directly into the lipid bilayer and pass through. They move from regions of high concentration to low concentration — the same thermodynamic principle (entropy increasing, free energy decreasing) that causes a drop of food coloring to spread through water. The membrane just provides the medium. No proteins involved, no energy required.

**Facilitated diffusion** works by the same logic — still down the concentration gradient, still no ATP — but uses membrane proteins to help molecules that cannot dissolve in the lipid core. Channel proteins form permanent hydrophilic pores (aquaporins for water, ion channels for Na⁺, K⁺, Cl⁻). Carrier proteins bind a specific molecule, change shape, and release it on the other side. The key point that trips people up: the word "facilitated" means *assisted*, not *energized*. The protein lowers the energy barrier for crossing, but the gradient does the work.

**Osmosis** is a special case of diffusion: the movement of *water* across a selectively permeable membrane. Water moves toward the side with lower water potential, which means toward higher solute concentration. In an isotonic solution, solute concentrations are equal on both sides and there is no net water movement. In a hypotonic solution (lower solute outside), water enters the cell and it swells. In a hypertonic solution (higher solute outside), water leaves and the cell shrinks. Plant cells experience this as turgor pressure or plasmolysis; animal cells experience swelling or crenation. Building the habit of thinking in terms of *water potential* (not just solute concentration) will serve you well when these concepts appear in more advanced physiology.

The contrast between passive and active transport comes next: active transport will introduce what happens when the cell needs to move substances *against* their gradient, which requires energy (ATP) and protein pumps. Keep in mind that passive transport sets the baseline — any movement requiring ATP is doing extra thermodynamic work precisely because it fights the spontaneous passive direction.

