---
id: crispr-gene-editing
title: CRISPR-Cas9 Gene Editing
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: molecular-cloning
  type: hard
- id: gene-regulation-eukaryotes
  type: hard
- id: dna-repair-mechanisms
  type: hard
- id: non-homologous-end-joining-nhej
  type: soft
tags:
- CRISPR
- Cas9
- guide RNA
- gene editing
- HDR
- NHEJ
- genome editing
stage: formal-systems
status: validated
---

# CRISPR-Cas9 Gene Editing

## Core Idea
CRISPR-Cas9 is an RNA-guided endonuclease system adapted from bacterial adaptive immunity that enables precise, programmable editing of genomic DNA. A single guide RNA (sgRNA) complementary to a 20-nucleotide target sequence directs the Cas9 protein to the desired locus, where it creates a double-strand break. The break is then repaired by either non-homologous end joining (NHEJ), which typically introduces insertions or deletions that disrupt gene function, or homology-directed repair (HDR), which uses a provided template to introduce precise edits. CRISPR has transformed biomedical research and is being developed for therapies for genetic diseases such as sickle cell disease.

## How It's Best Learned
Design a guide RNA for a gene of interest, verify that a PAM sequence (NGG) is present adjacent to the target, and predict both NHEJ and HDR outcomes. Discuss ethical considerations alongside the technical applications.

## Common Misconceptions
- CRISPR does not directly edit DNA; it creates a break that cellular repair machinery then mends — often imperfectly.
- Off-target cuts at sequences similar to the guide RNA are a real concern; high-fidelity Cas9 variants and careful guide design mitigate but do not eliminate this risk.

## Questions

```yaml
- question: "A researcher wants to use CRISPR to correct a point mutation that causes a genetic disease in patient cells. What components are required to achieve a precise correction via homology-directed repair?"
  type: multiple-choice
  options:
    - "Only a guide RNA matching the target sequence — Cas9 will correct the mutation automatically once it finds the site"
    - "A guide RNA, Cas9 protein, and a DNA repair template containing the corrected sequence flanked by homologous regions"
    - "A guide RNA and activation of NHEJ, which will insert the correct sequence at the cut site"
    - "Only Cas9 — the guide RNA is needed only for knockout experiments, not for precise corrections"
  answer: 1
  explanation: "Precise correction requires HDR, which copies from a template. Without a provided template, cells default to NHEJ, which joins broken ends imprecisely and typically introduces indels. HDR requires the guide RNA (for targeting), Cas9 (for cutting), and a template with the desired sequence flanked by sequences homologous to the genomic cut site."

- question: "Why does NHEJ editing with CRISPR typically result in gene disruption rather than a predictable specific change?"
  type: multiple-choice
  options:
    - "The Cas9 enzyme degrades nucleotides at the cut site before ligating the ends"
    - "NHEJ ligates broken ends without using a template, often introducing small insertions or deletions that shift the reading frame"
    - "The guide RNA degrades the target strand before the break is repaired, leaving a permanent gap"
    - "The indels are introduced by the PAM sequence adjacent to the cut site during repair"
  answer: 1
  explanation: "NHEJ is a fast but imprecise pathway — it rejoins broken ends without a template, and the ligation is error-prone. The resulting insertions or deletions (indels) are unpredictable in their exact sequence, but if they fall in a coding exon, they frequently disrupt the reading frame and produce a truncated, non-functional protein — a knockout."

- question: "CRISPR-Cas9 edits DNA by directly replacing the target sequence with a new sequence specified by the researcher."
  type: true-false
  answer: false
  explanation: "Cas9 only cuts both strands of DNA at the target site; it does not insert or replace any sequence. All sequence changes result from the cell's own DNA repair machinery. NHEJ repairs the break imprecisely (producing indels), while HDR can incorporate a provided template precisely — but in both cases, Cas9's role ends at the cut."

- question: "The PAM sequence (e.g., NGG for SpCas9) is required for Cas9 to initiate DNA unwinding and check for guide RNA complementarity at a potential target site."
  type: true-false
  answer: true
  explanation: "Cas9 first scans the genome for PAM sequences — its docking signal. Upon finding a PAM, it unwinds the adjacent DNA and checks whether the guide RNA matches. Without a PAM, Cas9 does not engage the DNA, even if the guide RNA matches the nearby sequence. This two-step recognition (PAM first, then base pairing) provides the specificity of targeting."

- question: "Explain why the repair pathway used after a CRISPR cut determines the nature of the edit, and why researchers cannot fully control which pathway the cell uses."
  type: short-answer
  answer: "Cas9 creates a double-strand break, but the outcome depends on which of the cell's repair pathways closes that break. NHEJ — the default, faster pathway — rejoins ends without a template, producing imprecise indels that usually disrupt gene function. HDR — a slower, template-dependent pathway — can incorporate a provided sequence precisely, but it requires the cell to be in S or G2 phase and competes with NHEJ. Because NHEJ is more active in most cell types and most of the cell cycle, it wins the competition most of the time. Researchers can bias toward HDR by supplying a template and sometimes by inhibiting NHEJ, but cannot guarantee which pathway the cell will use."
  explanation: "CRISPR's dependency on cellular repair machinery means its outcomes are probabilistic, not fully deterministic. This is why CRISPR is described as creating a break that repair machinery then 'mends — often imperfectly.'"
```

## Explainer

You already know from your study of DNA repair that cells have built-in machinery to fix double-strand breaks (DSBs), and from molecular cloning that biologists can introduce foreign DNA into cells. **CRISPR-Cas9** exploits both of these principles — it creates a targeted DSB at a specific genomic location and then lets the cell's own repair pathways introduce the desired change. What makes CRISPR revolutionary is not that it cuts DNA (restriction enzymes have done that for decades) but that it can be programmed to cut virtually any sequence in any organism simply by changing a short RNA molecule.

The system has two essential components: the **Cas9 protein** (a DNA-cutting enzyme) and a **single guide RNA (sgRNA)** that directs it to the target. The sgRNA contains a ~20 nucleotide sequence complementary to the target DNA. Cas9 scans the genome for a short motif called a **PAM** (protospacer adjacent motif, typically NGG for *S. pyogenes* Cas9) — this is its initial landing signal. When Cas9 finds a PAM, it unwinds the adjacent DNA and checks whether the sgRNA matches. If there is complementarity, Cas9 cuts both strands of the DNA. If there is no match, Cas9 moves on. This two-step recognition — PAM first, then guide RNA complementarity — provides specificity, though imperfect matches can still lead to off-target cuts.

Once the DSB is made, what happens next depends on which repair pathway the cell uses. **Non-homologous end joining (NHEJ)**, which you studied as a prerequisite, is the default in most cell types. It glues the broken ends back together quickly but imprecisely, often introducing small insertions or deletions (**indels**) at the cut site. If these indels disrupt a gene's reading frame or critical domain, the gene is effectively knocked out — this is how researchers create **gene knockouts**. Alternatively, if a DNA template with the desired edit flanked by sequences homologous to the target region is provided, **homology-directed repair (HDR)** can incorporate that template into the genome, enabling precise changes: correcting a disease-causing mutation, inserting a fluorescent tag, or swapping one version of a gene for another.

The practical impact has been enormous. Before CRISPR, making a targeted gene edit in a mouse took over a year and required specialized embryonic stem cell work. With CRISPR, the same edit can be achieved in weeks by injecting Cas9 and a guide RNA directly into embryos. In medicine, CRISPR-based therapies have already reached patients: the treatment for sickle cell disease works by using CRISPR to disrupt a repressor gene, reactivating fetal hemoglobin production to compensate for the defective adult hemoglobin. Ongoing challenges include improving HDR efficiency (NHEJ usually wins the competition), reducing off-target effects, and developing delivery methods to get CRISPR components into the right cells in a living organism. Newer variants — base editors that change single nucleotides without cutting both strands, and prime editors that write new sequences directly — are extending the technology beyond simple cuts toward precise molecular surgery.
