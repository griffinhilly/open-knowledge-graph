---
id: viral-capsid-structure
title: Viral Capsid Structure and Assembly
domain: biology
course: microbiology
prerequisites:
- id: viral-replication-cycle
  type: hard
- id: protein-quaternary-structure
  type: soft
builds-toward:
- viral-envelope-lipids-glycoproteins
tags:
- capsid
- structure
- assembly
stage: advanced
status: validated
---

# Viral Capsid Structure and Assembly

## Core Idea
Viral capsids are icosahedral or helical protein shells composed of many copies of one or a few protein types. The capsid protects the viral genome and determines virion shape and stability. Assembly is often spontaneous in vitro for simple viruses but assisted by scaffolding proteins and enzymatic maturation processes in cells.

## Questions

```yaml
- question: "A researcher purifies tobacco mosaic virus coat protein and mixes it with TMV RNA in a test tube. She observes that infectious virus-like particles form spontaneously, without any added cellular machinery. This result most directly demonstrates:"
  type: multiple-choice
  options:
    - "That cells are unnecessary for any step of viral replication, including genome copying"
    - "That all the information needed for capsid assembly is encoded in the shapes and interactions of the protein and nucleic acid components themselves"
    - "That viral scaffolding proteins are contaminating the purified coat protein preparation"
    - "That helical capsids are intrinsically more stable than icosahedral capsids"
  answer: 1
  explanation: "TMV in vitro assembly is a landmark demonstration that the assembly information resides entirely in the components — no external cellular machinery is needed to tell the protein where to go. The protein subunits and RNA carry complementary surfaces that guide self-assembly through non-covalent interactions. This does not mean cells are unnecessary for replication overall (option A is wrong — genome copying requires cellular and viral machinery), nor does it say anything about relative stability of capsid geometries. It specifically shows that assembly is encoded in the molecules themselves."

- question: "HIV protease inhibitor drugs block viral infectivity by preventing proteolytic cleavage of the Gag polyprotein after budding. This works because:"
  type: multiple-choice
  options:
    - "Uncleaved Gag coats the viral envelope and blocks the glycoproteins needed for cell entry"
    - "Gag cleavage releases free viral RNA that would otherwise be destroyed in the immature particle"
    - "Proteolytic cleavage is required to rearrange the immature spherical Gag lattice into the mature conical capsid that is competent for infectivity"
    - "Intact Gag prevents reverse transcriptase from entering the virus particle during budding"
  answer: 2
  explanation: "HIV's immature capsid is a spherical lattice of uncleaved Gag polyproteins. After budding, the viral protease cleaves Gag into its component domains (matrix, capsid, nucleocapsid), which rearrange into the characteristic conical mature capsid. This maturation is required for infectivity — particles with uncleaved Gag are non-infectious even though they contain all the viral components. Protease inhibitors block this cleavage step, producing particles that look complete but cannot infect cells. This illustrates that the capsid is not passive packaging but a dynamic structure whose rearrangement is functionally required."

- question: "Icosahedral capsids are favored by many viruses because icosahedral symmetry allows the largest internal volume for a given amount of protein, and the arrangement of subunits follows strict mathematical rules described by the triangulation number."
  type: true-false
  answer: true
  explanation: "Icosahedral symmetry is geometrically optimal for enclosing maximum volume with a given surface area, which is why it recurs across viruses as different as parvoviruses and adenoviruses. The triangulation number (T) describes how many protein subunits the icosahedron uses: T=1 requires 60 subunits (the minimum), while larger T values allow hundreds or thousands of subunits in multiples of 60. This mathematical framework explains why viral capsids are not arbitrary shapes — they follow specific symmetry rules dictated by the geometry of icosahedral packing."

- question: "Scaffolding proteins are permanent structural components of mature viral capsids — they remain in the final particle to maintain its structural integrity."
  type: true-false
  answer: false
  explanation: "Scaffolding proteins are temporary guides that assist assembly and are removed — either degraded by proteases or expelled through openings in the capsid — before the mature particle is complete. They are analogous to construction scaffolding: essential during building but absent from the finished structure. Many bacteriophages (e.g., T4, P22) and herpesviruses use scaffolding proteins this way. Their removal is often coupled to a conformational change that locks the capsid into its mature, stable form — a process called procapsid-to-capsid expansion."

- question: "Why can't the capsid of a large, complex virus simply use 60 identical protein subunits like the minimum icosahedron? What architectural solution do large viruses use to build bigger capsids without requiring many different protein types?"
  type: short-answer
  answer: "The minimum icosahedral capsid uses exactly 60 copies of one protein arranged in perfect 5-fold, 3-fold, and 2-fold symmetry. To enclose a larger genome, a larger capsid is needed, but 60 copies of a bigger protein would violate the symmetry constraints. The solution is the triangulation number (T): by dividing each triangular face of the icosahedron into smaller triangles, viruses can place more subunits on each face (60×T total) while maintaining quasi-equivalence — subunits occupy slightly different local environments but are still made from the same protein type. This allows adenovirus, for instance, to build a T=25 capsid from 1,500 copies of the same protein, encoding a large shell with minimal genetic investment."
  explanation: "The quasi-equivalence principle (Caspar and Klug) is the key insight: strict equivalence (all 60 subunits in identical environments) is impossible for larger capsids, but quasi-equivalence (subunits in similar but not identical environments) is achievable with one or a few protein types. This is why the T-number matters — it tells you how many distinct local environments exist in the capsid and how many subunits total are required. The genetic economy is enormous: a single capsid protein gene can encode a shell of thousands of subunits."
```

## Explainer

From your study of the viral replication cycle, you know that new virions must be assembled from freshly synthesized components before they can exit the host cell. The capsid — the protein shell that surrounds and protects the viral genome — is the structural core of this assembly process. Understanding capsid architecture explains how viruses solve a fundamental engineering problem: building a container large enough to hold a genome from the smallest possible number of distinct protein parts.

Most viral capsids adopt one of two basic geometries. **Helical capsids** are rod-shaped or filamentous structures where identical protein subunits (called **protomers**) spiral around the nucleic acid like steps in a spiral staircase. Tobacco mosaic virus is the classic example — a single coat protein type repeats 2,130 times to form a rigid tube. The length of the helix is determined by the length of the RNA it encloses, so the genome itself acts as a template for assembly. **Icosahedral capsids**, by contrast, form closed spherical shells with the symmetry of a 20-sided die. This geometry is favored by an enormous range of viruses — from tiny parvoviruses to large adenoviruses — because icosahedral symmetry allows the largest internal volume for a given amount of protein. The minimum icosahedral capsid uses 60 copies of a single protein, but most viruses use multiples of 60 (described by a **triangulation number**, T) to build larger shells from hundreds or thousands of subunits.

Your knowledge of protein quaternary structure helps here: capsid proteins self-assemble through the same non-covalent interactions — hydrophobic contacts, hydrogen bonds, electrostatic attractions — that drive any multi-subunit protein complex together. For simple viruses, purified capsid proteins and nucleic acid can spontaneously assemble into infectious particles in a test tube, demonstrating that all the information needed for assembly is encoded in the protein's shape. More complex viruses require **scaffolding proteins** — temporary internal structures that guide capsid assembly and are then removed or degraded, analogous to the scaffolding around a building under construction. Many viruses also undergo a **maturation** step after initial assembly, where a viral protease cleaves capsid proteins to trigger conformational changes that lock the structure into its final, stable form. HIV is a notable example: its immature capsid is a spherical lattice that is proteolytically remodeled into the distinctive cone-shaped mature capsid required for infectivity.

Capsid structure has direct practical consequences. The surface of the capsid (or the envelope proteins anchored above it) determines how the virus attaches to host cells, what immune epitopes are presented, and how stable the virion is outside the body. Naked (non-enveloped) viruses rely entirely on their capsid for environmental stability — the tight protein shell of norovirus, for instance, resists detergents, desiccation, and stomach acid, explaining why it spreads so effectively. Capsid architecture also constrains genome size: a larger genome requires a larger or more complex capsid, which is why the largest known viral genomes belong to viruses with elaborate multi-layered capsid structures.

## Explainer

From your study of the viral replication cycle, you know that a virus must package its genome into a protective particle before leaving the host cell. The structure responsible for this protection is the **capsid** — a protein shell built from many copies of one or a few protein subunits called **capsomeres**. The capsid's design solves a fundamental engineering problem: how to enclose a large nucleic acid molecule using the smallest possible amount of genetic information.

Two basic architectural solutions have evolved. **Icosahedral** capsids use 20 triangular faces arranged into a roughly spherical shape, the same geometry seen in a soccer ball. This design is extremely efficient because identical protein subunits can be arranged symmetrically to create a closed shell, with the number of subunits following precise mathematical rules described by the **triangulation number** (T-number). A T=1 capsid uses 60 subunits; larger capsids like adenovirus use T=25, requiring 1,500 copies arranged in slightly different local environments. The second solution is the **helical** capsid, where protein subunits spiral around the nucleic acid like steps in a staircase. Tobacco mosaic virus is the classic example — its rod-shaped particle is simply a helix of identical coat proteins wound around the RNA genome.

Your knowledge of protein quaternary structure helps explain why capsid assembly can be remarkably self-directed. The subunit interfaces are encoded in the protein's shape — complementary surfaces, hydrophobic patches, and electrostatic interactions guide each subunit into its correct position. For simple viruses like TMV, purified coat protein and RNA will spontaneously assemble into infectious particles in a test tube, demonstrating that all the assembly information is contained in the components themselves. More complex viruses, however, require **scaffolding proteins** that act as temporary templates during assembly and are removed or degraded in the final particle. Many bacteriophages and herpesviruses use this strategy.

After initial assembly, many capsids undergo a **maturation** step that dramatically changes their properties. In HIV, for example, the immature capsid is a spherical lattice of Gag polyproteins. After budding, the viral protease cleaves Gag into its component domains, which rearrange into the characteristic conical mature capsid. This maturation is essential for infectivity — protease inhibitor drugs exploit this dependency by blocking the cleavage step, producing non-infectious particles. The capsid is therefore not just passive packaging; it is a dynamic molecular machine whose structure determines viral stability in the environment, receptor interactions during entry, and the timing of genome release inside new host cells.
