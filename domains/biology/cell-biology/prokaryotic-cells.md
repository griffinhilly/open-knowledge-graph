---
id: prokaryotic-cells
title: Prokaryotic Cells
domain: biology
course: cell-biology
prerequisites:
- id: cell-theory
  type: hard
builds-toward:
- eukaryotic-cells
- cell-membrane-structure
tags:
- prokaryotes
- bacteria
- cell-structure
stage: concrete-operations
status: validated
---

# Prokaryotic Cells

## Core Idea
Prokaryotic cells lack a membrane-bound nucleus and other membrane-enclosed organelles; their genetic material floats freely in the cytoplasm in a region called the nucleoid. They include bacteria and archaea, and are typically much smaller (1–10 µm) than eukaryotic cells. Despite their structural simplicity, prokaryotes are metabolically diverse and ecologically dominant. Key structural features include the plasma membrane, cell wall (in most), ribosomes, and often plasmids.

## How It's Best Learned
Build a labeled diagram of a generalized bacterium. Compare it side-by-side with a eukaryotic cell diagram. Note which structures are universal (membrane, ribosomes, DNA) versus prokaryote-specific (cell wall composition, nucleoid, pili).

## Common Misconceptions
- Prokaryotes do have a cytoskeleton (primitive versions of actin and tubulin homologs), contrary to older textbook claims.
- 'No membrane-bound organelles' does not mean no internal structures — some bacteria have internal membranes for photosynthesis or other processes.

## Questions

```yaml
- question: "A new antibiotic is designed to block assembly of 80S ribosomes. Which organisms would this drug harm?"
  type: multiple-choice
  options:
    - "Bacteria only, because they use 80S ribosomes for protein synthesis"
    - "Both bacteria and human cells equally, since all cells use the same ribosomes"
    - "Human cells, because bacteria use 70S ribosomes — not 80S"
    - "Archaea only, since they are the prokaryotes with 80S ribosomes"
  answer: 2
  explanation: "Prokaryotes (bacteria and archaea) use 70S ribosomes; eukaryotes (including human cells) use 80S ribosomes. A drug targeting 80S ribosomes would harm human cells while leaving bacteria unaffected — the opposite of what an antibiotic should do. This ribosome size difference is medically exploited in reverse: antibiotics like erythromycin and tetracycline target 70S ribosomes to kill bacteria without harming human cells."

- question: "What is the nucleoid region in a prokaryotic cell?"
  type: multiple-choice
  options:
    - "A membrane-bound organelle that houses the main chromosome, analogous to a eukaryotic nucleus"
    - "A dense region of cytoplasm where the chromosome is concentrated, with no surrounding membrane"
    - "A specialized region where ribosomes are manufactured before being released into the cytoplasm"
    - "The outer membrane that separates Gram-positive from Gram-negative bacteria"
  answer: 1
  explanation: "The nucleoid is not a compartment — it has no bounding membrane. It is simply the region of cytoplasm where the single circular chromosome is most densely packed. This is the defining difference from a eukaryotic nucleus: the absence of a nuclear membrane means prokaryotic DNA is in direct contact with ribosomes, enabling simultaneous transcription and translation."

- question: "In prokaryotic cells, a ribosome can begin translating an mRNA molecule while it is still being transcribed from DNA — something impossible in eukaryotic cells."
  type: true-false
  answer: true
  explanation: "This is a direct consequence of the prokaryotic cell's defining feature: no nuclear membrane. In eukaryotes, transcription occurs inside the nucleus and the mRNA must be processed and exported before ribosomes (in the cytoplasm) can access it — separating the two processes in time and space. Prokaryotes have no such separation, so translation can begin on the emerging mRNA immediately."

- question: "Prokaryotic cells have no internal structures — they are uniform bags of cytoplasm bounded by a membrane."
  type: true-false
  answer: false
  explanation: "This is a common overgeneralization. Prokaryotes lack membrane-bound organelles, but they do have internal organization: ribosomes (70S) throughout the cytoplasm, the nucleoid region where DNA is concentrated, plasmids, and often a cell wall outside the membrane. Some bacteria also have internal membrane systems for photosynthesis. Additionally, prokaryotes have primitive cytoskeletal proteins (homologs of actin and tubulin), contrary to older textbook claims."

- question: "Why is the absence of a membrane-bound nucleus — rather than small size or structural simplicity — considered the defining characteristic of prokaryotic cells?"
  type: short-answer
  answer: "The nuclear membrane is functionally, not just structurally, significant: it determines whether transcription and translation are separated in space and time. All other 'simple' features of prokaryotes (small size, no organelles) are consequences or correlates, but a cell without a nucleus still operates as a prokaryote even if it were large or metabolically complex. The nuclear membrane defines whether gene expression follows the prokaryotic or eukaryotic pathway."
  explanation: "Size is not definitive — some prokaryotes are larger than some eukaryotes. Metabolic simplicity is not definitive — prokaryotes are often more metabolically diverse than eukaryotes. But the nuclear membrane determines the entire architecture of gene expression: whether mRNA is processed before translation, whether transcription and translation can occur simultaneously, and how the genome is organized. It is the structural feature with the most downstream functional consequences."
```

## Explainer

Cell theory tells you that all living things are made of cells and that cells are the basic unit of life. Prokaryotic cells are the simplest, oldest, and most abundant expression of that principle. The word "prokaryote" literally means "before the nucleus" — these cells lack the membrane-enclosed nucleus that defines eukaryotes. Instead, their DNA sits directly in the cytoplasm in a concentrated region called the **nucleoid**. This is not a compartment with a boundary; it is simply where the chromosome, typically a single circular DNA molecule, is most densely packed. The absence of a nuclear membrane means transcription and translation can happen simultaneously — a ribosome can begin translating an mRNA molecule while it is still being transcribed from the DNA, a feat impossible in eukaryotic cells where the nuclear envelope separates these processes.

The **plasma membrane** is the prokaryote's defining boundary, controlling what enters and exits the cell. Outside this membrane, most bacteria have a **cell wall** made of **peptidoglycan**, a polymer of sugars cross-linked by short peptide chains. This wall provides structural rigidity and protects against osmotic lysis — without it, the cell would swell and burst in dilute environments. The Gram stain, one of the first classification tools in microbiology, distinguishes bacteria by cell wall thickness: **Gram-positive** bacteria have a thick peptidoglycan layer that retains the crystal violet stain, while **Gram-negative** bacteria have a thinner peptidoglycan layer sandwiched between an inner and outer membrane. Archaea, the other major group of prokaryotes, have cell walls built from different materials entirely, reflecting their deep evolutionary divergence from bacteria.

Despite their small size (typically 1–10 µm), prokaryotes pack remarkable functional complexity into a minimal package. Their **ribosomes** (70S, smaller than eukaryotic 80S ribosomes) are the protein-synthesis factories, and this size difference is medically important — antibiotics like erythromycin and tetracycline target 70S ribosomes specifically, killing bacteria without harming human cells. Many prokaryotes carry **plasmids**, small circular DNA molecules separate from the main chromosome that often encode antibiotic resistance, toxin production, or metabolic capabilities. Plasmids can be transferred between cells through **conjugation**, allowing traits to spread horizontally through a population — a key reason antibiotic resistance can emerge so rapidly.

What prokaryotes lack in structural complexity, they make up for in metabolic diversity. While all eukaryotes are limited to a narrow range of metabolic strategies, prokaryotes collectively exploit nearly every energy source on Earth: sunlight, hydrogen gas, sulfur compounds, iron, methane, and organic molecules of every description. Some thrive in boiling hot springs, others in frozen Antarctic lakes, and still others in the oxygen-free depths of ocean sediments. This metabolic versatility, combined with rapid reproduction (some species divide every 20 minutes), makes prokaryotes the dominant form of life by biomass and ecological impact. They cycle nutrients, fix atmospheric nitrogen, decompose organic matter, and inhabit every environment on the planet — the eukaryotic world, including your own body, is built on a prokaryotic foundation.
