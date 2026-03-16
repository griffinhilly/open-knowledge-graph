---
id: mhc-class-i-presentation
title: MHC Class I Antigen Presentation Pathway
domain: biology
course: immunology
prerequisites:
- id: major-histocompatibility-complex
  type: hard
- id: antigen-processing-pathways
  type: hard
builds-toward:
- cd8-cytotoxic-t-cells
- cross-presentation-exogenous-antigens
tags:
- mhc-i
- antigen-presentation
- proteasome
stage: advanced
status: draft
---

# MHC Class I Antigen Presentation Pathway

## Core Idea
MHC Class I presents peptides derived from cytosolic proteins, primarily through the proteasomal-ER pathway. Cytosolic proteins are ubiquitinated and degraded by the 26S proteasome; peptides are transported to the ER by TAP, trimmed to 8-10 residues, and loaded onto MHC-I in the ER with chaperone assistance. Peptide-MHC-I complexes traffic through the Golgi to the cell surface where they signal CD8+ T cells.

## How It's Best Learned
Follow a viral protein through ubiquitination, proteasomal cleavage, TAP transport, peptide trimming, and MHC-I loading. Compare this with ER-resident protein processing.

## Common Misconceptions
- All peptides reach the ER through TAP (some are generated in the ER itself or transported back across the membrane). - MHC-I loading occurs in the cytoplasm (loading occurs in the ER-Golgi intermediate compartment).

## Explainer

From your study of the major histocompatibility complex and antigen processing, you know that MHC molecules display peptide fragments on the cell surface so T cells can survey what is happening inside cells. **MHC class I** is expressed on virtually all nucleated cells, and its job is to present a sample of the cell's internal protein content to **CD8+ cytotoxic T cells**. If a cell is infected by a virus or has become cancerous, fragments of viral or abnormal proteins will appear in MHC-I, flagging the cell for destruction. The MHC-I presentation pathway is essentially an internal surveillance system: it takes proteins made in the cytosol, chops them into short peptides, and displays them on the cell surface for immune inspection.

The pathway begins in the **cytoplasm** with protein turnover. Cells constantly degrade old, misfolded, or defective proteins by tagging them with **ubiquitin** chains and feeding them into the **26S proteasome**, a barrel-shaped protease complex. The proteasome cleaves proteins into peptide fragments, typically 8–15 amino acids long. During an immune response, cells upregulate a specialized version called the **immunoproteasome**, which has altered cleavage preferences that favor peptides with hydrophobic or basic C-terminal residues — exactly the anchor residues preferred by most MHC-I molecules. This is not coincidental; the proteasome and MHC-I have co-evolved to optimize antigen presentation.

The peptides generated in the cytosol must cross the ER membrane to reach MHC-I molecules, which are assembled and loaded inside the ER. This transport is performed by the **transporter associated with antigen processing (TAP)**, a heterodimeric ABC transporter (TAP1/TAP2) embedded in the ER membrane. TAP preferentially transports peptides of 8–16 residues with hydrophobic C-termini — again matching MHC-I binding preferences. Once inside the ER lumen, peptides that are slightly too long are trimmed to the optimal 8–10 residues by **ERAP** (ER aminopeptidase). Meanwhile, newly synthesized MHC-I heavy chains are held in a **peptide-loading complex** consisting of the chaperones **calnexin**, **calreticulin**, **ERp57**, and most importantly **tapasin**, which bridges MHC-I to TAP, ensuring that MHC-I molecules are positioned right at the mouth of the transporter to receive incoming peptides.

When a peptide of appropriate length and anchor residues binds in the MHC-I groove, the complex stabilizes, the chaperones release, and the peptide-MHC-I complex travels through the Golgi to the **cell surface**. Complexes that fail to bind a suitable peptide are unstable and recycled. At the surface, CD8+ T cells scan these complexes using their T cell receptor. If a T cell recognizes a foreign peptide — say, a fragment of a viral coat protein — it will kill the presenting cell. This is why viruses like herpes and cytomegalovirus have evolved mechanisms to block TAP or downregulate MHC-I: evading this pathway lets them hide from CD8+ surveillance.
