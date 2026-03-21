---
id: maternal-inheritance-and-extranuclear-genes
title: Maternal Inheritance and Extranuclear (Cytoplasmic) Genes
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: non-mendelian-inheritance
  type: hard
- id: meiosis
  type: soft
- id: cell-cycle-overview
  type: soft
builds-toward:
- genomic-imprinting-and-parent-of-origin-effects
tags:
- maternal-inheritance
- mitochondrial-dna
- chloroplast-dna
- heteroplasmy
stage: advanced
status: draft
---

# Maternal Inheritance and Extranuclear (Cytoplasmic) Genes

## Core Idea
Mitochondria and chloroplasts contain their own DNA and are inherited maternally in most organisms because the egg contributes most or all cytoplasm to the zygote, while sperm contributes little. Maternal inheritance produces non-Mendelian ratios: all offspring resemble the maternal parent regardless of paternal genotype, violating expectations for biparental inheritance. Heteroplasmy (cells containing multiple mitochondrial or chloroplast DNA variants) causes variable segregation of organellar genotypes during cell division, with random distribution of organelles to daughter cells. This leads to variable proportions of mutant and wild-type organelles in offspring (vegetative segregation), causing variable severity of phenotype. Mitochondrial diseases exhibit maternal inheritance, variable expressivity, and age-related manifestation due to heteroplasmy and organellar replication dynamics.

## Questions

```yaml
- question: "A man carries a pathogenic mitochondrial DNA mutation. His wife has no mitochondrial mutations. Which prediction about their children is correct?"
  type: multiple-choice
  options:
    - "Half of their children will carry the mutation, following a Mendelian dominant inheritance pattern"
    - "All of their children will carry the mutation, since the father expresses it and it will be passed to all offspring"
    - "None of their children will carry the mutation, because mitochondrial DNA is maternally inherited and fathers do not transmit it"
    - "Only daughters will carry the mutation, because mitochondrial inheritance is X-linked"
  answer: 2
  explanation: "Mitochondria are inherited maternally: sperm contributes virtually no cytoplasm at fertilization, so only the egg's mitochondria are transmitted to offspring. A father's mitochondrial DNA mutations are not passed to any of his children, regardless of sex. Since the mother has no mutation, none of the children will inherit the paternal mitochondrial mutation. This is the defining feature of maternal inheritance — transmission is exclusively through the maternal line. X-linked inheritance (option D) involves nuclear chromosomal genes and follows completely different patterns."

- question: "A heteroplasmic woman carries a mitochondrial disease mutation. She has four children with an unaffected father. One child is severely affected, two are mildly affected, and one is asymptomatic. Which explanation best accounts for this variation?"
  type: multiple-choice
  options:
    - "Recombination shuffled the maternal and paternal mitochondrial alleles differently in each child"
    - "Different children inherited different proportions of mutant and wild-type mitochondria due to stochastic vegetative segregation during oogenesis"
    - "The asymptomatic child received a compensatory nuclear mutation that corrects for the mitochondrial defect"
    - "Variable expressivity in X-linked conditions explains the range of severity across siblings"
  answer: 1
  explanation: "The mother is heteroplasmic — her cells contain a mixture of mutant and wild-type mitochondria. During oogenesis, these organelles are distributed to egg cells roughly at random. Some eggs receive a high proportion of mutant mitochondria, others a low proportion. Each child's disease severity tracks their proportion of mutant mitochondria: high mutant load → severe disease; low mutant load → mild or no symptoms. This stochastic vegetative segregation is the mechanistic explanation for variable expressivity among siblings born to the same heteroplasmic mother. Recombination (option A) does not occur between maternal and paternal mitochondria — there is no paternal mitochondrial contribution to recombine with."

- question: "In a cross between a white-flowered plant and a green-flowered plant, if flower color follows maternal inheritance, then the offspring's color will match the maternal parent regardless of which parent provides the pollen."
  type: true-false
  answer: true
  explanation: "Maternal inheritance means offspring phenotype is determined by the mother's cytoplasmic genotype, not the father's. Reciprocal crosses — white♀ × green♂ and green♀ × white♂ — give completely different results: offspring from white females are white regardless of pollen source; offspring from green females are green. This asymmetry between reciprocal crosses is the hallmark of maternal (cytoplasmic) inheritance, observed in Correns' original work with Mirabilis jalapa variegation. It contrasts sharply with nuclear Mendelian genes, where reciprocal crosses typically give the same F1 phenotype."

- question: "A child born to a heteroplasmic mother with a mitochondrial disease mutation will always express the disease because the mother passes all her mitochondria to every child."
  type: true-false
  answer: false
  explanation: "Heteroplasmy means the mother's cells contain a MIXTURE of mutant and wild-type mitochondria — not all mutant. During oogenesis and subsequent cell divisions, organelles are distributed stochastically, so each egg receives a different random sample. If a child happens to receive a small proportion of mutant mitochondria, they may be asymptomatic or mildly affected. Many mitochondrial diseases only manifest when mutant load exceeds a tissue-specific threshold (often 70–90%). A child of a heteroplasmic mother can receive so few mutant mitochondria that they remain entirely unaffected — as the scenario above illustrates."

- question: "Why does heteroplasmy make it difficult to predict mitochondrial disease severity in children of an affected mother, in ways that Mendelian nuclear gene inheritance would not?"
  type: short-answer
  answer: "In Mendelian inheritance, each parent contributes exactly one allele per locus, so each child's allelic state at every nuclear locus is determinate. Mitochondrial inheritance involves hundreds to thousands of organelles per cell, each potentially carrying a different DNA variant. A heteroplasmic mother's egg cells receive a stochastic sample of these organelles, so each egg differs in its ratio of mutant to wild-type mitochondria. After fertilization, further stochastic segregation during cell division creates within-individual variation across tissues. Disease manifests only when mutant load exceeds a tissue-specific threshold, and the relevant tissues (brain, muscle, heart) may differ from sampled tissues. None of this continuous, probabilistic variation is possible with Mendelian nuclear genes."
  explanation: "This explains why prenatal diagnosis of mitochondrial disease is difficult: even measuring the mutant load in a biopsy sample may not reflect mutant loads in clinically affected tissues. The irreducible stochasticity of organellar inheritance — arising from the fact that hundreds of independent genetic units, rather than two alleles, are being sampled — creates uncertainty that is fundamentally different from the combinatorial predictability of Mendelian genetics."
```

## Explainer

Mendelian genetics assumes that both parents contribute equally to offspring — one allele from each. But mitochondria and chloroplasts break this rule completely. These organelles carry their own small circular genomes, replicate independently of the nucleus, and — critically — are transmitted almost exclusively through the **egg cell**. Sperm contribute virtually no cytoplasm at fertilization, so the father's mitochondria are not passed on. This means that for any gene encoded in the mitochondrial or chloroplast genome, inheritance is strictly **maternal**: all offspring resemble their mother, regardless of the father's genotype. If a woman carries a mitochondrial mutation, all of her children will inherit it; if a man carries the same mutation, none of his children will.

This pattern is easy to recognize in crosses because it violates Mendelian expectations in a specific way. In a Mendelian cross, reciprocal crosses (A♀ × B♂ versus B♀ × A♂) give the same F1 phenotype. With maternal inheritance, the reciprocal crosses give different results — the offspring always match the mother. This was first observed in plants: Carl Correns noticed that leaf color variegation in *Mirabilis jalapa* (four o'clock plants) followed the maternal parent regardless of pollen source. The variegation was caused by mutations in chloroplast DNA, inherited through the egg's cytoplasm.

A complication arises because each cell contains hundreds or thousands of mitochondria (or chloroplasts), each with its own copy of the organellar genome. When a mutation occurs, it initially affects only one organelle, creating a state called **heteroplasmy** — a mixture of mutant and wild-type organellar DNA within the same cell. During cell division, organelles are distributed to daughter cells roughly at random, so some daughter cells may receive more mutant organelles and others more wild-type. Over successive divisions, this **vegetative segregation** can push cells toward pure mutant or pure wild-type populations. The same process occurs during egg cell formation, which is why a heteroplasmic mother can produce children with very different proportions of mutant mitochondria — and therefore very different severity of disease.

**Mitochondrial diseases** in humans illustrate these principles vividly. Conditions like Leber hereditary optic neuropathy (LHON) and mitochondrial myopathy show strict maternal inheritance, but affected families display striking variation in severity among siblings — one child may be severely affected while another is nearly asymptomatic, depending on the proportion of mutant mitochondria each received. Symptoms also tend to worsen with age because mitochondrial DNA accumulates damage over time (it lacks the robust repair mechanisms of nuclear DNA) and because tissues with high energy demands — brain, muscle, heart — are most sensitive to mitochondrial dysfunction. These features — maternal transmission, variable expressivity among siblings, and progressive deterioration — are the hallmarks that distinguish mitochondrial disease from any Mendelian disorder.
