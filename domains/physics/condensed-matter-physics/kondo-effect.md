---
id: kondo-effect
title: Kondo Effect
domain: physics
course: condensed-matter-physics
prerequisites:
- id: fermi-liquid-theory
  type: hard
- id: magnetism-paramagnetism-diamagnetism
  type: soft
tags:
- kondo-effect
- magnetic-impurity
- resistivity-minimum
- many-body
stage: expert
status: validated
---

# Kondo Effect

## Core Idea
The Kondo effect is the anomalous increase of resistivity at low temperatures in metals containing dilute magnetic impurities. Instead of the expected monotonic decrease (phonon scattering diminishes as T falls), the resistivity reaches a minimum and then rises logarithmically: rho ~ rho_0 - c ln(T/T_K), where T_K is the Kondo temperature. Below T_K, the impurity spin is screened by a cloud of conduction electrons forming a many-body singlet state, and the impurity behaves as a strong (unitary) scatterer. The Kondo problem was the first example in condensed matter of a renormalization group flow between weak-coupling and strong-coupling fixed points, solved exactly by Wilson's numerical RG (1975).

## Questions

```yaml
- question: "Why does a magnetic impurity in a metal cause the resistivity to increase as temperature decreases, unlike non-magnetic impurities which give a temperature-independent residual resistivity?"
  type: multiple-choice
  options:
    - "Magnetic impurities attract more electrons at low temperatures"
    - "The exchange coupling J between the impurity spin and conduction electron spins produces spin-flip scattering. At high T, this scattering is weak (perturbative). As T decreases, higher-order scattering processes (where the electron flips the impurity spin and then flips it back) interfere constructively, producing a logarithmically growing correction: δρ ∝ -J³N(0)² ln(T). This is a many-body resonance that strengthens at low T"
    - "The magnetic field of the impurity aligns nearby electron spins, creating a local barrier"
    - "Magnetic impurities have larger atomic radii that block electron paths at low temperature"
  answer: 1
  explanation: "The key is spin-flip scattering involving higher-order (multi-particle) processes. In second-order perturbation theory in J, a conduction electron can virtually flip the impurity spin and then flip it back, and the intermediate state involves the entire Fermi sea (a many-body effect). The resulting scattering amplitude has a ln(T) divergence because the virtual processes involve states at all energies up to the bandwidth, weighted by the Fermi function. This is the Kondo logarithm, and it signals the breakdown of perturbation theory below T_K."

- question: "Wilson's numerical renormalization group (NRG) showed that the Kondo problem flows from a weak-coupling fixed point (free impurity spin) to a strong-coupling fixed point (screened singlet). What is the physical picture at each fixed point?"
  type: multiple-choice
  options:
    - "At weak coupling the impurity is superconducting; at strong coupling it is insulating"
    - "At T >> T_K (weak coupling), the impurity spin is essentially free and the conduction electrons scatter weakly from it — the impurity contributes a Curie-like susceptibility and weak scattering. At T << T_K (strong coupling), the impurity spin is completely screened by a surrounding cloud of conduction electrons forming a many-body singlet, and the impurity site acts as a strong potential scatterer (unitarity limit) with no residual magnetic moment"
    - "Both fixed points describe free electrons with different effective masses"
    - "The strong-coupling fixed point has a local magnetic moment"
  answer: 1
  explanation: "The Kondo crossover from T >> T_K to T << T_K is one of the most beautiful examples of renormalization group flow in physics. At high T, the impurity is a free S = 1/2 moment with a Curie susceptibility χ ∝ 1/T and weak log(T) resistivity corrections. As T decreases through T_K, the effective coupling grows (flows to strong coupling), and the conduction electrons progressively screen the impurity spin. Below T_K, the ground state is a many-body singlet (S_total = 0), the impurity susceptibility saturates (Pauli-like, not Curie), and the resistivity reaches the unitarity limit. Wilson's NRG (Nobel Prize 1982) was the first method to quantitatively describe this crossover."

- question: "The Kondo temperature T_K = D exp(-1/JN(0)) has the same non-analytic form as the BCS gap Δ ~ ω_D exp(-1/N(0)V). This is not a coincidence."
  type: true-false
  answer: true
  explanation: "Both expressions reflect a non-perturbative instability of the Fermi sea. In BCS theory, an attractive interaction (however weak) destabilizes the Fermi surface toward Cooper pairing. In the Kondo problem, an antiferromagnetic exchange coupling (however weak) destabilizes the free-spin state toward singlet formation. Both involve logarithmic divergences in perturbation theory that signal the breakdown of the perturbative expansion and the emergence of a new energy scale (Δ or T_K) that is exponentially small in the coupling. The mathematical structure (log divergence → non-perturbative energy scale) is identical and reflects the high density of states at the Fermi level available for forming bound states."

- question: "Explain why the Kondo effect requires antiferromagnetic exchange coupling (J > 0) and does not occur for ferromagnetic coupling (J < 0)."
  type: short-answer
  answer: "For antiferromagnetic coupling (J > 0), the spin-flip scattering processes that produce the Kondo logarithm interfere constructively, making the effective coupling grow at lower energies (asymptotic freedom in reverse — the coupling flows to strong coupling). This produces the Kondo singlet ground state. For ferromagnetic coupling (J < 0), the same processes interfere destructively, and the effective coupling flows to zero at low energies — the impurity spin remains free and the resistivity contribution is simply a constant. The renormalization group beta function has opposite sign for the two cases: β(J) < 0 for AF coupling (relevant, flows to strong coupling) and β(J) > 0 for FM coupling (irrelevant, flows to weak coupling)."
  explanation: "This asymmetry is why only AF-coupled magnetic impurities (like Fe, Mn, Cr in copper or gold) show the Kondo effect, while FM-coupled impurities (which are rare in practice) do not. The sign of J depends on the specific hybridization between the impurity d or f orbitals and the conduction band, governed by the Schrieffer-Wolff transformation from the Anderson impurity model."
```

## Explainer

The Kondo effect has a remarkable history. In the 1930s, experimentalists noticed that some metals showed an unexpected **resistivity minimum** at low temperatures: instead of the expected monotonic decrease from phonon freezeout, the resistivity turned upward below ~10-30 K. The effect was traced to dilute magnetic impurities (a few ppm of iron in gold, for example), but its theoretical explanation eluded physicists for thirty years. In 1964, Jun Kondo showed that third-order perturbation theory in the exchange coupling J between the impurity spin and conduction electrons produces a logarithmic correction: delta rho proportional to J^3 N(0)^2 ln(k_BT/D), which diverges as T goes to 0 — explaining the resistivity upturn but also signaling the breakdown of perturbation theory.

The resolution came from Kenneth Wilson's **numerical renormalization group** (1975), which mapped the Kondo problem onto an equivalent one-dimensional chain that could be solved iteratively by keeping only the lowest-energy states at each step. Wilson showed that the physics crosses over smoothly between two limits. Above the **Kondo temperature** T_K = D exp(-1/JN(0)), the impurity spin is essentially free: it contributes a Curie susceptibility chi proportional to 1/T and scatters conduction electrons weakly. Below T_K, the conduction electrons form a many-body **singlet state** with the impurity spin — a "Kondo cloud" of radius xi_K ~ hbar v_F/k_BT_K that collectively screens the impurity moment to zero.

The screened impurity at T << T_K is a remarkable object. It has no magnetic moment (the susceptibility becomes Pauli-like), but it scatters conduction electrons at the maximum possible rate — the **unitarity limit**. The impurity behaves as an infinitely strong potential scatterer, contributing a residual resistivity proportional to sin^2(delta_0)/E_F where delta_0 = pi/2 (the phase shift is maximal). The crossover from free spin to screened singlet is completely smooth — no phase transition occurs — and is captured by a single energy scale T_K.

The Kondo effect has become a paradigm for strong-coupling many-body physics. Its mathematical structure — a logarithmic divergence in perturbation theory leading to a non-perturbative energy scale T_K — parallels the BCS problem and asymptotic freedom in QCD. The Kondo effect extends far beyond dilute impurities: **Kondo lattice** systems (where every site carries a magnetic moment, as in heavy-fermion compounds) are among the most complex many-body systems in condensed matter. And in the quantum dot context, a single quantum dot connected to leads acts as an artificial magnetic impurity, allowing the Kondo effect to be studied with unprecedented control — tuning T_K with gate voltages and directly observing the Kondo resonance in the differential conductance.
