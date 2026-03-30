---
id: magnetism-paramagnetism-diamagnetism
title: "Magnetism: Paramagnetism and Diamagnetism"
domain: physics
course: condensed-matter-physics
prerequisites:
- id: angular-momentum-quantum
  type: hard
- id: fermi-liquid-theory
  type: soft
tags:
- paramagnetism
- diamagnetism
- magnetic-susceptibility
- langevin
- pauli
stage: expert
status: validated
---

# Magnetism: Paramagnetism and Diamagnetism

## Core Idea
All materials exhibit some magnetic response to an applied field. Diamagnetism (χ < 0) is the universal tendency of orbital electron motion to oppose an applied field, present in all materials but typically weak (~10^{-5}). Paramagnetism (χ > 0) arises from alignment of permanent magnetic moments: in insulators with localized moments, the Curie law χ = C/T describes the competition between field alignment and thermal disorder. In metals, Pauli paramagnetism gives a temperature-independent χ = μ_B^2 g(E_F), reflecting that only Fermi-surface electrons contribute to the spin response. The net susceptibility of a material is the sum of all contributions.

## Questions

```yaml
- question: "Pauli paramagnetism in metals is temperature-independent, while Curie paramagnetism in insulators follows χ ∝ 1/T. What causes this fundamental difference?"
  type: multiple-choice
  options:
    - "Metals have stronger magnetic moments than insulators"
    - "In metals, the Pauli exclusion principle restricts spin flips to the ~k_BT energy shell near E_F; the number of available spins grows as T but each contributes less by 1/T, and these effects cancel. In insulators, all localized moments are free to reorient, so thermal disorder (∝ T) directly competes with field alignment (∝ 1/T)"
    - "The crystal structure of metals suppresses the temperature dependence"
    - "Insulators have more unpaired electrons per atom"
  answer: 1
  explanation: "In Curie paramagnetism, N independent moments each contribute μ²B/3k_BT to the susceptibility, giving χ = Nμ²/(3k_BT) — pure competition between magnetic energy and thermal energy. In Pauli paramagnetism, the Fermi sea blocks most spin flips. Only electrons within ~k_BT of E_F can respond, but the density of these electrons (proportional to g(E_F)) is temperature-independent at leading order. The result is χ_Pauli = μ_B² g(E_F), independent of T. The ratio χ_Pauli/χ_Curie ~ k_BT/E_F ~ 1/100 at room temperature — Pauli paramagnetism is much weaker."

- question: "Lenz's law applied at the atomic level explains diamagnetism: an applied field induces orbital currents that oppose the field. Why is diamagnetic susceptibility typically so small?"
  type: multiple-choice
  options:
    - "Diamagnetism is small because the induced currents are on the atomic scale — the induced moment per atom is proportional to <r²>, the mean square orbital radius, which is tiny (~Å²), and the proportionality constant involves e²/mc², which is very small"
    - "Diamagnetism is only present in superconductors"
    - "The diamagnetic response cancels with the paramagnetic response in most materials"
    - "Only core electrons contribute to diamagnetism"
  answer: 0
  explanation: "The Langevin diamagnetic susceptibility per atom is χ_dia = -e²N<r²>/(6mc²), where <r²> is the mean square distance of electrons from the nucleus. With <r²> ~ 1 Å² and N ~ 10-30 electrons, the susceptibility is of order -10^{-5} to -10^{-6} in CGS units. This is universally present but easily overwhelmed by paramagnetism when unpaired spins exist. Materials with no unpaired electrons (noble gases, many ionic crystals, bismuth) show measurable diamagnetism."

- question: "Superconductors are 'perfect diamagnets' with χ = -1. This is qualitatively different from ordinary diamagnetism."
  type: true-false
  answer: true
  explanation: "Ordinary (Langevin/Larmor) diamagnetism gives tiny susceptibilities (χ ~ -10^{-5}) from atomic-scale induced currents. Superconducting diamagnetism (the Meissner effect) gives χ = -1 (perfect screening) from macroscopic persistent currents that flow on the surface and completely expel the magnetic field from the interior. The physical mechanisms are completely different: Larmor diamagnetism is a perturbative response of individual atoms, while the Meissner effect is a collective quantum phenomenon involving the macroscopic coherence of the superconducting condensate."

- question: "Why do rare earth ions often have much larger paramagnetic moments than transition metal ions, despite both having unpaired f or d electrons?"
  type: short-answer
  answer: "In rare earth ions, the 4f electrons are deep inside the atom, well-shielded from the crystal electric field by the outer 5s and 5p shells. Spin-orbit coupling is strong and acts on the full J = L + S multiplet, and the crystal field is too weak to quench the orbital angular momentum. The moment is μ = g_J√(J(J+1)) μ_B with the full J value. In transition metal ions, the 3d electrons are the outermost shell and experience strong crystal fields that typically quench the orbital angular momentum (L is frozen). The moment is approximately μ ≈ 2√(S(S+1)) μ_B with g ≈ 2 and only the spin contribution. Since J (with both L and S) can be much larger than S alone, rare earth moments are often larger."
  explanation: "This is the origin of Hund's rules applied to solids: rare earths follow the free-ion J values closely, while transition metals are often 'spin-only' due to crystal field quenching of L."
```

## Explainer

Magnetism in condensed matter begins with two universal but weak effects. **Diamagnetism** is present in every material: an applied magnetic field induces tiny orbital currents (Lenz's law at the atomic scale) that produce a moment opposing the field. The resulting susceptibility chi_dia = -e^2 N <r^2> / (6mc^2) is negative, small (~10^{-5}), and temperature-independent. It is the dominant magnetic response only in materials with no unpaired electrons — noble gases, many ionic crystals, and organic molecules.

**Paramagnetism** occurs when atoms or ions carry permanent magnetic moments (from unpaired electrons). In insulators with localized moments, each moment independently tries to align with the field while thermal agitation randomizes it. The Langevin/Brillouin theory gives the **Curie law**: chi = C/T, where the Curie constant C depends on the magnitude of the atomic moment. This 1/T dependence is the signature of thermal demagnetization: at high temperature, moments are randomly oriented and the susceptibility is small; at low temperature, alignment is easier and chi grows. The saturation magnetization is reached only when mu B >> k_BT.

In **metals**, paramagnetism takes a different form. Conduction electrons have spin-1/2 magnetic moments, but the Fermi-Dirac distribution restricts which electrons can respond to a field. Only those within ~k_BT of the Fermi level have access to empty states with opposite spin. This produces **Pauli paramagnetism**: chi_Pauli = mu_B^2 g(E_F), which is temperature-independent and much smaller than Curie paramagnetism would predict for the same number of spins. The ratio chi_Pauli / chi_Curie is of order k_BT/E_F ~ 1/100 at room temperature. Additionally, the orbital motion of conduction electrons contributes **Landau diamagnetism**, which is exactly -1/3 of the Pauli susceptibility for free electrons (and modified by band structure effects in real metals).

The magnetic properties of a material are the sum of all contributions: core-electron diamagnetism, Pauli spin paramagnetism, Landau orbital diamagnetism, and (if present) Curie paramagnetism from localized moments. Van Vleck paramagnetism — a temperature-independent correction from virtual transitions to excited states — can also contribute. In most simple metals, the net susceptibility is weakly paramagnetic (Pauli > Landau + core diamagnetism). These weak magnetic responses are the "background" on which cooperative phenomena — ferromagnetism, antiferromagnetism, and spin glass behavior — are built.
