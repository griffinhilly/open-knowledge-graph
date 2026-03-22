---
id: heterozygote-advantage
title: Heterozygote Advantage and Overdominance
domain: biology
course: evolutionary-biology
prerequisites:
- id: adaptation-and-fitness
  type: hard
- id: dominance-and-recessiveness
  type: hard
- id: balancing-selection
  type: soft
builds-toward:
- balancing-selection
- population-genetics-intro
tags:
- selection
- polymorphism
- allele-frequency
- fitness
stage: advanced
status: draft
---

# Heterozygote Advantage and Overdominance

## Core Idea
Heterozygotes possess higher fitness than both homozygotes, maintaining genetic polymorphism at stable intermediate allele frequencies. Classic example: sickle-cell trait confers malaria resistance without severe anemia cost in heterozygotes.

## Questions

```yaml
- question: "In a malaria-endemic region, the HbS allele is initially very rare. What does heterozygote advantage predict will happen to its frequency over subsequent generations?"
  type: multiple-choice
  options:
    - "It will be eliminated, because sickle-cell anemia kills homozygous HbS/HbS individuals before reproduction"
    - "Its frequency will increase, because when rare it almost exclusively appears in high-fitness HbA/HbS heterozygotes"
    - "Its frequency will remain constant, because the allele is selectively neutral when rare"
    - "Its frequency will increase only if the HbA allele is simultaneously lost from the population"
  answer: 1
  explanation: "When HbS is rare, nearly every copy exists in HbA/HbS heterozygotes — the highest-fitness genotype. Selection therefore strongly favors the allele when it is rare. This is the self-correcting dynamic of overdominance: rarity means high fitness, driving the allele upward until it reaches equilibrium."

- question: "In a population with fitness costs s = 0.2 for HbA/HbA (malaria susceptibility) and t = 0.8 for HbS/HbS (sickle-cell disease), what is the predicted equilibrium frequency of the HbS allele?"
  type: multiple-choice
  options:
    - "0.50 — both alleles reach equal frequency at equilibrium"
    - "0.80 — the allele with the smaller homozygote fitness cost dominates"
    - "0.20 — the equilibrium frequency equals s/(s + t)"
    - "0.04 — the allele with the larger fitness cost remains very rare"
  answer: 2
  explanation: "The equilibrium frequency formula q̂ = s/(s + t) = 0.2/(0.2 + 0.8) = 0.2. The HbS allele reaches a stable 20% frequency — not zero (despite causing anemia) and not 50% (despite heterozygote advantage). The asymmetry in fitness costs (t >> s) means the population holds far more HbA than HbS alleles at equilibrium."

- question: "At the heterozygote advantage equilibrium, if the frequency of HbS rises above its equilibrium value, selection will push it back down because an increasing proportion of HbS copies end up in low-fitness HbS/HbS homozygotes."
  type: true-false
  answer: true
  explanation: "This is the stabilizing logic of overdominance. As HbS becomes common, more copies pair with other HbS alleles, producing costly aa homozygotes. Selection then favors HbA and drives HbS back toward equilibrium. The same logic in reverse prevents HbS from disappearing when rare. The equilibrium is stable."

- question: "Heterozygote advantage is a form of dominance: the HbA allele dominates in HbA/HbS heterozygotes, masking the HbS allele and conferring the heterozygote's high fitness."
  type: true-false
  answer: false
  explanation: "Overdominance is fundamentally different from classical dominance. In classical dominance, one allele masks the other and the heterozygote resembles one homozygote. In overdominance, the heterozygote has HIGHER fitness than BOTH homozygotes — it is not that one allele 'wins.' The sickle-cell heterozygote's advantage comes from having both allele products present, not from one suppressing the other."

- question: "Explain why natural selection cannot drive the HbS allele to either fixation or elimination in a malaria-endemic population, even though both HbS/HbS and HbA/HbA homozygotes have lower fitness than the heterozygote."
  type: short-answer
  answer: "When HbS is rare, almost all HbS copies exist in high-fitness HbA/HbS heterozygotes, so selection increases the allele's frequency. When HbS is common, many copies end up in low-fitness HbS/HbS homozygotes, so selection decreases its frequency. The allele can never disappear (rarity makes it advantageous) and can never fix (commonness makes it costly). This frequency-dependent fitness creates a stable equilibrium where selection actively maintains both alleles."
  explanation: "The key insight is that the fitness of an allele in a diploid organism depends not just on the allele itself but on what it is paired with — and what it is paired with depends on allele frequency. Overdominance converts this frequency dependence into a stable equilibrium, the clearest mechanism by which selection maintains genetic variation."
```

## Explainer

From adaptation and fitness, you know that natural selection increases the frequency of alleles that confer higher reproductive success. From dominance and recessiveness, you know that diploid organisms carry two copies of each gene and that the phenotypic expression of alleles depends on their dominance relationships. Heterozygote advantage — also called **overdominance** — arises when the heterozygous genotype (one copy of each allele, Aa) has *higher fitness* than either homozygote (AA or aa). This creates a situation where selection cannot drive either allele to fixation, because as one allele becomes common, the other becomes rare and increasingly appears in the high-fitness heterozygous state.

The sickle-cell example makes the logic concrete. The hemoglobin S allele (HbS), when homozygous (HbS/HbS), causes severe sickle-cell anemia — a devastating condition that sharply reduces fitness. The normal allele (HbA), when homozygous (HbA/HbA), produces healthy red blood cells but offers no special resistance to malaria. The heterozygote (HbA/HbS) gets the best of both worlds: enough normal hemoglobin to avoid serious anemia, but enough altered hemoglobin to create an inhospitable environment for *Plasmodium falciparum* parasites inside red blood cells. In malaria-endemic regions of sub-Saharan Africa, the heterozygote survives both threats better than either homozygote. The result is **balancing selection** that maintains both alleles in the population at a stable equilibrium frequency.

The equilibrium frequency is predictable from the relative fitness values. If we define the fitness of AA as 1 - s (reduced by malaria susceptibility), Aa as 1 (highest), and aa as 1 - t (reduced by sickle-cell disease), then the equilibrium frequency of the HbS allele is q̂ = s / (s + t). The allele cannot disappear because when it is rare, nearly all copies exist in heterozygotes where they are positively selected; it cannot go to fixation because when it is common, too many homozygous aa individuals are produced and removed by selection. This **frequency-dependent dynamic** is self-correcting — any perturbation from equilibrium is automatically corrected by selection, making the polymorphism stable rather than transient.

Beyond sickle cell, heterozygote advantage has been proposed for several other systems: cystic fibrosis heterozygotes may have had increased resistance to cholera or typhoid; MHC heterozygotes present a broader array of pathogen peptides to the immune system, improving pathogen recognition. However, unambiguous cases of overdominance are rarer than once thought — many apparent examples turn out to involve other forms of balancing selection (frequency-dependent selection, spatially varying selection) rather than true overdominance. The concept remains important because it provides the clearest mechanism by which natural selection *actively maintains* genetic variation, countering the common misconception that selection always reduces variation by driving alleles to fixation or loss.
