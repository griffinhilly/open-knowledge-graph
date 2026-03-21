---
id: centrosomes-and-spindle-pole-bodies
title: Centrosomes and Spindle Pole Bodies
domain: biology
course: cell-biology
prerequisites:
- id: centrosome-microtubule-organization
  type: hard
- id: mitosis
  type: soft
builds-toward:
- kinetochore-structure-and-function
- cell-cycle-phases-transitions
tags:
- centrosomes
- MTOC
- spindle-poles
stage: advanced
status: draft
---

# Centrosomes and Spindle Pole Bodies

## Core Idea
Centrosomes (also called microtubule-organizing centers, MTOCs) nucleate and organize microtubules throughout the cell cycle, serving as major spindle poles during cell division. Each centrosome contains two orthogonal centrioles (9 triplet microtubule arrangements) surrounded by pericentriolar material (PCM) enriched in γ-tubulin ring complexes that template microtubule minus-end polymerization. Centrosome duplication occurs during S phase, and the duplicated pair migrates to opposite cell poles, establishing bipolarity of the mitotic spindle apparatus.

## How It's Best Learned
Isolate and characterize centrosomes biochemically; track centrosome duplication through the cell cycle using immunofluorescence. Ablate centrosomes with laser microdissection to assess their role in spindle assembly.

## Common Misconceptions
- Centrosomes are essential for all cell division; plant cells divide without centrosomes using alternative pole assembly mechanisms. - Centrioles directly nucleate microtubules; the surrounding PCM and γ-tubulin are required for nucleation.

## Questions

```yaml
- question: "A research team uses laser ablation to destroy both centrosomes in a dividing animal cell just before mitosis. Based on your understanding, what would you predict?"
  type: multiple-choice
  options:
    - "The cell will immediately die because centrosomes are required for all aspects of cell division"
    - "The cell will form a bipolar spindle through alternative mechanisms (chromosome-driven Ran-GTP pathway and motor proteins), but division will be slower and spindle orientation may be unreliable"
    - "The cell will attempt division but will always produce multipolar spindles, leading to chromosome missegregation"
    - "The chromosomes will replicate normally but be unable to attach to any spindle fibers"
  answer: 1
  explanation: "Centrosomes are important but not absolutely required for spindle formation in animal cells. When centrosomes are ablated, microtubules can still nucleate near chromosomes via the Ran-GTP gradient, and motor proteins can organize these microtubules into a bipolar spindle. However, centrosomes normally provide speed (rapid bipolarity) and reliable spindle orientation — without them, division occurs but is slower and spatially less precise. This is why plant cells (which naturally lack centrosomes) can still divide normally using these alternative pathways. Option C describes what happens with extra centrosomes (not absent ones), which is a distinct problem."

- question: "What structure within the centrosome directly templates the minus end of new microtubules during nucleation?"
  type: multiple-choice
  options:
    - "The centriole barrel itself, whose triplet microtubules serve as seeds for new polymer growth"
    - "The γ-tubulin ring complex (γ-TuRC) within the pericentriolar material"
    - "The α/β-tubulin dimers anchored to the centriole wall"
    - "The coiled-coil PCM scaffold proteins that define the centrosome's outer boundary"
  answer: 1
  explanation: "This is the most common misconception about centrosome function. Centrioles provide structural scaffolding, but they do not nucleate microtubules directly. Nucleation occurs in the pericentriolar material (PCM) surrounding the centrioles, specifically through the γ-tubulin ring complex (γ-TuRC). The ring geometry of γ-TuRC matches the 13-protofilament arrangement of a microtubule, providing a template on which α/β-tubulin dimers assemble. The centrioles' role is to recruit and anchor PCM components — remove the centrioles but preserve PCM and you can still nucleate microtubules; have centrioles without PCM and nucleation fails."

- question: "Centrioles are the primary sites of microtubule nucleation within the centrosome."
  type: true-false
  answer: false
  explanation: "Centrioles are structural organelles that recruit and scaffold the pericentriolar material (PCM), but microtubule nucleation itself is performed by the γ-tubulin ring complexes (γ-TuRCs) embedded in the PCM. The centrioles provide the positional organization and stability of the centrosome, but their triplet microtubule walls are not templates for new cytoplasmic microtubules. This is why increasing PCM recruitment (centrosome maturation at mitotic entry) dramatically increases microtubule nucleation without changing the centrioles themselves."

- question: "Centrosome duplication begins during S phase, coinciding temporally with DNA replication."
  type: true-false
  answer: true
  explanation: "Just as DNA must be replicated once and only once per cell cycle, each centrosome must duplicate once and only once. Both processes begin during S phase, which is why cells entering mitosis have two centrosomes (one for each daughter cell) just as they have two copies of each chromosome. This coupling is not coincidental — many of the same CDK/cyclin complexes that regulate DNA replication also regulate centrosome duplication, ensuring that the two processes are coordinated. Disruptions to this coupling — allowing re-duplication without cell division — produce supernumerary centrosomes associated with cancer."

- question: "Why does having extra centrosomes (supernumerary centrosomes) in a cell contribute to genomic instability?"
  type: short-answer
  answer: "Normally, two centrosomes establish two spindle poles, creating a bipolar spindle that pulls one copy of each chromosome to each daughter cell. Extra centrosomes create additional spindle poles, forming a multipolar spindle. During anaphase, chromosomes can be pulled to three or more poles simultaneously, distributing them unequally among daughter cells. This produces aneuploid daughters — cells with incorrect chromosome numbers — which is a hallmark of many cancers. Supernumerary centrosomes thus convert a normally precise binary segregation event into a chaotic multi-way chromosome distribution."
  explanation: "This question tests whether students understand the functional consequence of centrosome number control, connecting the structural biology of centrosomes to the clinical significance of chromosome instability in cancer. The key insight is that bipolarity depends on having exactly two poles — the centrosome duplication cycle is a quality control mechanism for this geometry, and its failure has downstream consequences for genome integrity."
```

## Explainer

From your study of microtubule organization, you know that microtubules are dynamic polar polymers with a fast-growing plus end and a minus end that is typically anchored. The **centrosome** is the primary structure that anchors minus ends in animal cells, serving as the cell's main **microtubule-organizing center (MTOC)**. During interphase, a single centrosome near the nucleus organizes the radial array of microtubules that positions organelles and supports intracellular transport. During mitosis, two centrosomes move to opposite sides of the cell and become the **spindle poles**, establishing the bipolar architecture that pulls chromosomes apart.

Each centrosome has two structural layers. At its core sit a pair of **centrioles** — short cylindrical structures built from nine sets of triplet microtubules arranged in a pinwheel pattern, oriented at right angles to each other. The centrioles are surrounded by a dense protein cloud called the **pericentriolar material (PCM)**, which is where microtubule nucleation actually occurs. The key nucleation component within the PCM is the **γ-tubulin ring complex (γ-TuRC)** — a ring-shaped assembly of γ-tubulin molecules that serves as a template for the minus end of a new microtubule. Think of the γ-TuRC as a molecular socket: the ring's geometry matches the 13-protofilament structure of a microtubule, so α/β-tubulin dimers assemble directly on top of it, growing outward from the centrosome with their plus ends facing the cell periphery.

**Centrosome duplication** is tightly coupled to the cell cycle, ensuring that exactly two centrosomes are present at the onset of mitosis. Duplication begins during **S phase** (the same phase when DNA replicates) when each centriole pair separates slightly, and a new "daughter" centriole begins to assemble perpendicular to each existing "mother" centriole. By G2, the cell has two centrosomes, each with one old and one new centriole. As the cell enters mitosis, the PCM expands dramatically (a process called **centrosome maturation**), recruiting additional γ-TuRC complexes and increasing microtubule nucleation capacity. The two centrosomes then migrate to opposite poles of the cell, driven by motor proteins walking along microtubules, and the mitotic spindle assembles between them.

It is important to recognize that centrosomes are important but not absolutely essential for spindle formation. Plant cells, which lack centrosomes entirely, build functional spindles using chromosome-driven and motor-mediated microtubule organization. Even in animal cells, laser ablation of centrosomes does not prevent spindle assembly — microtubules can nucleate near chromosomes via the Ran-GTP pathway and be organized into a bipolar spindle by motor proteins. However, centrosomes provide speed and reliability: they ensure rapid establishment of bipolarity and correct spindle orientation, which determines the plane of cell division and is critical for tissue architecture during development. When centrosome number goes wrong — extra centrosomes from failed cytokinesis, for instance — cells can form multipolar spindles that missegregate chromosomes, contributing to the genomic instability seen in many cancers.
