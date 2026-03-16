---
id: periodic-table-electronic-structure
title: The Periodic Table and Atomic Electronic Structure
domain: physics
course: modern-physics
prerequisites:
- id: electron-configuration-aufbau-principle
  type: hard
tags:
- quantum
- atoms
- periodic-table
stage: abstract-reasoning
status: draft
---

# The Periodic Table and Atomic Electronic Structure

## Core Idea
The periodic table's structure emerges directly from electronic configuration and the aufbau principle. Elements in the same group have similar valence electron configurations, explaining chemical periodicity. Periods correspond to filling successive shells; blocks (s, p, d, f) reflect which subshell is being populated. This quantum mechanical understanding unifies the empirical periodic table.

## Explainer

The periodic table was originally an empirical discovery — Mendeleev arranged elements by atomic mass and noticed that properties repeated at regular intervals. The quantum mechanical explanation you now have makes the underlying reason transparent: properties repeat because electronic configurations repeat. From the aufbau principle you know that electrons fill orbitals in order of increasing energy, subject to the Pauli exclusion principle (at most two electrons per orbital) and Hund's rules (within a degenerate set, maximize spin). Every element's ground-state configuration is just the result of filling one more electron than the previous element.

The table's rows, called **periods**, correspond to filling a new principal quantum number shell. Period 1 fills the 1s subshell (2 elements: H and He). Period 2 fills 2s and 2p (8 elements). Period 3 fills 3s and 3p (8 elements). Period 4 is longer — 18 elements — because the 3d subshell, energetically lower than 4p, fills during this period (the transition metals). The width of each row directly reflects the number of orbitals being filled: 2 elements for s-subshells, 6 for p-subshells, 10 for d-subshells, 14 for f-subshells (the lanthanides and actinides). This is why the table has its characteristic staircase shape.

The columns, called **groups**, collect elements with the same **valence electron configuration** — the electrons in the outermost occupied shell that are not part of a completed inner shell. Group 1 elements (alkali metals) all have one s-electron outside a closed configuration: H is 1s¹, Li is [He]2s¹, Na is [Ne]3s¹, K is [Ar]4s¹. Because their outer electrons see a similar effective nuclear charge (shielded by inner electrons) and occupy similar orbital types, they behave chemically alike — all readily donate that one electron and form +1 cations. Group 17 (halogens) all have configurations ending in np⁵ — one electron short of a full p-subshell — so they all readily accept an electron. The periodicity of chemistry is the periodicity of valence configurations.

The four **blocks** of the table (s, p, d, f) mark which subshell type is being filled. The s-block (groups 1–2) fills s-orbitals; the p-block (groups 13–18) fills p-orbitals; the d-block (transition metals, groups 3–12) fills d-orbitals; the f-block (lanthanides and actinides) fills f-orbitals. **Periodic trends** in atomic radius, ionization energy, and electron affinity all follow from how effectively the nuclear charge is screened by inner electrons (**shielding**) and how tightly the valence electrons are held. Across a period, nuclear charge increases while shielding stays roughly constant, so the effective nuclear charge Z_eff increases — atomic radius shrinks and ionization energy rises. Down a group, each new period adds a new shell farther from the nucleus, increasing atomic radius and decreasing ionization energy.

## Questions

```yaml
- question: "Why are sodium (Na) and potassium (K) placed in the same group, and why do they have similar chemical properties?"
  type: short-answer
  answer: "Both have a single s-electron outside a filled noble-gas core: Na is [Ne]3s¹ and K is [Ar]4s¹. Their valence electron configuration is the same type (one s-electron, relatively loosely held), so both metals readily lose that electron to form stable +1 cations, react vigorously with water, and form similar ionic compounds."
  explanation: "Group membership is determined by valence configuration, not total electrons. The key similarity is the single outer s-electron facing a shielded nuclear charge. K has that electron in a higher shell (farther from nucleus), so it is even more loosely held than Na's — potassium reacts more violently with water, consistent with lower ionization energy."

- question: "Cobalt (Z=27) is in period 4 and the d-block. Write its electron configuration and explain which block and period it belongs to based on that configuration."
  type: short-answer
  answer: "Co: [Ar] 3d⁷ 4s². It belongs to period 4 (outer electrons are in n=4 shell: 4s²) and the d-block (the partially filled subshell being filled is 3d). It is element 9 in the d-block (3d⁷ means seven of the possible ten d-electrons are present, placing it in group 9)."
  explanation: "Identifying block: look at which subshell type holds the last electron added (or the partially filled subshell): here it is 3d, so d-block. Identifying period: the outermost occupied principal quantum number shell is n=4 (the 4s electrons), so period 4. The d-block fills n−1 d-orbitals while n s-orbitals are also occupied, which is why transition metals are in the 4th period but fill 3d orbitals."
```
