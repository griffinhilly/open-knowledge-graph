---
id: anterior-pituitary-hormone-axes
title: Anterior Pituitary Hormone Axes and Control
domain: biology
course: physiology
prerequisites:
- id: hypothalamus-pituitary-axis
  type: hard
- id: hypothalamic-neuroendocrine-integration
  type: hard
builds-toward:
- thyroid-hormone-thermoregulation
- cortisol-stress-axis-adaptation
- insulin-glucagon-glucose-homeostasis
tags:
- anterior pituitary
- hormone axes
- feedback
- thyroid
- adrenal
- growth
stage: formal-systems
status: validated
---

# Anterior Pituitary Hormone Axes and Control

## Core Idea
The anterior pituitary secretes hormones (TSH, ACTH, FSH/LH, prolactin, growth hormone) in response to releasing factors from the hypothalamus. Each hormone exhibits negative feedback from its target gland, maintaining tight control. These axes regulate metabolism, stress response, and reproduction. Understanding feedback loops explains why removing negative feedback signals causes excessive hormone secretion.

## Questions

```yaml
- question: "A patient has low circulating T3/T4 levels, and lab tests reveal that TSH is dramatically elevated. Where is the defect most likely located?"
  type: multiple-choice
  options:
    - "The pituitary gland — it is failing to respond to TRH and secreting too much TSH"
    - "The hypothalamus — excess TRH is driving TSH and therefore elevating thyroid hormones"
    - "The thyroid gland itself — it is failing to produce T3/T4, so negative feedback is lost and TSH rises"
    - "The adrenal glands — cortisol suppresses TSH, so adrenal insufficiency allows TSH to rise"
  answer: 2
  explanation: "High TSH with low T3/T4 is the hallmark of primary hypothyroidism — the thyroid gland is failing. Normally, T3/T4 provide negative feedback to the pituitary, suppressing TSH. When the thyroid fails, T3/T4 levels fall, that negative feedback is lost, and the pituitary responds by dramatically upregulating TSH secretion. If the pituitary were the problem (secondary hypothyroidism), both TSH and T3/T4 would be low — the pituitary would be failing to send the signal, so the thyroid would also be understimulated. The pattern of high/low at adjacent tiers localizes the defect."

- question: "A patient sustains damage to the pituitary stalk that interrupts all communication between the hypothalamus and anterior pituitary. Which anterior pituitary hormone would be most likely to INCREASE as a result?"
  type: multiple-choice
  options:
    - "TSH — because TRH stimulation drives TSH, so losing TRH causes TSH to rise"
    - "ACTH — because cortisol negative feedback is disrupted"
    - "Prolactin — because dopamine normally tonically suppresses it, and stalk damage stops dopamine delivery"
    - "Growth hormone — because IGF-1 negative feedback can no longer reach the pituitary"
  answer: 2
  explanation: "Prolactin is the exception to the general rule that hypothalamic inputs are stimulatory. Dopamine, secreted by the hypothalamus, tonically *inhibits* prolactin release. When the stalk is cut and dopamine cannot reach the anterior pituitary, this tonic brake is removed — prolactin secretion rises. By contrast, TSH, ACTH, and the gonadotropins all fall after stalk damage because their hypothalamic *releasing* hormones are cut off. Recognizing prolactin's inhibitory control is essential for correctly predicting and diagnosing pituitary stalk lesions."

- question: "In the hypothalamic-pituitary-thyroid axis, rising T3/T4 levels suppress both TRH secretion from the hypothalamus and TSH responsiveness in the anterior pituitary, maintaining hormone levels within a narrow range."
  type: true-false
  answer: true
  explanation: "The HPT axis uses dual-site negative feedback: thyroid hormones act on both the hypothalamus (to suppress TRH release) and the anterior pituitary (to decrease TSH secretion and reduce pituitary sensitivity to TRH). This redundancy makes the regulation more precise and robust. When T3/T4 levels are too high, both suppression points activate simultaneously, rapidly reducing the drive to produce more hormone. The same three-tier negative feedback architecture applies to the HPA and HPG axes."

- question: "If both ACTH and cortisol are simultaneously low, the most likely defect is in the adrenal glands failing to produce cortisol."
  type: true-false
  answer: false
  explanation: "Primary adrenal failure (Addison's disease) produces low cortisol but *elevated* ACTH — the loss of cortisol negative feedback removes the brake on the pituitary and hypothalamus, driving ACTH up in a futile attempt to stimulate the failing glands. Low cortisol with *low* ACTH points to a pituitary or hypothalamic defect (secondary or tertiary adrenal insufficiency): the pituitary is not producing enough ACTH to drive cortisol production, so both tiers are low. Simultaneously low ACTH and cortisol rules out primary adrenal failure and points up the cascade."

- question: "A patient presents with low cortisol. Explain how measuring ACTH simultaneously helps a clinician determine whether the problem is in the adrenal glands, the pituitary, or the hypothalamus."
  type: short-answer
  answer: "The HPA axis is a three-tier cascade: hypothalamus (CRH) → pituitary (ACTH) → adrenal cortex (cortisol). Cortisol feeds back negatively to suppress both tiers above it. Measuring ACTH alongside cortisol localizes the defect: (1) Low cortisol + high ACTH = primary adrenal insufficiency — the adrenal glands are failing, negative feedback is lost, and ACTH is elevated trying to stimulate them. (2) Low cortisol + low ACTH = secondary (pituitary) or tertiary (hypothalamic) insufficiency — the upstream signal is absent, so neither ACTH nor cortisol is being produced. If further localization is needed, measuring CRH or doing a stimulation test distinguishes pituitary from hypothalamic origin."
  explanation: "This diagnostic framework is one of the most clinically powerful applications of understanding feedback loops. Without knowing the feedback structure, you might assume all low-cortisol conditions look the same. The feedback architecture turns two measurements into a complete map of where in the cascade the defect lies — a principle that generalizes to every axis (HPT, HPG) and guides both diagnosis and treatment selection."
```

## Explainer

From your study of the hypothalamic-pituitary axis, you know the basic architecture: the hypothalamus sends releasing (and inhibiting) hormones through the hypophyseal portal system to the anterior pituitary, which then secretes its own hormones into the systemic circulation. The anterior pituitary hormone axes take this one step further by adding target glands — the thyroid, adrenal cortex, and gonads — creating **three-tier cascades** where each level amplifies the signal from the level above and feeds back to suppress it.

Consider the **hypothalamic-pituitary-thyroid (HPT) axis** as the prototype. The hypothalamus releases **thyrotropin-releasing hormone (TRH)**, which stimulates **thyroid-stimulating hormone (TSH)** release from the anterior pituitary. TSH travels to the thyroid gland and promotes synthesis and secretion of thyroid hormones (T3 and T4). When circulating T3 and T4 levels rise, they act back on both the hypothalamus (suppressing TRH) and the anterior pituitary (suppressing TSH responsiveness to TRH). This **negative feedback loop** is the thermostat of the system: it prevents runaway hormone production and keeps circulating levels within a narrow physiological range. The same three-tier logic applies to the **hypothalamic-pituitary-adrenal (HPA) axis** — CRH drives ACTH, which drives cortisol, which feeds back to suppress both — and the **hypothalamic-pituitary-gonadal (HPG) axis**, where GnRH drives FSH and LH, which drive sex steroid production.

Not all anterior pituitary hormones follow this three-tier pattern. **Growth hormone (GH)** acts on the liver to produce insulin-like growth factor 1 (IGF-1), which provides the negative feedback signal, but GH also has direct metabolic effects on many tissues. **Prolactin** is unusual because its primary hypothalamic control is *inhibitory* — dopamine tonically suppresses prolactin secretion, so damage to the pituitary stalk (which interrupts dopamine delivery) causes prolactin to *rise* rather than fall. This is the opposite of what happens with TSH, ACTH, or the gonadotropins, which all decrease when their hypothalamic releasing hormones are cut off.

The clinical power of understanding these axes comes from predicting what happens when a link in the chain breaks. If the thyroid gland is destroyed, T3/T4 levels fall, negative feedback is lost, and TSH rises dramatically — this is **primary hypothyroidism** with elevated TSH. If instead the pituitary is damaged, both TSH and T3/T4 fall — **secondary hypothyroidism** with inappropriately low TSH. By measuring hormone levels at two tiers simultaneously (e.g., TSH and free T4), clinicians can localize the defect to the gland, the pituitary, or the hypothalamus. The same diagnostic logic applies to every axis: high ACTH with low cortisol points to the adrenal glands (primary adrenal insufficiency); low ACTH with low cortisol points to the pituitary or hypothalamus. Feedback loops are not just a regulatory mechanism — they are a diagnostic framework.
