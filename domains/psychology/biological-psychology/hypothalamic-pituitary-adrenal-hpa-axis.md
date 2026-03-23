---
id: hypothalamic-pituitary-adrenal-hpa-axis
title: Hypothalamic-Pituitary-Adrenal (HPA) Axis and Stress Response
domain: psychology
course: biological-psychology
prerequisites:
- id: hypothalamus-pituitary-axis
  type: soft
- id: adrenal-steroid-hormones-stress-response
  type: soft
- id: anterior-pituitary-hormone-axes
  type: hard
- id: hypothalamic-pituitary-axis
  type: soft
builds-toward:
- stress-response-and-coping
- depression-and-hpa-dysregulation
tags:
- stress
- hormones
- homeostasis
stage: formal-systems
status: draft
---

# Hypothalamic-Pituitary-Adrenal (HPA) Axis and Stress Response

## Core Idea
The HPA axis controls the stress response: corticotropin-releasing hormone (CRH) from the hypothalamus stimulates the anterior pituitary to release adrenocorticotropic hormone (ACTH), which stimulates cortisol release from the adrenal cortex. Cortisol provides negative feedback, shutting down the axis. Chronic stress dysregulates this system, elevating baseline cortisol and impairing feedback, contributing to depression, anxiety, and cognitive impairment.

## Questions

```yaml
- question: "A patient under chronic work stress has persistently elevated cortisol that does not drop significantly after stressors are removed. Based on the HPA axis model, the most likely underlying mechanism is:"
  type: multiple-choice
  options:
    - "The adrenal glands have physically enlarged from chronic ACTH stimulation and can no longer be downregulated"
    - "Chronic activation has downregulated glucocorticoid receptors in the hypothalamus and pituitary, impairing the negative feedback loop"
    - "The hypothalamus has permanently stopped producing CRH due to overstimulation"
    - "Elevated cortisol has destroyed the pituitary cells that respond to CRH signals"
  answer: 1
  explanation: "The mechanism is receptor downregulation, not gland destruction. Normally, cortisol feeds back to glucocorticoid receptors in the hypothalamus and pituitary to suppress CRH and ACTH production — a self-terminating loop. Under chronic stress, the prolonged cortisol signal reduces the number or sensitivity of these receptors. With fewer functional receptors, the feedback signal is weaker, the 'shut off' signal is not heard, and baseline cortisol remains elevated. This is HPA dysregulation: the negative feedback mechanism is degraded, not the hormone-producing glands themselves."

- question: "What is the correct sequence of hormone signaling in the HPA axis, from stress detection to cortisol release?"
  type: multiple-choice
  options:
    - "ACTH from the pituitary → CRH from the hypothalamus → cortisol from the adrenal cortex"
    - "CRH from the hypothalamus → ACTH from the anterior pituitary → cortisol from the adrenal cortex"
    - "CRH from the hypothalamus → cortisol from the adrenal cortex → ACTH from the pituitary as feedback"
    - "Cortisol from the adrenal cortex → ACTH from the pituitary → CRH from the hypothalamus in a forward cascade"
  answer: 1
  explanation: "The HPA axis is a sequential three-stage amplification chain: (1) the hypothalamus detects stress and releases CRH into the portal blood connecting it to the anterior pituitary; (2) CRH stimulates the anterior pituitary to release ACTH into systemic circulation; (3) ACTH travels via blood to the adrenal cortex (the outer layer of the adrenal glands) and triggers cortisol synthesis and release. Cortisol then provides negative feedback to suppress both CRH and ACTH. The cascade flows strictly hypothalamus → anterior pituitary → adrenal cortex."

- question: "The hippocampus plays a role in the HPA negative feedback loop, and chronic cortisol elevation can damage hippocampal neurons, further weakening the feedback — a vicious cycle."
  type: true-false
  answer: true
  explanation: "The hippocampus is densely packed with glucocorticoid receptors and contributes to suppressing HPA activity when cortisol is elevated. Chronically high cortisol damages hippocampal neurons through excitotoxic mechanisms. As those neurons are lost, the hippocampal contribution to HPA feedback weakens, allowing cortisol to rise further — creating a self-perpetuating dysregulation cycle. This also explains the cognitive impairment seen in chronic stress and depression: the hippocampus is critical for memory consolidation, so its damage has dual consequences (weakened feedback and impaired memory)."

- question: "Cortisol is released from the adrenal medulla (the inner core of the adrenal gland) in response to ACTH stimulation during the HPA stress response."
  type: true-false
  answer: false
  explanation: "Cortisol is released from the adrenal cortex — the outer layer of the adrenal gland — not the medulla. The adrenal medulla releases catecholamines (epinephrine and norepinephrine) as part of the rapid sympathetic fight-or-flight response. These two stress systems are anatomically housed in the same gland but are functionally and mechanistically distinct: the sympathetic/adrenal medulla pathway is neural and fast (seconds), while the HPA/adrenal cortex pathway is hormonal and slower (minutes), producing a sustained response."

- question: "Explain why chronic stress produces worse physiological and psychological outcomes than acute stress, using the HPA axis as your framework."
  type: short-answer
  answer: "Acute stress activates the HPA cascade — CRH → ACTH → cortisol — and cortisol feeds back to shut down the response. This self-terminating loop is adaptive: cortisol mobilizes energy, suppresses immune activity, and sharpens attention for the immediate threat, then dissipates. Chronic stress repeatedly or continuously activates the axis, downregulating glucocorticoid receptors in the hypothalamus, pituitary, and hippocampus. With degraded feedback, cortisol remains chronically elevated. The same mechanisms that are adaptive in short bursts become harmful over time: sustained immune suppression increases infection risk, hippocampal damage impairs memory and weakens feedback further, and dysregulated mood circuits contribute to depression and anxiety."
  explanation: "The key insight is that the HPA axis evolved for episodic, resolvable threats. Modern chronic stressors maintain activation beyond the system's regulatory capacity. Receptor downregulation converts a self-correcting feedback system into a self-perpetuating dysregulated one — the biological bridge between life stress, brain structural changes, and mood disorders like depression."
```

## Explainer

The HPA axis is the body's main hormonal stress response pathway — a three-stage amplification chain from brain to blood. From your work on the anterior pituitary and hypothalamic hormone axes, you know how hypothalamic releasing hormones trigger pituitary responses. The HPA axis works the same way: the hypothalamus detects stress and releases **corticotropin-releasing hormone (CRH)** into the portal blood connecting it to the anterior pituitary. The pituitary responds by releasing **adrenocorticotropic hormone (ACTH)** into systemic circulation. ACTH travels to the adrenal cortex — the outer layer of the adrenal glands sitting atop the kidneys — and triggers release of **cortisol**, a steroid hormone with widespread metabolic and immunological effects.

Cortisol serves the body well in short bursts. It mobilizes energy (raising blood glucose), suppresses immune activity, sharpens attention, and prepares the organism to handle a threat. The critical elegance of the system is its **negative feedback loop**: cortisol itself circulates back to the hypothalamus and pituitary, binding receptors there that inhibit further CRH and ACTH release. Once the stressor is resolved, cortisol shuts off its own production — a self-terminating response. This is homeostatic regulation in action: the product of the cascade feeds back to suppress the cascade.

The problem arises with chronic stress. When stressors are prolonged — persistent work pressure, trauma, poverty — the HPA axis is activated repeatedly or continuously. Over time, cortisol receptors in the hypothalamus and hippocampus become **downregulated** (reduced in number or sensitivity), degrading the feedback signal. The axis loses its ability to self-regulate: baseline cortisol rises, remains elevated even after stressors pass, and the shutdown mechanism becomes sluggish. This is HPA dysregulation — the system stuck in an "on" state.

Chronically elevated cortisol has cascading consequences. It damages hippocampal neurons (which are dense with glucocorticoid receptors), impairing memory consolidation and further weakening HPA feedback — a vicious cycle. It chronically suppresses immune function, increasing vulnerability to infection. And it dysregulates mood circuits: elevated cortisol is strongly associated with major depression, particularly melancholic presentations with early morning awakening and flattened diurnal cortisol rhythms. Understanding the HPA axis provides the biological bridge between life stress, brain structure, and mood disorder — a foundation for everything from antidepressant mechanisms to the neurobiology of trauma.
