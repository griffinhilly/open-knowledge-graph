---
id: half-reactions-and-balancing
title: Half-Reactions and Oxidation States
domain: chemistry
course: general-chemistry
prerequisites:
- id: oxidation-reduction-basics
  type: hard
- id: oxidation-numbers
  type: hard
- id: electrochemistry-oxidation-reduction-applications
  type: soft
- id: oxidation-state-and-oxidation-numbers
  type: hard
builds-toward:
- balancing-redox-equations
- galvanic-electrochemical-cells
tags:
- half-reactions
- oxidation
- reduction
stage: formal-systems
status: validated
---
# Half-Reactions and Oxidation States

## Core Idea
Half-reactions separate oxidation from reduction in redox reactions. The oxidation half-reaction shows electron loss; the reduction half-reaction shows electron gain. Balancing half-reactions is essential for balancing overall redox equations.

## How It's Best Learned
Practice writing half-reactions in acidic and basic solutions separately, then combining them.

## Questions

```yaml
- question: "You separate Zn + Cu²⁺ → Zn²⁺ + Cu into two half-reactions: Zn → Zn²⁺ + 2e⁻ and Cu²⁺ + 2e⁻ → Cu. When you add them together, what condition ensures the electrons cancel correctly?"
  type: multiple-choice
  options:
    - "The number of electrons produced in the oxidation half-reaction must equal the number consumed in the reduction half-reaction"
    - "The total charge on each side of both half-reactions must individually sum to zero"
    - "The electrons cancel automatically in any ionic redox reaction without needing to be equalized"
    - "The atoms of the oxidized element must equal the atoms of the reduced element in the combined equation"
  answer: 0
  explanation: "Electron conservation is the fundamental requirement: every electron released in the oxidation half-reaction must be accepted in the reduction half-reaction. In this example, both half-reactions involve exactly 2e⁻, so they cancel cleanly when added. When half-reactions have different electron counts (e.g., 3e⁻ for Mn reduction and 2e⁻ for Fe oxidation), you multiply each by the appropriate integer to equalize them before adding. Electrons never cancel 'automatically' — you must explicitly match the counts."

- question: "What is the correct sequence of steps for balancing a half-reaction in acidic aqueous solution?"
  type: multiple-choice
  options:
    - "Balance O with H₂O → balance H with H⁺ → balance all other atoms → balance charge with e⁻"
    - "Balance all atoms except O and H → balance O by adding H₂O → balance H by adding H⁺ → balance charge by adding e⁻"
    - "Balance charge with e⁻ → balance H with H⁺ → balance O with H₂O → balance remaining atoms"
    - "Add H₂O and H⁺ to the more negative side → balance atoms → balance charge with e⁻"
  answer: 1
  explanation: "The standard sequence is: (1) balance all atoms except O and H first; (2) balance O by adding H₂O to the oxygen-deficient side; (3) balance H by adding H⁺ to the hydrogen-deficient side; (4) balance charge by adding electrons to the more positive side. This order matters because H₂O introduces H atoms that must then be balanced, and you need the final atomic balance before you can balance charge. For basic solution, you then add OH⁻ equal to the number of H⁺ ions to both sides, converting H⁺ + OH⁻ → H₂O."

- question: "In any correctly balanced redox equation, the total number of electrons lost by the oxidized species must equal the total number of electrons gained by the reduced species."
  type: true-false
  answer: true
  explanation: "This is the conservation law at the heart of all redox chemistry: electrons are not created or destroyed, only transferred. The half-reaction method makes this explicit — you multiply each half-reaction by the integer that equalizes electron counts before adding. If the electrons don't cancel (same number on both sides when the half-reactions are added), the equation is not correctly balanced. This principle also underlies electrochemistry: in a galvanic cell, every electron leaving the anode (oxidation) arrives at the cathode (reduction)."

- question: "When balancing a redox reaction in basic solution, you should add OH⁻ ions to both sides first, before applying the standard acidic-solution balancing procedure."
  type: true-false
  answer: false
  explanation: "The correct order is reversed: balance the half-reaction using the acidic procedure first (balancing O with H₂O, H with H⁺, then charge with e⁻). Only afterward do you add OH⁻ — one OH⁻ for each H⁺ present — to both sides, converting each H⁺ + OH⁻ into H₂O. Then cancel any H₂O molecules that appear on both sides. Adding OH⁻ first complicates the procedure unnecessarily because you haven't yet established how many H⁺ ions need to be neutralized."

- question: "Why is the half-reaction method more powerful than trying to balance a complex redox equation directly, all at once?"
  type: short-answer
  answer: "A complex redox equation requires simultaneously satisfying mass balance for multiple elements and charge balance across many species — a combinatorially hard problem done by trial and error. The half-reaction method decomposes it: each half-reaction enforces mass balance and charge balance independently for just one electrode process, using a systematic step-by-step procedure. Once both halves are balanced, multiplying to equalize electron counts and adding guarantees conservation of both mass and charge in the combined equation. It also makes the electron transfer explicit — you can see exactly who is oxidized, who is reduced, and by how much — preventing the errors that arise when electrons are treated as implicit."
  explanation: "The half-reaction framework directly maps to electrochemistry: in a galvanic cell, oxidation and reduction literally occur at separate electrodes, and each half-reaction describes what happens at one electrode. The method thus teaches chemistry that is physically real, not just a balancing algorithm — and it scales to arbitrarily complex reactions that would be nearly impossible to balance by inspection."
```

## Explainer

From your study of oxidation-reduction basics and oxidation numbers, you know that redox reactions involve the transfer of electrons — one species is oxidized (loses electrons) while another is reduced (gains electrons). **Half-reactions** are the tool that makes this electron transfer explicit by splitting the overall reaction into two separate pieces: one showing only the oxidation and one showing only the reduction. Each half-reaction is balanced independently and shows the electrons as a product (oxidation) or reactant (reduction).

Consider the reaction between zinc metal and copper(II) sulfate solution, where zinc dissolves and copper metal plates out. The oxidation half-reaction is: Zn → Zn²⁺ + 2e⁻. Zinc loses two electrons, and its oxidation number increases from 0 to +2. The reduction half-reaction is: Cu²⁺ + 2e⁻ → Cu. Copper gains two electrons, and its oxidation number decreases from +2 to 0. When you add the two half-reactions together, the electrons cancel (2e⁻ appear on both sides), yielding the balanced overall equation: Zn + Cu²⁺ → Zn²⁺ + Cu. This cancellation is the key requirement — **electrons lost must equal electrons gained** — and it is what makes half-reactions so powerful for balancing complex redox equations.

Balancing half-reactions in aqueous solution requires a systematic procedure because oxygen and hydrogen atoms often need to be balanced using water molecules and H⁺ ions. In **acidic solution**, the steps are: (1) balance all atoms except O and H, (2) balance oxygen by adding H₂O, (3) balance hydrogen by adding H⁺, (4) balance charge by adding electrons to the more positive side. For **basic solution**, you follow the same four steps for acidic conditions, then add OH⁻ to both sides to neutralize every H⁺ into water, and cancel any water molecules that appear on both sides. For example, balancing the reduction of MnO₄⁻ to MnO₂ in basic solution: first balance in acid (MnO₄⁻ + 4H⁺ + 3e⁻ → MnO₂ + 2H₂O), then add 4OH⁻ to both sides to convert 4H⁺ into 4H₂O, yielding MnO₄⁻ + 2H₂O + 3e⁻ → MnO₂ + 4OH⁻.

Once both half-reactions are balanced, you combine them by multiplying each by the appropriate integer so that electron counts match, then adding and canceling species that appear on both sides. This method works for any redox reaction, no matter how complicated — it reduces a daunting balancing problem into two manageable pieces where conservation of mass and conservation of charge are enforced step by step. The half-reaction framework also directly connects to electrochemistry: in a galvanic cell, the two half-reactions literally occur at separate electrodes, making the electron transfer observable as an electric current.
