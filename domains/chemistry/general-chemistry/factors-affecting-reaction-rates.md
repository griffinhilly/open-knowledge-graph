---
id: factors-affecting-reaction-rates
title: Factors Affecting Reaction Rates and Speed
domain: chemistry
course: general-chemistry
prerequisites:
- id: chemical-kinetics
  type: hard
builds-toward:
- activation-energy-catalysis-reaction-pathways
tags:
- rate
- kinetics
- temperature
- concentration
stage: formal-systems
status: draft
---

# Factors Affecting Reaction Rates and Speed

## Core Idea
Reaction rate depends on concentration (higher concentration increases collision frequency), temperature (increases molecular speed and collision energy), nature of reactants (molecular structure and bonding), surface area (for heterogeneous reactions), and presence of catalysts (provides alternative lower-energy pathway). Understanding these factors is essential for controlling reaction speed in synthesis and safety.

## Questions

```yaml
- question: "Temperature has a much larger effect on reaction rate than simply increasing collision frequency would predict. What is the primary reason?"
  type: multiple-choice
  options:
    - "Higher temperature increases the activation energy, making bonds more reactive"
    - "Higher temperature shifts the Maxwell-Boltzmann distribution so that a much larger fraction of molecules have energy exceeding the activation barrier — a small temperature rise can double the rate"
    - "Higher temperature increases molecular size, improving the probability that collisions occur with the correct orientation"
    - "Temperature primarily works by reducing solvent molecule concentration, clearing the path for productive collisions"
  answer: 1
  explanation: "The key insight is that most molecules at room temperature have energies below the activation barrier — they collide but don't react. The fraction that exceeds the threshold depends exponentially on temperature (via the Boltzmann factor e^{−Ea/RT}). Even a modest temperature increase disproportionately enlarges the high-energy tail of the Maxwell-Boltzmann distribution, so the fraction of productive collisions rises much faster than collision frequency alone. Temperature does not increase activation energy (option A) — it increases the fraction of molecules already above the fixed activation barrier. This exponential dependence explains why a 10°C rise can double the reaction rate."

- question: "A chemist adds a platinum catalyst to a reaction and observes the rate increase dramatically. A student concludes that the catalyst must have increased the collision frequency between reactants. What does the catalyst actually do?"
  type: multiple-choice
  options:
    - "The student is correct — the solid catalyst surface concentrates reactants, dramatically increasing collision frequency"
    - "The catalyst provides an alternative reaction pathway with lower activation energy, so a much larger fraction of existing collisions have enough energy to produce products"
    - "The catalyst raises the temperature of the reaction mixture by releasing stored chemical energy"
    - "The catalyst changes the equilibrium constant, shifting the reaction toward products and speeding up the forward rate"
  answer: 1
  explanation: "A catalyst works by providing an alternative mechanism — a different sequence of steps with a lower activation energy barrier. Because the activation energy is lower, a much larger fraction of collisions (which occur at the same frequency) now have sufficient energy to cross the barrier. Critically, a catalyst does not change the thermodynamics: ΔH and the equilibrium constant are unchanged, because the energy difference between reactants and products is unchanged (option D is wrong). The catalyst lowers the hill that molecules must climb, not the difference in elevation between the starting valley and the destination valley."

- question: "Adding a catalyst to a reaction changes both the reaction rate and the overall energy change (ΔH) of the reaction."
  type: true-false
  answer: false
  explanation: "A catalyst increases rate but does NOT change ΔH, the equilibrium constant, or the identity of the products. It provides an alternative pathway with lower activation energy — lowering the barrier between reactants and products — but the energy levels of the reactants and products themselves are unchanged. ΔH depends only on the difference in bond energies between reactants and products, which is independent of the path taken. A catalyst equally accelerates both the forward and reverse reactions (consistent with an unchanged equilibrium constant), which is why it cannot shift the final equilibrium position."

- question: "For a heterogeneous reaction involving a solid reactant, grinding the solid into a fine powder increases reaction rate by increasing the surface area available for collisions with the other reactant."
  type: true-false
  answer: true
  explanation: "In heterogeneous reactions (reactants in different phases), only surface atoms of the solid participate in collisions with the other reactant — the interior is inaccessible. Grinding into powder enormously increases the surface-area-to-volume ratio, proportionally increasing the number of reactive collision sites. This is why finely powdered metals can be highly reactive or even explosive while the same metal in bulk form is relatively inert — the same chemistry, but vastly different effective collision opportunities. This factor connects directly to the underlying principle: rate depends on how often effective collisions occur, and surface area directly controls that frequency for heterogeneous systems."

- question: "Explain why all five factors affecting reaction rate (concentration, temperature, nature of reactants, surface area, and catalysts) can be understood through a single unifying principle. What is that principle?"
  type: short-answer
  answer: "The unifying principle is: for a reaction to occur, reactant particles must collide with (1) sufficient energy to overcome the activation barrier and (2) the correct orientation to allow bond-breaking and bond-forming. Every factor works by changing one or both of these requirements. Concentration increases collision frequency (more molecules per volume = more collisions). Temperature increases the fraction of collisions with energy above the activation barrier (and slightly increases frequency). Nature of reactants determines the activation energy itself (how strong the bonds to be broken are). Surface area increases the number of accessible collision sites in heterogeneous reactions. Catalysts lower the activation energy, increasing the fraction of collisions that succeed without changing collision frequency."
  explanation: "Framing all five factors through this single collision principle makes the concepts predictive rather than just a memorized list. If a reaction is too slow, you can systematically ask: should I increase collision frequency (concentration, surface area), increase the energy of collisions (temperature), or lower the threshold energy needed (catalyst)? The 'nature of reactants' factor reminds you that some reactions are intrinsically fast (ion recombination in solution) or slow (breaking triple bonds) regardless of conditions — the activation energy is set by the chemistry itself, not by external manipulation."
```

## Explainer

Chemical kinetics, which you have already been introduced to, asks *how fast* a reaction proceeds and what controls that speed. The five major factors that influence reaction rate — concentration, temperature, nature of reactants, surface area, and catalysts — all connect back to one underlying principle: for a reaction to occur, reactant particles must collide with sufficient energy and in the correct orientation. Every factor on this list works by changing either how often molecules collide, how hard they collide, or how effectively those collisions lead to bond-breaking and bond-forming.

**Concentration** is the most intuitive factor. If you double the number of reactant molecules in a given volume, collisions become roughly twice as frequent, and the reaction speeds up. Think of it like a crowded dance floor versus an empty one — more people means more bumping into each other. **Temperature** has a subtler but more powerful effect. Raising the temperature does increase collision frequency slightly (molecules move faster), but the dominant effect is that a much larger fraction of collisions now carry enough energy to overcome the activation barrier. A common rule of thumb is that a 10°C increase roughly doubles the reaction rate, though this varies with the specific activation energy involved.

The **nature of the reactants** refers to how the identity and bonding of the molecules themselves affect reactivity. Reactions that require breaking strong covalent bonds (like the N≡N triple bond in nitrogen gas) proceed much more slowly than reactions involving weak bonds or ions in solution, which can rearrange almost instantly. This factor is intrinsic to the chemistry and cannot be easily manipulated, unlike concentration or temperature. **Surface area** matters specifically for heterogeneous reactions — those where reactants exist in different phases. A solid iron nail rusts slowly because only the surface atoms contact oxygen, but iron filings with enormously greater surface area can rust so rapidly they become a fire hazard. Grinding, powdering, or dissolving a solid reactant exposes more molecules to collisions.

Finally, **catalysts** accelerate reactions without being consumed, by providing an alternative reaction pathway that requires less energy to traverse. A catalyst does not change the thermodynamics of a reaction — the same products form, and the overall energy change (ΔH) is unchanged — but it lowers the energetic hill that reactant molecules must climb, allowing a much larger fraction of collisions to succeed. Understanding all five factors together gives you predictive power: if a reaction is too slow, you can systematically ask whether increasing concentration, raising temperature, increasing surface area, or adding a catalyst would be the most practical and safe intervention. This systematic thinking about rate control is foundational for everything from industrial chemical engineering to cooking.
