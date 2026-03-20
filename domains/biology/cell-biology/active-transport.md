---
id: active-transport
title: Active Transport
domain: biology
course: cell-biology
prerequisites:
- id: passive-transport
  type: hard
- id: enzyme-structure-and-function
  type: soft
- id: electrochemistry-basics
  type: soft
- id: endoplasmic-reticulum-and-golgi
  type: soft
builds-toward:
- cell-signaling-intro
tags:
- active-transport
- ATP
- pumps
- endocytosis
- exocytosis
stage: advanced
status: validated
---
# Active Transport

## Core Idea
Active transport moves substances against their concentration gradient, requiring energy in the form of ATP. Primary active transport directly uses ATP hydrolysis (e.g., the Na⁺/K⁺ ATPase pump). Secondary active transport couples the movement of one ion down its gradient to drive another molecule against its gradient (co-transport). Bulk transport (endocytosis and exocytosis) uses vesicles to move large molecules or particles into or out of the cell.

## How It's Best Learned
Trace the Na⁺/K⁺ pump cycle step-by-step: 3 Na⁺ out, 2 K⁺ in, 1 ATP hydrolyzed per cycle. Understand why this asymmetry is essential to nerve signal propagation. Then contrast with endocytosis to understand scale differences in transport.

## Common Misconceptions
- Active transport does not always move molecules from low to high concentration — it moves them against their electrochemical gradient, which incorporates both concentration and charge.
- Endocytosis brings material into the cell but does not deliver it directly to the cytoplasm — vesicles must fuse with other compartments first.

## Questions

```yaml
- question: "The Na⁺/K⁺ ATPase pump moves 3 Na⁺ out of the cell and 2 K⁺ into the cell per ATP hydrolyzed. What is the net electrical effect on the cell interior?"
  type: multiple-choice
  options: ["No net change, because ions are exchanged in both directions", "The interior becomes slightly more negative (hyperpolarization)", "The interior becomes slightly more positive (depolarization)", "The effect depends entirely on the current membrane potential"]
  answer: 1
  explanation: "3 positive charges leave and 2 positive charges enter per cycle, for a net outward movement of 1 positive charge. This makes the cell interior slightly more negative, contributing to the resting membrane potential. The pump is electrogenic — it moves charge, not just concentration."

- question: "Active transport always moves molecules from a region of low concentration to a region of high concentration."
  type: true-false
  answer: false
  explanation: "Active transport moves substances against their electrochemical gradient, which combines both concentration and electrical charge. For charged ions, a molecule can be at lower concentration inside the cell but the electrical gradient may favor its entry. The relevant driving force is the electrochemical potential, not concentration alone."

- question: "Explain the difference between primary and secondary active transport, and give an example of each."
  type: short-answer
  answer: "Primary active transport directly couples ATP hydrolysis to ion movement (e.g., the Na⁺/K⁺ ATPase pump). Secondary active transport uses the electrochemical gradient established by primary transport to drive a second molecule against its gradient (e.g., the sodium-glucose cotransporter SGLT, which uses the inward Na⁺ gradient to pull glucose into intestinal cells)."
  explanation: "Secondary active transport does not directly consume ATP, but it is still 'active' because it ultimately depends on the energy invested in creating the ion gradient by primary transport. This is why inhibiting the Na⁺/K⁺ pump eventually halts secondary transport as well."
```

## Explainer

From your study of passive transport and diffusion, you know that molecules naturally move down their concentration gradients — from regions of high concentration to low. Active transport breaks this rule: it moves substances *against* the gradient, which requires energy input. This is analogous to pumping water uphill — thermodynamically unfavorable without an external energy source, in this case ATP.

The most important example is the Na⁺/K⁺ ATPase pump, found in virtually every animal cell. Each pump cycle hydrolyzes one ATP molecule and uses the released energy to export 3 sodium ions out of the cell while importing 2 potassium ions. Because both ions are positively charged, this asymmetric exchange creates a net outward movement of charge, making the inside of the cell slightly more negative — a direct contribution to the resting membrane potential. This gradient matters enormously for neurons: the Na⁺ concentration difference established by the pump powers the rush of sodium into the cell during an action potential.

Not all active transport uses ATP directly. Secondary active transport harnesses the electrochemical gradients created by primary pumps to move other molecules. The sodium-glucose cotransporter in the intestinal wall is a classic example: it couples glucose transport to sodium moving *down* its gradient (inward), using the energy stored in that gradient to drag glucose *against* its gradient simultaneously. No ATP is consumed directly by this transporter — but the Na⁺/K⁺ pump must continuously run to maintain the sodium gradient it exploits. This is why blocking the Na⁺/K⁺ pump eventually shuts down glucose absorption too.

Bulk transport — endocytosis and exocytosis — operates at a completely different scale. Instead of moving individual ions through protein channels, the cell engulfs material or secretes cargo by reshaping its membrane into vesicles. Endocytosis wraps large molecules, particles, or even entire pathogens in a membrane pocket and pulls them into the cell. Critically, the material does not enter the cytoplasm directly — it arrives enclosed in an endosome, which must fuse with a lysosome or other compartment for further processing. Exocytosis runs the reverse: vesicles fuse with the plasma membrane to release contents outside (e.g., neurotransmitter release at a synapse).

The unifying principle across all forms of active transport is directionality achieved through energy investment. Whether the energy source is ATP hydrolysis, an ion gradient, or membrane deformation, active transport achieves something passive diffusion cannot: selective, regulated movement of specific substances against thermodynamic constraints — maintaining the precise internal environment required for life.
