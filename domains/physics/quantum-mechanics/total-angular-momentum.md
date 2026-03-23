---
id: total-angular-momentum
title: Total Angular Momentum
domain: physics
course: quantum-mechanics
prerequisites:
- id: orbital-angular-momentum-quantum
  type: hard
- id: spin-angular-momentum
  type: hard
builds-toward:
- angular-momentum-coupling
tags:
- angular-momentum
- quantum-numbers
stage: advanced
status: validated
---

# Total Angular Momentum

## Core Idea
Total angular momentum J⃗ = L⃗ + S⃗ is conserved in rotationally symmetric systems. The quantum number j ranges from |l − s| to l + s; for an electron (s = ½), j = l ± ½.

## Questions

```yaml
- question: "An electron has orbital quantum number l = 2 and spin s = 1/2. What are the possible values of the total angular momentum quantum number j?"
  type: multiple-choice
  options:
    - "j = 5/2 only, since j = l + s is the maximum total"
    - "j = 3/2 and j = 5/2, since j ranges from |l − s| to l + s in integer steps"
    - "j = 2, 3/2, 1, 1/2 — all half-integer values from 1/2 up to l + s"
    - "j = l × s = 1, since quantum numbers combine multiplicatively"
  answer: 1
  explanation: "The total angular momentum quantum number j takes all values from |l − s| to l + s in integer steps. For l = 2, s = 1/2: |l − s| = |2 − 1/2| = 3/2 and l + s = 5/2. The integer-step rule gives j = 3/2 and j = 5/2 — exactly two values. The j = 3/2 level has 2j+1 = 4 magnetic substates and j = 5/2 has 6, totaling 10 states — matching the (2l+1)(2s+1) = 5×2 = 10 states in the uncoupled basis, confirming the two descriptions span the same space."

- question: "When spin-orbit coupling is significant in an atom, why do physicists prefer the coupled basis |j, mⱼ⟩ over the uncoupled basis |mₗ, mₛ⟩?"
  type: multiple-choice
  options:
    - "Because mₗ and mₛ are not measurable in principle for any real atomic state"
    - "Because spin-orbit coupling means L and S are no longer separately conserved — J is the good conserved quantity, making |j, mⱼ⟩ the natural eigenbasis for the Hamiltonian"
    - "Because the coupled basis always produces smaller quantum numbers, simplifying calculations"
    - "Because the uncoupled basis |mₗ, mₛ⟩ violates the Pauli exclusion principle for electrons"
  answer: 1
  explanation: "The spin-orbit interaction H_SO ∝ L⃗·S⃗ does not commute with Lz or Sz individually, meaning mₗ and mₛ are no longer good quantum numbers — they are not conserved. However, H_SO does commute with J², Jz, L², and S², so j and mⱼ (along with l and s) are good quantum numbers. When solving the hydrogen fine structure, one works in the coupled basis because those are the actual energy eigenstates. The uncoupled basis is used when spin-orbit coupling is negligible (e.g., weak external magnetic field dominating — the Paschen-Back regime)."

- question: "For an electron in an s orbital (l = 0), the only possible total angular momentum quantum number is j = 1/2."
  type: true-false
  answer: true
  explanation: "The range of j is from |l − s| to l + s in integer steps. For l = 0, s = 1/2: |0 − 1/2| = 1/2 and 0 + 1/2 = 1/2. The only value is j = 1/2. This means an s-orbital electron has total angular momentum entirely from its spin, with no orbital contribution to j. The two magnetic substates are mⱼ = +1/2 and mⱼ = −1/2."

- question: "The coupled basis |j, mⱼ⟩ and the uncoupled basis |mₗ, mₛ⟩ span Hilbert spaces of different dimensions, since combining angular momenta changes the number of accessible quantum states."
  type: true-false
  answer: false
  explanation: "Both bases span exactly the same Hilbert space with the same number of dimensions: (2l+1)(2s+1). The coupled and uncoupled bases are two different ways of spanning the same space — like two different coordinate systems in the same vector space. For l = 1, s = 1/2: the uncoupled basis has (3)(2) = 6 states. The coupled basis has j = 3/2 (4 states) and j = 1/2 (2 states) — again 6 total. The Clebsch-Gordan coefficients are precisely the unitary transformation between these two bases."

- question: "Why is the total angular momentum J⃗ = L⃗ + S⃗ the conserved quantity in spin-orbit coupling, rather than L⃗ and S⃗ separately? What physically breaks the separate conservation?"
  type: short-answer
  answer: "Spin-orbit coupling arises from the interaction between an electron's magnetic moment (from its spin) and the magnetic field it experiences due to its orbital motion around the nucleus. This interaction is proportional to L⃗·S⃗. Because this term mixes L and S, neither L nor S is individually conserved under time evolution — their directions precess around the total J⃗. However, J⃗ = L⃗ + S⃗ commutes with the full Hamiltonian (including H_SO), so J⃗ is conserved. Physically, L and S are coupled by the interaction and exchange angular momentum between them, while J (their sum) is the quantity the system conserves. The magnitudes L² and S² (and hence l and s) are still conserved; only the z-components Lz and Sz are not."
  explanation: "This is a general principle in quantum mechanics: when two systems interact, individually conserved quantities can cease to be conserved, but the total of the coupled system often remains conserved by symmetry. Spin-orbit coupling is the physical mechanism behind atomic fine structure — the splitting of spectral lines into doublets and multiplets. The sodium D-line doublet, for example, arises from the j = 3/2 and j = 1/2 levels of the 3p electron (l = 1), with the energy splitting proportional to the L⃗·S⃗ expectation value in each state."
```

## Explainer

From your study of orbital angular momentum L⃗ and spin angular momentum S⃗, you know that each has its own quantum numbers (l, mₗ) and (s, mₛ) respectively, each satisfies the angular momentum commutation relations, and each has its own quantization axis. When a particle has both orbital motion and spin — an electron in a hydrogen atom, for instance — the full rotational state is described by both simultaneously. But the two angular momenta are not independent: they interact through **spin-orbit coupling**, and the physically conserved quantity in the presence of that coupling is their vector sum, the **total angular momentum** J⃗ = L⃗ + S⃗.

The mathematical structure of J⃗ follows directly from the commutation relations of L⃗ and S⃗. Because L⃗ and S⃗ operate on different spaces (spatial wavefunctions vs. spinor space), all components of L⃗ commute with all components of S⃗. Their sum J⃗ therefore satisfies [Jᵢ, Jⱼ] = iℏ εᵢⱼₖ Jₖ — the same algebra as any angular momentum. This means J² and Jz can be simultaneously diagonalized, giving states |j, mⱼ⟩ with J²|j, mⱼ⟩ = ℏ²j(j+1)|j, mⱼ⟩ and Jz|j, mⱼ⟩ = ℏmⱼ|j, mⱼ⟩. The quantum number j takes values from |l − s| to l + s in integer steps, and mⱼ ranges from −j to +j.

For a single electron (s = ½) with orbital quantum number l, the only possibilities are j = l + ½ and j = l − ½ (as long as l ≥ 1; for l = 0, only j = ½ exists). This is the origin of the doublet structure in atomic spectra: a p-electron (l = 1) splits into a j = 3/2 level and a j = 1/2 level, producing the familiar doublets seen in sodium's yellow emission lines. The j = 3/2 level has 2j+1 = 4 substates and the j = 1/2 level has 2 substates, accounting for all 6 states from the (mₗ, mₛ) basis.

The two descriptions — the **uncoupled basis** |l, mₗ; s, mₛ⟩ and the **coupled basis** |j, mⱼ⟩ — are related by the **Clebsch-Gordan coefficients**. These are the expansion coefficients ⟨l, mₗ; s, mₛ | j, mⱼ⟩, which can be looked up in tables or computed using ladder operators. You use the uncoupled basis when L⃗ and S⃗ independently conserved quantities (e.g., weak magnetic fields where spin-orbit coupling can be neglected); you use the coupled basis when spin-orbit coupling mixes them, which is the physically relevant case for atomic fine structure and for understanding spectroscopic selection rules in real atoms.
