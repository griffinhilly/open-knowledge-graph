---
id: adsorption-thermodynamics-entropy
title: Adsorption Thermodynamics and Surface Entropy
domain: chemistry
course: physical-chemistry
prerequisites:
- id: surface-chemistry-and-catalysis
  type: hard
- id: entropy-and-gibbs-free-energy
  type: hard
builds-toward:
- brunnauer-emmett-teller-bET-theory
tags:
- adsorption
- thermodynamics
- entropy
- surface
stage: formal-systems
status: validated
---

# Adsorption Thermodynamics and Surface Entropy

## Core Idea
Adsorption is the accumulation of adsorbate molecules on a surface, driven by enthalpy reduction but opposed by entropy loss (adsorbate loses translational freedom). The Gibbs free energy for adsorption depends on temperature: at low T, ΔH dominates and adsorption is favorable; at high T, the -TΔS term dominates and desorption is favored. Surface coverage and desorption temperature depend on temperature and adsorbate pressure through thermodynamic relations.

## Questions

```yaml
- question: "A catalytic surface is operating at 200°C and is then heated to 600°C while exposed to the same gas pressure. What happens to surface coverage, and why?"
  type: multiple-choice
  options:
    - "Coverage increases because higher temperature gives molecules more kinetic energy to reach the surface"
    - "Coverage decreases because the −TΔS penalty grows large enough to make ΔG positive, favoring desorption"
    - "Coverage stays the same because the adsorption enthalpy does not change with temperature"
    - "Coverage first increases then decreases at the Sabatier optimum temperature"
  answer: 1
  explanation: "Adsorption has ΔH < 0 (favorable) and ΔS < 0 (unfavorable, adsorbate loses translational freedom). At 200°C the enthalpy term dominates and ΔG is negative; at 600°C the −TΔS term is much larger, making ΔG positive, so desorption is thermodynamically favored. This is why catalytic surfaces 'clean themselves' at high temperatures."

- question: "Gas A adsorbs with ΔH_ads = −20 kJ/mol and Gas B with ΔH_ads = −80 kJ/mol. At a fixed temperature and pressure, which gas has higher equilibrium surface coverage?"
  type: multiple-choice
  options:
    - "Gas A, because weaker binding allows faster equilibrium exchange with the gas phase"
    - "Gas B, because the more negative ΔH shifts the adsorption equilibrium toward the surface-bound state"
    - "They are equal because entropy terms dominate at all temperatures"
    - "Cannot be determined without knowing the entropy of adsorption for each gas"
  answer: 1
  explanation: "More negative ΔH_ads makes ΔG more negative at a given temperature, shifting the equilibrium toward higher coverage. Gas B's stronger surface interaction produces a more stable adsorbed state. While entropy matters quantitatively, the question specifically contrasts enthalpy values — the thermodynamic driving force is clearly larger for Gas B."

- question: "When a molecule adsorbs onto a solid surface, its entropy increases because it achieves a more ordered, lower-energy configuration."
  type: true-false
  answer: false
  explanation: "The adsorbate's entropy DECREASES upon adsorption. A gas-phase molecule freely translates and rotates in three dimensions; once pinned to a surface it loses these degrees of freedom. ΔS_ads is negative. The favorable driving force for adsorption is the enthalpy release (bond formation), not entropy."

- question: "A surface that binds reaction intermediates with a very large, negative ΔH_ads will always be a more effective catalyst than one with moderate binding."
  type: true-false
  answer: false
  explanation: "This violates Sabatier's principle. If the surface binds intermediates or products too strongly, they cannot desorb and the surface becomes poisoned — catalytic activity collapses. An effective catalyst must bind reactants strongly enough to lower the activation barrier but weakly enough for products to desorb. The optimal binding strength lies between too weak and too strong."

- question: "Why does increasing temperature generally cause desorption from a surface, even though adsorption itself releases energy (ΔH < 0)?"
  type: short-answer
  answer: "Because adsorption also involves a loss of entropy (ΔS < 0 for the adsorbate). The Gibbs free energy is ΔG = ΔH − TΔS. Even though ΔH is negative, ΔS is also negative, so the −TΔS term is positive and grows with temperature. At high enough temperature, −TΔS overwhelms ΔH, making ΔG positive and desorption thermodynamically favorable."
  explanation: "This is the central thermodynamic insight: adsorption is an enthalpy-entropy competition. At low T, enthalpy wins (adsorption spontaneous); at high T, entropy wins (desorption spontaneous). The crossover temperature depends on the ratio ΔH/ΔS and is directly related to the desorption temperature observed experimentally."
```

## Explainer

From your study of Gibbs free energy, you know that a process occurs spontaneously when ΔG = ΔH − TΔS is negative. Adsorption — the binding of gas or liquid molecules onto a solid surface — is a beautiful case study in the competition between enthalpy and entropy. When a gas molecule lands on a surface and forms a bond (whether a weak van der Waals interaction in **physisorption** or a strong chemical bond in **chemisorption**), the system releases energy: ΔH is negative. But that same molecule, which was freely translating and rotating in three dimensions, is now pinned to a two-dimensional surface with restricted motion. It has lost degrees of freedom, and its entropy has decreased: ΔS is negative for the adsorbate.

At low temperatures, the TΔS penalty is small, and the favorable (negative) ΔH drives ΔG negative — adsorption proceeds spontaneously and surface coverage builds up. As temperature increases, the TΔS term grows. At some crossover temperature, the entropy penalty overwhelms the enthalpy gain, ΔG turns positive, and the surface begins to clear as molecules desorb. This is why catalytic surfaces clean themselves at high temperatures and why adsorption experiments typically show decreasing coverage with increasing temperature at a fixed pressure. The **desorption temperature** — where coverage drops sharply — is a direct readout of the adsorption enthalpy: stronger surface bonds require higher temperatures to overcome.

The quantitative tool for analyzing these relationships is the **Clausius-Clapeyron equation for adsorption**, which relates the change in equilibrium pressure with temperature to the enthalpy of adsorption. By measuring adsorption isotherms (coverage versus pressure) at several temperatures, you can extract ΔH_ads from the slope of ln(P) versus 1/T at constant coverage. More negative ΔH_ads values correspond to stronger surface binding and higher desorption temperatures. The entropy of adsorption can also be extracted and provides insight into the mobility of the adsorbate: a molecule that retains some translational freedom along the surface (mobile adsorption) has a smaller entropy loss than one locked into a fixed site (localized adsorption).

Understanding these thermodynamic balances is essential for designing catalysts and adsorbents. An ideal catalyst binds reactants strongly enough to hold them on the surface and lower activation barriers, but not so strongly that the products cannot desorb — a principle known as Sabatier's principle. Similarly, industrial adsorbents for gas separation (like zeolites or activated carbon) are engineered so that the target molecule adsorbs preferentially at operating temperature but can be regenerated by heating. In every case, it is the interplay between ΔH and TΔS that determines where the thermodynamic sweet spot lies.
