---
id: protein-trafficking-secretion
title: Protein Trafficking and Secretory Pathways
domain: biology
course: cell-biology
prerequisites:
- id: protein-targeting-and-subcellular-localization
  type: hard
tags:
- protein-trafficking
- secretion
- signal-sequences
- vesicular-transport
stage: advanced
status: draft
---

# Protein Trafficking and Secretory Pathways

## Core Idea
Secreted and membrane proteins bear signal sequences that direct them to the rough ER, where the Signal Recognition Particle (SRP) recognizes them and directs them to the ER translocon for co-translational translocation. Proteins traverse the secretory pathway (ER → Golgi → secretory vesicles), where they are modified (glycosylation, phosphorylation, proteolytic cleavage) and sorted to their destination by coat proteins and adaptors. Misfolded proteins are retained in the ER and targeted for degradation via the proteasome.

## Questions

```yaml
- question: "A researcher engineers a secretory protein with a scrambled signal peptide that SRP cannot recognize. Which outcome is most likely?"
  type: multiple-choice
  options:
    - "The protein is synthesized normally in the cytosol and later imported into the ER post-translationally via a separate receptor."
    - "The protein is synthesized in the cytosol without ER targeting, and will likely misfold or be degraded since it cannot enter the secretory pathway."
    - "The protein enters the ER via COPI-coated vesicles instead of the translocon."
    - "The ERAD pathway detects the missing signal peptide and redirects the protein to the Golgi."
  answer: 1
  explanation: "SRP recognition of the signal peptide is the essential first step in co-translational translocation. If SRP cannot recognize the signal peptide, the ribosome remains in the cytosol and translation completes there. The protein never enters the ER lumen, cannot be glycosylated or folded by ER chaperones, and cannot enter the secretory pathway. It will likely be degraded by cytosolic proteasomes. Post-translational import does exist for some organelles (mitochondria, peroxisomes) but is not the default alternative for secretory proteins."

- question: "At which location in the secretory pathway are proteins sorted into routes leading to lysosomes, the plasma membrane, or regulated secretory granules?"
  type: multiple-choice
  options:
    - "At the ER translocon, based on the signal peptide sequence."
    - "In the ER lumen, after N-linked glycosylation is complete."
    - "At the trans-Golgi network, based on sorting signals in the protein's sequence."
    - "At the plasma membrane, after default secretion delivers all proteins there first."
  answer: 2
  explanation: "Sorting decisions are made at the trans-Golgi network (TGN). This is where proteins are packaged into different vesicle populations based on their sorting signals: lysosomal enzymes carry a mannose-6-phosphate tag that is recognized by receptors directing them to lysosomes; regulated secretory proteins are packaged into dense-core granules for stimulus-triggered release; constitutive secretory proteins are continuously transported to the plasma membrane. The ER and cis/medial Golgi are for processing (folding, glycosylation modification), not final sorting."

- question: "Translation of secretory proteins is completed in the cytosol before the signal peptide is recognized by SRP and the protein is imported into the ER."
  type: true-false
  answer: false
  explanation: "Translocation into the ER is co-translational: it occurs simultaneously with translation. As soon as the signal peptide emerges from the ribosome (~20 amino acids in), SRP binds it and pauses further translation. The ribosome-SRP complex then docks with the SRP receptor on the rough ER membrane, and translation resumes with the growing polypeptide threaded directly into the translocon as it is synthesized. This co-translational mechanism is critical because fully-synthesized cytosolic proteins cannot be imported into the ER — they would fold prematurely and be too large for the translocon."

- question: "Misfolded proteins that fail ER quality control are destroyed within the ER lumen by ER-resident proteases."
  type: true-false
  answer: false
  explanation: "The ER has no proteasomes — proteasomes are cytosolic/nuclear. Misfolded proteins that persist despite repeated chaperone-assisted folding attempts are retrotranslocated back into the cytoplasm through the translocon (or associated channels) in a process called ER-associated degradation (ERAD). Once in the cytoplasm, they are ubiquitinated and degraded by the 26S proteasome. This retrotranslocation step is essential — ERAD is a cytoplasmic process, not an ER-lumenal one."

- question: "What is the role of the Signal Recognition Particle (SRP), and why is it functionally important that it acts co-translationally rather than after translation is complete?"
  type: short-answer
  answer: "SRP is a ribonucleoprotein complex that recognizes the hydrophobic signal peptide as it emerges from the ribosome, pauses translation, and escorts the ribosome-nascent chain complex to the SRP receptor on the rough ER membrane, where translation resumes and the polypeptide is threaded into the translocon. Co-translational action is essential because proteins destined for the ER must be unfolded as they pass through the narrow translocon channel. If translation were allowed to complete first, the protein would fold in the cytosol and could not be translocated. Pause-then-dock ensures the protein is threaded in while it is still an unstructured, elongating chain."
  explanation: "This co-translational mechanism is also energetically efficient: the ribosome's own translation energy drives the polypeptide through the translocon, coupling two processes that would otherwise require separate energy inputs."
```

## Explainer

From your study of protein targeting and subcellular localization, you know that signal sequences act as molecular zip codes directing proteins to specific compartments. The secretory pathway is the major highway that delivers proteins to the cell surface, the extracellular space, and membrane-bound organelles like lysosomes. Understanding this pathway means following a protein from the moment its signal sequence emerges from the ribosome to its final destination.

The journey begins during translation. As the ribosome synthesizes a secretory protein, the first ~20 amino acids to emerge form a hydrophobic **signal peptide**. The **Signal Recognition Particle (SRP)** — a ribonucleoprotein complex — binds this signal peptide and temporarily pauses translation. SRP then docks with its receptor on the rough ER membrane, threading the growing polypeptide into the **translocon**, a protein-conducting channel. Translation resumes, and the polypeptide is pushed through the translocon into the ER lumen as it is being made — this is **co-translational translocation**. Once inside, signal peptidase cleaves off the signal peptide, and ER-resident chaperones (like BiP) help the protein fold correctly.

Inside the ER, the protein receives its first modifications. **N-linked glycosylation** attaches a pre-assembled sugar tree to asparagine residues, which assists folding and serves as a quality-control tag. Chaperones and lectins (calnexin, calreticulin) inspect the protein's folding state by reading these sugar modifications. Properly folded proteins are packaged into **COPII-coated vesicles** that bud from the ER and fuse with the Golgi apparatus. Misfolded proteins are retained, given additional folding attempts, and if they persistently fail, retrotranslocated back to the cytoplasm for degradation by the proteasome — a process called **ER-associated degradation (ERAD)**.

The **Golgi apparatus** functions as the cell's processing and sorting center. Proteins enter at the cis-Golgi and move through medial and trans cisternae, receiving sequential modifications: trimming and adding sugars, adding sulfate groups, and proteolytic processing (such as cleaving proinsulin into active insulin). At the trans-Golgi network, proteins are sorted into different vesicle populations based on sorting signals in their amino acid sequence. Lysosomal enzymes receive a mannose-6-phosphate tag that directs them to lysosomes. Constitutive secretory proteins are continuously exported to the cell surface. Regulated secretory proteins are stored in dense-core granules and released only upon a specific signal — like calcium influx triggering neurotransmitter release at a synapse. Each of these routes uses distinct **coat proteins** (clathrin, COPI, COPII) and **SNARE proteins** that ensure vesicles fuse only with the correct target membrane.
