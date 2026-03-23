---
id: electrochemistry-basics
title: Oxidation-Reduction Reactions
domain: chemistry
course: general-chemistry
prerequisites:
- id: ionic-bonding
  type: hard
- id: chemical-equations-balancing
  type: hard
- id: metallic-bonding
  type: soft
builds-toward:
- electrochemical-cells
tags:
- redox
- oxidation-state
- oxidizing-agent
- reducing-agent
- half-reaction
- activity-series
stage: formal-systems
status: validated
---
# Oxidation-Reduction Reactions

## Core Idea
Oxidation-reduction (redox) reactions involve the transfer of electrons between species: oxidation is loss of electrons (increase in oxidation state) and reduction is gain of electrons (decrease in oxidation state) — summarized as 'OIL RIG.' Oxidation states are formal electron-bookkeeping assignments governed by rules (fluorine is always −1; oxygen is usually −2, etc.). The half-reaction method for balancing redox equations separately balances oxidation and reduction halves (balancing atoms, then charge with electrons), then combines with appropriate coefficients.

## How It's Best Learned
Practice assigning oxidation states for atoms in a large variety of compounds and ions before attempting to balance redox equations. Balance redox equations systematically in both acidic (add H⁺ and H₂O) and basic (add OH⁻) solutions. Use the activity series to predict which single-displacement reactions are spontaneous.

## Common Misconceptions
- The oxidizing agent is the species that is reduced (gains electrons), and the reducing agent is the species that is oxidized (loses electrons) — the naming describes what is done to the other species, which is counterintuitive.
- Oxidation states are formal bookkeeping assignments, not actual charges on atoms — in covalent compounds, atoms rarely carry the integer charges their oxidation states imply.

## Questions

```yaml
- question: "In the reaction Zn + CuSO₄ → ZnSO₄ + Cu, zinc is oxidized. Which species is the oxidizing agent?"
  type: multiple-choice
  options:
    - "Zinc (Zn)"
    - "Copper ion (Cu²⁺)"
    - "Sulfate ion (SO₄²⁻)"
    - "Zinc sulfate (ZnSO₄)"
  answer: 1
  explanation: "The oxidizing agent is the species that causes oxidation by accepting electrons — it is the species that gets reduced itself. Cu²⁺ gains two electrons to become Cu(0), so it is reduced. Therefore Cu²⁺ is the oxidizing agent. Zinc loses electrons (is oxidized) making it the reducing agent. The naming is counterintuitive: the oxidizing agent is itself reduced."

- question: "An atom's oxidation state in a compound is equal to its actual electric charge."
  type: true-false
  answer: false
  explanation: "Oxidation states are a bookkeeping formalism, not measurements of real charge. They are assigned by applying a set of rules (e.g., shared electrons go to the more electronegative atom). In covalent compounds like CO₂, carbon has an oxidation state of +4, but it carries nothing close to a +4 charge — the electrons are shared, not transferred. Only in purely ionic compounds do oxidation states approximate actual charges."

- question: "What does 'OIL RIG' stand for, and why is each half of a redox reaction called a 'half-reaction'?"
  type: short-answer
  answer: "OIL RIG: Oxidation Is Loss (of electrons), Reduction Is Gain (of electrons). Each half-reaction is called that because it captures only one side of the electron transfer: the oxidation half shows the species losing electrons, and the reduction half shows the species gaining them. Together they sum to the complete redox reaction."
  explanation: "Separating a redox reaction into two half-reactions is useful because it lets you balance electrons, atoms, and charge independently in each half before combining. The number of electrons lost in oxidation must equal the number gained in reduction, which is enforced by multiplying the half-reactions by appropriate coefficients before adding."
```

## Explainer

Redox reactions are fundamentally about electron transfer. In any redox reaction, one species loses electrons and another gains them — the electrons do not simply disappear. The mnemonic "OIL RIG" encodes the definitions: Oxidation Is Loss of electrons, Reduction Is Gain of electrons. These two processes always occur together (you cannot have one without the other), which is why they are packaged as "oxidation-reduction." When iron rusts, iron loses electrons to oxygen; when a battery discharges, electrons flow from the anode (where oxidation occurs) to the cathode (where reduction occurs).

Oxidation states are a bookkeeping system that tracks where the electrons "go" in a redox reaction, especially in covalent compounds where electrons are shared rather than fully transferred. The rules for assigning oxidation states are conventions — not measurements. Fluorine is always −1 (most electronegative element). Oxygen is usually −2 (with exceptions like peroxides). Hydrogen is +1 when bonded to nonmetals, −1 when bonded to metals. Once you know these anchor rules, you can determine the oxidation state of any other atom using the constraint that oxidation states in a neutral compound must sum to zero, and in a polyatomic ion must sum to the ion's charge. A change in oxidation state is your signal that a redox reaction has occurred.

The naming of oxidizing and reducing agents confuses almost everyone at first because it describes what is done *to the other species*, not to the agent itself. The *oxidizing agent* is the species that oxidizes something else — and to do that, it must accept electrons, meaning it is itself reduced. The *reducing agent* is the species that reduces something else — and to do that, it must donate electrons, meaning it is itself oxidized. A reliable check: the oxidizing agent's oxidation state decreases (gains electrons); the reducing agent's oxidation state increases (loses electrons).

Balancing redox equations by the half-reaction method makes the electron accounting explicit. Write the oxidation half-reaction and balance atoms, then add electrons to the appropriate side to balance charge. Do the same for the reduction half-reaction. Then multiply each half-reaction by a coefficient so that the electrons in each half are equal — electrons cancel when you add the two halves together, leaving a balanced net ionic equation. In acidic solution you can add H⁺ and H₂O freely; in basic solution you use OH⁻.

The activity series predicts which single-displacement redox reactions are spontaneous. A more active metal will spontaneously reduce a less active metal's ion from solution. For example, zinc is more active than copper, so zinc displaces copper from CuSO₄ solution: Zn + Cu²⁺ → Zn²⁺ + Cu. This electron-transfer chemistry is the foundation of electrochemical cells — voltaic cells harness the energy released by spontaneous redox reactions to do electrical work, a topic you will explore next.
