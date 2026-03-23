---
id: inbreeding-depression-genetic-rescue
title: Inbreeding Depression and Genetic Rescue Mechanisms
domain: biology
course: ecology-and-evolution
prerequisites:
- id: inbreeding-consequences
  type: hard
- id: population-bottleneck-drift-inbreeding
  type: hard
- id: effective-population-size
  type: soft
- id: sampling-distributions
  type: soft
builds-toward:
- conservation-genetics-effective-size
tags:
- inbreeding-depression
- genetic-load
- purging
- genetic-rescue
stage: formal-systems
status: validated
---

# Inbreeding Depression and Genetic Rescue Mechanisms

## Core Idea
Inbreeding depression is reduced fitness in inbred individuals due to increased homozygosity of deleterious recessive alleles. Purging—selection against deleterious recessive mutations—can reduce inbreeding depression over time. Genetic rescue through immigration introduces new alleles and restores heterozygosity. Conservation programs must balance genetic rescue against swamping of local adaptations.

## Questions

```yaml
- question: "A critically endangered wolf population of 25 individuals shows reduced litter sizes, increased pup mortality, and higher parasite loads. Conservationists propose introducing 3 unrelated wolves from a distant population. What is the most likely immediate effect?"
  type: multiple-choice
  options:
    - "The deleterious recessive alleles will be permanently removed from the population by intensified selection"
    - "The immigrants' alleles will restore heterozygosity at many loci, masking deleterious recessives and improving fitness"
    - "The immigrants' better-adapted alleles will replace the local population's inferior alleles over several generations"
    - "Purging will intensify as inbreeding temporarily increases due to the small immigrant group size"
  answer: 1
  explanation: "Genetic rescue works by restoring heterozygosity — masking deleterious recessives that were being expressed because inbred individuals were homozygous for them. This effect is immediate (within one generation) and does not require selection to remove alleles. Option A describes purging, which is a separate, slower, and unreliable process. Option C mischaracterizes the mechanism — immigrant alleles don't 'replace' local alleles as superior; they restore complementarity that hides recessive damage. Option D is wrong — immigration reduces inbreeding, not increases it."

- question: "A population of desert lizards has undergone severe inbreeding. Conservationists consider rescuing it with immigrants from a cold-montane population. The key genetic risk of this approach is:"
  type: multiple-choice
  options:
    - "The immigrant individuals will outcompete local lizards for food resources before their offspring are produced"
    - "Introducing alleles adapted to very different conditions may disrupt locally adapted gene combinations"
    - "Immigrants may carry novel pathogens to which the inbred population has no immunity"
    - "Gene flow from immigrants will halt purging, preventing removal of deleterious alleles"
  answer: 1
  explanation: "Outbreeding depression is the risk that hybrid offspring are poorly adapted to either parental environment because locally adapted gene combinations are disrupted. Desert adaptations (heat tolerance, water conservation) may be incompatible with cold-montane adaptations, producing hybrid offspring less fit than either parent population. This is why conservation biologists must evaluate genetic distance, severity of inbreeding depression, and degree of local adaptation before recommending rescue. Option A is an ecological competition concern, not a genetic mechanism risk. Option D is wrong — gene flow does not halt purging."

- question: "Purging is a reliable mechanism for eliminating inbreeding depression in small populations because natural selection becomes more efficient at removing deleterious alleles when they are expressed in homozygous form."
  type: true-false
  answer: false
  explanation: "Purging is explicitly described as unreliable. While increased homozygosity does allow selection to act more efficiently against strongly deleterious recessives, purging fails against the many mildly deleterious alleles that collectively drag down fitness. In very small populations, drift removes alleles randomly before purging can operate, and the extinction vortex may accelerate faster than purging can rescue the population. Purging can work under moderate inbreeding but is not a reliable conservation strategy for populations already in severe decline."

- question: "Inbreeding depression is caused primarily by the accumulation of new harmful mutations in inbred populations, rather than by the unmasking of deleterious alleles already present in the population's standing genetic variation."
  type: true-false
  answer: false
  explanation: "Inbreeding depression is caused by increased homozygosity *revealing* deleterious recessive alleles already present in the population — not by generating new mutations. In a large outbreeding population, most deleterious recessives are masked in heterozygotes and hidden from selection. Inbreeding increases the probability that an individual inherits the same allele from both parents, homozygosing these already-existing alleles and exposing their effects. The mechanism is exposure of existing variation, not accumulation of new mutations."

- question: "Why does genetic rescue work within a single generation, whereas purging takes multiple generations — and what does this difference reveal about the mechanism of inbreeding depression?"
  type: short-answer
  answer: "Genetic rescue is immediate because it directly restores heterozygosity: immigrant alleles pair with local alleles at deleterious loci, creating heterozygotes where the harmful recessive is masked. The fitness benefit appears in F1 offspring — heterozygous at thousands of loci that were previously homozygous. Purging, by contrast, works through selection: deleterious alleles must be expressed in homozygous form, reduce fitness, fail to reproduce, and thereby decrease in frequency — a multigenerational process. The difference reveals that inbreeding depression is about *masking*, not allele removal. The deleterious alleles are still present after genetic rescue; they are just hidden again in heterozygotes."
  explanation: "This has practical importance: genetic rescue is not a permanent fix. If the rescued population again becomes isolated and inbred, deleterious alleles can be unmasked again in future generations. Ongoing gene flow — not a one-time rescue event — is what maintains heterozygosity and suppresses inbreeding depression long-term."
```

## Explainer

You already know from studying inbreeding consequences that mating between relatives increases homozygosity across the genome. **Inbreeding depression** is the fitness cost of that increased homozygosity. The mechanism is straightforward: every population carries deleterious recessive alleles at low frequency — mutations that are harmful when homozygous but masked when heterozygous. In a large, outbreeding population, most individuals carry these alleles in heterozygous form, so the damage stays hidden. When relatives mate, the probability of inheriting the same deleterious allele from both parents rises sharply. The result is offspring that are homozygous at more loci, exposing recessive diseases, reduced fertility, weakened immune function, and lower survival. This is why small, isolated populations — the kind you studied in population bottlenecks and drift — suffer disproportionately: drift removes alleles randomly, and the remaining individuals are increasingly related to one another.

A natural question follows: if inbreeding exposes deleterious recessives, can selection remove them? This process is called **purging**. When deleterious alleles become homozygous and reduce fitness, natural selection acts more efficiently against them than it could when they were hidden in heterozygotes. Over multiple generations of moderate inbreeding, purging can reduce the frequency of strongly deleterious recessives and partially alleviate inbreeding depression. However, purging is unreliable — it works best against alleles of large effect and fails against the many mildly deleterious alleles that collectively drag down fitness. Populations that crash to very small sizes often lose too much genetic variation through drift before purging can operate effectively, creating an "extinction vortex" where small size leads to inbreeding, which reduces fitness, which further shrinks the population.

**Genetic rescue** is the introduction of unrelated individuals (immigrants) into an inbred population to restore heterozygosity and mask deleterious recessives. Even a small number of immigrants can have dramatic effects. The classic example is the Florida panther: by the 1990s, fewer than 30 individuals remained, showing kinked tails, heart defects, and poor sperm quality — hallmarks of inbreeding depression. Eight female Texas pumas were introduced in 1995, and within a generation the population tripled and the physical abnormalities largely disappeared. The immigrant alleles restored heterozygosity at thousands of loci simultaneously.

The challenge in conservation genetics is that genetic rescue is not without risk. If the immigrant population is adapted to very different environmental conditions, introducing their alleles can disrupt locally adapted gene combinations — a phenomenon called **outbreeding depression**. A population of desert-adapted fish rescued with individuals from a cold-water population might produce hybrid offspring poorly suited to either environment. Conservation biologists must therefore evaluate the genetic distance between donor and recipient populations, the severity of inbreeding depression, and the degree of local adaptation before recommending genetic rescue. The effective population size concept you studied helps quantify how urgently rescue is needed: populations with very low effective size are losing heterozygosity rapidly and face the greatest risk of inbreeding depression overwhelming their capacity to persist.
