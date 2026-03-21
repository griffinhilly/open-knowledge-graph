---
id: mood-disorder-neurobiology
title: Neurobiological Mechanisms of Mood Disorders
domain: psychology
course: clinical-psychology
prerequisites:
- id: serotonin-system
  type: hard
- id: dopamine-reward-system
  type: hard
- id: hormones-and-behavior
  type: soft
- id: intracellular-signaling-and-second-messengers
  type: soft
- id: monoamine-synthesis-and-catabolism
  type: hard
- id: neurotransmitter-systems
  type: hard
builds-toward:
- antidepressant-medications
- mood-stabilizers-anxiolytics
tags:
- neurobiology
- mood
- serotonin
- dopamine
- hpa-axis
stage: advanced
status: draft
---

# Neurobiological Mechanisms of Mood Disorders

## Core Idea
Mood disorders involve dysregulation in multiple neurotransmitter systems (serotonin, dopamine, norepinephrine), the hypothalamic-pituitary-adrenal (HPA) axis, and inflammatory markers. Genetic vulnerability interacts with environmental stress to shape these systems; critical periods in early development (trauma, attachment disruption) have lasting effects. Neuroimaging reveals structural and functional abnormalities in prefrontal and limbic regions, though causality and directionality remain unclear.

## Questions

```yaml
- question: "Antidepressants that block serotonin reuptake (SSRIs) increase synaptic serotonin within hours of the first dose, yet most patients don't experience clinical improvement for 2–4 weeks. What does this delay most strongly suggest?"
  type: multiple-choice
  options:
    - "SSRIs are correcting a serotonin deficiency, but patients are slow to notice the biochemical improvement"
    - "The therapeutic effect depends on downstream adaptive changes — receptor desensitization, increased BDNF expression, and new synaptic growth — that take weeks to develop"
    - "SSRIs need to accumulate to therapeutic blood levels before they can be effective, which takes several weeks"
    - "The delay is a placebo effect; SSRIs' actual biological action is immediate but patients are slow to trust the medication"
  answer: 1
  explanation: "If depression were simply a monoamine deficiency, restoring those levels quickly should produce rapid improvement — but it doesn't. The 2–4 week delay is the strongest argument that the therapeutic mechanism is not monoamine restoration per se, but rather the downstream cascades that monoamines activate over time: receptor desensitization, upregulation of the cAMP-PKA-CREB pathway, increased BDNF expression, and ultimately synaptic plasticity and hippocampal neurogenesis. New neurons and synapses take weeks to mature, which aligns with the clinical timeline."

- question: "Chronic stress elevates cortisol, which damages the hippocampus. Which mechanism creates a self-perpetuating vicious cycle?"
  type: multiple-choice
  options:
    - "Cortisol stimulates the amygdala to produce more stress, which triggers more cortisol release indefinitely"
    - "Hippocampal damage impairs the glucocorticoid feedback receptors that normally shut down cortisol secretion, leaving the HPA axis chronically hyperactive"
    - "Cortisol destroys norepinephrine neurons in the locus coeruleus, which then cannot inhibit the HPA axis"
    - "High cortisol permanently destroys the pituitary gland, which can no longer regulate adrenal output"
  answer: 1
  explanation: "The hippocampus contains glucocorticoid receptors that provide negative feedback to the HPA axis — detecting high cortisol and signaling the hypothalamus to reduce CRH secretion, shutting down cortisol release. When sustained high cortisol damages hippocampal neurons, this feedback mechanism is impaired: the HPA axis stays active longer, releasing more cortisol, causing more hippocampal damage, further impairing feedback. This vicious cycle helps explain why early trauma sensitizes the stress system for decades and why depression with HPA dysregulation is harder to treat."

- question: "The monoamine hypothesis of depression is simply wrong — SSRIs and other monoaminergic antidepressants do not actually work through their effects on serotonin, dopamine, or norepinephrine."
  type: true-false
  answer: false
  explanation: "The monoamine hypothesis is *incomplete*, not wrong. Monoaminergic drugs do have antidepressant effects, and monoamine systems are genuinely dysregulated in depression. The problem is that simple deficiency/restoration doesn't explain the treatment delay or why depleting monoamines doesn't reliably cause depression in healthy people. The current view is that monoamine effects are real but work *through* downstream cascades — the cAMP-CREB pathway, BDNF, neuroplasticity — rather than by directly correcting a deficiency. It is a useful framework requiring augmentation, not replacement."

- question: "Reduced BDNF expression in the hippocampus and prefrontal cortex is associated with depression, and antidepressants restore BDNF levels — consistent with the neuroplasticity hypothesis."
  type: true-false
  answer: true
  explanation: "This is well-supported and forms a key pillar of the neuroplasticity hypothesis. BDNF promotes neuronal survival, synaptic plasticity, and hippocampal neurogenesis. Stress and depression reduce BDNF expression; antidepressants, electroconvulsive therapy, and exercise all increase it. The timeline of BDNF restoration — weeks — matches the clinical timeline of antidepressant response, providing stronger support for the neuroplasticity hypothesis than for simple monoamine restoration."

- question: "Why does the neuroplasticity hypothesis of depression better explain antidepressant action than the original monoamine deficiency hypothesis?"
  type: short-answer
  answer: "The monoamine hypothesis predicts rapid improvement once monoamine levels are restored — but clinical improvement takes 2–4 weeks despite monoamines rising within hours. The neuroplasticity hypothesis explains this delay: antidepressants activate the cAMP-PKA-CREB signaling cascade downstream of monoamine receptors, which increases BDNF expression and promotes synaptic remodeling and hippocampal neurogenesis. These structural changes take weeks to develop, matching the actual clinical timeline. The hypothesis also explains why exercise and ECT — which also increase BDNF — have antidepressant effects."
  explanation: "The treatment delay is the Achilles' heel of the simple deficiency model and the primary motivation for the neuroplasticity hypothesis. It shifts the focus from 'how much neurotransmitter is in the synapse' to 'what adaptive changes in neural circuitry does that neurotransmitter ultimately drive' — a fundamentally different and better-supported account of antidepressant action."
```

## Explainer

From your study of the serotonin and dopamine systems, you know these neurotransmitters play distinct roles in mood, motivation, and reward. The **monoamine hypothesis** of depression — the founding idea in this field — proposed that depression results from a deficiency of monoamine neurotransmitters (serotonin, dopamine, and norepinephrine) at synapses, and that antidepressants work by correcting this deficiency. This hypothesis was clinically productive: it predicted that drugs blocking monoamine reuptake or breakdown would have antidepressant effects, and they do. But the monoamine hypothesis is now understood to be incomplete. Antidepressants increase synaptic monoamines within hours, yet clinical improvement takes weeks — a delay that doesn't fit a simple deficiency story and points toward downstream adaptive changes (receptor desensitization, neuroplasticity, neurogenesis) as the actual therapeutic mechanism.

The **HPA axis** — hypothalamus, pituitary, adrenal gland — adds a second layer. Stress activates this axis, releasing cortisol. From your study of hormones and behavior, you know cortisol mobilizes energy and coordinates the stress response. In acute doses, this is adaptive. But in mood disorders, particularly melancholic depression, the HPA axis is chronically hyperactive: cortisol levels are elevated, the normal circadian rhythm of cortisol is blunted, and the feedback loop that shuts down cortisol secretion (via hippocampal glucocorticoid receptors) appears impaired. High, sustained cortisol damages hippocampal neurons, reduces hippocampal volume, and impairs the very feedback mechanisms that should terminate the stress response — a vicious cycle. This helps explain why early adverse experiences (trauma, neglect) increase lifetime risk for mood disorders: they sensitize the HPA axis during a critical developmental period, leaving it prone to overreaction for decades.

From your study of intracellular signaling and second messengers, you can appreciate that neurotransmitter dysregulation is not just about how much is released but about how downstream signaling cascades respond. One key pathway is the **cAMP-PKA-CREB** cascade: serotonin and norepinephrine receptors activate this pathway, which ultimately drives expression of brain-derived neurotrophic factor (**BDNF**). BDNF supports neuronal survival, synaptic plasticity, and hippocampal neurogenesis. In depression, BDNF expression in the hippocampus and prefrontal cortex is reduced; antidepressants restore it. This **neuroplasticity hypothesis** better accounts for the treatment delay than the monoamine hypothesis alone — it takes weeks for new synapses to form and new neurons to mature.

Neuroimaging studies have added anatomical specificity. Depression is consistently associated with **reduced activity and volume in the prefrontal cortex** — the region that regulates emotion through top-down inhibition of the amygdala — and **hyperactivity in limbic regions** including the amygdala and subgenual anterior cingulate cortex. This pattern fits a model where weakened prefrontal control fails to regulate an overactive threat/salience system, producing sustained negative affect, rumination, and impaired reward processing. Importantly, however, causality runs in both directions: depression may cause these structural changes (via stress-induced neuronal atrophy), but premorbid differences in these regions may also confer vulnerability. The neurobiological picture of mood disorders is a web of mutually reinforcing dysregulations — monoamines, HPA axis, inflammatory cytokines, and plasticity cascades — rather than a single broken mechanism.
