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

## Explainer

From your understanding of protein structure and the innate immune response, you know that the immune system must detect threats hidden inside cells — viruses hijacking cellular machinery, or tumor proteins that should not exist. But T cells cannot see intact proteins. They can only recognize short peptide fragments displayed on the cell surface by MHC molecules. **Antigen processing** is the critical intermediate step that converts full-length proteins into these presentable peptide fragments, and the cell uses two fundamentally different pathways depending on where the protein originated.

The **proteasomal pathway** handles proteins from inside the cell — the cell's own proteins, viral proteins being manufactured by hijacked ribosomes, or defective proteins marked for destruction. The **proteasome**, a barrel-shaped protein complex in the cytoplasm, threads these proteins through its central channel and cleaves them into short peptides, typically 8–10 amino acids long. These peptides are then pumped into the endoplasmic reticulum by the **TAP transporter** (Transporter Associated with antigen Processing), where they are loaded onto MHC class I molecules. The loaded MHC-I complex travels to the cell surface, presenting the peptide to CD8+ cytotoxic T cells. This pathway is how every nucleated cell in your body continuously reports on its internal protein content — a molecular surveillance system that reveals viral infection or malignant transformation.

The **endosomal pathway** handles proteins from outside the cell — bacteria that have been engulfed by phagocytosis, debris from dead cells, or soluble antigens captured by receptor-mediated endocytosis. These exogenous proteins enter the cell in membrane-bound compartments called endosomes, which progressively acidify and fuse with lysosomes. Inside these acidic compartments, **cathepsins** and other proteases digest the proteins into longer peptides, typically 13–25 amino acids. MHC class II molecules, synthesized in the ER with their peptide-binding groove blocked by a placeholder protein called the **invariant chain**, travel to these endosomal compartments. The invariant chain is degraded, leaving a small fragment called CLIP in the groove, which is then exchanged for an antigenic peptide with the help of the chaperone HLA-DM. The loaded MHC-II complex is transported to the cell surface for recognition by CD4+ helper T cells.

The elegance of this two-pathway system is that it sorts antigens by their origin and routes them to the appropriate T cell type. Intracellular threats (viruses, tumors) are processed through the proteasomal pathway and presented on MHC-I to CD8+ T cells, which kill the infected cell. Extracellular threats (bacteria, toxins) are processed through the endosomal pathway and presented on MHC-II to CD4+ T cells, which coordinate broader immune responses including antibody production and macrophage activation. This division of labor ensures that the immune response is matched to the nature of the threat.
