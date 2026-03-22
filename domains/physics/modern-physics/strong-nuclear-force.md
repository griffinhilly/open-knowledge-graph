---
id: strong-nuclear-force
title: The Strong Nuclear Force
domain: physics
course: modern-physics
prerequisites:
- id: nuclear-structure
  type: hard
builds-toward:
- binding-energy-stability-curve
tags:
- nuclear-physics
- forces
stage: advanced
status: draft
---

# The Strong Nuclear Force

## Core Idea
The strong nuclear force holds protons and neutrons together in nuclei, overcoming electrostatic repulsion among protons. It is the strongest known force but acts only at extremely short range (~1 fm). The strong force is charge-independent (protons and neutrons feel it equally) and exhibits saturation: binding energy per nucleon saturates (~8.8 MeV) as nuclei grow, indicating each nucleon binds primarily to its neighbors rather than all other nucleons.

## Questions

```yaml
- question: "As a nucleus grows from A = 10 to A = 200, the binding energy per nucleon (B/A) roughly:"
  type: multiple-choice
  options:
    - "Increases proportionally with A, because more nucleons means more bonds"
    - "Decreases sharply, because proton repulsion grows faster than binding energy"
    - "Stays roughly constant, peaking near iron at ~8.8 MeV/nucleon"
    - "Oscillates depending on whether A is even or odd"
  answer: 2
  explanation: "B/A saturates near 8.8 MeV/nucleon rather than growing with A, because the strong force is short-range — each nucleon binds only to its immediate neighbors, not to every other nucleon in the nucleus. If the force were long-range like gravity, B/A would grow with A, but it doesn't. This saturation is direct evidence of the short-range character of the strong force and explains why nuclei have well-defined, roughly constant density cores."

- question: "A proton on the far side of a large nucleus (e.g., uranium, A ≈ 238) relative to another proton. Which statement best describes their interaction?"
  type: multiple-choice
  options:
    - "They interact via both the strong force and Coulomb repulsion equally"
    - "They interact via Coulomb repulsion but not via the strong force"
    - "They interact via the strong force but not Coulomb repulsion, since protons cancel"
    - "They interact via neither force at nuclear distances"
  answer: 1
  explanation: "The strong force is effective only at ranges of ~2–3 fm, so nucleons on opposite sides of a large nucleus (separated by ~15 fm for uranium) do not feel each other's strong-force pull. However, the Coulomb (electrostatic) repulsion between protons is long-range (falls off as 1/r²) and is felt across the entire nucleus. This imbalance — every proton repels every other proton, but strong binding is only local — is why very heavy nuclei become increasingly unstable."

- question: "The strong nuclear force acts with nearly equal strength between proton-proton, proton-neutron, and neutron-neutron pairs."
  type: true-false
  answer: true
  explanation: "This property is called charge independence (or isospin symmetry). Experimental data from scattering experiments shows that the strong force does not distinguish between protons and neutrons — both are treated as nucleons differing only in their charge state. This symmetry is a deep hint that protons and neutrons are two faces of the same underlying particle, explained in the modern quark picture by the fact that the residual strong force between nucleons arises from quark-level color interactions that don't 'see' electric charge."

- question: "Because the strong force is the most powerful known force, large nuclei are more tightly bound per nucleon than small ones."
  type: true-false
  answer: false
  explanation: "The strength of the strong force does not translate into higher binding energy per nucleon for larger nuclei, because of saturation. Each nucleon binds only to its immediate neighbors (short range), so adding more nucleons adds more bonds proportionally — B/A stays roughly flat. In fact, for very large nuclei (beyond iron), B/A actually decreases slightly because Coulomb repulsion from the growing number of protons cannot be offset by the short-range strong force acting only locally. The 'most powerful force' claim applies at very short range; its short-range character is precisely what limits binding energy growth."

- question: "Explain why saturation of binding energy per nucleon is direct evidence that the strong nuclear force has short range, rather than being a long-range force like gravity."
  type: short-answer
  answer: "If the strong force were long-range, each new nucleon added to a nucleus would bind to all existing nucleons, so total binding energy would scale as A² (number of pairs) and B/A would grow proportionally with A. Instead, B/A saturates near 8.8 MeV/nucleon because each nucleon only bonds to its nearest neighbors — adding a nucleon creates only a few new bonds regardless of how large the nucleus already is. Total binding energy thus scales linearly with A, giving constant B/A. Saturation is the macroscopic fingerprint of a short-range interaction."
  explanation: "This is the central reasoning chain that connects the observed nuclear data (flat B/A curve) to the microscopic property of the strong force (short range). Students who only memorize 'the strong force is short-range' without understanding how saturation proves it are missing the key insight."
```

## Explainer

From your study of nuclear structure, you know that nuclei contain positively charged protons packed within a radius of a few femtometers. The electrostatic repulsion between protons at that range is enormous — on the order of hundreds of keV per proton pair. Yet nuclei are stable. Something must be overpowering electrostatic repulsion, and that something is the **strong nuclear force**, sometimes called the **nuclear force** or **hadronic force**.

The defining feature of the strong force is its extreme short range. Unlike gravity or electrostatics, which fall off as 1/r² and extend to infinity, the strong force drops to essentially zero beyond about 2–3 fm (~2–3 × 10⁻¹⁵ m). This is why only nearby nucleons interact — a proton in a large nucleus does not feel a direct strong-force pull from protons on the other side. This behavior is well modeled by a **Yukawa potential**: V(r) ∝ (e^{−r/r₀})/r, where r₀ ≈ 1.4 fm is the range. At short range (< 0.5 fm) the force becomes repulsive, giving nucleons a hard core that prevents nuclei from collapsing inward.

**Charge independence** is the key empirical observation that the strong force is nearly identical between proton-proton, proton-neutron, and neutron-neutron pairs. This symmetry hints at a deeper underlying structure — protons and neutrons are both **nucleons**, different charge states of the same particle in the modern quark picture. The strong force between nucleons is actually a residual effect of the color force binding quarks inside each nucleon, analogous to how van der Waals forces between neutral molecules are residuals of the underlying electromagnetic interaction.

**Saturation** is the practical consequence of short range. Because each nucleon binds only to its immediate neighbors, the total binding energy scales roughly linearly with the number of nucleons A. Binding energy per nucleon B/A peaks near iron (≈ 8.8 MeV/nucleon) and stays roughly flat across medium and heavy nuclei. If the strong force were long-range like gravity, B/A would keep increasing with A and matter would not have stable, finite nuclei — everything would clump together. Saturation is why nuclei have well-defined densities (~2.3 × 10¹⁷ kg/m³) and roughly constant density cores: adding more nucleons grows the nucleus but does not densify its core.
