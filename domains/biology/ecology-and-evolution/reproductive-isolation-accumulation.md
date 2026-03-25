---
id: reproductive-isolation-accumulation
title: 'Reproductive Isolation: Mechanism Accumulation During Divergence'
domain: biology
course: ecology-and-evolution
prerequisites:
- id: reproductive-isolation
  type: hard
- id: speciation
  type: hard
- id: allopatric-speciation
  type: soft
- id: polyploidy-instant-speciation
  type: soft
builds-toward:
- modes-of-speciation-allopatric-peripatric-parapatric-sympatric
tags:
- reproductive-isolation
- barrier-evolution
- divergence
- speciation
stage: formal-systems
status: validated
---
# Reproductive Isolation: Mechanism Accumulation During Divergence

## Core Idea
Reproductive isolation accumulates gradually during allopatric divergence through drift and selection on different traits. Prezygotic barriers (mate choice, courtship incompatibility) often evolve first; postzygotic barriers (hybrid inviability, sterility) follow. The Dobzhansky-Muller model explains how independent mutations in different populations create reproductive incompatibilities.

## Questions

```yaml
- question: "An ancestral population has genotype AABB. Population 1 evolves to AAbb; Population 2 evolves to aaBB. Hybrids (AaBb) are inviable. Which of the following best explains why?"
  type: multiple-choice
  options:
    - "Both populations had to pass through a low-fitness intermediate, and the inviable hybrid reflects that historical bottleneck"
    - "The a and b alleles combine in hybrids for the first time, and this novel combination was never tested by natural selection in either lineage"
    - "Genetic drift in isolated populations always produces deleterious alleles that are expressed in hybrids"
    - "Postzygotic barriers require that one allele be directly deleterious, and natural selection failed to remove it"
  answer: 1
  explanation: "This is the Dobzhansky-Muller model. The key insight is that neither 'a' (in AAbb) nor 'b' (in aaBB) is deleterious in its home genetic background — each allele evolved and was fixed in a context where the other was absent. The incompatibility arises only when a and b are brought together in the hybrid for the first time — a combination that was never tested by selection in either lineage. No fitness valley was crossed because each step was neutral or beneficial locally."

- question: "Why do prezygotic barriers typically evolve earlier during allopatric divergence than postzygotic barriers?"
  type: multiple-choice
  options:
    - "Prezygotic barriers are simpler genetically and require only a single-locus change to become complete"
    - "Mate recognition traits are often under strong sexual selection and can diverge rapidly; postzygotic barriers require incompatible genetic interactions to accumulate across two genomes"
    - "Natural selection directly favors prezygotic barriers in allopatry as soon as populations separate"
    - "Postzygotic barriers can only arise after prezygotic barriers have already reduced gene flow"
  answer: 1
  explanation: "Mate recognition signals (songs, colors, pheromones) and habitat preferences are often under strong sexual and ecological selection, allowing rapid divergence even in isolated populations. Postzygotic incompatibilities, by contrast, require specific incompatible alleles to arise independently in two separate populations — a process that depends on particular mutations accumulating and interacting badly in hybrids. This takes longer because it is not directly selected for in allopatry. Note: reinforcement can later directly select for stronger prezygotic barriers once hybrids are unfit, but this is a secondary contact phenomenon, not an allopatric one."

- question: "The Dobzhansky-Muller model requires that at least one population pass through a period of reduced fitness as incompatible alleles accumulate."
  type: true-false
  answer: false
  explanation: "This is precisely the problem that the Dobzhansky-Muller model solves. The 'fitness valley' problem asks: how can incompatible alleles be fixed by natural selection if intermediate genotypes are unfit? D-M resolves this by showing that each allele is fixed in a genetic background where it is compatible — allele 'a' fixes in a population that still has B, so the aB combination is functional. Only when a and b are brought together in a hybrid does the incompatibility manifest. No population ever experiences reduced fitness during the accumulation process."

- question: "Reinforcement — natural selection strengthening prezygotic isolation — can only work if postzygotic barriers are already partially in place."
  type: true-false
  answer: true
  explanation: "Reinforcement requires that hybridization be costly: selection acts against individuals that waste reproductive effort on unfit hybrids, favoring those that avoid cross-population mating. But this selection only exists if hybrids are actually less fit — which requires postzygotic barriers to already be present. Without postzygotic barriers, hybrids are viable and fertile, and there is no selection pressure against hybridization. Reinforcement is thus a secondary-contact mechanism that depends on a prior stage of genetic divergence producing hybrid dysfunction."

- question: "Explain how two populations can accumulate postzygotic incompatibility without either population experiencing reduced fitness, using the Dobzhansky-Muller model."
  type: short-answer
  answer: "In the Dobzhansky-Muller model, incompatibility arises from independently evolved alleles that are each functional in their home genetic background. Imagine the ancestral genotype is AABB. Population 1 evolves a new allele 'a' in a genome that still has B — the aB combination works fine, so 'a' can be fixed by drift or selection. Population 2 independently evolves 'b' in a genome that still has A — Ab also works fine. When these populations hybridize, the hybrid carries both 'a' and 'b' for the first time. If 'a' and 'b' interact badly (incompatible protein products, disrupted developmental pathways), the hybrid is inviable or sterile — yet neither population ever had to survive a low-fitness intermediate."
  explanation: "The Dobzhansky-Muller model resolves the 'valley crossing' problem by showing that postzygotic incompatibility is an emergent property of independent evolution in two lineages, not a result of selection for incompatibility or any population passing through reduced fitness. The incompatible combination (a+b together) simply never existed in either population's evolutionary history — it is a novel combination that natural selection never had the opportunity to evaluate."
```

## Explainer

You already know the categories of reproductive isolation — prezygotic barriers that prevent mating or fertilization, and postzygotic barriers that reduce hybrid fitness. And you know that speciation requires these barriers to form between populations. The question this topic addresses is: *how do these barriers actually accumulate during divergence?* The answer reveals that speciation is not a single event but a process, with different types of barriers arising at different stages and through different mechanisms.

Consider two populations of the same species separated by a geographic barrier — the classic allopatric scenario you have studied. In their separate environments, each population experiences different selection pressures and accumulates different mutations through drift. Over time, their courtship signals may diverge: one population's males evolve slightly different songs, colors, or pheromones in response to local conditions. If the populations later come into contact, females from one population may not recognize males from the other as suitable mates. This is a **prezygotic barrier**, and it tends to evolve relatively early because traits involved in mate recognition are often under strong sexual selection and can diverge rapidly. Temporal isolation (breeding at different times) and habitat isolation (preferring different microhabitats) can also arise early as populations adapt to different local environments.

**Postzygotic barriers** — hybrid inviability and hybrid sterility — typically take longer to accumulate because they require genetic incompatibilities between the diverging genomes. The **Dobzhansky-Muller model** explains how this happens without requiring any population to pass through a fitness valley. Imagine the ancestral population has genotype AABB at two interacting loci. Population 1 evolves to AAbb (mutation at the B locus), and Population 2 evolves to aaBB (mutation at the A locus). Each new allele works fine in its home genetic background. But a hybrid with genotype AaBb brings together the a and b alleles for the first time — a combination that was never tested by natural selection in either population. If these alleles interact badly (the protein products are incompatible, or they disrupt a shared developmental pathway), the hybrid is inviable or sterile. The key insight is that incompatibility arises not from deleterious mutations but from the novel combination of independently evolved alleles.

The accumulation of barriers follows a rough temporal sequence: behavioral and ecological prezygotic barriers first, then gametic isolation, then postzygotic inviability, and finally hybrid sterility. This ordering matters because it means that if populations make secondary contact early in divergence, prezygotic barriers may be weak and hybridization can reverse speciation. **Reinforcement** — natural selection strengthening prezygotic barriers when hybrids are unfit — can accelerate the completion of speciation. But reinforcement only works if postzygotic barriers are already partially in place, creating selection against hybridization. The full picture is one of accumulation and feedback: barriers build on each other, and the process accelerates as more barriers arise, until gene flow between the populations effectively ceases.
