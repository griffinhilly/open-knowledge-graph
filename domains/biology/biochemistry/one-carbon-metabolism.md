---
id: one-carbon-metabolism
title: One-Carbon Metabolism and Methylation
domain: biology
course: biochemistry
prerequisites:
- id: sulfur-amino-acid-metabolism
  type: hard
builds-toward:
- nucleotide-biosynthesis-integration
tags:
- folate
- methylation
- nucleotide-synthesis
stage: formal-systems
status: validated
---

# One-Carbon Metabolism and Methylation

## Core Idea
One-carbon metabolism transfers one-carbon units at the formyl, hydroxymethyl, and methyl oxidation levels, using folate as the carrier. These units are essential for nucleotide synthesis (purines and pyrimidines) and methylation reactions via S-adenosylmethionine. The pathway integrates amino acid degradation, nucleotide biosynthesis, and gene regulation.

## Questions

```yaml
- question: "Vitamin B₁₂ deficiency causes symptoms identical to folate deficiency even when folate levels are adequate. Which mechanism best explains this?"
  type: multiple-choice
  options:
    - "B₁₂ is required to absorb folate in the intestine, so B₁₂ deficiency reduces folate uptake"
    - "Without B₁₂, methionine synthase cannot transfer the methyl group from methyl-THF to homocysteine, trapping folate as methyl-THF and preventing THF recycling"
    - "B₁₂ deficiency blocks SAM synthesis, which depletes the methyl groups needed for folate activation"
    - "B₁₂ directly activates folate reductase; without B₁₂, folate cannot be converted to its active form"
  answer: 1
  explanation: "This is the 'methyl trap.' Methionine synthase requires B₁₂ as cofactor to transfer the methyl group from N⁵-methyl-THF to homocysteine. When B₁₂ is absent, this reaction stalls and folate accumulates as methyl-THF — a dead-end form that cannot re-enter the folate cycle. Free THF becomes depleted, starving the cell of one-carbon units for nucleotide synthesis and producing megaloblastic anemia indistinguishable from folate deficiency. Folate supplementation alone cannot fix B₁₂ deficiency."

- question: "Methotrexate is used as a chemotherapy drug. Which aspect of one-carbon metabolism does it target, and why does this kill rapidly dividing cancer cells?"
  type: multiple-choice
  options:
    - "It blocks SAM synthesis, depleting methyl donors needed for DNA methylation-based gene silencing"
    - "It inhibits dihydrofolate reductase, preventing THF regeneration and starving cells of one-carbon units for both purine and thymidylate synthesis"
    - "It competes with serine for serine hydroxymethyltransferase, blocking the primary one-carbon unit source"
    - "It inhibits methionine synthase, trapping folate as methyl-THF and blocking homocysteine recycling"
  answer: 1
  explanation: "Dihydrofolate reductase (DHFR) regenerates active tetrahydrofolate (THF) after it is oxidized during thymidylate synthesis. Methotrexate tightly inhibits DHFR, causing THF to deplete rapidly. Without THF, cells cannot synthesize purines (needed for DNA and RNA) or thymidylate (dTMP, needed for DNA). Rapidly dividing cells with high nucleotide demand — like cancer cells — are killed selectively. Normal slow-dividing cells are partially protected, though toxicity to gut epithelium and bone marrow is a major side effect."

- question: "Folate deficiency and B₁₂ deficiency both cause megaloblastic anemia through the same biochemical bottleneck."
  type: true-false
  answer: true
  explanation: "Both deficiencies converge on THF depletion. Folate deficiency directly starves cells of one-carbon units. B₁₂ deficiency (via the methyl trap) traps folate as methyl-THF, also depleting functional THF. In both cases, thymidylate synthesis is impaired, blocking DNA replication. Rapidly dividing bone marrow precursors fail to divide properly, producing abnormally large, immature red blood cells — megaloblasts. This is why the anemias look clinically identical, even though B₁₂ deficiency also causes neurological damage (from impaired myelin synthesis) that folate deficiency does not."

- question: "SAM (S-adenosylmethionine) is the universal methyl donor for DNA methylation, histone methylation, and neurotransmitter synthesis. After it donates a methyl group, the pathway is complete and SAM is regenerated directly."
  type: true-false
  answer: false
  explanation: "After SAM donates a methyl group, it becomes SAH (S-adenosylhomocysteine), which is hydrolyzed to homocysteine. Homocysteine must then be remethylated by methionine synthase (using N⁵-methyl-THF and requiring B₁₂) to regenerate methionine, which is then reactivated to SAM using ATP. The cycle depends entirely on folate and B₁₂ to close. Elevated homocysteine — a sign of blocked remethylation — is associated with cardiovascular risk and marks failure of this cycle."

- question: "Explain why one-carbon metabolism is described as a 'metabolic crossroads' — what three major cellular processes does it connect, and how?"
  type: short-answer
  answer: "One-carbon metabolism connects amino acid catabolism, nucleotide biosynthesis, and methylation-based gene regulation. Serine (an amino acid) donates its hydroxymethyl group to THF, feeding one-carbon units into the folate cycle. These units are used to synthesize purines (carbons C2 and C8) and thymidylate (dTMP), supplying both DNA and RNA precursors. The methionine cycle converts N⁵-methyl-THF to methionine/SAM, which methylates DNA, histones, and other substrates to regulate gene expression. A single nutrient deficiency (folate or B₁₂) thus simultaneously impairs cell division, genome synthesis, and epigenetic control."
  explanation: "The integration means that disrupting one arm has ripple effects across all three processes. A folate-deficient pregnant woman faces impaired neural tube closure (nucleotide synthesis for rapidly dividing neural tissue), but also altered DNA methylation patterns that may affect embryo development epigenetically. This is why folate supplementation before and during early pregnancy is one of the most evidence-based interventions in clinical nutrition."
```

## Explainer

From your study of sulfur amino acid metabolism, you know that methionine is activated to **S-adenosylmethionine (SAM)**, the universal methyl donor, and that its demethylation produces homocysteine. One-carbon metabolism is the broader network that regenerates methionine from homocysteine, supplies one-carbon units for building nucleotides, and connects these processes through a shared carrier: the B-vitamin **folate** (tetrahydrofolate, or THF).

Think of THF as a molecular taxi that picks up single-carbon fragments from amino acid breakdown and delivers them wherever the cell needs a one-carbon unit. The carbon can ride at different **oxidation states** — as a formyl group (–CHO, most oxidized), a methylene group (–CH₂–), or a methyl group (–CH₃, most reduced) — and the cell can interconvert between these forms. The primary source of one-carbon units is **serine**, which donates its hydroxymethyl group to THF via serine hydroxymethyltransferase, producing glycine and N⁵,N¹⁰-methylene-THF. This methylene-THF sits at a metabolic branch point: it can be oxidized to formyl-THF for **purine synthesis** (contributing carbons C2 and C8 of the purine ring), used directly by **thymidylate synthase** to methylate dUMP to dTMP (essential for DNA synthesis), or reduced to methyl-THF for methionine regeneration.

The **methionine cycle** closes the loop. N⁵-methyl-THF donates its methyl group to homocysteine via **methionine synthase**, a reaction that requires vitamin B₁₂ as a cofactor. This regenerates both methionine (which can be reactivated to SAM) and free THF (which can pick up another one-carbon unit). SAM then methylates dozens of substrates — DNA (gene silencing via CpG methylation), histones (chromatin regulation), neurotransmitters, phospholipids, and more. Every methylation reaction produces **S-adenosylhomocysteine (SAH)**, which is hydrolyzed back to homocysteine, restarting the cycle.

The clinical importance of this pathway is enormous. **Folate deficiency** starves the cell of one-carbon units, impairing both DNA synthesis (causing megaloblastic anemia from failed cell division in bone marrow) and neural tube closure in embryos. **B₁₂ deficiency** traps folate as methyl-THF — the so-called "methyl trap" — because without B₁₂, methyl-THF cannot donate its methyl group and regenerate free THF. The result mimics folate deficiency even when folate intake is adequate. Elevated homocysteine, a marker of impaired one-carbon metabolism, is associated with cardiovascular risk. Drugs like **methotrexate** exploit this pathway by inhibiting dihydrofolate reductase, blocking THF regeneration and halting DNA synthesis in rapidly dividing cancer cells. One-carbon metabolism is thus the metabolic crossroads where amino acid catabolism, nucleotide biosynthesis, epigenetic regulation, and clinical pharmacology all converge.
