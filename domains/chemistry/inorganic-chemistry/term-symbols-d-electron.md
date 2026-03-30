---
id: term-symbols-d-electron
title: Term Symbols for d-Electron Configurations
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: crystal-field-theory
  type: hard
- id: group-theory-applications-inorganic
  type: soft
builds-toward:
- electronic-spectra-tanabe-sugano
- jahn-teller-effect
tags:
- term symbols
- Russell-Saunders coupling
- microstates
- spectroscopic terms
- Hund's rules
stage: expert
status: validated
---

# Term Symbols for d-Electron Configurations

## Core Idea
Term symbols (²ˢ⁺¹L) describe the electronic states of multi-electron atoms and ions by specifying the total orbital angular momentum (L), total spin (S), and multiplicity (2S+1). For d-electron configurations, term symbols enumerate all possible electronic states — including ground and excited states — which directly correspond to the energy levels seen in electronic spectra. Deriving term symbols from microstate analysis is the foundation for understanding Tanabe-Sugano diagrams and the full electronic spectrum of any transition metal complex.

## Questions

```yaml
- question: "What is the ground-state term symbol for a d³ free ion, and which of Hund's rules determines it?"
  type: multiple-choice
  options:
    - "⁴F — Hund's first rule (maximize S) gives S = 3/2 (quartet), and among the possible L values for this S, Hund's second rule (maximize L) selects L = 3 (F term)"
    - "³D — the maximum multiplicity for d³ is 3"
    - "⁴P — maximum S = 3/2 is correct, but L = 1 for a less-than-half-filled shell"
    - "²G — maximize L first, then find the matching S"
  answer: 0
  explanation: "For d³, place three electrons in five d-orbitals (ml = +2, +1, 0, −1, −2) following Hund's first rule: maximize spin. All three electrons have parallel spins: S = 3/2, giving multiplicity 2S+1 = 4 (quartet). Hund's second rule: among all microstates with S = 3/2, maximize L. The maximum L is achieved with ml values +2, +1, 0 → L = 3, which is an F term. The ground-state term is ⁴F. This same term arises for Cr³⁺ and V²⁺ (both d³). Hund's rules are applied sequentially: first maximize S, then maximize L for that S value, then apply the third rule for J if needed."

- question: "The number of microstates for a d² configuration is 45, and these microstates distribute among multiple term symbols whose total microstate count sums to 45."
  type: true-false
  answer: true
  explanation: "For d², the number of microstates is C(10,2) = 45, where 10 = 2×5 is the number of available spin-orbital combinations for d-orbitals. These 45 microstates belong to the terms ³F (21 microstates), ³P (9), ¹G (9), ¹D (5), ¹S (1): total = 21 + 9 + 9 + 5 + 1 = 45. Each term symbol ²ˢ⁺¹L has (2S+1)(2L+1) microstates. The complete enumeration of terms from microstates is a combinatorial exercise that ensures every possible electronic arrangement is accounted for."

- question: "A d⁸ configuration has the same set of term symbols as a d² configuration."
  type: true-false
  answer: true
  explanation: "This is the hole formalism: a d-shell with n electrons produces the same term symbols as one with (10−n) electrons. d² and d⁸ both give ³F, ³P, ¹G, ¹D, ¹S. The physical reason is that 8 electrons in 10 orbitals is equivalent to 2 holes — the angular momentum coupling of the holes produces the same terms as the electrons. However, the ground state J values differ (Hund's third rule): for d² (less than half-filled), J = |L−S| is lowest; for d⁸ (more than half-filled), J = L+S is lowest. The hole formalism simplifies term-symbol derivation by reducing a d⁶, d⁷, d⁸, or d⁹ problem to its equivalent d⁴, d³, d², or d¹ problem."

- question: "Starting from the microstates of a d² configuration, explain the systematic procedure for identifying all term symbols."
  type: short-answer
  answer: "1) List all 45 microstates by their ml and ms values for two electrons in d-orbitals, respecting the Pauli exclusion principle. 2) Tabulate the microstates in an ML vs MS grid (ML ranges from +4 to −4, MS from +1 to −1). 3) Identify the highest ML,MS entry: ML = +3, MS = +1 → this defines a ³F term (L=3, S=1). Remove all (2×1+1)(2×3+1) = 21 microstates belonging to ³F. 4) The highest remaining entry is ML = +2, MS = +1 → ³P term (L=1, S=1), but checking carefully, the next highest is ML = +4, MS = 0 → ¹G term (L=4, S=0). Continue removing: ¹G (9), then ³P (9), ¹D (5), ¹S (1). 5) Verify: 21 + 9 + 9 + 5 + 1 = 45. All microstates are accounted for."
  explanation: "This systematic 'peeling' procedure works for any d^n configuration. For d³, you start with C(10,3) = 120 microstates and extract ⁴F, ⁴P, ²H, ²G, ²F, ²D(×2), ²P terms. The procedure is tedious but algorithmic — each step reduces the microstate table until empty."
```

## Explainer

Crystal field theory describes d-orbital splitting using a single-electron picture: each d-electron occupies one of the split orbitals. But real multi-electron ions have electron-electron repulsions that create multiple electronic states — a d² ion does not have just one "d²" state but multiple states (³F, ³P, ¹G, ¹D, ¹S) with different energies determined by how the two electrons are arranged. Term symbols label these states, and understanding them is prerequisite to interpreting the full electronic spectra of transition metal complexes through Tanabe-Sugano diagrams.

A term symbol ²ˢ⁺¹L encodes two pieces of information. The orbital part L describes the total orbital angular momentum from all d-electrons coupled together: L = 0 (S term), 1 (P), 2 (D), 3 (F), 4 (G), and so on. The spin multiplicity 2S+1 describes the total spin: singlet (1), doublet (2), triplet (3), quartet (4), etc. Each term represents a distinct electronic state with its own energy, and the number of microstates (individual electron arrangements) within each term is (2S+1)(2L+1). Hund's rules predict the ground-state term: first maximize S, then maximize L for that S, then determine J by L−S (less than half-filled) or L+S (more than half-filled).

Deriving term symbols requires the microstate method. For d², you enumerate all 45 ways to place two electrons in five d-orbitals (with both spatial and spin quantum numbers, respecting Pauli exclusion). These microstates are organized in a table indexed by ML (sum of individual ml values) and MS (sum of individual ms values). The terms are then extracted sequentially: find the largest ML at the largest MS, identify the corresponding ²ˢ⁺¹L term, subtract its microstates, and repeat. The procedure is algorithmic and guarantees that every microstate is assigned to exactly one term.

The hole formalism provides a powerful shortcut: d^n and d^(10−n) have identical term symbols. This means you only need to work out terms for d¹ through d⁵; the d⁶ through d⁹ results follow by symmetry. When a crystal field is applied, each free-ion term splits into multiple components labeled by the irreducible representations of the point group — and these split terms become the energy levels plotted in Tanabe-Sugano diagrams. The connection is direct: the term symbols derived here are the y-axis labels at x = 0 (the free-ion limit) of every Tanabe-Sugano diagram.
