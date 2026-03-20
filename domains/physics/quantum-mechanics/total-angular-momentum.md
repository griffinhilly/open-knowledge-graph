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
status: draft
---

# Total Angular Momentum

## Core Idea
Total angular momentum J⃗ = L⃗ + S⃗ is conserved in rotationally symmetric systems. The quantum number j ranges from |l − s| to l + s; for an electron (s = ½), j = l ± ½.

## Explainer

From your study of orbital angular momentum L⃗ and spin angular momentum S⃗, you know that each has its own quantum numbers (l, mₗ) and (s, mₛ) respectively, each satisfies the angular momentum commutation relations, and each has its own quantization axis. When a particle has both orbital motion and spin — an electron in a hydrogen atom, for instance — the full rotational state is described by both simultaneously. But the two angular momenta are not independent: they interact through **spin-orbit coupling**, and the physically conserved quantity in the presence of that coupling is their vector sum, the **total angular momentum** J⃗ = L⃗ + S⃗.

The mathematical structure of J⃗ follows directly from the commutation relations of L⃗ and S⃗. Because L⃗ and S⃗ operate on different spaces (spatial wavefunctions vs. spinor space), all components of L⃗ commute with all components of S⃗. Their sum J⃗ therefore satisfies [Jᵢ, Jⱼ] = iℏ εᵢⱼₖ Jₖ — the same algebra as any angular momentum. This means J² and Jz can be simultaneously diagonalized, giving states |j, mⱼ⟩ with J²|j, mⱼ⟩ = ℏ²j(j+1)|j, mⱼ⟩ and Jz|j, mⱼ⟩ = ℏmⱼ|j, mⱼ⟩. The quantum number j takes values from |l − s| to l + s in integer steps, and mⱼ ranges from −j to +j.

For a single electron (s = ½) with orbital quantum number l, the only possibilities are j = l + ½ and j = l − ½ (as long as l ≥ 1; for l = 0, only j = ½ exists). This is the origin of the doublet structure in atomic spectra: a p-electron (l = 1) splits into a j = 3/2 level and a j = 1/2 level, producing the familiar doublets seen in sodium's yellow emission lines. The j = 3/2 level has 2j+1 = 4 substates and the j = 1/2 level has 2 substates, accounting for all 6 states from the (mₗ, mₛ) basis.

The two descriptions — the **uncoupled basis** |l, mₗ; s, mₛ⟩ and the **coupled basis** |j, mⱼ⟩ — are related by the **Clebsch-Gordan coefficients**. These are the expansion coefficients ⟨l, mₗ; s, mₛ | j, mⱼ⟩, which can be looked up in tables or computed using ladder operators. You use the uncoupled basis when L⃗ and S⃗ independently conserved quantities (e.g., weak magnetic fields where spin-orbit coupling can be neglected); you use the coupled basis when spin-orbit coupling mixes them, which is the physically relevant case for atomic fine structure and for understanding spectroscopic selection rules in real atoms.
