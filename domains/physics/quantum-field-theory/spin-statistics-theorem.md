---
id: spin-statistics-theorem
title: Spin-Statistics Theorem
domain: physics
course: quantum-field-theory
prerequisites:
- id: dirac-field-quantization
  type: hard
- id: klein-gordon-field-quantization
  type: hard
tags:
- spin-statistics
- fermions
- bosons
stage: expert
status: validated
---

# Spin-Statistics Theorem

## Core Idea
The spin-statistics theorem proves that particles with integer spin (0, 1, 2, ...) must be bosons (obeying Bose-Einstein statistics with commutation relations) and particles with half-integer spin (1/2, 3/2, ...) must be fermions (obeying Fermi-Dirac statistics with anticommutation relations). This connection between spin and statistics is not an empirical observation but a theorem derivable from Lorentz invariance, locality, and positive energy.

## Questions

```yaml
- question: "A student proposes quantizing a spin-1/2 field using commutation relations (bosonic statistics) instead of anticommutation relations. What goes wrong?"
  type: multiple-choice
  options:
    - "The theory violates Lorentz invariance"
    - "Two things fail: (1) the energy is unbounded below — the Hamiltonian has no ground state because the negative-frequency modes contribute negative energy with unlimited occupation; and (2) microcausality is violated — the field commutator at spacelike separation does not vanish, violating relativistic causality"
    - "The field equations change"
    - "The propagator develops tachyonic poles"
  answer: 1
  explanation: "Both failures are fatal. The energy instability means the vacuum is unstable against unlimited pair creation. The microcausality violation means measurements at spacelike separations can influence each other, violating the principle that information cannot travel faster than light. Anticommutation relations for half-integer spin fields cure both problems simultaneously: they make the energy positive (by reinterpreting negative-frequency modes as antiparticle creation operators) and ensure that the anticommutator of the field at spacelike separations vanishes. The connection is not a coincidence but a mathematical necessity."

- question: "For integer-spin fields, the reverse problem occurs: quantizing with anticommutation relations produces a theory where the field anticommutator at spacelike separation does not vanish (microcausality fails) and all states have zero norm."
  type: true-false
  answer: true
  explanation: "For a spin-0 field quantized with anticommutation relations, the equal-time anticommutator {phi(x), phi(y)} does not vanish at spacelike separation. Additionally, the states would have zero or negative norm (the Fock space construction fails). With commutation relations, both problems disappear: the commutator [phi(x), phi(y)] vanishes at spacelike separation, and the Fock space has positive-definite norm. Thus, integer-spin fields must be quantized as bosons, completing the spin-statistics connection."

- question: "The spin-statistics theorem explains why matter is stable. If electrons were bosons, all electrons in an atom would collapse into the lowest energy state, and matter would be radically different."
  type: true-false
  answer: true
  explanation: "If electrons obeyed Bose-Einstein statistics, the Pauli exclusion principle would not apply. All electrons in an atom would occupy the 1s orbital, atoms would be much smaller, the periodic table would not exist, and chemistry would be fundamentally different. In a macroscopic object, the degeneracy pressure that prevents gravitational collapse of white dwarf stars (electron degeneracy pressure) and neutron stars (neutron degeneracy pressure) would be absent. The stability of bulk matter — the fact that the energy of N atoms grows proportionally to N rather than N^{7/5} or worse — depends crucially on fermionic statistics. The spin-statistics theorem therefore underpins the existence of the physical world as we know it."

- question: "Outline the key steps in proving the spin-statistics theorem, identifying the three axioms required and where each enters the argument."
  type: short-answer
  answer: "The proof requires: (1) Lorentz invariance — the field transforms correctly under the Lorentz group, which constrains how positive and negative frequency modes are related by CPT. (2) Locality (microcausality) — field operators at spacelike separation must commute (bosons) or anticommute (fermions) to ensure no faster-than-light signaling. (3) Positive energy (spectral condition) — the energy spectrum is bounded below, ensuring a stable vacuum. The argument proceeds by showing that for half-integer spin, the commutator at spacelike separation does not vanish (fails locality) while the anticommutator does; and for integer spin, the anticommutator at spacelike separation does not vanish while the commutator does. Combining locality with positive energy forces the correct choice: commutators for integer spin, anticommutators for half-integer spin."
  explanation: "The proof is not trivial — it requires the full machinery of Lorentz group representations and the PCT theorem. Pauli gave the first proof in 1940; Streater and Wightman gave a rigorous axiomatic proof in the 1960s. The theorem is one of the deepest results in physics, connecting the rotational properties of particles (spin) to their collective behavior (statistics) through the structure of relativistic spacetime."
```

## Explainer

The **spin-statistics theorem** is one of the most profound results in theoretical physics. It states that the spin of a particle -- a property determined by the representation of the Lorentz group under which it transforms -- uniquely determines its quantum statistics. Integer-spin particles (spin 0, 1, 2, ...) must be bosons, and half-integer-spin particles (spin 1/2, 3/2, ...) must be fermions. There is no choice: the connection is forced by consistency requirements of relativistic quantum field theory.

The proof relies on three axioms. **Lorentz invariance** determines how fields transform and constrains the relationship between positive and negative frequency solutions. **Locality** (microcausality) requires that observables at spacelike separations commute, ensuring that measurements outside each other's light cones cannot influence each other -- the relativistic causality requirement. **Positive energy** (the spectral condition) requires the existence of a stable vacuum state with a lower bound on energy.

The argument works by showing that the wrong statistics violate one or both of the physical requirements. For a spin-1/2 field quantized with commutators (bosonic statistics), the commutator [psi(x), psi-bar(y)] does not vanish at spacelike separation -- microcausality fails. Additionally, the Hamiltonian is unbounded below -- the theory has no stable vacuum. For a spin-0 field quantized with anticommutators (fermionic statistics), the anticommutator {phi(x), phi(y)} does not vanish at spacelike separation, and the Fock space has states with zero or negative norm. In both cases, the wrong choice of statistics produces an inconsistent theory. The correct choice (anticommutators for half-integer spin, commutators for integer spin) satisfies all three axioms.

The physical consequences are immense. The **Pauli exclusion principle** -- that no two identical fermions can occupy the same quantum state -- is a direct consequence of anticommutation relations and hence of the spin-statistics theorem. This principle underlies the structure of the periodic table, the stability of matter, the existence of white dwarf and neutron stars, and essentially all of chemistry and materials science. Without the spin-statistics connection, matter as we know it could not exist. The theorem explains why this deep connection between an intrinsic property of individual particles (spin) and the collective behavior of identical particles (statistics) is not a coincidence but a mathematical necessity in any consistent relativistic quantum theory.
