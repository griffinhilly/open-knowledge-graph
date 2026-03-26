---
id: aromatic-amino-acid-catabolism
title: Aromatic Amino Acid Metabolism
domain: biology
course: biochemistry
prerequisites:
- id: amino-acid-degradation-overview
  type: hard
- id: electrophilic-aromatic-substitution
  type: soft
- id: branched-chain-amino-acid-catabolism
  type: soft
builds-toward:
- phenylketonuria-and-metabolic-disease
tags:
- amino-acids
- phenylalanine
- tyrosine
- tryptophan
stage: formal-systems
status: validated
---
# Aromatic Amino Acid Metabolism

## Core Idea
Phenylalanine is converted to tyrosine by phenylalanine hydroxylase; tyrosine is a precursor for dopamine, norepinephrine, epinephrine, and thyroid hormones. Tryptophan serves as precursor for serotonin and the kynurenine pathway. All three aromatic amino acids are exclusively glucogenic, with carbon skeletons entering the citric acid cycle.

## Questions

```yaml
- question: "A patient has a loss-of-function mutation in phenylalanine hydroxylase (PKU). Which set of metabolic consequences would you expect?"
  type: multiple-choice
  options:
    - "Elevated blood tyrosine and reduced phenylalanine, because the blocked enzyme normally degrades phenylalanine"
    - "Reduced catecholamine synthesis and elevated serotonin, as the tryptophan pathway compensates"
    - "Accumulation of phenylalanine in blood and reduced tyrosine production, because the hydroxylation step converting phenylalanine to tyrosine is blocked"
    - "Deficiency of NAD+ because phenylalanine normally feeds into the kynurenine pathway"
  answer: 2
  explanation: "Phenylalanine hydroxylase converts phenylalanine to tyrosine; when this enzyme fails, phenylalanine cannot enter the tyrosine pathway and accumulates. Because phenylalanine must be converted to tyrosine before further catabolism, tyrosine must now be obtained entirely from the diet — it becomes conditionally essential. The toxic accumulation of phenylalanine and its transamination products causes neurological damage. NAD+ synthesis comes from tryptophan (kynurenine pathway), not phenylalanine."

- question: "Which molecule is the direct biosynthetic precursor to both dopamine (a neurotransmitter) and thyroid hormones (T3/T4)?"
  type: multiple-choice
  options:
    - "Phenylalanine — it is converted directly to L-DOPA in catecholamine synthesis"
    - "Tryptophan — it serves as the universal aromatic amino acid precursor for signaling molecules"
    - "Tyrosine — it is hydroxylated to L-DOPA for catecholamine synthesis and iodinated for thyroid hormone synthesis"
    - "L-DOPA — it is the central hub molecule for all catecholamine and thyroid hormone biosynthesis"
  answer: 2
  explanation: "Tyrosine is the true metabolic hub. For catecholamines: tyrosine → L-DOPA → dopamine → norepinephrine → epinephrine. For thyroid hormones: tyrosine residues within thyroglobulin are iodinated and coupled to form T3 and T4. Phenylalanine must first be converted to tyrosine before it can enter any of these pathways — it is not a direct precursor. L-DOPA is an intermediate, not a hub upstream of thyroid hormones."

- question: "Tryptophan serves as a dietary source for de novo NAD+ biosynthesis because the kynurenine pathway produces a pyridine nucleotide precursor."
  type: true-false
  answer: true
  explanation: "True — the major catabolic route for tryptophan is the kynurenine pathway, which opens the indole ring and produces several intermediates, including quinolinate. Quinolinate is a direct precursor for NAD+ synthesis. This is why tryptophan is considered a niacin equivalent in nutrition: adequate dietary tryptophan can partially compensate for niacin (vitamin B3) deficiency, since NAD+ can be synthesized from either."

- question: "Phenylalanine and tyrosine are catabolized through largely separate biochemical pathways with no shared intermediates or enzymatic steps."
  type: true-false
  answer: false
  explanation: "False — phenylalanine is first converted to tyrosine by phenylalanine hydroxylase, after which both amino acids enter the same downstream degradation pathway. This convergence is why tyrosine is described as the metabolic hub: whether the aromatic carbon enters as phenylalanine or tyrosine, it passes through the same sequence leading to fumarate (glucogenic) and acetoacetate (ketogenic). The two pathways are not separate; they merge at tyrosine."

- question: "Why is tyrosine described as a 'metabolic hub' among the aromatic amino acids? Name two distinct physiological systems that depend on tyrosine as their biosynthetic starting point."
  type: short-answer
  answer: "Tyrosine is the convergence point for phenylalanine catabolism and the upstream precursor for multiple major biosynthetic pathways. Two distinct systems: (1) the catecholamine neurotransmitter/hormone system — tyrosine → L-DOPA → dopamine → norepinephrine → epinephrine, which governs motor control, reward, and stress response; and (2) thyroid hormone synthesis — tyrosine residues in thyroglobulin are iodinated and coupled to form T3 and T4, which regulate metabolism and thermogenesis. Melanin synthesis in skin is a third pathway."
  explanation: "The term 'hub' is warranted because multiple upstream pathways (phenylalanine input) and multiple downstream biosynthetic branches all pass through tyrosine. This means defects in tyrosine availability — whether from PKU or dietary restriction — have cascading effects across unrelated physiological systems."
```

## Explainer

From your study of amino acid degradation, you know the general strategy: remove the amino group (via transamination or oxidative deamination), then channel the remaining carbon skeleton into central metabolic intermediates. The **aromatic amino acids** — phenylalanine, tyrosine, and tryptophan — follow this same logic, but their bulky aromatic rings make their degradation pathways more elaborate and biochemically distinctive. These three amino acids are also unique because their catabolic intermediates serve as precursors to some of the body's most important signaling molecules.

The most clinically significant pathway begins with **phenylalanine**. The enzyme **phenylalanine hydroxylase** (PAH) adds a hydroxyl group to phenylalanine's aromatic ring, converting it to tyrosine. This reaction requires molecular oxygen and the cofactor **tetrahydrobiopterin** (BH4), which gets oxidized in the process and must be regenerated by dihydrobiopterin reductase. This single reaction is so important that its failure — through mutations in PAH or BH4 metabolism — causes **phenylketonuria** (PKU), one of the most well-known inborn errors of metabolism. Because phenylalanine is converted to tyrosine before further degradation, tyrosine is the true hub of aromatic amino acid catabolism: both phenylalanine and tyrosine converge on the same downstream pathway.

Tyrosine degradation proceeds through a five-step pathway that ultimately yields **fumarate** (a citric acid cycle intermediate) and **acetoacetate** (a ketone body). This makes tyrosine both glucogenic and ketogenic. But tyrosine's metabolic significance extends far beyond its degradation. In specialized tissues, tyrosine is hydroxylated to form **L-DOPA**, which is decarboxylated to **dopamine** — the neurotransmitter central to motor control, reward, and motivation. Dopamine is further hydroxylated to **norepinephrine** and then methylated to **epinephrine**, forming the catecholamine signaling cascade. In the thyroid gland, tyrosine residues within thyroglobulin are iodinated and coupled to produce thyroid hormones (T3 and T4). In melanocytes, tyrosine is oxidized to form melanin pigments. No other amino acid feeds into as many physiologically critical biosynthetic pathways.

**Tryptophan** follows its own distinctive route. The major catabolic pathway is the **kynurenine pathway**, which opens the indole ring and ultimately produces **alanine** (glucogenic) and **acetyl-CoA** through a series of oxidative steps. Along the way, intermediates of this pathway include kynurenine and quinolinate, the latter being a precursor for NAD+ biosynthesis — making tryptophan the dietary source for de novo synthesis of this essential coenzyme. In a separate, quantitatively minor pathway, tryptophan is hydroxylated by **tryptophan hydroxylase** to form 5-hydroxytryptophan, which is then decarboxylated to produce **serotonin** — the neurotransmitter that regulates mood, sleep, and appetite. Serotonin can be further converted to **melatonin** in the pineal gland. The clinical importance of these branching pathways explains why aromatic amino acid metabolism appears so frequently in biochemistry and medical contexts.
