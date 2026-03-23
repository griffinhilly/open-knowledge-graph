---
id: reaction-coordinate-diagrams
title: Reaction Coordinate Diagrams
domain: chemistry
course: general-chemistry
prerequisites:
- id: chemical-kinetics
  type: hard
- id: arrhenius-equation
  type: soft
builds-toward:
- chemical-equilibrium
tags:
- activation-energy
- transition-state
- reaction-intermediate
- energy-diagram
- catalyst
- reaction-progress
- Ea
stage: formal-systems
status: validated
---
# Reaction Coordinate Diagrams

## Core Idea
A reaction coordinate diagram (energy profile) plots potential energy against reaction progress, revealing the energy landscape a reaction traverses. The activation energy (Ea) is the energy barrier between reactants and the transition state — the highest-energy, most unstable configuration along the pathway. The difference between reactant and product energies equals ΔH for the reaction. Multi-step reactions show multiple peaks and valleys: each peak is a transition state and each valley between peaks is a reaction intermediate. A catalyst lowers Ea by providing an alternative pathway but does not change ΔH or the equilibrium position — it speeds up both forward and reverse reactions equally.

## How It's Best Learned
Draw and label diagrams for exothermic and endothermic one-step reactions, then extend to two-step mechanisms with an intermediate. Identify the rate-determining step as the one with the highest activation energy barrier. Compare catalyzed and uncatalyzed profiles side by side to see how Ea changes while reactant and product energies remain the same.

## Common Misconceptions
- A catalyst does not change the thermodynamics of a reaction (ΔH and ΔG are unchanged). It only lowers the kinetic barrier, making the reaction faster.
- A reaction intermediate is a real (though short-lived) species that sits in an energy minimum, while a transition state is a maximum-energy configuration that cannot be isolated. Students often confuse the two.

## Questions

```yaml
- question: "A chemist adds a platinum catalyst to a reaction that is strongly exothermic (ΔH = −200 kJ/mol) but proceeds negligibly slowly at room temperature. Which statement best describes the effect of the catalyst?"
  type: multiple-choice
  options:
    - "The reaction becomes more exothermic because the catalyst lowers the energy of the products"
    - "The equilibrium position shifts toward products, increasing the theoretical yield"
    - "The activation energy decreases, speeding up both forward and reverse reactions equally without changing ΔH"
    - "The transition state becomes a stable reaction intermediate that can be isolated"
  answer: 2
  explanation: "A catalyst lowers activation energy by providing an alternative mechanistic pathway, but it does not change the energies of reactants or products. Therefore ΔH, ΔG, and the equilibrium position are all unchanged. Because Ea is lowered for both directions equally, both forward and reverse rates increase by the same factor, so equilibrium is reached faster but not shifted. The reaction was slow because of a high kinetic barrier, not thermodynamic unfavorability."

- question: "In the energy profile of a two-step reaction, what does a valley (local energy minimum) between two peaks represent?"
  type: multiple-choice
  options:
    - "A transition state — the highest-energy configuration on that segment of the pathway"
    - "A reaction intermediate — a real, transiently stable species that forms and then reacts further"
    - "The activation energy of the rate-determining step"
    - "The point at which the forward and reverse reaction rates become equal"
  answer: 1
  explanation: "In a multi-step energy profile, peaks are transition states (maximum-energy configurations that cannot be isolated) and valleys between peaks are reaction intermediates (real chemical species in local energy minima with finite, if brief, lifetimes). This distinction is critical: transition states exist for only a molecular vibration (~femtoseconds), while intermediates can sometimes be detected spectroscopically or even isolated under the right conditions."

- question: "A reaction with a large negative ΔH (highly exothermic) must have a small activation energy, since releasing a large amount of energy implies the reactants are already close to the transition state."
  type: true-false
  answer: false
  explanation: "Activation energy (Ea) and reaction enthalpy (ΔH) are independent quantities. Ea measures the energy barrier from reactants to the transition state; ΔH measures the energy difference between reactants and products. A reaction can be strongly exothermic (large negative ΔH) yet still have a high Ea — meaning it is thermodynamically favorable but kinetically slow. Combustion of diamond is a classic example: highly exothermic but effectively does not occur at room temperature due to an enormous kinetic barrier."

- question: "Adding a catalyst to a reaction lowers the activation energy for both the forward and reverse reactions by the same amount."
  type: true-false
  answer: true
  explanation: "A catalyst works by providing an alternative reaction pathway. Because it does not change the energies of reactants or products (the endpoints), the difference between the new Ea,forward and Ea,reverse must still equal ΔH — which is unchanged. Therefore if the forward barrier is lowered by some amount ΔEa, the reverse barrier is also lowered by the same ΔEa. This is why catalysts accelerate both directions and cannot shift equilibrium."

- question: "Why can a highly exothermic reaction still proceed very slowly at room temperature? Use the features of a reaction coordinate diagram to explain the difference between thermodynamic favorability and kinetic accessibility."
  type: short-answer
  answer: "Thermodynamic favorability (ΔH or ΔG) describes the energy difference between reactants and products — whether the reaction releases or absorbs energy overall. Kinetic accessibility describes how easily the system can get from reactants to products, which depends on the activation energy (the height of the peak in the energy diagram). A reaction coordinate diagram for a slow exothermic reaction shows a deep drop from reactants to products (large negative ΔH), but a tall peak in between (large Ea). Molecules at room temperature lack sufficient thermal energy to surmount this barrier, so the reaction is negligible even though products are much lower in energy. The two quantities are independent: ΔH tells you where you end up; Ea tells you how hard it is to get there."
```

## Explainer

From chemical kinetics, you know that reaction rates depend on an energy barrier that reactants must overcome. The Arrhenius equation gave you a mathematical relationship between this barrier, temperature, and rate. A **reaction coordinate diagram** makes that abstraction visual: it plots potential energy on the vertical axis against "reaction progress" on the horizontal axis, creating an energy landscape that shows exactly what molecules experience as they transform from reactants to products.

For a simple one-step exothermic reaction, the diagram starts with reactants at some energy level on the left, rises to a peak, then drops to products at a lower energy level on the right. The peak represents the **transition state** — a fleeting, maximum-energy configuration where old bonds are partially broken and new bonds are partially formed. The energy difference between the reactants and this peak is the **activation energy (Eₐ)**, the minimum energy that colliding molecules must possess for the reaction to proceed. The vertical distance between reactants and products is **ΔH**: if products are lower than reactants, the reaction is exothermic; if higher, endothermic. Notice that Eₐ and ΔH are independent quantities — a reaction can be strongly exothermic yet have a high activation energy, meaning it is thermodynamically favorable but kinetically slow.

Multi-step reactions produce diagrams with multiple peaks and valleys. Each peak is a separate transition state for one elementary step, and each valley between peaks represents a **reaction intermediate** — a real chemical species that forms transiently, sits in a local energy minimum, and then reacts further. The distinction matters: a transition state exists for only a molecular vibration (femtoseconds) and cannot be isolated, while an intermediate, though short-lived, has a finite lifetime and can sometimes be detected spectroscopically. The **rate-determining step** is the elementary step with the highest activation energy barrier — it controls the overall reaction speed, just as the slowest step in an assembly line limits total output.

A **catalyst** appears on the diagram as an alternative pathway with a lower highest peak. It does not change the starting energy of reactants or the final energy of products — ΔH is identical for catalyzed and uncatalyzed reactions. What changes is the route between them: the catalyst provides a different mechanism (often with more steps but each having a lower individual barrier) so that the overall Eₐ is reduced. This is why catalysts speed up reactions without being consumed and without shifting the equilibrium position — they lower the kinetic barrier equally for both the forward and reverse directions, allowing equilibrium to be reached faster but not changing where it lies.
