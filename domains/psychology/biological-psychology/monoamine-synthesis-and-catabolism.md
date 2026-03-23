---
id: monoamine-synthesis-and-catabolism
title: Monoamine Neurotransmitter Synthesis and Catabolism
domain: psychology
course: biological-psychology
prerequisites:
- id: neurotransmitter-synthesis-storage
  type: hard
- id: dopamine-reward-system
  type: soft
- id: amino-acid-structure-and-properties
  type: hard
- id: aromatic-amino-acid-catabolism
  type: soft
builds-toward:
- dopamine-receptor-subtypes-and-signaling
- serotonin-reuptake-mechanisms
- antidepressant-medications-ssris
tags:
- neurotransmitter
- dopamine
- serotonin
- norepinephrine
- metabolism
stage: formal-systems
status: draft
---

# Monoamine Neurotransmitter Synthesis and Catabolism

## Core Idea
Monoamine neurotransmitters (dopamine, serotonin, norepinephrine, histamine) are synthesized from amino acids and catabolized by monoamine oxidase (MAO) or catechol-O-methyltransferase (COMT). The balance between synthesis rate, reuptake efficiency, and degradation determines synaptic monoamine concentration. Individual differences in these enzymatic activities (influenced by genetics, diet, and aging) contribute to personality traits and vulnerability to mood disorders.

## How It's Best Learned
Trace the biochemical pathway from tyrosine to dopamine to trace metabolites, and from tryptophan to serotonin. Study how MAO inhibitors increase synaptic levels and understand why COMT variation affects working memory.

## Common Misconceptions
Monoamines are not rapidly degraded solely by reuptake; enzymatic breakdown by MAO/COMT is a major pathway. MAO inhibitors increase monoamine levels but carry dietary restrictions due to tyramine risks.

## Questions

```yaml
- question: "A patient taking an MAOI antidepressant eats aged cheese, which is high in tyramine. What is the likely consequence and why?"
  type: multiple-choice
  options:
    - "The tyramine is converted to dopamine in the brain, amplifying the antidepressant effect"
    - "Nothing unusual — MAO inhibitors block monoamine synthesis, not tyramine metabolism"
    - "Tyramine that would normally be degraded by MAO in the gut accumulates and can trigger a dangerous hypertensive crisis"
    - "Tyramine competes with serotonin at the synapse, partially reversing the antidepressant's effect"
  answer: 2
  explanation: "MAO in the gut wall normally breaks down dietary tyramine before it can enter the bloodstream. When MAO is inhibited, tyramine accumulates and enters circulation, where it triggers norepinephrine release from sympathetic terminals, causing severe vasoconstriction and hypertensive crisis. This is a real medical emergency. The question illustrates a key point: MAO doesn't just degrade neurotransmitters in the brain — it also inactivates dietary amines in peripheral tissues, and inhibiting it has consequences throughout the body."

- question: "A researcher blocks the serotonin transporter (SERT) with an SSRI. By what primary mechanism does synaptic serotonin increase?"
  type: multiple-choice
  options:
    - "Tryptophan hydroxylase accelerates serotonin synthesis in response to reduced reuptake"
    - "COMT is inhibited secondarily, reducing serotonin breakdown in the postsynaptic neuron"
    - "Serotonin released into the synapse remains there longer because its reuptake into the presynaptic terminal is blocked"
    - "MAO activity declines because less serotonin enters the presynaptic terminal where MAO is located"
  answer: 2
  explanation: "The dominant route for clearing synaptic serotonin is reuptake — the serotonin transporter (SERT) pulls released serotonin back into the presynaptic terminal. SSRIs block SERT, so serotonin lingers in the synapse longer and has more opportunity to bind postsynaptic receptors. Synthesis rate and enzymatic degradation are not the primary targets. Option D has a subtle logic to it (less serotonin in the terminal could mean less MAO substrate) but this is a minor secondary effect, not the primary mechanism."

- question: "The rate-limiting step in dopamine synthesis is the conversion of L-DOPA to dopamine by DOPA decarboxylase."
  type: true-false
  answer: false
  explanation: "The rate-limiting step is the FIRST reaction: tyrosine hydroxylase converting tyrosine to L-DOPA. This is the step that controls how much dopamine the neuron can produce. DOPA decarboxylase (which converts L-DOPA to dopamine) is fast and rarely rate-limiting. This distinction has direct clinical relevance: L-DOPA supplements work in Parkinson's disease precisely because supplying L-DOPA bypasses the deficient tyrosine hydroxylase step in the dopaminergic neurons of the substantia nigra."

- question: "Individuals with the COMT Val/Val genotype tend to have lower prefrontal dopamine levels than Met/Met individuals, which can impair working memory."
  type: true-false
  answer: true
  explanation: "The Val variant of COMT degrades dopamine roughly four times faster than the Met variant, resulting in lower steady-state dopamine levels in the prefrontal cortex. Since prefrontal dopamine is critical for working memory, Val homozygotes tend to show worse working memory performance under normal conditions. Paradoxically, they may also show more resilience to certain stress-induced dopamine surges, illustrating the 'warrior-worrier' tradeoff associated with this polymorphism."

- question: "Why do MAO inhibitors require tyramine dietary restrictions while SSRIs do not? What does this reveal about the difference between these two pharmacological mechanisms?"
  type: short-answer
  answer: "MAOIs block the enzyme that degrades tyramine in the gut wall and periphery, allowing dietary tyramine to accumulate and trigger dangerous sympathetic activation. SSRIs only block reuptake at serotonergic synapses in the nervous system and have no effect on MAO or peripheral tyramine metabolism, so no dietary restriction is needed. This illustrates that the two drug classes target entirely different steps in the monoamine cycle: MAOIs affect enzymatic degradation (a metabolic step), while SSRIs affect the transporter (a reuptake step)."
  explanation: "The distinction matters clinically: reuptake blockers are synapse-specific and have minimal peripheral effects because the transporter is expressed mainly at serotonergic terminals. MAO, by contrast, is expressed in peripheral tissues throughout the body — gut, liver, platelets — where it serves as a general amine clearance system. Inhibiting it therefore affects all amines, including dietary ones, not just monoamine neurotransmitters in the brain."
```

## Explainer

Monoamine neurotransmitters are built from amino acids you already know from biochemistry. **Dopamine** and **norepinephrine** (catecholamines) both trace back to tyrosine. The pathway runs: tyrosine → L-DOPA (via tyrosine hydroxylase, the rate-limiting step) → dopamine (via DOPA decarboxylase) → norepinephrine (via dopamine β-hydroxylase). **Serotonin** (a non-catecholamine monoamine) starts from tryptophan instead: tryptophan → 5-hydroxytryptophan → serotonin via analogous steps. Understanding these pathways tells you immediately where drugs can intervene — L-DOPA supplements are given in Parkinson's precisely because tyrosine hydroxylase activity has collapsed in the substantia nigra.

Once released into the synapse, monoamines face two fates: reuptake into the presynaptic terminal (the dominant route) or enzymatic degradation. The two major degrading enzymes are **monoamine oxidase (MAO)**, located primarily in mitochondria of presynaptic terminals and astrocytes, and **catechol-O-methyltransferase (COMT)**, located in postsynaptic neurons and glial cells. MAO oxidatively deaminates monoamines into aldehyde intermediates; COMT transfers a methyl group. Dopamine's primary breakdown products are DOPAC (via MAO) and HVA (via COMT then MAO); serotonin's main metabolite is 5-HIAA. You'll see these metabolites measured in cerebrospinal fluid as indirect proxies for neurotransmitter turnover.

The balance between synthesis, reuptake, and degradation determines synaptic monoamine concentration — and this balance is highly tunable pharmacologically. **MAO inhibitors (MAOIs)** block enzymatic degradation, flooding the synapse with monoamines; they're used as antidepressants but require dietary tyramine restriction because tyramine (normally degraded by MAO in the gut) can trigger hypertensive crises if it accumulates. **Selective serotonin reuptake inhibitors (SSRIs)** block the serotonin transporter (SERT) rather than degradation, prolonging serotonin's presence in the synapse without affecting synthesis. **COMT inhibitors** like entacapone are used adjunctively in Parkinson's to reduce L-DOPA breakdown in peripheral tissues.

Individual genetic variation in these enzymes creates meaningful differences in mood, cognition, and disease vulnerability. The **COMT Val158Met polymorphism** is one of the most studied: the Val variant degrades dopamine roughly four times faster than the Met variant. Val homozygotes have lower prefrontal dopamine levels, which impairs working memory performance but may confer resilience to certain psychotic symptoms. Met homozygotes maintain higher prefrontal dopamine, boosting working memory capacity but potentially increasing anxiety and rumination. This single nucleotide difference illustrates how the biochemical pathways you've learned aren't just abstract chemistry — they're the molecular substrate of personality differences.
