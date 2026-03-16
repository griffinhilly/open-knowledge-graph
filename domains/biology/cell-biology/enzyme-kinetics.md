---
id: enzyme-kinetics
title: Enzyme Kinetics
domain: biology
course: cell-biology
prerequisites:
- id: enzyme-structure-and-function
  type: hard
- id: chemical-kinetics
  type: soft
- id: chemical-equilibrium
  type: soft
- id: graphing-rational-functions
  type: soft
- id: rate-law-determination
  type: soft
- id: differential-equations-intro
  type: soft
- id: reaction-rate-and-factors-affecting-rate
  type: soft
- id: integrated-rate-laws
  type: soft
builds-toward:
- glycolysis
- krebs-cycle
tags:
- michaelis-menten
- Vmax
- Km
- inhibition
- kinetics
stage: abstract-reasoning
status: validated
---

# Enzyme Kinetics

## Core Idea
Enzyme kinetics describes the rate of enzyme-catalyzed reactions quantitatively. The Michaelis-Menten model relates reaction velocity to substrate concentration: V = Vmax[S] / (Km + [S]), where Vmax is maximum velocity and Km (Michaelis constant) approximates the substrate concentration at half-maximal velocity. Inhibitors slow enzyme activity: competitive inhibitors bind the active site, raising apparent Km; noncompetitive inhibitors bind elsewhere, lowering Vmax. Allosteric regulation adjusts enzyme activity through conformational changes.

## How It's Best Learned
Plot V vs [S] curves and practice interpreting Vmax and Km from graphs. Add inhibitor curves and reason through which type of inhibition is present. Lineweaver-Burk plots provide an alternative linear representation useful for distinguishing inhibition types.

## Common Misconceptions
- Km is not a direct measure of enzyme affinity — it's the [S] at half-Vmax, which approximates affinity when the dissociation step is slow.
- Competitive inhibition can be overcome by adding more substrate; noncompetitive inhibition cannot.

## Questions

```yaml
- question: "An inhibitor raises the apparent Km of an enzyme but does not change Vmax. Adding more substrate eventually restores the original reaction rate. What type of inhibitor is this?"
  type: multiple-choice
  options: ["Noncompetitive inhibitor", "Competitive inhibitor", "Irreversible inhibitor", "Allosteric activator"]
  answer: 1
  explanation: "A competitive inhibitor binds the active site and competes with substrate. A raised Km means more substrate is needed to achieve half-maximal velocity, but at saturating substrate concentrations the inhibitor is outcompeted and Vmax is reached. Noncompetitive inhibitors lower Vmax and cannot be overcome by adding substrate."

- question: "Adding more substrate can overcome noncompetitive inhibition and restore the enzyme's maximum reaction velocity."
  type: true-false
  answer: false
  explanation: "Noncompetitive inhibitors bind at an allosteric site distinct from the active site. Substrate and inhibitor are not competing for the same binding location, so flooding the reaction with substrate does not displace the inhibitor. Vmax is permanently reduced as long as the inhibitor is present, regardless of substrate concentration."

- question: "At a substrate concentration equal to Km, what fraction of the enzyme's maximum velocity is being achieved, and what does this tell you about enzyme active site occupancy?"
  type: short-answer
  answer: "At [S] = Km, the reaction velocity equals Vmax/2 — half the maximum rate. This corresponds to approximately half the enzyme active sites being occupied by substrate at any given moment."
  explanation: "This follows directly from the Michaelis-Menten equation: V = Vmax[S]/(Km + [S]). Substituting [S] = Km gives V = Vmax·Km/(2Km) = Vmax/2. Km is therefore defined as the substrate concentration that produces half-maximal velocity, which under steady-state assumptions reflects ~50% active site occupancy."
```

## Explainer

From your study of enzyme structure and function, you know that enzymes are catalysts that lower activation energy by binding substrates at the active site and stabilizing the transition state. Enzyme kinetics asks a quantitative follow-up: *how fast* does an enzyme work, and *what controls that rate?*

At very low substrate concentrations, most enzyme active sites are empty and reactions are slow — every substrate molecule that diffuses to an active site gets processed quickly because there is always a free site waiting. As substrate concentration increases, active sites fill more of the time and the rate increases. But the rate cannot increase forever: once every active site is occupied at all times (enzyme **saturation**), adding more substrate has no effect. The maximum rate at saturation is **Vmax**, and it depends on the amount of enzyme and how fast each enzyme molecule can process substrate (its turnover number, kcat).

The **Michaelis constant** Km is the substrate concentration at which the reaction proceeds at half of Vmax. It is *not* simply an affinity constant, though it approximates affinity in many cases: a low Km means the enzyme reaches half-Vmax at low substrate concentrations (efficient binding), while a high Km means the enzyme needs lots of substrate to reach half-maximal velocity. The Michaelis-Menten equation — V = Vmax[S]/(Km + [S]) — captures the entire hyperbolic relationship between velocity and substrate concentration. On a V vs [S] graph, the curve rises steeply at first, then flattens as it approaches Vmax asymptotically.

Inhibitors modify this picture in distinct ways. A **competitive inhibitor** resembles the substrate and occupies the active site, blocking substrate access. It raises the apparent Km (more substrate is needed to compete the inhibitor out) but leaves Vmax intact — at sufficiently high substrate concentrations, the substrate wins. A **noncompetitive inhibitor** binds a separate allosteric site and distorts the enzyme's shape, slowing catalysis regardless of what's in the active site. The Km stays the same (substrate can still bind), but Vmax drops because each bound substrate is processed more slowly. You cannot "outcompete" a noncompetitive inhibitor with more substrate. This distinction — can more substrate rescue activity? — is the key diagnostic question.

These concepts directly set up your study of metabolic pathways. In glycolysis and the Krebs cycle, enzymes are regulated precisely through inhibition and allosteric modulation to match the cell's energy demands. Understanding kinetics means you can predict what happens when a metabolite accumulates, when ATP is plentiful versus scarce, or when a drug targets a specific enzyme — the equations turn biological control into something you can reason about quantitatively.
