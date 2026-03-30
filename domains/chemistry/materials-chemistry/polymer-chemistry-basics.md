---
id: polymer-chemistry-basics
title: Polymer Chemistry Basics
domain: chemistry
course: materials-chemistry
prerequisites:
- id: covalent-bonding
  type: hard
- id: intermolecular-forces
  type: hard
- id: chemical-kinetics
  type: soft
builds-toward:
- conducting-polymers-chemistry
- composite-materials-chemistry
- biomaterials-chemistry
tags:
- polymers
- polymerization
- molecular weight
- crystallinity
- glass transition
stage: advanced
status: validated
---

# Polymer Chemistry Basics

## Core Idea
Polymers are macromolecules built from repeating monomer units linked by covalent bonds. The two fundamental polymerization mechanisms — chain-growth (addition) and step-growth (condensation) — produce materials with different molecular weight distributions and architectures. Polymer properties depend on molecular weight, chain architecture (linear, branched, cross-linked), tacticity, crystallinity, and the glass transition temperature (T_g). Below T_g, an amorphous polymer is glassy and brittle; above T_g, it becomes rubbery and flexible. Understanding these structure-property relationships allows rational design of materials from soft elastomers to rigid engineering plastics.

## Questions

```yaml
- question: "Nylon-6,6 is produced by the reaction of hexamethylenediamine with adipic acid. What type of polymerization is this, and what small molecule is eliminated?"
  type: multiple-choice
  options:
    - "Chain-growth polymerization; no small molecule is eliminated"
    - "Step-growth (condensation) polymerization; water is eliminated at each coupling step"
    - "Ring-opening polymerization; CO2 is eliminated"
    - "Free radical polymerization; HCl is eliminated"
  answer: 1
  explanation: "Each amide bond forms by reaction of an amine (-NH2) with a carboxylic acid (-COOH), eliminating one water molecule. This is step-growth polymerization: any two oligomers with complementary end groups can react at any time, and molecular weight builds slowly until very high conversion. The distinction from chain-growth polymerization (where monomers add one at a time to an active chain end) has practical consequences: step-growth requires very high conversion (>99%) to achieve high molecular weight, making stoichiometric balance of the two monomers critical."

- question: "A polymer sample has a number-average molecular weight (M_n) of 50,000 g/mol and a weight-average molecular weight (M_w) of 150,000 g/mol. What is the polydispersity index, and what does it indicate?"
  type: short-answer
  answer: "PDI = M_w/M_n = 150,000/50,000 = 3.0. This indicates a broad molecular weight distribution — the sample contains chains of widely varying lengths. A PDI of 1.0 would mean all chains are identical (monodisperse). Step-growth polymers typically have PDI near 2.0 (the most probable distribution); a PDI of 3.0 suggests either a broad step-growth distribution at moderate conversion or a blend of fractions. Living polymerization techniques can achieve PDI < 1.1."
  explanation: "Polymers are fundamentally different from small molecules in that a sample is always a mixture of chains with different lengths. M_n weights every chain equally; M_w gives more weight to longer chains. Their ratio (PDI) measures the breadth of the distribution. This matters because many properties (melt viscosity, toughness, processability) depend on the full distribution, not just the average. Gel permeation chromatography (GPC) is the standard method for measuring both averages."

- question: "Below its glass transition temperature, polystyrene is hard and brittle. Above T_g, it becomes soft and flexible. This transition involves melting of the crystalline regions."
  type: true-false
  answer: false
  explanation: "The glass transition is NOT a melting transition. It occurs in amorphous regions (or entirely amorphous polymers like atactic polystyrene) and represents the onset of large-scale segmental motion of the polymer backbone. Below T_g, chains are frozen in place and the material behaves like a glass. Above T_g, chains gain enough thermal energy for cooperative segmental motion, making the material rubbery. Melting (T_m) is a separate, first-order transition that occurs only in crystalline regions at a higher temperature. Many polymers have both T_g (amorphous regions) and T_m (crystalline regions)."

- question: "Why does cross-linking a polymer prevent it from dissolving in solvents?"
  type: short-answer
  answer: "Cross-links are covalent bonds connecting different polymer chains into a single network. Because dissolving a polymer requires separating individual chains and surrounding them with solvent, a cross-linked network cannot dissolve — the chains are permanently bonded together. The network can swell (absorb solvent and expand) but not dissolve, because breaking covalent cross-links requires energies far exceeding the thermal energy available in solution. The degree of cross-linking determines the swelling ratio: lightly cross-linked networks swell extensively, while heavily cross-linked materials barely swell at all."
  explanation: "This distinction between dissolving and swelling is fundamental. A linear polymer dissolves because individual chains separate into solution. A cross-linked polymer (vulcanized rubber, epoxy resin, hydrogel) forms a single macroscopic molecule — the entire sample is one covalently bonded entity. This is why cross-linked polymers are thermosets: they cannot be melted and reprocessed, unlike thermoplastic linear polymers."
```

## Explainer

Polymer chemistry is the science of building and understanding macromolecules — chains of hundreds to millions of atoms formed by linking small monomer units through covalent bonds. The field rests on two pillars: the **chemistry of polymerization** (how you make the chains) and the **physics of polymer structure** (how chain architecture determines material properties).

**Chain-growth** (addition) polymerization adds one monomer at a time to an active chain end — a radical, cation, or anion. The chain grows rapidly once initiated; at any moment, the reaction mixture contains unreacted monomer, fully grown dead chains, and a few actively growing chains. Polyethylene, polystyrene, and poly(methyl methacrylate) are made this way. **Step-growth** (condensation) polymerization allows any two molecules with complementary functional groups to react — monomer with monomer, dimer with trimer, oligomer with oligomer. Molecular weight builds gradually, and high molecular weight requires very high conversion (>99%). Polyesters, polyamides (nylon), and polyurethanes are step-growth polymers. The distinction matters practically: chain-growth gives high molecular weight early; step-growth requires patience and precise stoichiometry.

The properties of a polymer are not determined by its chemical formula alone — **architecture** matters enormously. Linear polyethylene (HDPE) is rigid and crystalline; branched polyethylene (LDPE) is flexible and largely amorphous. The branches disrupt chain packing, reducing crystallinity and density. **Tacticity** — the stereochemical arrangement of substituents along the chain — similarly affects crystallinity. Isotactic polypropylene (all methyl groups on the same side) crystallizes readily and is a strong structural plastic; atactic polypropylene (random arrangement) is an amorphous gum.

The **glass transition temperature** (T_g) is perhaps the most important single parameter for amorphous polymer behavior. It marks the temperature at which cooperative segmental motion of the backbone begins. Below T_g, the material is hard, brittle, and glassy. Above T_g, it is soft, flexible, and rubbery. T_g depends on chain stiffness (aromatic backbones raise T_g), side group bulkiness (large groups restrict motion, raising T_g), and intermolecular interactions (hydrogen bonding raises T_g). Designing a polymer for a specific application often starts with targeting the right T_g — a tire rubber needs T_g well below room temperature, while an engineering plastic needs T_g well above it.
