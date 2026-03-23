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
status: validated
---

# Quantum Tunneling and Reaction Rate Enhancement

## Core Idea
Quantum mechanics allows particles to penetrate potential barriers below the classical activation energy through tunneling. Tunneling is especially important for light particles (protons, electrons, hydrogen atoms) and lowers effective activation barriers by orders of magnitude. This explains anomalously fast rates in enzyme catalysis (e.g., monoamine oxidase), photosynthesis electron transfer, and proton-coupled reactions.

## How It's Best Learned
Calculate tunneling transmission coefficients for proton transfer using WKB approximation; measure H/D kinetic isotope effects to detect tunneling contributions; analyze temperature-dependent rate data to extract curvature signatures of tunneling; compare experimental and theoretical KIEs.

## Common Misconceptions
- Assuming tunneling only occurs in enzymes or extremely fast reactions; it contributes to ordinary chemical reactions, especially those involving protons. - Treating tunneling as a small perturbation; for very light particles and low barriers, tunneling can dominate the rate, making semiclassical TST invalid.

## Questions

```yaml
- question: "An enzyme-catalyzed proton transfer shows a kinetic isotope effect kH/kD = 18 at room temperature. Classical transition state theory predicts a maximum KIE of about 7 from zero-point energy differences alone. What does the anomalously large KIE most directly indicate?"
  type: multiple-choice
  options:
    - "The enzyme binds deuterium more tightly, slowing the reaction"
    - "The C–H bond is fundamentally different from the C–D bond in this enzyme"
    - "Quantum tunneling is contributing significantly to the proton transfer rate"
    - "The measurement is erroneous because KIE cannot exceed 7"
  answer: 2
  explanation: "A KIE above ~7 at room temperature is the classic experimental signature of proton tunneling. Classical TST predicts KIE values in the range of 2–7, arising from zero-point energy differences between C–H and C–D bonds. Values well above 7 cannot be explained classically and indicate that the proton is tunneling through the barrier rather than surmounting it. Because tunneling probability depends exponentially on mass (see WKB), replacing H with D (doubling the mass) dramatically reduces tunneling, explaining the large rate difference."

- question: "A reaction involving proton transfer shows normal Arrhenius behavior (straight ln k vs 1/T line) at high temperatures, but the plot curves and levels off at low temperatures — the rate approaches a constant value rather than continuing to decrease. What does this indicate?"
  type: multiple-choice
  options:
    - "The reaction becomes thermodynamically barrierless at low temperature"
    - "Solvent freezing changes the reaction mechanism at low temperature"
    - "At low temperature, the rate is dominated by tunneling, which is nearly temperature-independent"
    - "Activation energy decreases at low temperatures due to conformational changes"
  answer: 2
  explanation: "Classical Arrhenius behavior k = A·exp(−Ea/RT) predicts that ln k decreases linearly as 1/T increases — the rate approaches zero as temperature falls. Tunneling, however, is driven by the wavefunction penetration of the barrier, which is nearly temperature-independent. When tunneling dominates, the rate reaches a finite floor at low temperature rather than approaching zero. This curvature on the Arrhenius plot — a leveling off rather than a straight line — is a key diagnostic tool for quantifying the tunneling contribution."

- question: "Quantum tunneling contributes to proton transfer rates only in exotic situations like enzymes or cryogenic temperatures; it is negligible for ordinary chemical reactions under typical laboratory conditions."
  type: true-false
  answer: false
  explanation: "Tunneling contributes to ordinary proton and hydrogen atom transfer reactions at room temperature, not just in enzymes or at extreme conditions. The WKB transmission coefficient depends on barrier width and mass — protons (mass ~1 amu) can tunnel appreciably through narrow barriers even near 300 K. Enzymes enhance tunneling by compressing donor-acceptor distance, but the phenomenon is present in simple solution-phase proton transfers as well. Dismissing tunneling as exotic is the most common misconception in reaction kinetics."

- question: "Replacing a transferring hydrogen atom with deuterium slows a tunneling-dominated reaction more than it slows a purely classical over-barrier reaction."
  type: true-false
  answer: true
  explanation: "In the WKB approximation, tunneling probability depends on exp(−2∫√(2m(V−E))dx). Because mass appears under a square root, going from H (1 amu) to D (2 amu) increases the exponent by √2 — but more importantly, tunneling probability is exponentially sensitive to mass, so even a factor of 2 in mass causes a dramatic reduction in the tunneling rate. Classical rate differences from isotope substitution arise only from zero-point energy shifts (KIE ≤ 7), whereas tunneling-dominated reactions can show KIE values of 10–100 or higher."

- question: "Why does the tunneling probability depend so sensitively on the mass of the tunneling particle, and what experimental measurement directly exploits this mass dependence to detect tunneling in a reaction?"
  type: short-answer
  answer: "The WKB transmission coefficient T ≈ exp(−2∫√(2m(V−E)/ℏ²)dx) places mass m inside the square root of the exponent — a small increase in mass produces a large decrease in tunneling probability because of the exponential sensitivity. Replacing hydrogen (1 amu) with deuterium (2 amu) therefore dramatically reduces the tunneling rate. The kinetic isotope effect (kH/kD) directly measures this: classical reactions show KIE ≤ 7 (from zero-point energy differences), while tunneling-dominated reactions show anomalously large KIE values, sometimes exceeding 50 at room temperature."
  explanation: "The exponential dependence on √m is why tunneling is most important for the lightest particles — electrons, protons, and hydrogen atoms — and negligible for heavier nuclei like carbon. The KIE measurement is experimentally clean because it requires only comparing rates of H- vs D-labeled substrates under identical conditions. The combination of KIE > 7 and Arrhenius plot curvature at low temperature constitutes the standard two-pronged diagnostic for tunneling contributions."
```

## Explainer

In classical transition state theory, a reaction proceeds only when the system acquires enough kinetic energy to surmount the potential energy barrier separating reactants from products. From your study of the Born-Oppenheimer approximation, you know that nuclear motion occurs on a potential energy surface defined by the electronic Hamiltonian. Classical mechanics says a particle with energy E below the barrier height V₀ is strictly reflected — it cannot appear on the other side. Quantum mechanics disagrees. Because nuclei are described by wavefunctions, not point particles, a portion of the wavefunction penetrates into and through the barrier region, giving a nonzero probability of appearing on the product side. This is **quantum tunneling**.

The tunneling probability depends exponentially on three factors: the barrier width, the barrier height above the particle's energy, and the particle's mass. The **WKB approximation** gives the transmission coefficient as T ≈ exp(−2∫√(2m(V(x)−E))/ℏ dx), integrated across the classically forbidden region. Because mass m appears under the square root, lighter particles tunnel far more effectively. A proton (mass 1 amu) tunnels orders of magnitude more readily than a deuteron (mass 2 amu) through the same barrier. This mass dependence is the origin of the **kinetic isotope effect** (KIE): replacing hydrogen with deuterium slows a reaction if tunneling contributes significantly. KIE values above ~7 at room temperature are a strong experimental signature of tunneling, because classical transition state theory predicts smaller isotope effects from zero-point energy differences alone.

The practical impact is striking. In many enzyme-catalyzed proton and hydride transfers, the measured rate is far faster than classical TST predicts. The enzyme does not merely lower the activation barrier — it also narrows it, compressing the donor-acceptor distance so that the tunneling probability increases dramatically. Electron transfer in photosynthesis similarly relies on tunneling: electrons traverse protein barriers over distances of 10–15 Å where classical hopping would be negligibly slow. Even in simple organic reactions, proton transfers along hydrogen bonds can proceed partly through the barrier rather than over it.

Temperature dependence provides another diagnostic. Classical Arrhenius behavior gives a straight line on a ln(k) vs. 1/T plot. Tunneling causes the rate to level off at low temperatures — the Arrhenius plot curves downward because the tunneling contribution is nearly temperature-independent. At very low temperatures, the rate may become entirely dominated by tunneling, reaching a finite value rather than dropping to zero as the classical prediction would require. Recognizing this curvature in experimental data is key to quantifying how much of a reaction rate is due to over-barrier crossing versus through-barrier penetration.
