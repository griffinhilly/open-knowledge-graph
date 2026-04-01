---
id: major-histocompatibility-complex
title: Major Histocompatibility Complex Structure and Function
domain: biology
course: immunology
prerequisites:
- id: protein-tertiary-structure
  type: hard
- id: cell-signaling-intro
  type: soft
builds-toward:
- mhc-class-i-presentation
- mhc-class-ii-presentation
tags:
- mhc
- antigen-presentation
- hla
stage: advanced
status: validated
---

# Major Histocompatibility Complex Structure and Function

## Core Idea
The major histocompatibility complex (MHC) molecules present peptide antigens to T cells, controlling adaptive immune responses. MHC Class I (α-chain + β2-microglobulin) displays intracellular peptides to CD8+ T cells and is expressed on all nucleated cells. MHC Class II (α + β heterodimer) displays endosomal peptides to CD4+ T cells and is expressed on antigen-presenting cells. MHC polymorphism among individuals ensures population-level pathogen recognition diversity.

## How It's Best Learned
Sketch the three-dimensional MHC-peptide complex showing the peptide-binding groove, anchor residues, and TCR contact surfaces. Compare MHC-I and MHC-II peptide binding pockets and binding preferences.

## Common Misconceptions
- All MHC molecules bind the same peptides (peptide-binding specificity varies with MHC allotype). - MHC-I is only on immune cells (all nucleated cells express MHC-I).

## Questions

```yaml
- question: "A hepatocyte (liver cell) becomes infected by a virus. Can the adaptive immune system detect this infection, and if so, how?"
  type: multiple-choice
  options:
    - "No — only professional antigen-presenting cells like dendritic cells can activate T cells, and hepatocytes are not APCs"
    - "Yes — hepatocytes express MHC class I, which displays viral peptides from the cytoplasm to patrolling CD8+ cytotoxic T cells"
    - "Yes — but only after the hepatocyte upregulates MHC class II to activate CD4+ helper T cells"
    - "No — the liver degrades viral proteins via autophagy before they can be loaded onto MHC molecules"
  answer: 1
  explanation: "This question targets a key misconception: MHC class I is expressed on ALL nucleated cells, not just immune cells. Every nucleated cell in the body continuously samples its cytoplasmic proteins via the proteasome and loads the resulting peptides onto MHC-I. If a hepatocyte is infected, viral proteins are degraded in the cytoplasm, the peptides are loaded onto MHC-I, and the complex is displayed on the cell surface. CD8+ cytotoxic T cells recognize foreign peptide-MHC-I complexes and kill the infected cell. This is precisely why MHC-I is ubiquitous — every cell needs to be able to signal infection or transformation."

- question: "What structural feature of MHC class II explains why it presents longer peptides (13–25 amino acids) than MHC class I (8–10 amino acids)?"
  type: multiple-choice
  options:
    - "MHC class II molecules are physically larger and have a deeper binding groove"
    - "MHC class II has an open-ended peptide-binding groove, while MHC class I has closed ends that constrain peptide length"
    - "MHC class I uses disulfide bonds to clamp the peptide ends, while class II uses only non-covalent contacts"
    - "MHC class II binds peptides covalently, allowing longer chains to be accommodated"
  answer: 1
  explanation: "In MHC class I, the peptide-binding groove is closed at both ends, with conserved residues that anchor the N- and C-termini of the peptide. This physically constrains the peptide length to 8–10 amino acids — shorter or longer peptides do not fit. MHC class II has an open groove with no end constraints, allowing peptides of 13–25 amino acids to extend beyond the groove ends. This structural difference directly reflects the different sources of peptides: cytoplasmic proteasomes generate shorter, more uniform fragments; endosomal proteases generate longer, more variable ones."

- question: "MHC class I molecules display peptides derived from proteins synthesized inside the cell, allowing the immune system to detect viral infection or cancer even without any extracellular pathogen."
  type: true-false
  answer: true
  explanation: "This is the fundamental purpose of MHC class I. Cells continuously degrade their own proteins via the proteasome (including viral proteins if infected, or mutant proteins if cancerous), and the resulting peptides are loaded onto MHC-I in the endoplasmic reticulum. The MHC-I–peptide complex is then displayed on the cell surface as a 'status report' of the cell's interior. CD8+ T cells patrol these displays; any foreign peptide triggers killing. This is how the immune system detects intracellular threats that antibodies and extracellular receptors cannot see."

- question: "MHC polymorphism — the existence of thousands of HLA alleles in the human population — is a disadvantage for organ transplantation but serves no broader protective function for the species."
  type: true-false
  answer: false
  explanation: "MHC polymorphism serves a critical population-level function: each allelic variant has a different peptide-binding groove, meaning different alleles present different subsets of pathogen-derived peptides. A pathogen that evolves peptides that escape one person's MHC alleles will still be presented by someone else's different alleles. This diversity ensures that no single pathogen strain can simultaneously evade immune recognition in the entire population. The transplantation problem is a side-effect of this adaptive diversity — donor MHC molecules look 'foreign' to the recipient's T cells, triggering rejection."

- question: "Why does it make biological sense for MHC class I to be expressed on all nucleated cells rather than only on dedicated immune cells?"
  type: short-answer
  answer: "Viruses and cancer mutations can occur in any cell type in the body — not just immune cells. If only immune cells expressed MHC-I, a virus infecting a hepatocyte, lung cell, or neuron would be invisible to CD8+ T cells; the infected cell could replicate virus indefinitely with no way to signal distress. By expressing MHC-I on every nucleated cell, the immune system gains continuous surveillance coverage across all tissues. Every cell becomes its own sentinel, displaying a sample of its intracellular protein environment. This turns every cell into a potential target for cytotoxic T cells if it is infected or transformed — a much more robust surveillance system than restricting it to dedicated immune cells."
  explanation: "The universality of MHC-I expression reflects the scope of the threat it guards against: intracellular pathogens and malignant transformation can happen anywhere in the body. The cost is the self-tolerance machinery required to prevent CD8+ T cells from killing healthy cells displaying normal self-peptides — an elaborate system of thymic selection and peripheral tolerance that is precisely what breaks down in some autoimmune diseases."
```

## Explainer

From your study of protein structure, you know that the three-dimensional shape of a protein determines its function and binding specificity. From cell signaling, you know that surface receptors allow cells to communicate information about their internal state. The **major histocompatibility complex (MHC)** molecules combine both principles: they are cell-surface proteins whose sole job is to display short peptide fragments — molecular snapshots of what is happening inside the cell — for inspection by T cells. Without MHC, T cells would be blind to intracellular infections, cancers, and foreign proteins, because T cell receptors cannot recognize free-floating antigens the way antibodies can.

**MHC class I** molecules are expressed on virtually all nucleated cells in the body. They consist of a transmembrane **α chain** with three extracellular domains (α1, α2, α3) non-covalently associated with **β2-microglobulin**, a small soluble protein. The α1 and α2 domains form a **peptide-binding groove** — a cleft with a floor of β-pleated sheet and walls of α-helices — that holds peptides of 8–10 amino acids. These peptides are derived from proteins degraded by the **proteasome** in the cytoplasm: normal self-proteins, viral proteins if the cell is infected, or mutant proteins in cancer cells. The loaded MHC-I complex is then transported to the cell surface, where **CD8+ cytotoxic T cells** survey it. If the displayed peptide is foreign (viral, for example), the CD8+ T cell kills the presenting cell. This system means that every nucleated cell in your body is continuously displaying a sample of its internal protein content for immune surveillance — a cellular "inspection window" that reveals infection or transformation.

**MHC class II** molecules have a different structure and a different job. They are heterodimers of an **α chain** and a **β chain**, each contributing one domain to form the peptide-binding groove. Unlike MHC-I, the groove is open at both ends, accommodating longer peptides of 13–25 amino acids. MHC-II expression is restricted to professional **antigen-presenting cells** — dendritic cells, macrophages, and B cells — rather than all nucleated cells. These cells capture extracellular pathogens and proteins through phagocytosis or receptor-mediated endocytosis, degrade them in acidic endosomal compartments, and load the resulting peptides onto MHC-II molecules. The MHC-II–peptide complexes are presented to **CD4+ helper T cells**, which then orchestrate the broader immune response by activating B cells, macrophages, and other effectors.

The most remarkable feature of MHC is its **polymorphism** — the MHC genes (called **HLA** in humans) are the most genetically variable loci in the human genome, with thousands of alleles in the population. Each allelic variant encodes a slightly different peptide-binding groove with different anchor residue preferences, meaning different MHC alleles present different subsets of peptides from the same pathogen. This diversity operates at the population level: a pathogen that evolves to avoid presentation by one person's MHC alleles will still be presented by someone else's. This is why MHC matching is critical for organ transplantation — the recipient's T cells recognize donor MHC molecules as foreign and attack the graft — and why populations with greater MHC diversity tend to be more resilient against epidemic pathogens.
