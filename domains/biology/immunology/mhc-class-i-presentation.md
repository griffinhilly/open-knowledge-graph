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

## Questions

```yaml
- question: "A cell is infected by a virus. A viral protein is synthesized in the cytoplasm. Trace its peptide fragments to the cell surface, and identify where a TAP1-inactivating mutation blocks this pathway."
  type: multiple-choice
  options:
    - "Viral protein is ubiquitinated → degraded by the proteasome → peptides transported by TAP into the ER → trimmed by ERAP → loaded onto MHC-I → Golgi → cell surface; TAP inactivation traps peptides in the cytosol"
    - "Viral protein enters the ER directly → TAP loads it onto MHC-I in the Golgi → transported to cell surface; TAP inactivation blocks Golgi trafficking"
    - "Viral protein is degraded in the lysosome → peptides bind MHC-I in the cytoplasm → vesicle transport to surface; TAP inactivation has no effect"
    - "Viral protein is first displayed on MHC-II → converted to MHC-I presentation by TAP; TAP inactivation prevents class switching"
  answer: 0
  explanation: "The MHC class I pathway proceeds: ubiquitin tagging → 26S proteasomal degradation in the cytosol → TAP1/TAP2 transport across the ER membrane → ERAP peptide trimming → loading onto MHC-I within the peptide-loading complex (tapasin, calreticulin, ERp57) → Golgi trafficking → cell surface. A TAP1 mutation blocks the critical step of transporting cytosolic peptides into the ER, preventing MHC-I loading. Viruses like herpes simplex exploit this by encoding TAP inhibitor proteins — infected cells become invisible to CD8+ T cells."

- question: "Many viruses (herpes, CMV) encode proteins that block TAP or downregulate MHC-I surface expression. What is the evolutionary advantage of this immune evasion strategy?"
  type: multiple-choice
  options:
    - "TAP blockade prevents viral replication from being detected by innate immune sensors like Toll-like receptors"
    - "Preventing viral peptides from appearing on MHC-I stops CD8+ T cells from recognizing and killing the infected cell"
    - "Downregulating MHC-I prevents the complement system from lysing infected cells"
    - "TAP blockade prevents NK cells from releasing perforin, protecting the virus-producing cell"
  answer: 1
  explanation: "MHC class I displays peptides from intracellular proteins on the cell surface; CD8+ cytotoxic T cells patrol these displays and kill any cell presenting foreign peptides. By blocking TAP or downregulating MHC-I, a virus prevents its peptide fragments from reaching the surface, making the infected cell invisible to CD8+ T cells. This allows replication to continue without cytotoxic killing — a direct evolutionary counter to MHC-I surveillance. Note: viruses that downregulate MHC-I too aggressively risk NK cell killing, since NK cells are activated by the *absence* of MHC-I, creating an immune evasion tradeoff."

- question: "The immunoproteasome, upregulated during immune responses, preferentially generates peptides with hydrophobic C-terminal residues — the same anchor residues favored by most MHC class I binding grooves — suggesting the proteasome and MHC-I have co-evolved for optimal antigen presentation."
  type: true-false
  answer: true
  explanation: "Yes. The standard 26S proteasome cleaves proteins somewhat nonspecifically. The immunoproteasome swaps in specialized catalytic subunits (LMP2, LMP7, MECL1) that preferentially generate peptides with the hydrophobic or basic C-termini that most MHC-I alleles require for high-affinity binding. The TAP transporter is similarly biased toward peptides with these C-terminal characteristics. The entire pathway — from proteasomal cleavage to ER transport to MHC-I binding — appears tuned to efficiently generate and present peptides in the MHC-I preferred format, a system refined over millions of years of co-evolution."

- question: "MHC class I molecules present antigens derived from extracellular pathogens that have been phagocytosed and degraded in the lysosome."
  type: true-false
  answer: false
  explanation: "That description applies to MHC class II, which presents exogenous antigens to CD4+ helper T cells. MHC class I presents peptides derived from *intracellular* (cytosolic) proteins — the cell's own proteins, plus those of any intracellular pathogen such as viruses. The pathway runs: cytosolic protein → ubiquitin/proteasome → TAP → ER → MHC-I → CD8+ T cell. The MHC-I/MHC-II distinction reflects a fundamental immunological division: MHC-I monitors what is being *made* inside the cell; MHC-II monitors what has been *engulfed* from outside."

- question: "Why is MHC class I expressed on virtually all nucleated cells rather than just on professional antigen-presenting cells? What would be the immunological consequence if MHC-I were restricted to dendritic cells and macrophages?"
  type: short-answer
  answer: "Any nucleated cell can be infected by a virus or undergo malignant transformation — not just professional antigen-presenting cells. If MHC-I were restricted to dendritic cells and macrophages, viruses infecting neurons, hepatocytes, epithelial cells, or muscle would be completely invisible to CD8+ cytotoxic T cells: those cells would display no 'infected' signal, and the surveillance system would fail. The broad expression of MHC-I makes every nucleated cell a sentinel reporting on its internal state to the immune system. Any cell displaying foreign or abnormal peptides can be identified and killed before the infection spreads, regardless of cell type."
  explanation: "The contrast with MHC class II is instructive: MHC-II is restricted to professional APCs precisely because it presents exogenous antigens for helper T cell activation — a function only APCs need to perform. MHC-I's universal expression reflects its role as a comprehensive surveillance mechanism for intracellular threats, matching the universal vulnerability of any nucleated cell to infection."
```

## Explainer

From your study of the major histocompatibility complex and antigen processing, you know that MHC molecules display peptide fragments on the cell surface so T cells can survey what is happening inside cells. **MHC class I** is expressed on virtually all nucleated cells, and its job is to present a sample of the cell's internal protein content to **CD8+ cytotoxic T cells**. If a cell is infected by a virus or has become cancerous, fragments of viral or abnormal proteins will appear in MHC-I, flagging the cell for destruction. The MHC-I presentation pathway is essentially an internal surveillance system: it takes proteins made in the cytosol, chops them into short peptides, and displays them on the cell surface for immune inspection.

The pathway begins in the **cytoplasm** with protein turnover. Cells constantly degrade old, misfolded, or defective proteins by tagging them with **ubiquitin** chains and feeding them into the **26S proteasome**, a barrel-shaped protease complex. The proteasome cleaves proteins into peptide fragments, typically 8–15 amino acids long. During an immune response, cells upregulate a specialized version called the **immunoproteasome**, which has altered cleavage preferences that favor peptides with hydrophobic or basic C-terminal residues — exactly the anchor residues preferred by most MHC-I molecules. This is not coincidental; the proteasome and MHC-I have co-evolved to optimize antigen presentation.

The peptides generated in the cytosol must cross the ER membrane to reach MHC-I molecules, which are assembled and loaded inside the ER. This transport is performed by the **transporter associated with antigen processing (TAP)**, a heterodimeric ABC transporter (TAP1/TAP2) embedded in the ER membrane. TAP preferentially transports peptides of 8–16 residues with hydrophobic C-termini — again matching MHC-I binding preferences. Once inside the ER lumen, peptides that are slightly too long are trimmed to the optimal 8–10 residues by **ERAP** (ER aminopeptidase). Meanwhile, newly synthesized MHC-I heavy chains are held in a **peptide-loading complex** consisting of the chaperones **calnexin**, **calreticulin**, **ERp57**, and most importantly **tapasin**, which bridges MHC-I to TAP, ensuring that MHC-I molecules are positioned right at the mouth of the transporter to receive incoming peptides.

When a peptide of appropriate length and anchor residues binds in the MHC-I groove, the complex stabilizes, the chaperones release, and the peptide-MHC-I complex travels through the Golgi to the **cell surface**. Complexes that fail to bind a suitable peptide are unstable and recycled. At the surface, CD8+ T cells scan these complexes using their T cell receptor. If a T cell recognizes a foreign peptide — say, a fragment of a viral coat protein — it will kill the presenting cell. This is why viruses like herpes and cytomegalovirus have evolved mechanisms to block TAP or downregulate MHC-I: evading this pathway lets them hide from CD8+ surveillance.
