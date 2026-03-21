---
id: antigen-processing-pathways
title: 'Antigen Processing: Proteasomal and Endosomal Pathways'
domain: biology
course: immunology
prerequisites:
- id: protein-denaturation-and-renaturation
  type: soft
- id: innate-immune-response
  type: soft
builds-toward:
- mhc-class-i-presentation
- mhc-class-ii-presentation
tags:
- antigen-processing
- proteolysis
- presentation
stage: advanced
status: draft
---

# Antigen Processing: Proteasomal and Endosomal Pathways

## Core Idea
Antigen processing converts proteins into peptides suitable for MHC presentation through two main routes: the proteasomal pathway (cytosolic, MHC-I-associated) and the endosomal pathway (exogenous, MHC-II-associated). Proteasomal processing generates 8-10 residue peptides through sequential cleavage; endosomal processing generates 13-25 residue peptides via cathepsin digestion. Both pathways involve specific peptidase activities that determine the resulting peptide repertoire.

## How It's Best Learned
Compare proteasomal versus endosomal proteolysis in terms of enzyme specificity, peptide length, and functional outcomes. Map which processing pathway is appropriate for viral, tumor, and bacterial antigens.

## Common Misconceptions
- Proteasomal cleavage is random (the proteasome has sequence-specific cleavage preferences). - Only proteasomal and endosomal pathways exist (alternative pathways via autophagy also present).

## Questions

```yaml
- question: "A cell is infected by a virus that is using the cell's ribosomes to manufacture viral proteins. Which processing pathway handles these proteins, and which T cells will respond?"
  type: multiple-choice
  options:
    - "Endosomal pathway → MHC class II → CD4+ helper T cells, because viruses are foreign pathogens"
    - "Proteasomal pathway → MHC class I → CD8+ cytotoxic T cells, because the proteins are being produced inside the cell's cytoplasm"
    - "Both pathways equally, since the immune system cannot determine where inside the cell a protein was made"
    - "Proteasomal pathway → MHC class II → CD4+ helper T cells, because MHC-II is expressed on all nucleated cells"
  answer: 1
  explanation: "The proteasomal pathway handles intracellular proteins — including viral proteins made by hijacked ribosomes. The proteasome cleaves them into short peptides (8–10 aa), TAP transports them into the ER, and they are loaded onto MHC class I for display to CD8+ cytotoxic T cells. The sorting logic is: intracellular origin → MHC-I → CD8+ T cells → kill the infected cell. Option A is the most tempting distractor — 'virus = foreign' — but what matters is not foreign vs. self, but where in the cell the protein was produced."

- question: "A macrophage engulfs and destroys a bacterium through phagocytosis. How will fragments of bacterial proteins be presented to T cells?"
  type: multiple-choice
  options:
    - "Proteasomal pathway → MHC class I → CD8+ cytotoxic T cells, because the bacterium is now inside the cell"
    - "Endosomal pathway → MHC class II → CD4+ helper T cells, because the bacterial proteins entered the cell as exogenous material in an endosomal compartment"
    - "Both pathways in equal measure, since phagocytosis bridges intracellular and extracellular antigen handling"
    - "Endosomal pathway → MHC class I → CD8+ cytotoxic T cells, because endosomal antigens always load onto MHC-I"
  answer: 1
  explanation: "Phagocytosis is a form of endocytosis — the bacterium enters in a membrane-bound compartment (endosome/phagosome), not freely in the cytoplasm. The endosomal pathway handles exogenous antigens: cathepsins digest proteins in acidifying endosomes, and the peptides (13–25 aa) are loaded onto MHC class II for presentation to CD4+ helper T cells. The common mistake is reasoning 'the bacterium is now inside the cell, so it's intracellular → proteasomal pathway.' The pathway is determined by the compartment, not merely cell interior vs. exterior."

- question: "Every nucleated cell in the body uses MHC class I to continuously display samples of its internal protein content, allowing the immune system to detect viral infection or malignant transformation."
  type: true-false
  answer: true
  explanation: "All nucleated cells express MHC class I and continuously load it with peptides derived from the proteasomal degradation of intracellular proteins — including normal self-proteins. This constitutive surveillance means CD8+ T cells are constantly sampling what each cell is producing. If a cell is infected by a virus, viral peptides appear on MHC-I and trigger a cytotoxic response. This is why viruses that downregulate MHC-I expression (as many do) can evade CD8+ T cell killing."

- question: "Proteasomal cleavage of proteins into peptides is essentially random, producing a largely unpredictable mixture of fragments for MHC loading."
  type: true-false
  answer: false
  explanation: "The proteasome has sequence-specific cleavage preferences — it cleaves preferentially after hydrophobic and basic residues, and certain sequences are cleaved more efficiently than others. This means the peptide repertoire loaded onto MHC class I is not random but shaped by the proteasome's enzymatic specificity. Additionally, immunoproteasomes (induced by interferon-γ) have altered subunit composition that shifts cleavage preferences toward generating peptides that bind MHC-I more effectively, actively tuning antigen presentation during infection."

- question: "Explain why the two-pathway system — proteasomal for intracellular antigens and endosomal for extracellular antigens — is functionally appropriate for the immune responses each pathway triggers."
  type: short-answer
  answer: "Intracellular threats (viruses manufacturing proteins inside cells, tumor mutations) are detected via the proteasomal pathway and presented on MHC class I to CD8+ cytotoxic T cells, which kill the presenting cell. This is appropriate because the cell itself is the problem — destroying it eliminates the source of infection or malignant protein. Extracellular threats (bacteria, toxins, debris) are processed via the endosomal pathway and presented on MHC class II to CD4+ helper T cells, which coordinate broader responses (antibody production via B cells, macrophage activation) without directly killing the presenting cell. The sorting matches the response type to the location and nature of the threat."
  explanation: "This functional logic is the core insight of the topic: the two pathways are not just mechanistically different — they are matched to the immune strategies needed for each threat type. Intracellular → kill the cell; extracellular → coordinate systemic response."
```

## Explainer

From your understanding of protein structure and the innate immune response, you know that the immune system must detect threats hidden inside cells — viruses hijacking cellular machinery, or tumor proteins that should not exist. But T cells cannot see intact proteins. They can only recognize short peptide fragments displayed on the cell surface by MHC molecules. **Antigen processing** is the critical intermediate step that converts full-length proteins into these presentable peptide fragments, and the cell uses two fundamentally different pathways depending on where the protein originated.

The **proteasomal pathway** handles proteins from inside the cell — the cell's own proteins, viral proteins being manufactured by hijacked ribosomes, or defective proteins marked for destruction. The **proteasome**, a barrel-shaped protein complex in the cytoplasm, threads these proteins through its central channel and cleaves them into short peptides, typically 8–10 amino acids long. These peptides are then pumped into the endoplasmic reticulum by the **TAP transporter** (Transporter Associated with antigen Processing), where they are loaded onto MHC class I molecules. The loaded MHC-I complex travels to the cell surface, presenting the peptide to CD8+ cytotoxic T cells. This pathway is how every nucleated cell in your body continuously reports on its internal protein content — a molecular surveillance system that reveals viral infection or malignant transformation.

The **endosomal pathway** handles proteins from outside the cell — bacteria that have been engulfed by phagocytosis, debris from dead cells, or soluble antigens captured by receptor-mediated endocytosis. These exogenous proteins enter the cell in membrane-bound compartments called endosomes, which progressively acidify and fuse with lysosomes. Inside these acidic compartments, **cathepsins** and other proteases digest the proteins into longer peptides, typically 13–25 amino acids. MHC class II molecules, synthesized in the ER with their peptide-binding groove blocked by a placeholder protein called the **invariant chain**, travel to these endosomal compartments. The invariant chain is degraded, leaving a small fragment called CLIP in the groove, which is then exchanged for an antigenic peptide with the help of the chaperone HLA-DM. The loaded MHC-II complex is transported to the cell surface for recognition by CD4+ helper T cells.

The elegance of this two-pathway system is that it sorts antigens by their origin and routes them to the appropriate T cell type. Intracellular threats (viruses, tumors) are processed through the proteasomal pathway and presented on MHC-I to CD8+ T cells, which kill the infected cell. Extracellular threats (bacteria, toxins) are processed through the endosomal pathway and presented on MHC-II to CD4+ T cells, which coordinate broader immune responses including antibody production and macrophage activation. This division of labor ensures that the immune response is matched to the nature of the threat.
