---
id: thyroid-disorders-pathophysiology
title: 'Thyroid Disorders: Hyper- and Hypothyroidism'
domain: health-and-human-development
course: pathophysiology
prerequisites:
- id: thyroid-gland-anatomy-and-function
  type: hard
- id: hypothalamic-pituitary-axis
  type: hard
- id: thyroid-hormone-synthesis
  type: soft
builds-toward:
- graves-disease-pathophysiology
- hashimotos-thyroiditis
tags:
- thyroid-disease
- hormonal-disorders
- metabolism
stage: advanced
status: draft
---

# Thyroid Disorders: Hyper- and Hypothyroidism

## Core Idea
Hyperthyroidism involves excessive thyroid hormone production causing increased metabolism, heat production, and sympathetic activation (tachycardia, tremor, anxiety). Hypothyroidism causes decreased metabolism, cold intolerance, and depression. Iodine status, autoimmunity, and TSH-receptor mutations drive pathology.

## How It's Best Learned
Use TSH and free T4 levels to diagnose and classify. Understand the feedback axis: low T4/T3 → high TSH; high T4/T3 → low TSH. Review etiologies: Graves' disease, Hashimoto's thyroiditis, thyroiditis, and iodine deficiency.

## Common Misconceptions
TSH elevation does not always indicate primary hypothyroidism—it rises in response to low T4, including central hypothyroidism. Subclinical hypothyroidism (high TSH, normal T4) is not benign; it increases cardiovascular and cognitive risk.

## Questions

```yaml
- question: "A patient's lab results show: TSH elevated, free T4 low. Where is the most likely site of pathology, and what is the physiological explanation?"
  type: multiple-choice
  options:
    - "The pituitary gland is failing — it cannot produce enough TSH to stimulate the thyroid"
    - "The thyroid gland is failing — the pituitary is correctly sensing low T4 and compensating with elevated TSH"
    - "The hypothalamus is overactive — excess TRH is driving TSH up regardless of T4 levels"
    - "This pattern indicates hyperthyroidism — high TSH stimulates the thyroid to produce excess T4"
  answer: 1
  explanation: "High TSH + low free T4 is the hallmark pattern of primary hypothyroidism — the thyroid gland itself is failing. The pituitary gland is functioning correctly: it detects low T4/T3 levels (reduced negative feedback), releases its suppression, and produces more TSH in a compensatory attempt to stimulate the failing thyroid. TSH elevation is the pituitary's correct response to insufficient thyroid hormone, not the cause of the problem. This pattern localizes pathology to the thyroid (primary), not the pituitary or hypothalamus."

- question: "A patient presents with palpitations, weight loss despite increased appetite, heat intolerance, and anxiety. Lab results: TSH nearly undetectable, free T4 and T3 markedly elevated. What does the suppressed TSH indicate in this context?"
  type: multiple-choice
  options:
    - "The pituitary is also failing — both the thyroid and pituitary are diseased simultaneously"
    - "The pituitary is functioning correctly — it detects excess thyroid hormone and appropriately suppresses TSH secretion"
    - "TSH suppression is a direct effect of the sympathetic activation caused by hyperthyroidism"
    - "Low TSH indicates central hypothyroidism coexisting with a separate thyroid hormone-producing tumor"
  answer: 1
  explanation: "In hyperthyroidism (e.g., Graves' disease), the thyroid produces excess T4/T3 that strongly suppresses the pituitary via negative feedback. The near-zero TSH is the pituitary correctly responding to hormone excess — it has suppressed its output as far as possible. The pituitary is not failing; it is functioning perfectly. This is why the TSH/free T4 combination is so diagnostically useful: it distinguishes where the axis is perturbed. Undetectable TSH + elevated T4 = hyperthyroidism; low TSH + low T4 = central failure."

- question: "TSH is the most sensitive early indicator of thyroid dysfunction because small changes in circulating T4/T3 produce large changes in TSH secretion due to the amplifying nature of the hypothalamic-pituitary feedback loop."
  type: true-false
  answer: true
  explanation: "Correct. The negative feedback relationship between T4/T3 and TSH is steep — a small reduction in thyroid hormone output causes a large rise in TSH, and a small excess causes TSH to fall to near-zero. This amplification makes TSH the best screening test: it can detect subclinical dysfunction (abnormal TSH with still-normal free T4) before the patient develops symptoms or frank hormonal abnormalities. A single TSH measurement integrates the entire axis's assessment of thyroid hormone adequacy."

- question: "A very low TSH combined with a low free T4 indicates hyperthyroidism, since the suppressed TSH means the pituitary is being over-inhibited by thyroid hormones."
  type: true-false
  answer: false
  explanation: "Low TSH + low free T4 is the pattern for central (secondary or tertiary) hypothyroidism, not hyperthyroidism. In this scenario, the problem lies above the thyroid — at the pituitary (secondary hypothyroidism) or hypothalamus (tertiary). The pituitary fails to produce adequate TSH, so the thyroid receives insufficient stimulation and produces less T4/T3. Both TSH and T4 are low because the signal is broken at the top of the axis. In hyperthyroidism, T4 is high and TSH is suppressed (the pituitary correctly detecting excess hormone). The two scenarios both show low TSH but have opposite T4 levels."

- question: "In Graves' disease, TSH is suppressed to near-zero even though the patient is producing excess thyroid hormone. Explain the mechanism that drives this suppression."
  type: short-answer
  answer: "In Graves' disease, autoimmune antibodies (thyroid-stimulating immunoglobulins, TSI) mimic TSH by binding and chronically activating the TSH receptor on thyroid follicular cells. This drives continuous, unregulated T4 and T3 production independent of the normal feedback loop. The excess T4/T3 circulates and reaches the anterior pituitary, where it strongly suppresses TRH and TSH secretion via negative feedback — the same mechanism that suppresses TSH in any state of high thyroid hormone. The pituitary is functioning correctly; it detects excess hormone and stops signaling. TSH is near-zero because the hypothalamic-pituitary arm of the axis is working as designed — it is the thyroid stimulus (the autoantibody) that is abnormal and uncontrollable."
  explanation: "This illustrates the diagnostic power of reading TSH/free T4 together: Graves' disease suppresses TSH not because the pituitary is broken, but because it is correctly responding to a hormone excess driven by a receptor-level bypass of normal regulation. The pattern (low TSH, high T4) localizes the problem to autonomous thyroid overproduction, distinguishing it from primary hypothyroidism (high TSH, low T4) and central hypothyroidism (low TSH, low T4)."
```

## Explainer

Your prerequisite knowledge of the hypothalamic-pituitary axis gives you the essential diagnostic framework for thyroid disorders. Recall the feedback loop: the hypothalamus secretes **TRH** (thyrotropin-releasing hormone), which stimulates the anterior pituitary to release **TSH** (thyroid-stimulating hormone), which drives the thyroid gland to synthesize and release **T4** (thyroxine) and **T3** (triiodothyronine). T4 is largely a prohormone — it circulates and is converted peripherally to the more active T3 by deiodinase enzymes. T3 and T4 feed back negatively to suppress both TRH and TSH release, completing the loop. This feedback architecture means that TSH is the most sensitive indicator of thyroid function: when thyroid hormone levels are even slightly low, TSH rises to stimulate more production; when slightly high, TSH is suppressed. A single TSH measurement reflects the integrated state of the entire axis.

**Hypothyroidism** is a state of thyroid hormone deficiency. With insufficient T3/T4, the cellular machinery slows: basal metabolic rate falls, heart rate decreases, reflexes slow, the gut moves sluggishly (constipation), temperature regulation falters (cold intolerance), and cognitive processing dulls. Peripherally, low thyroid hormone allows glycosaminoglycans to accumulate in subcutaneous tissue, producing the characteristic nonpitting edema called **myxedema**. In primary hypothyroidism (the most common form, often due to Hashimoto's thyroiditis — autoimmune destruction of the thyroid), the failing gland produces less hormone, feedback suppression of the pituitary is lifted, and TSH rises. The lab picture is unambiguous: high TSH, low free T4. In central hypothyroidism (rare, from pituitary or hypothalamic failure), TSH is inappropriately low or normal despite low T4 — the axis itself is broken, not just the gland. This is the correction to the misconception: TSH elevation signals that the pituitary is working correctly to compensate for low T4, not that TSH elevation is itself the cause.

**Hyperthyroidism** reverses all of this. Excess T3/T4 accelerates cellular metabolism: the heart races (tachycardia, palpitations), the nervous system is overdriven (anxiety, tremor, insomnia), body weight falls despite increased appetite, and heat production increases dramatically (heat intolerance, sweating). **Graves' disease** — the most common cause — is an autoimmune condition where antibodies mimic TSH by binding and chronically stimulating the TSH receptor, independent of pituitary feedback. Because the stimulus bypasses the normal loop, TSH is suppressed to near-zero (the pituitary correctly detects excess hormone and stops signaling), while T4 and T3 are elevated. The lab picture: very low or undetectable TSH, elevated free T4 and/or T3. Thyroid storm, the extreme of hyperthyroidism, is a life-threatening emergency where unchecked sympathetic activation causes hyperthermia, cardiovascular collapse, and altered mental status.

The pattern recognition skill this topic builds is reading the TSH/free T4 combination to localize pathology: high TSH + low T4 = primary hypothyroidism (thyroid failing, pituitary compensating); low TSH + high T4 = hyperthyroidism (excess hormone suppressing pituitary); low TSH + low T4 = central hypothyroidism (axis broken above thyroid level); normal TSH + normal T4 = euthyroid. **Subclinical** versions of both disorders show an abnormal TSH with a still-normal free T4 — representing early dysfunction before the full hormonal derangement develops, but already carrying clinical risk. The thyroid's centrality to metabolism means its dysfunction touches nearly every organ system, making this feedback axis one of the most clinically consequential in endocrinology.
