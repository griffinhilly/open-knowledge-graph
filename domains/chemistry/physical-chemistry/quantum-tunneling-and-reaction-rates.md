---
id: quantum-tunneling-and-reaction-rates
title: Quantum Tunneling and Reaction Rate Enhancement
domain: chemistry
course: physical-chemistry
prerequisites:
- id: born-oppenheimer-approximation
  type: hard
- id: transition-state-theory-and-kinetics
  type: soft
tags:
- quantum
- tunneling
- kinetics
- barrier-penetration
stage: advanced
status: draft
---

# Quantum Tunneling and Reaction Rate Enhancement

## Core Idea
Quantum mechanics allows particles to penetrate potential barriers below the classical activation energy through tunneling. Tunneling is especially important for light particles (protons, electrons, hydrogen atoms) and lowers effective activation barriers by orders of magnitude. This explains anomalously fast rates in enzyme catalysis (e.g., monoamine oxidase), photosynthesis electron transfer, and proton-coupled reactions.

## How It's Best Learned
Calculate tunneling transmission coefficients for proton transfer using WKB approximation; measure H/D kinetic isotope effects to detect tunneling contributions; analyze temperature-dependent rate data to extract curvature signatures of tunneling; compare experimental and theoretical KIEs.

## Common Misconceptions
- Assuming tunneling only occurs in enzymes or extremely fast reactions; it contributes to ordinary chemical reactions, especially those involving protons. - Treating tunneling as a small perturbation; for very light particles and low barriers, tunneling can dominate the rate, making semiclassical TST invalid.

## Explainer

In classical transition state theory, a reaction proceeds only when the system acquires enough kinetic energy to surmount the potential energy barrier separating reactants from products. From your study of the Born-Oppenheimer approximation, you know that nuclear motion occurs on a potential energy surface defined by the electronic Hamiltonian. Classical mechanics says a particle with energy E below the barrier height V₀ is strictly reflected — it cannot appear on the other side. Quantum mechanics disagrees. Because nuclei are described by wavefunctions, not point particles, a portion of the wavefunction penetrates into and through the barrier region, giving a nonzero probability of appearing on the product side. This is **quantum tunneling**.

The tunneling probability depends exponentially on three factors: the barrier width, the barrier height above the particle's energy, and the particle's mass. The **WKB approximation** gives the transmission coefficient as T ≈ exp(−2∫√(2m(V(x)−E))/ℏ dx), integrated across the classically forbidden region. Because mass m appears under the square root, lighter particles tunnel far more effectively. A proton (mass 1 amu) tunnels orders of magnitude more readily than a deuteron (mass 2 amu) through the same barrier. This mass dependence is the origin of the **kinetic isotope effect** (KIE): replacing hydrogen with deuterium slows a reaction if tunneling contributes significantly. KIE values above ~7 at room temperature are a strong experimental signature of tunneling, because classical transition state theory predicts smaller isotope effects from zero-point energy differences alone.

The practical impact is striking. In many enzyme-catalyzed proton and hydride transfers, the measured rate is far faster than classical TST predicts. The enzyme does not merely lower the activation barrier — it also narrows it, compressing the donor-acceptor distance so that the tunneling probability increases dramatically. Electron transfer in photosynthesis similarly relies on tunneling: electrons traverse protein barriers over distances of 10–15 Å where classical hopping would be negligibly slow. Even in simple organic reactions, proton transfers along hydrogen bonds can proceed partly through the barrier rather than over it.

Temperature dependence provides another diagnostic. Classical Arrhenius behavior gives a straight line on a ln(k) vs. 1/T plot. Tunneling causes the rate to level off at low temperatures — the Arrhenius plot curves downward because the tunneling contribution is nearly temperature-independent. At very low temperatures, the rate may become entirely dominated by tunneling, reaching a finite value rather than dropping to zero as the classical prediction would require. Recognizing this curvature in experimental data is key to quantifying how much of a reaction rate is due to over-barrier crossing versus through-barrier penetration.
