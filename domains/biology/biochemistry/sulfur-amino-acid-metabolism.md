---
id: sulfur-amino-acid-metabolism
title: Sulfur Amino Acid Metabolism
domain: biology
course: biochemistry
prerequisites:
- id: amino-acid-degradation-overview
  type: hard
- id: branched-chain-amino-acid-catabolism
  type: soft
builds-toward:
- one-carbon-metabolism
tags:
- methionine
- cysteine
- sulfur
stage: formal-systems
status: validated
---
# Sulfur Amino Acid Metabolism

## Core Idea
Methionine is activated to S-adenosylmethionine (SAM), the universal methyl donor for biosynthetic reactions. Cysteine is synthesized from serine and homocysteine and is a precursor for glutathione, taurine, and coenzyme A. Homocysteine is remethylated to methionine or converted to cysteine, linking these pathways to one-carbon metabolism.

## Questions

```yaml
- question: "A patient with vitamin B₁₂ deficiency shows elevated plasma homocysteine. The most direct explanation is:"
  type: multiple-choice
  options:
    - "B₁₂ is needed for the transsulfuration pathway, so homocysteine cannot be converted to cysteine"
    - "B₁₂ is a cofactor for methionine synthase, which remethylates homocysteine back to methionine; without B₁₂, this route is blocked and homocysteine accumulates"
    - "B₁₂ deficiency reduces SAM synthesis, forcing more homocysteine to accumulate upstream"
    - "B₁₂ is required for the initial activation of methionine to SAM by methionine adenosyltransferase"
  answer: 1
  explanation: "Methionine synthase — which uses N⁵-methyl-THF to remethylate homocysteine back to methionine — requires vitamin B₁₂ as a cofactor. When B₁₂ is deficient, this reaction stalls, blocking the remethylation route. Homocysteine accumulates because it cannot be recycled. Option A is wrong: the transsulfuration pathway requires B₆ (for cystathionine β-synthase), not B₁₂. Options C and D describe steps that do not require B₁₂."

- question: "SAM is described as the 'universal methyl donor' because:"
  type: multiple-choice
  options:
    - "It is the only molecule capable of transferring methyl groups in biological systems"
    - "It donates methyl groups to a vast range of acceptors — DNA, neurotransmitters, lipids, metabolites — making it a central hub of biosynthetic methylation across biology"
    - "It is universally present in all known organisms and always functions in the same pathway"
    - "It transfers methyl groups only to universal biosynthetic precursors rather than to specific end-products"
  answer: 1
  explanation: "SAM's 'universal' role refers to the extraordinary breadth of methylation reactions it supports: DNA methylation (epigenetic regulation), conversion of norepinephrine to epinephrine, creatine biosynthesis, phosphatidylcholine production, and dozens more. This breadth is possible because SAM carries a high-energy sulfonium-bound methyl group that is reactive toward many different nucleophilic acceptors. Option A is incorrect — other methyl donors exist, but SAM is by far the most important across biology."

- question: "Cysteine is an essential amino acid because humans cannot synthesize it under any circumstances."
  type: true-false
  answer: false
  explanation: "Cysteine is *conditionally* essential — the body can synthesize it via the transsulfuration pathway (serine + homocysteine → cystathionine → cysteine), but only when methionine supply is adequate (to provide homocysteine) and vitamin B₆ is sufficient (for cystathionine β-synthase). If methionine intake is low or B₆ is deficient, cysteine synthesis fails and dietary cysteine becomes necessary. This distinguishes it from truly essential amino acids like lysine, which humans cannot synthesize at all."

- question: "After SAM donates its methyl group, the resulting S-adenosylhomocysteine (SAH) is eventually converted to homocysteine, which sits at a metabolic branch point between remethylation and transsulfuration."
  type: true-false
  answer: true
  explanation: "This accurately traces the methionine cycle: SAM → (methyl transfer) → SAH → (hydrolysis by SAH hydrolase) → homocysteine + adenosine. Homocysteine then either enters remethylation (back to methionine via methionine synthase using B₁₂/N⁵-methyl-THF, or via betaine-homocysteine methyltransferase) or transsulfuration (forward to cystathionine and then cysteine, requiring B₆). This branch point is clinically critical: failures at either branch — from B₆, B₁₂, or folate deficiency — cause homocysteine accumulation."

- question: "Why does folate deficiency raise plasma homocysteine, even though folate is not directly part of the methionine cycle itself?"
  type: short-answer
  answer: "Folate (as N⁵-methyl-THF) is the methyl donor that methionine synthase uses to remethylate homocysteine back to methionine. The enzyme transfers the methyl group from N⁵-methyl-THF onto homocysteine (with B₁₂ as cofactor), regenerating methionine. Without adequate folate, N⁵-methyl-THF is unavailable, so methionine synthase cannot complete the remethylation. Homocysteine accumulates because the primary recycling route is blocked. This explains why folate deficiency — like B₁₂ and B₆ deficiencies — is associated with hyperhomocysteinemia and the cardiovascular and neural tube risks linked to elevated homocysteine."
  explanation: "Folate connects the sulfur amino acid pathway to one-carbon metabolism (the topic this builds toward). N⁵-methyl-THF is generated by the folate cycle and used in the methionine cycle; the two cycles are therefore coupled. Deficiency in either folate or B₁₂ blocks the same enzymatic step (methionine synthase), which is why both produce similar clinical findings including elevated homocysteine and megaloblastic anemia."
```

## Explainer

From your study of amino acid degradation, you know that each amino acid has its own catabolic fate. The sulfur-containing amino acids — **methionine** and **cysteine** — are special because their metabolism is not primarily about energy extraction. Instead, these pathways exist to manage the sulfur atom and, critically, to generate **S-adenosylmethionine (SAM)**, the most important methyl donor in all of biochemistry.

The methionine cycle begins when methionine reacts with ATP in an unusual reaction catalyzed by **methionine adenosyltransferase (MAT)**. The entire adenosyl group of ATP is transferred to the sulfur atom, producing SAM — a molecule with a high-energy sulfonium ion that makes its methyl group highly reactive. SAM donates this methyl group to an enormous variety of acceptors: DNA (for epigenetic regulation), norepinephrine (to make epinephrine), guanidinoacetate (to make creatine), and phosphatidylethanolamine (to make phosphatidylcholine), among many others. After donating its methyl group, SAM becomes **S-adenosylhomocysteine (SAH)**, which is hydrolyzed to **homocysteine** and adenosine.

Homocysteine sits at a critical metabolic branch point. It can be **remethylated** back to methionine — either by methionine synthase (using N⁵-methyl-THF as the methyl donor, requiring vitamin B₁₂) or by betaine-homocysteine methyltransferase (using betaine from choline). Alternatively, homocysteine can be committed irreversibly to the **transsulfuration pathway**: cystathionine β-synthase (requiring vitamin B₆) condenses homocysteine with serine to form cystathionine, which is then cleaved to yield **cysteine**. This makes cysteine a conditionally essential amino acid — the body can synthesize it, but only if methionine intake is adequate.

The clinical relevance of this pathway is substantial. Elevated plasma **homocysteine** (hyperhomocysteinemia) is associated with cardiovascular disease, neural tube defects, and cognitive decline. Deficiencies in vitamins B₆, B₁₂, or folate all impair homocysteine disposal and raise its levels, which is why these vitamins are so tightly linked to cardiovascular health. Meanwhile, cysteine feeds into **glutathione** synthesis — the cell's primary antioxidant defense — and provides sulfur for taurine, iron-sulfur clusters, and the pantetheine moiety of coenzyme A. Understanding this network reveals why sulfur amino acid metabolism sits at the intersection of methylation biology, antioxidant defense, and one-carbon metabolism.
