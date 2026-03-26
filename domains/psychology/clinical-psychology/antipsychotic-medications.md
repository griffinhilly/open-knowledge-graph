---
id: antipsychotic-medications
title: 'Antipsychotic Medications: Types and Mechanisms'
domain: psychology
course: clinical-psychology
prerequisites:
- id: schizophrenia-spectrum-disorders
  type: hard
- id: dopamine-system
  type: hard
- id: dopamine-reward-system
  type: hard
builds-toward:
- comorbidity-complex-presentations
tags:
- antipsychotics
- dopamine
stage: expert
status: validated
---

# Antipsychotic Medications: Types and Mechanisms

## Core Idea
Antipsychotics block dopamine activity to reduce psychotic symptoms. Typical antipsychotics (first-generation) effectively treat positive symptoms but cause movement disorders. Atypical antipsychotics (second-generation) treat positive and negative symptoms with reduced movement side effects but metabolic risks. Long-term use is essential for maintaining remission in schizophrenia.

## Questions

```yaml
- question: "A patient on a typical (first-generation) antipsychotic develops Parkinson-like tremor, rigidity, and slowness of movement. Which dopamine pathway is most directly responsible?"
  type: multiple-choice
  options:
    - "The mesolimbic pathway — the same pathway that mediates antipsychotic efficacy against positive symptoms"
    - "The mesocortical pathway — which regulates executive function and working memory"
    - "The nigrostriatal pathway — which coordinates voluntary movement and is disrupted by D2 blockade"
    - "The tuberoinfundibular pathway — which regulates prolactin secretion from the pituitary"
  answer: 2
  explanation: "Typical antipsychotics are nonselective D2 antagonists that block all four major dopamine pathways simultaneously. The nigrostriatal pathway connects the substantia nigra to the striatum and coordinates voluntary movement — the same pathway damaged in Parkinson's disease. Blocking D2 here mimics Parkinsonism: rigidity, bradykinesia, tremor, and with chronic use, tardive dyskinesia. The mesolimbic pathway is the therapeutic target (reducing positive symptoms), but typicals cannot selectively block one pathway and spare the others."

- question: "Atypical antipsychotics show reduced extrapyramidal side effects (EPS) compared to typicals primarily because they:"
  type: multiple-choice
  options:
    - "Do not block D2 receptors at all, achieving antipsychotic effect through serotonin blockade alone"
    - "Block only mesolimbic D2 receptors while leaving all other dopamine pathways completely unaffected"
    - "Have weaker or faster-dissociating D2 blockade combined with 5-HT2A antagonism, preserving dopamine tone in motor circuits"
    - "Act on GABA receptors rather than dopamine receptors, bypassing dopamine-related side effects entirely"
  answer: 2
  explanation: "Atypicals still block D2 receptors — the 'atypical' designation doesn't mean D2-free. They reduce EPS through two main mechanisms: weaker or faster-dissociating D2 binding in the nigrostriatal pathway (the 'fast-off' hypothesis), and combined 5-HT2A antagonism that disinhibits dopamine release in the nigrostriatal pathway, partially counteracting D2 blockade there. This preserves enough dopamine tone in motor circuits to prevent Parkinsonian side effects while still reducing mesolimbic activity to treat psychosis."

- question: "Blocking D2 receptors in the mesocortical pathway — which already shows reduced dopamine activity in schizophrenia — can worsen negative symptoms and cognitive function."
  type: true-false
  answer: true
  explanation: "The dopamine hypothesis of schizophrenia is pathway-specific: mesolimbic overactivity drives positive symptoms, while mesocortical hypoactivity contributes to negative symptoms (flat affect, poverty of speech, reduced motivation) and cognitive deficits. Typical antipsychotics block D2 everywhere, including the already-underactive mesocortical pathway, compounding its deficit. This is why typicals are poor at treating negative symptoms and may actually worsen them — a major clinical limitation that atypicals partially address."

- question: "Atypical antipsychotics are safer than typical antipsychotics in most respects, having fewer side effects without introducing any new risks."
  type: true-false
  answer: false
  explanation: "Atypicals reduce EPS but introduce a distinct class of side effects: metabolic syndrome — weight gain, dyslipidemia, and elevated blood glucose — which significantly increases cardiovascular risk with long-term use. Clozapine additionally carries risk of agranulocytosis, requiring regular blood monitoring. The choice between typical and atypical antipsychotics involves matching each drug's side effect profile to a patient's individual risk factors. Atypicals represent a tradeoff, not a clear overall superiority."

- question: "Explain why typical antipsychotics effectively reduce positive symptoms of schizophrenia but often worsen negative symptoms and cause movement disorders."
  type: short-answer
  answer: "Typical antipsychotics are potent, nonselective D2 antagonists that block dopamine activity across all four major dopamine pathways simultaneously. The antipsychotic effect comes from blocking D2 in the mesolimbic pathway (where overactivity drives hallucinations and delusions). But the same blockade hits the nigrostriatal pathway (causing Parkinson-like EPS), the mesocortical pathway (worsening the already-reduced dopamine activity underlying negative symptoms and cognitive deficits), and the tuberoinfundibular pathway (causing hyperprolactinemia). Because all pathways share the D2 receptor, therapeutic effect and these side effects are an unavoidable package with nonselective typicals."
  explanation: "This is the core limitation of first-generation antipsychotics and the motivation for developing atypicals: selectively blocking mesolimbic D2 while preserving nigrostriatal and mesocortical dopamine tone is the goal, but typicals achieve it poorly due to their nonselective binding profile."
```

## Explainer

From your study of schizophrenia-spectrum disorders, you know that psychosis involves positive symptoms — hallucinations, delusions, disorganized thinking — and negative symptoms — flat affect, poverty of speech, reduced motivation. From your study of the dopamine system, you know that dopamine pathways project from midbrain nuclei to distinct brain regions, each mediating different functions. Antipsychotic pharmacology is built on exploiting this anatomy: by blocking dopamine D2 receptors selectively in the mesolimbic pathway, it is possible to reduce psychotic symptoms, while ideally sparing other pathways that depend on dopamine for critical functions.

**Typical (first-generation) antipsychotics** — haloperidol, chlorpromazine, fluphenazine — are potent, nonselective D2 receptor antagonists. They block D2 receptors throughout all four major dopamine pathways simultaneously. Their effectiveness against positive symptoms reflects the dopamine hypothesis: overactivity in the mesolimbic pathway is thought to underlie hallucinations and delusions, and blocking D2 there reduces this signal. However, blocking D2 in the nigrostriatal pathway — which coordinates movement — produces **extrapyramidal side effects (EPS)**: Parkinson-like rigidity and tremor, restlessness (akathisia), and with chronic use, the potentially irreversible tardive dyskinesia. Blocking D2 in the mesocortical pathway, which already shows reduced dopamine activity in schizophrenia, can worsen negative symptoms and cognitive function rather than improving them.

**Atypical (second-generation) antipsychotics** — clozapine, olanzapine, risperidone, quetiapine — were developed to reduce EPS while maintaining antipsychotic efficacy. They achieve this through a combination of mechanisms: weaker or faster-dissociating D2 block (the "fast-off" hypothesis), combined D2 and serotonin 5-HT2A antagonism (serotonin modulates dopamine release, and blocking 5-HT2A in the nigrostriatal pathway preserves dopamine tone), and action at additional receptor targets. The atypicals, particularly clozapine, also show meaningful improvement in negative symptoms and cognition, possibly because the serotonin-dopamine balance in the prefrontal cortex is more favorably adjusted. The tradeoff is **metabolic side effects** — weight gain, dyslipidemia, elevated blood glucose — which significantly increase cardiovascular risk with long-term use.

The therapeutic rationale for long-term antipsychotic use in schizophrenia rests on two facts: psychosis causes neurobiological damage (each episode is associated with further cortical thinning and cognitive decline), and relapse rates after discontinuation are very high. This creates a difficult clinical calculus — the benefits of sustained remission must be weighed against the progressive metabolic and neurological risks of chronic medication. Understanding antipsychotics means understanding not just their acute receptor pharmacology, but also how the brain adapts to sustained receptor blockade (D2 receptor upregulation, for instance, may explain why dose reduction often precipitates relapse) and why selecting the right agent requires matching the patient's symptom profile and risk tolerance to each drug's receptor profile.
