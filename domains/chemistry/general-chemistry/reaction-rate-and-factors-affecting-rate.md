---
id: reaction-rate-and-factors-affecting-rate
title: Reaction Rate and Factors Affecting Reaction Speed
domain: chemistry
course: general-chemistry
prerequisites:
- id: chemical-kinetics
  type: hard
builds-toward:
- rate-law-determination
- collision-theory-advanced-kinetics
tags:
- reaction rate
- rate factors
- concentration
- temperature
- catalyst
stage: formal-systems
status: draft
---

# Reaction Rate and Factors Affecting Reaction Speed

## Core Idea
Reaction rate is the change in concentration over time. Concentration, temperature, surface area, and catalysts all affect reaction speed by altering collision frequency and molecular energy.

## How It's Best Learned
Observe how changing one factor at a time affects reaction rate in experiments or simulations.

## Questions

```yaml
- question: "Two identical samples of hydrogen peroxide decompose: Sample A at 25°C and Sample B at 35°C. Sample B decomposes approximately twice as fast. What is the dominant reason for this rate increase?"
  type: multiple-choice
  options:
    - "At 35°C, molecules move faster and collide more frequently"
    - "At 35°C, a greater fraction of molecules have enough energy to overcome the activation energy barrier"
    - "At 35°C, the activation energy of the reaction is lower"
    - "At 35°C, the solution volume expands slightly, increasing the effective concentration"
  answer: 1
  explanation: "While higher temperature does increase collision frequency slightly, the dominant effect is the Boltzmann factor: the fraction of molecules whose kinetic energy exceeds the activation energy Ea grows exponentially with temperature. The Maxwell-Boltzmann energy distribution shifts to higher energies, dramatically increasing the proportion of molecules in the high-energy tail that can overcome Ea. This exponential sensitivity explains why a modest 10°C increase can double or triple rates for many reactions. Option C is wrong — temperature does not lower the activation energy. That is what catalysts do. Activation energy is a property of the reaction pathway, not of temperature."

- question: "A student adds a catalyst to a reversible reaction at equilibrium and later observes that the equilibrium concentrations are unchanged after re-equilibration. She concludes: 'The catalyst must have malfunctioned because it didn't shift the equilibrium.' What is wrong with her reasoning?"
  type: multiple-choice
  options:
    - "She is correct — a working catalyst should increase product concentrations at equilibrium"
    - "Catalysts lower the activation energy equally for both forward and reverse reactions, so the equilibrium position is unchanged — only the rate of reaching equilibrium increases"
    - "Catalysts only work on irreversible reactions and cannot affect equilibria"
    - "The catalyst shifted the equilibrium, but she didn't wait long enough to observe the change"
  answer: 1
  explanation: "This is the critical misconception about catalysts. A catalyst provides an alternative reaction pathway with lower activation energy, but it lowers Ea equally for both the forward and reverse reactions. Equilibrium position is determined by ΔG° — the thermodynamic free energy difference between reactants and products — not by kinetic energy barriers. Since the catalyst doesn't change ΔG°, it cannot change the equilibrium constant K or the equilibrium concentrations. It only changes how fast the system reaches that equilibrium. The student's catalyst worked perfectly; her expectation was wrong. To shift the equilibrium, you need to change temperature or concentrations (Le Chatelier's principle), not add a catalyst."

- question: "Grinding a solid reactant into fine powder increases reaction rate because it exposes more surface area, allowing more reactant molecules to participate in collisions at any given moment."
  type: true-false
  answer: true
  explanation: "For reactions involving solid reactants, only molecules at the exposed surface can collide with other reactants — the interior is inaccessible. Grinding increases the surface-to-volume ratio of the solid, making more reactant molecules available for collision at any instant without changing the total amount of reactant. This explains why powdered sugar dissolves almost instantly while a sugar cube dissolves slowly, why powdered iron rusts faster than an iron bar, and why industrial catalysts are manufactured as fine particles or porous coatings — maximizing active surface area maximizes the rate of surface-dependent reactions."

- question: "Doubling the concentration of a reactant always doubles the reaction rate."
  type: true-false
  answer: false
  explanation: "Whether doubling concentration doubles the rate depends on the reaction order, which must be determined experimentally — it cannot be assumed from stoichiometry. For a first-order reaction (rate = k[A]¹), doubling [A] doubles the rate. For a second-order reaction (rate = k[A]²), doubling [A] quadruples the rate. For a zero-order reaction (rate = k), changing concentration has no effect on rate. The statement implicitly assumes all reactions are first-order in the relevant reactant, which is incorrect. The rate law and reaction orders are empirical properties of specific reactions, not consequences of how many molecules appear in the balanced equation."

- question: "Explain why a catalyst increases reaction rate without changing the equilibrium position of the reaction. What does the catalyst change, and what does it leave unchanged?"
  type: short-answer
  answer: "A catalyst increases reaction rate by providing an alternative reaction pathway with a lower activation energy barrier, allowing more molecules to successfully reach the transition state per unit time. What the catalyst changes: the activation energy Ea (lower for the alternative pathway) and the reaction rates in both directions (both forward and reverse proceed faster). What the catalyst leaves unchanged: the overall free energy difference ΔG° between reactants and products, and therefore the equilibrium constant K. Because the catalyst lowers Ea equally for both the forward and reverse reactions, the ratio of forward to reverse rates — which equals K at equilibrium — remains the same. Thermodynamics determines the destination (equilibrium concentrations); kinetics determines the speed of travel (how fast equilibrium is reached). Catalysts accelerate the journey without changing where it ends."
```

## Explainer

From your study of chemical kinetics you know that reactions proceed at measurable speeds — some explosively fast, others imperceptibly slow. **Reaction rate** formalizes this idea: it is the change in concentration of a reactant or product per unit time, typically expressed in mol·L⁻¹·s⁻¹. For a reaction A → B, the rate can be written as −Δ[A]/Δt (negative because reactant concentration decreases) or +Δ[B]/Δt. The key insight is that rate is not a fixed property of a reaction — it changes as conditions change, and understanding *which* conditions matter and *why* is the core of this topic.

**Concentration** is the most intuitive factor. If you double the number of reactant molecules in a given volume, collisions between them become more frequent, and the reaction speeds up. Think of it like a crowded dance floor: the more people packed into the room, the more often they bump into each other. This is why many reactions start fast (high concentration) and slow down as reactants are consumed. The precise mathematical relationship between concentration and rate — the rate law — is the subject of the next topic, but the qualitative principle is straightforward: more molecules per liter means more collisions per second.

**Temperature** affects rate through molecular energy, not just collision frequency. Raising the temperature does increase how often molecules collide, but the dominant effect is that a larger fraction of collisions now carry enough energy to overcome the **activation energy barrier** — the minimum energy required for bonds to break and reform. A useful rule of thumb is that many reactions roughly double in rate for every 10 °C increase. This is why refrigeration slows food spoilage (fewer molecules have the energy to drive decomposition reactions) and why a spark can ignite a fuel-air mixture (locally raising temperature past the activation threshold).

**Surface area** matters for reactions involving solids. A sugar cube dissolves slowly in water, but the same mass of powdered sugar dissolves almost instantly. The total amount of sugar is the same, but the powder exposes vastly more surface to the water, allowing many more collisions between sugar molecules and water molecules at any given moment. This factor is especially important in industrial chemistry, where catalysts are often ground into fine particles or spread across porous supports to maximize the reactive surface.

**Catalysts** increase reaction rate without being consumed. They work by providing an alternative reaction pathway with a lower activation energy. The reactants and products are unchanged — the catalyst simply makes it easier for molecules to reach the transition state. Enzymes in biological systems are a familiar example: they accelerate reactions by factors of millions, allowing life-sustaining chemistry to proceed at body temperature. Crucially, catalysts do not shift the position of equilibrium; they speed up both the forward and reverse reactions equally, so the system reaches equilibrium faster but at the same concentrations.
