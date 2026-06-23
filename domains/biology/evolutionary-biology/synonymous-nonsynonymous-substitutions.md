---
id: synonymous-nonsynonymous-substitutions
title: Synonymous vs. Non-synonymous Substitutions
domain: biology
course: evolutionary-biology
prerequisites:
- id: genetic-code
  type: hard
- id: molecular-evolution
  type: hard
- id: codon-bias-and-selection
  type: soft
- id: nearly-neutral-evolution
  type: soft
- id: positive-selection
  type: soft
- id: horizontal-gene-transfer
  type: soft
tags:
- molecular-evolution
- selection
stage: advanced
status: validated
---
# Synonymous vs. Non-synonymous Substitutions

## Core Idea
Synonymous substitutions (silent, do not change amino acids) accumulate faster than non-synonymous substitutions due to weaker purifying selection. The ratio dN/dS (non-synonymous to synonymous rate) reveals selection pressure: dN/dS < 1 indicates purifying selection, dN/dS > 1 suggests positive selection for protein change.

## Questions

```yaml
- question: "You compare a gene encoding a core histone protein between humans and yeast and find dN/dS = 0.005. You compare a gene encoding a reproductive protein and find dN/dS = 1.8. What do these values indicate about the selective pressures on each protein?"
  type: multiple-choice
  options:
    - "The histone gene mutates 360 times more slowly than the reproductive gene because histones are better protected by DNA repair"
    - "The histone gene is under intense purifying selection (nearly all amino acid changes are deleterious), while the reproductive gene is under positive selection favoring amino acid change"
    - "The histone gene has fewer nonsynonymous sites, making dN/dS artificially low"
    - "Both genes are evolving neutrally, but the histone gene has a much lower mutation rate"
  answer: 1
  explanation: "dN/dS reflects selection, not mutation rate — synonymous changes serve as the internal control for the neutral mutation rate in the same gene. A dN/dS of 0.005 for histones means 99.5% of amino acid changes are removed by purifying selection (histones are so constrained that they are nearly identical across all eukaryotes). A dN/dS of 1.8 means nonsynonymous changes are accumulating faster than synonymous ones — impossible under neutrality, and only explainable by selection actively *favoring* protein evolution, as occurs in immune and reproductive arms races. Option D is wrong because the synonymous rate is the baseline — if mutation rate differed, both dN and dS would change proportionally."

- question: "A synonymous substitution changes a codon from CUU to CUC. Why is this substitution expected to accumulate at approximately the neutral mutation rate?"
  type: multiple-choice
  options:
    - "Synonymous substitutions are in non-coding regions and are not visible to repair machinery"
    - "Both codons encode leucine, so the amino acid sequence is unchanged; the protein's function is unaffected, leaving natural selection no foothold to remove or favor the change"
    - "Synonymous changes occur at the third codon position, which mutates faster due to polymerase slippage"
    - "Natural selection cannot detect changes smaller than a full codon"
  answer: 1
  explanation: "The key is that synonymous substitutions leave the protein sequence unchanged — and protein function is what selection primarily acts on. A change that does not alter the protein provides no fitness difference, so selection neither removes it (no purifying selection) nor promotes it (no positive selection). These changes are effectively neutral and accumulate at the rate determined by the background mutation rate. Option C contains a kernel of truth (wobble position mutates more readily) but that is not the reason synonymous changes are neutral — they accumulate neutrally because they have no protein-level consequence."

- question: "A gene showing dN/dS ≈ 1 across its entire length is likely evolving under positive selection that is balanced against purifying selection."
  type: true-false
  answer: false
  explanation: "dN/dS ≈ 1 is the signature of *neutral evolution*, not a balance between positive and purifying selection. It means nonsynonymous and synonymous changes are accumulating at the same rate, implying that amino acid changes in this protein have little or no fitness effect — the protein is not strongly constrained but is also not under directional pressure. Balanced positive and purifying selection would produce different dN/dS values at different sites or lineages, not a genome-wide average near 1. Pure neutrality (no selection at all) is the most parsimonious interpretation of dN/dS = 1."

- question: "A synonymous substitution can, in principle, affect an organism's fitness even though it does not change the encoded amino acid."
  type: true-false
  answer: true
  explanation: "Synonymous substitutions are treated as *approximately* neutral in the dN/dS framework, but they are not always perfectly neutral. Synonymous changes can affect codon usage bias (some codons are translated faster or more accurately, affecting protein production speed), mRNA secondary structure (which influences stability and translation), exonic splicing enhancers (regulatory sequences that overlap with coding sequence), and in some cases protein folding speed (cotranslational folding can depend on translation pauses at rare codons). The dN/dS method uses synonymous rate as an approximation of the neutral mutation rate, and for most genes this is reasonable — but it is an approximation."

- question: "Explain why dN/dS > 1 can only arise from positive (diversifying) selection, and cannot simply reflect a higher neutral mutation rate at nonsynonymous sites."
  type: short-answer
  answer: "The dN/dS ratio is designed to control for mutation rate differences. Both dN and dS are calculated from the same gene, exposed to the same mutation rate — synonymous changes serve as the internal control. If mutation rate were elevated at nonsynonymous sites specifically, it would elevate dS at those positions too (since third-codon synonymous sites and second-codon nonsynonymous sites share the same gene context). The only way dN can exceed dS is if natural selection is *removing* synonymous changes (making dS artificially low) — which makes no sense, since synonymous changes are neutral — or if selection is *favoring* nonsynonymous changes and increasing their fixation rate above the neutral expectation. The latter is positive selection by definition."
  explanation: "In other words, because synonymous changes are used as the neutral rate benchmark *within the same gene*, the ratio is self-normalizing with respect to mutation rate. dN/dS > 1 is a clear signal that cannot be explained by mutation alone — it requires that natural selection is driving amino acid divergence at a rate exceeding what neutral drift would produce."
```

## Explainer

From the genetic code, you know that most amino acids are encoded by multiple codons — for example, leucine has six codons (UUA, UUG, CUU, CUC, CUA, CUG). This redundancy means that some nucleotide changes in a protein-coding gene alter the amino acid sequence while others do not. A **synonymous substitution** (also called a silent substitution) changes a codon to another codon that specifies the same amino acid — for instance, CUU → CUC both encode leucine. A **nonsynonymous substitution** changes the amino acid — for instance, CUU (leucine) → CCU (proline). This distinction, rooted in the structure of the genetic code, turns out to be one of the most powerful tools in molecular evolution.

The logic is straightforward: synonymous changes leave the protein untouched, so they are largely invisible to natural selection and accumulate at a rate close to the neutral mutation rate. Nonsynonymous changes alter the protein, and most such alterations are harmful, so purifying selection removes them. The result is that the **nonsynonymous substitution rate** (dN) is typically much lower than the **synonymous substitution rate** (dS). When you compare the same gene across two species, counting synonymous and nonsynonymous differences separately gives you a direct window into the selective forces acting on that protein.

The ratio **dN/dS** (also called ω or Ka/Ks) is the key metric. When dN/dS < 1, nonsynonymous changes are being removed faster than they accumulate — this is the signature of **purifying selection** constraining the protein. The lower the ratio, the stronger the constraint. When dN/dS ≈ 1, nonsynonymous and synonymous changes accumulate at the same rate, suggesting the protein (or that region of it) is evolving **neutrally** — amino acid changes have no fitness effect. When dN/dS > 1, nonsynonymous changes are accumulating *faster* than synonymous ones, which can only happen if natural selection is actively favoring amino acid changes — the hallmark of **positive selection** driving protein adaptation.

To make this concrete, consider a comparison between humans and mice. Histone genes, which encode proteins critical to chromosome structure, have dN/dS ratios near 0.01 — almost all amino acid changes are lethal and removed. Olfactory receptor genes have dN/dS around 0.3–0.5 — moderately constrained but tolerating some change. Genes involved in immune defense or reproduction sometimes show dN/dS > 1 in specific regions, indicating an evolutionary arms race where protein change is actively favored. By computing dN/dS across thousands of genes, researchers can identify which proteins are under the strongest constraint, which are evolving neutrally, and which are sites of adaptive evolution — all from sequence data alone.
