---
id: nucleic-acid-structures
title: Nucleic Acid Structures
domain: biology
course: structural-biology
prerequisites:
- id: x-ray-crystallography
  type: hard
- id: dna-structure
  type: hard
- id: rna-structure-and-base-pairing
  type: soft
builds-toward:
- macromolecular-assemblies
tags:
- DNA-forms
- RNA-architecture
- B-DNA
- A-DNA
- Z-DNA
- ribozyme
- pseudoknot
- riboswitch
- protein-nucleic-acid
stage: expert
status: validated
---
# Nucleic Acid Structures

## Core Idea
Nucleic acid structural biology determines the three-dimensional architecture of DNA and RNA molecules and their complexes with proteins, revealing how structure encodes function beyond the primary sequence. DNA adopts distinct helical forms — B-form (the canonical right-handed Watson-Crick duplex), A-form (wider, shorter, adopted by RNA duplexes and DNA-RNA hybrids), and Z-form (left-handed, formed by alternating purine-pyrimidine sequences under high salt) — each with characteristic geometric parameters (rise, twist, groove dimensions) that determine protein recognition and biological activity. RNA structural biology is richer still: single-stranded RNA folds into complex three-dimensional architectures through a hierarchy of structural organization (secondary structure motifs like stems, loops, bulges, and pseudoknots; tertiary structure through long-range interactions, metal coordination, and ribose zippers) that enable catalytic (ribozymes), regulatory (riboswitches), and structural (ribosome) functions. Structural methods (crystallography, cryo-EM, NMR) have revealed the atomic details of major protein-nucleic acid complexes including the ribosome, nucleosome, CRISPR-Cas systems, and transcription factors bound to DNA.

## Questions

```yaml
- question: "What structural feature distinguishes B-DNA from A-DNA, and why do RNA duplexes adopt the A-form rather than B-form?"
  type: multiple-choice
  options:
    - "B-DNA and A-DNA are identical except for their sequence"
    - "B-DNA has a wide, shallow major groove and narrow, deep minor groove with 10 bp per turn, while A-DNA has a narrow, deep major groove and shallow, wide minor groove with 11 bp per turn. RNA duplexes adopt A-form because the 2'-OH group on ribose creates a steric clash in the B-form geometry — the C3'-endo sugar pucker required to accommodate the 2'-OH forces the A-form helix parameters"
    - "A-DNA is always left-handed while B-DNA is right-handed"
    - "The only difference is that A-DNA uses adenine while B-DNA uses all four bases"
  answer: 1
  explanation: "The distinction between B-form and A-form DNA is fundamentally a matter of sugar pucker and the geometric consequences that follow. In B-DNA, the deoxyribose sugar adopts a C2'-endo pucker, producing a helix with 10 bp per turn, 3.4 A rise per bp, and characteristic groove dimensions that proteins like transcription factors read for sequence recognition. In A-DNA (and all RNA duplexes), the sugar adopts a C3'-endo pucker, producing a wider, shorter helix with 11 bp per turn and 2.6 A rise. The 2'-OH of ribose sterically favors the C3'-endo conformation, which is why RNA duplexes are exclusively A-form. This structural difference has functional consequences: the A-form geometry of RNA duplexes creates a distinct pattern of groove accessibility that RNA-binding proteins recognize, and the wider major groove of A-form RNA is less accessible for sequence-specific reading."

- question: "RNA is structurally limited to forming simple Watson-Crick duplexes, similar to DNA."
  type: true-false
  answer: false
  explanation: "RNA forms vastly more complex three-dimensional structures than DNA. While RNA does form Watson-Crick duplexes (in A-form), single-stranded RNA folds back on itself through a hierarchy of structural organization: secondary structure (stems, internal loops, bulges, hairpins, junctions), tertiary interactions (pseudoknots where a loop base-pairs with a region outside its own stem, long-range kissing loops, A-minor motifs where adenines dock into the minor groove of helices, ribose zippers), and quaternary assembly (subunit interfaces in the ribosome). This structural complexity enables RNA to perform catalysis (ribozymes — the ribosome's peptidyl transferase center is an RNA enzyme), gene regulation (riboswitches that change conformation upon binding metabolites), and structural scaffolding (the ribosomal RNA that organizes ribosomal protein assembly). The structural repertoire of RNA rivals that of proteins."

- question: "How do riboswitches use structural transitions to regulate gene expression, and what structural methods have revealed their mechanism?"
  type: short-answer
  answer: "Riboswitches are structured RNA elements in the 5' untranslated regions of mRNAs that directly bind small-molecule metabolites (adenine, guanine, SAM, thiamine pyrophosphate, glycine, etc.) and undergo conformational changes that regulate transcription or translation of the downstream gene. The riboswitch has two functional domains: an aptamer domain that binds the ligand with high specificity and affinity, and an expression platform that transduces binding into a regulatory output (typically by forming or disrupting a transcription terminator hairpin or a Shine-Dalgarno sequestering structure). X-ray crystallography of riboswitch aptamer domains bound to their ligands has revealed the atomic details of recognition — showing how RNA pockets achieve molecular recognition rivaling antibody-antigen interactions, using base stacking, hydrogen bonding to Watson-Crick edges, sugar edges, and Hoogsteen edges, and metal-ion-mediated contacts. Structures of both ligand-bound and ligand-free states (when obtainable) reveal the conformational switch."
  explanation: "The adenine riboswitch structure (Serganov et al., 2004) showed that a single nucleotide change in the binding pocket switches specificity from adenine to guanine — a remarkable example of how RNA structure achieves molecular selectivity. CRISPR-Cas structures have similarly revolutionized understanding of RNA-guided DNA recognition, showing how guide RNA geometry determines target specificity."

- question: "What structural insights about protein-nucleic acid recognition have emerged from structures of CRISPR-Cas complexes?"
  type: short-answer
  answer: "Structures of CRISPR-Cas complexes (Cas9, Cas12, Cas13 bound to guide RNA and target DNA/RNA) revealed several key principles: (1) the guide RNA forms a scaffold that positions the spacer sequence for base-pairing with the target, with the protein providing a binding channel that accommodates the RNA-DNA heteroduplex; (2) Cas9 recognizes the PAM (protospacer adjacent motif) through direct protein-DNA contacts in the major groove, explaining PAM specificity; (3) target strand unwinding proceeds directionally from the PAM-proximal seed region, creating an R-loop structure; (4) the HNH and RuvC nuclease domains cleave opposite strands at defined positions relative to the PAM. These structures enabled rational engineering of Cas9 variants with altered PAM specificity, reduced off-target activity (high-fidelity variants that destabilize mismatched R-loops), and new functionalities (base editors, prime editors) — a direct example of how structural biology drives biotechnology."
  explanation: "The Cas9 structures also revealed why off-target cleavage occurs: mismatches in the PAM-distal region of the guide-target duplex are tolerated because the protein does not contact every base pair with equal stringency. This structural insight guided the engineering of high-fidelity Cas9 variants (eSpCas9, HiFi Cas9) that introduce additional contacts or energetic penalties for mismatches."
```

## Explainer

Structural biology has historically been protein-centric — the vast majority of structures in the PDB are proteins or protein-ligand complexes. But nucleic acids are structural molecules in their own right, and some of the most important structures in biology are nucleic acids or nucleic acid-protein complexes. Understanding nucleic acid structure requires different principles from protein structure: the backbone is a phosphodiester chain rather than a peptide chain, the monomers (nucleotides) are larger and more structurally homogeneous than amino acids, and the dominant organizing principle is base pairing rather than hydrophobic collapse.

**DNA structure** is defined by the iconic double helix, but the helix exists in multiple forms depending on sequence, hydration, and the presence of bound proteins. **B-DNA** — the form discovered by Watson and Crick and predominant under physiological conditions — is a right-handed helix with 10 base pairs per turn, a rise of 3.4 Angstroms per base pair, and a characteristic pattern of a wide major groove (where most transcription factors read the sequence through hydrogen bonding to base edges) and a narrow minor groove (important for minor-groove-binding drugs and AT-rich recognition). **A-DNA** is a wider, more compact right-handed helix (11 bp/turn, 2.6 A rise) adopted under dehydrating conditions and by all RNA duplexes and DNA-RNA hybrids. **Z-DNA** is a left-handed helix formed by alternating purine-pyrimidine sequences (especially d(CG) repeats) under high-salt conditions; its biological role remains debated but it has been linked to transcription regulation and immune sensing (the ZBP1 protein recognizes Z-form nucleic acids). These forms are not mere crystallographic curiosities — local transitions between B and A or B and Z forms occur in vivo and affect protein binding, replication, and recombination.

**RNA structural biology** is dramatically more complex than DNA. While DNA is primarily a double helix that stores information, RNA is a structurally versatile polymer that folds into three-dimensional shapes rivaling proteins in complexity. The key to RNA's structural repertoire is its single-stranded nature and the 2'-OH group on ribose. Single-stranded regions fold back on themselves to form **secondary structure** — stems (Watson-Crick duplexes), hairpin loops (single-stranded loops capping stems), internal loops, bulges, and multi-way junctions. These secondary structure elements then pack against each other through **tertiary interactions**: pseudoknots (where nucleotides in a loop pair with a distant region, threading the chain through itself), A-minor motifs (adenines docking into the minor groove of a helix), tetraloop-receptor interactions, ribose zippers, and metal-ion-mediated contacts (Mg2+ ions are essential for RNA tertiary structure). This hierarchical folding produces functional structures — **ribozymes** that catalyze chemical reactions (the ribosome's peptidyl transferase is an RNA enzyme), **riboswitches** that sense metabolites and regulate gene expression through conformational change, and **structural scaffolds** that organize protein assembly (ribosomal RNA provides the architectural framework for the ribosome).

The structural biology of **protein-nucleic acid complexes** has been revolutionized by cryo-EM, which can image large complexes that resist crystallization. The ribosome structures (Nobel Prize 2009 to Ramakrishnan, Steitz, and Yonath) revealed that the peptidyl transferase center is entirely RNA — confirming the ribosome as a ribozyme and supporting the RNA world hypothesis. Nucleosome structures showed how 147 bp of DNA wrap around the histone octamer in 1.65 left-handed superhelical turns, with sequence-dependent bending and specific histone-DNA contacts that influence gene regulation. CRISPR-Cas structures revealed the molecular basis of RNA-guided DNA recognition and cleavage, directly enabling the rational engineering of genome-editing tools. In each case, the three-dimensional structure provided mechanistic insights that biochemistry alone could not — understanding how a transcription factor distinguishes its target sequence, how the ribosome maintains reading frame, or how Cas9 discriminates on-target from off-target sites requires seeing the atomic architecture of these molecular machines.
