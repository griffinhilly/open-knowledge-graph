---
id: cluster-compounds
title: Cluster Compounds
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: metal-metal-bonding
  type: hard
- id: organometallic-chemistry-fundamentals
  type: soft
builds-toward: []
tags:
- metal clusters
- Wade's rules
- electron counting
- boranes
- carboranes
- transition metal clusters
stage: expert
status: validated
---

# Cluster Compounds

## Core Idea
Cluster compounds contain three or more metal (or main group) atoms bonded directly to one another, forming polyhedral frameworks. Their structures are governed by electron-counting rules — particularly Wade's rules, which predict the cluster geometry from the number of skeletal electron pairs (SEP). These rules unify the structural chemistry of boranes, carboranes, and transition metal clusters under a single electron-counting framework, revealing deep connections between apparently disparate classes of compounds.

## Questions

```yaml
- question: "A borane cluster B₆H₆²⁻ has 7 skeletal electron pairs. According to Wade's rules, what geometry does the B₆ framework adopt?"
  type: multiple-choice
  options:
    - "Pentagonal bipyramidal (nido, n+1 SEP for a 7-vertex parent)"
    - "Octahedral (closo, n+1 = 7 SEP for n = 6 vertices)"
    - "Trigonal prismatic"
    - "Planar hexagonal"
  answer: 1
  explanation: "Wade's rules: for a closo (closed) cluster with n vertices, the number of skeletal electron pairs is n+1. B₆H₆²⁻ has 6 boron atoms, so n = 6. The predicted SEP count for a closo structure is 6+1 = 7. Each BH unit contributes 2 skeletal electrons (B has 3 valence electrons, 1 is used for the B-H bond, 2 remain for the skeleton); 6 BH units give 12 electrons, plus the 2⁻ charge gives 14 electrons = 7 SEP. This matches the closo prediction, so the B₆ framework is a regular octahedron. This is confirmed experimentally: B₆H₆²⁻ is indeed a perfect octahedral cage."

- question: "Wade's rules predict that nido clusters have n+2 skeletal electron pairs for n vertices, which corresponds geometrically to a closo polyhedron with one vertex removed."
  type: true-false
  answer: true
  explanation: "Wade's nomenclature classifies clusters by their electron count relative to the number of vertices: closo (n+1 SEP, closed polyhedron), nido (n+2 SEP, one vertex removed from the next-larger closo polyhedron), arachno (n+3 SEP, two vertices removed). B₅H₉ is a classic nido borane: 5 boron atoms with n+2 = 7 SEP. Its B₅ framework is a square pyramid — which is an octahedron (the 6-vertex closo structure) with one vertex removed. This pattern — adding electrons opens the cluster — reflects the antibonding character of the additional electron pairs."

- question: "The isolobal analogy allows Wade's rules, originally developed for boranes, to be applied to transition metal clusters by recognizing that a BH fragment is isolobal with certain metal-ligand fragments."
  type: true-false
  answer: true
  explanation: "The isolobal analogy (developed by Roald Hoffmann) identifies molecular fragments that have the same number, symmetry, and approximate energy of frontier orbitals. A BH fragment has two skeletal electrons and three frontier orbitals — it is isolobal with fragments like Fe(CO)₃, Co(CO)₃⁺, and Re(CO)₃(Cp). This means a transition metal cluster compound can be analyzed using Wade's rules by replacing each MLₙ fragment with its isolobal BH equivalent and counting skeletal electrons the same way. Os₆(CO)₁₈ (an octahedral cluster) has the same 7 SEP as B₆H₆²⁻ — both are closo."

- question: "Explain why adding two electrons to a closo cluster (converting it to nido) causes one vertex to 'open,' and relate this to the electronic structure of the cluster."
  type: short-answer
  answer: "In a closo cluster, all n+1 bonding MOs of the skeletal framework are filled — these are the MOs that hold the cage together. Adding two more electrons (to reach n+2 SEP) must place them in what was the LUMO of the closo cage, which is an antibonding MO concentrated at one vertex. Populating this antibonding orbital weakens the bonding at that vertex, causing it to 'open' — the bonds to that vertex elongate and eventually the atom at that position becomes a bridging or external group rather than a true vertex. The result is a nido geometry: the same basic cage with one vertex removed. Further electron addition (n+3 SEP, arachno) populates another antibonding MO, opening a second vertex."
  explanation: "This is an elegant example of the connection between electron count and structure. The rules are not arbitrary — they arise from the MO energy level pattern of polyhedral clusters, where the number of bonding MOs is always n+1 for an n-vertex cage (a result provable from Euler's theorem for polyhedra)."
```

## Explainer

Cluster chemistry bridges the gap between discrete molecular compounds and bulk solids. A cluster — three or more atoms bonded directly to one another in a polyhedral arrangement — represents a size regime where the bonding is neither that of small molecules (localized two-center, two-electron bonds) nor that of extended solids (delocalized bands). Instead, cluster bonding involves delocalized skeletal electrons shared across the entire polyhedral framework, and the number of these electrons determines the shape.

Wade's rules, developed by Kenneth Wade in the 1970s, provide the unifying electron-counting framework. The key quantity is the number of skeletal electron pairs (SEP) — the electrons available for holding the cage together after subtracting those used for terminal bonds (like B-H or M-CO). For n vertices: n+1 SEP gives a closo (closed) polyhedron, n+2 gives nido (one vertex removed), n+3 gives arachno (two vertices removed). The underlying MO theory explains why: an n-vertex deltahedron (a convex polyhedron with all triangular faces) always has exactly n+1 bonding skeletal MOs, regardless of the specific shape. Filling these gives a stable closo cage. Additional electrons enter antibonding MOs that weaken specific vertices, opening the cage.

The isolobal analogy extends Wade's rules from main-group borane clusters to transition metal clusters. A BH fragment (2 skeletal electrons, 3 frontier orbitals) is isolobal with metal fragments like Fe(CO)₃ or Co(Cp). This allows you to treat Os₃(CO)₁₂ (a triangle of osmium atoms) the same way as B₃H₈⁻ (an arachno borane): count the skeletal electrons, apply Wade's rules, predict the geometry. The analogy works because the relevant frontier orbitals — those that participate in cluster bonding — have the same symmetry and occupancy regardless of whether they come from a boron atom or a metal-ligand fragment.

Cluster compounds are not just intellectual curiosities. Metal clusters are models for metal surfaces and heterogeneous catalysts — they share the same multi-center bonding and coordinative unsaturation that make surfaces reactive. Cluster catalysis operates at the boundary between homogeneous and heterogeneous regimes. Biologically, iron-sulfur clusters (Fe₂S₂, Fe₃S₄, Fe₄S₄) are essential electron transfer cofactors whose properties are directly analyzed using cluster bonding models. And the structural principles encoded in Wade's rules reappear in larger nano-clusters and nanoparticles, providing intellectual continuity from molecular chemistry to materials science.
