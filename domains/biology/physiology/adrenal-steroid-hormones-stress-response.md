---
id: adrenal-steroid-hormones-stress-response
title: Adrenal Steroid Hormones and the Stress Response
domain: biology
course: physiology
prerequisites:
- id: endocrine-system-overview
  type: hard
- id: hypothalamus-pituitary-axis
  type: hard
- id: autonomic-nervous-system
  type: soft
tags:
- adrenal
- cortisol
- stress
- HPA axis
stage: advanced
status: draft
---

# Adrenal Steroid Hormones and the Stress Response

## Core Idea
The adrenal cortex produces glucocorticoids (cortisol) and mineralocorticoids (aldosterone), with cortisol being central to the stress response. Cortisol is released from the zona fasciculata in response to ACTH from the anterior pituitary, which is stimulated by CRH from the hypothalamus during physical stress (trauma, hypoglycemia), emotional stress, or metabolic demands. Cortisol promotes gluconeogenesis and glucose mobilization, suppresses immune and inflammatory responses, and increases sympathetic nervous system sensitivity, preparing the body for "fight or flight." The hypothalamic-pituitary-adrenal (HPA) axis exhibits tight negative feedback: elevated cortisol inhibits CRH and ACTH release through actions on the hypothalamus and pituitary, preventing excessive stress hormone production.

## How It's Best Learned
Measure plasma cortisol (high in morning, low in evening) and ACTH in response to acute stressors (cold pressor test, mental arithmetic) and chronic stress. Study Cushing syndrome (excess cortisol) and Addison disease (cortisol deficiency). Understand dexamethasone suppression test for diagnosis.

## Common Misconceptions
Epinephrine is not produced by the adrenal cortex; it is produced by the adrenal medulla (derived from neural crest tissue) and is part of the sympathetic nervous system, not the endocrine axis.

## Questions

```yaml
- question: "A patient is injected with epinephrine (adrenaline) to treat a severe allergic reaction. Which structure produced this epinephrine in a healthy individual?"
  type: multiple-choice
  options:
    - "The zona fasciculata of the adrenal cortex, as part of the HPA axis"
    - "The zona glomerulosa of the adrenal cortex, which produces mineralocorticoids"
    - "The adrenal medulla, which is derived from neural crest tissue and is part of the sympathetic nervous system"
    - "The anterior pituitary, which produces epinephrine in response to ACTH"
  answer: 2
  explanation: "Epinephrine (adrenaline) is produced by the adrenal medulla, not the adrenal cortex. The medulla is derived from neural crest tissue and is functionally a modified sympathetic ganglion — its chromaffin cells are postganglionic neurons that release epinephrine directly into the bloodstream rather than onto a target organ. The adrenal cortex (the outer layer) produces steroid hormones: cortisol from the zona fasciculata and aldosterone from the zona glomerulosa. The two zones are structurally adjacent but functionally distinct: the medulla is part of the sympathetic nervous system while the cortex is part of the endocrine HPA axis."

- question: "A clinician administers dexamethasone (a synthetic glucocorticoid) to a patient and finds that ACTH and cortisol levels do not fall. What does this indicate?"
  type: multiple-choice
  options:
    - "The patient has Addison disease (cortisol deficiency), confirming that the adrenal cortex cannot produce cortisol"
    - "The HPA axis negative feedback loop is broken — a hallmark of conditions like Cushing syndrome where autonomous cortisol or ACTH production bypasses feedback control"
    - "The test is working correctly — ACTH and cortisol should not fall in response to dexamethasone"
    - "The patient has a pituitary adenoma that secretes excess growth hormone, not ACTH"
  answer: 1
  explanation: "The dexamethasone suppression test exploits the HPA axis negative feedback: in a healthy individual, dexamethasone (a potent synthetic glucocorticoid) signals the hypothalamus and pituitary to suppress CRH and ACTH release, which causes endogenous cortisol to fall. Failure to suppress means the feedback loop is disrupted. This is the hallmark of Cushing syndrome, where an autonomous cortisol-secreting adrenal tumor, an ACTH-secreting pituitary adenoma, or ectopic ACTH production overrides the feedback signal. Addison disease would show low baseline cortisol with no need to suppress further."

- question: "Epinephrine and cortisol are both produced by the adrenal cortex as part of the HPA axis stress response."
  type: true-false
  answer: false
  explanation: "False. Epinephrine is produced by the adrenal medulla (derived from neural crest, part of the sympathetic nervous system), not the adrenal cortex. Cortisol is produced by the zona fasciculata of the adrenal cortex as the terminal product of the HPA axis (hypothalamus → CRH → pituitary → ACTH → adrenal cortex → cortisol). The two systems are anatomically adjacent and both respond to stress, but they are distinct in origin, mechanism, and timescale: epinephrine provides the immediate alarm response (seconds), while cortisol provides the sustained metabolic response (minutes to hours)."

- question: "Elevated cortisol inhibits both CRH release from the hypothalamus and ACTH release from the anterior pituitary, forming a negative feedback loop that prevents excessive HPA axis activation."
  type: true-false
  answer: true
  explanation: "True. Cortisol acts at both levels of the HPA axis to shut down its own production: it suppresses CRH release from the hypothalamus and directly inhibits ACTH secretion from the anterior pituitary. This dual negative feedback ensures that the stress response is self-limiting — cortisol rises to address the metabolic demands of stress and then signals the axis to stand down. This feedback is so reliable that its integrity can be assessed clinically (dexamethasone suppression test): failure to suppress indicates loss of feedback control, as seen in various forms of Cushing syndrome."

- question: "Why does the body need both epinephrine (from the adrenal medulla) and cortisol (from the adrenal cortex) during a stress response? What does each contribute that the other cannot?"
  type: short-answer
  answer: "Epinephrine provides the immediate alarm response: within seconds, it increases heart rate and cardiac output, redirects blood flow from gut to muscle, dilates airways, and mobilizes glucose from glycogen — readying the body for immediate physical action. This fast response is mediated through membrane receptors (adrenergic receptors) and requires no gene transcription. Cortisol operates on a slower timescale (minutes to hours) and addresses the sustained metabolic demands of the stress response: it promotes gluconeogenesis (generating new glucose from amino acids and glycerol), breaks down muscle protein and fat to supply substrates, suppresses immune and inflammatory responses that would divert energy, and sensitizes the cardiovascular system to epinephrine. Cortisol essentially provides the logistics to sustain what epinephrine initiates — without cortisol, the fuel supply for a prolonged stress response would fail."
  explanation: "The complementarity of the two systems is illustrated by Addison disease (cortisol deficiency): patients can mount an initial fight-or-flight response via epinephrine, but they cannot sustain it metabolically and are dangerously vulnerable to even mild stressors. Cushing syndrome shows the opposite problem: chronic excess cortisol produces hyperglycemia, muscle wasting, and immune suppression even in the absence of acute stress — every effect of cortisol carried to a pathological extreme. Together, these conditions confirm that cortisol's role is not interchangeable with epinephrine's, and that each is necessary for a fully functional stress response."
```

## Explainer

When your body encounters a threat — whether it is a physical injury, a dangerous drop in blood sugar, or the psychological pressure of a high-stakes exam — it activates a hormonal cascade called the **hypothalamic-pituitary-adrenal (HPA) axis**. You already know from studying the hypothalamus-pituitary axis that the hypothalamus translates neural signals into hormonal commands, and that the anterior pituitary amplifies those commands by releasing tropic hormones into the bloodstream. The HPA axis is one of the most important specific instances of this general architecture: the hypothalamus releases **corticotropin-releasing hormone (CRH)**, which stimulates the anterior pituitary to secrete **adrenocorticotropic hormone (ACTH)**, which travels to the adrenal cortex and triggers release of **cortisol** from the zona fasciculata.

Cortisol is the body's primary long-duration stress hormone, and its effects are fundamentally metabolic. While the sympathetic nervous system you studied earlier provides the immediate "fight or flight" response — increased heart rate, dilated pupils, redirected blood flow — cortisol operates on a slower timescale of minutes to hours, ensuring the body has the fuel to sustain that response. It promotes **gluconeogenesis** in the liver, converting amino acids and glycerol into glucose. It breaks down muscle protein and adipose tissue to supply those substrates. It suppresses non-essential functions like immune surveillance and inflammation, which consume energy the body needs elsewhere during acute stress. Think of cortisol as the logistics officer behind the front lines: while epinephrine sounds the alarm, cortisol redirects supply chains to keep the fighting force operational.

The HPA axis is kept in check by **negative feedback**: when cortisol levels in the blood rise sufficiently, cortisol itself acts on receptors in both the hypothalamus and the anterior pituitary to suppress further CRH and ACTH release. This is the same feedback principle you learned in the endocrine system overview — the product of the cascade inhibits the cascade's own initiation. The result is a self-limiting loop: stress triggers cortisol release, cortisol addresses the metabolic demands of stress, and then rising cortisol levels shut down the axis to prevent overproduction. This feedback mechanism is so reliable that clinicians exploit it diagnostically: the **dexamethasone suppression test** administers a synthetic glucocorticoid and checks whether ACTH and cortisol fall appropriately. If they do not, the feedback loop is broken — a hallmark of conditions like Cushing syndrome.

When the HPA axis malfunctions, the consequences illustrate how precisely calibrated it must be. **Cushing syndrome** (chronic cortisol excess) produces hyperglycemia, muscle wasting, fat redistribution to the trunk and face, immune suppression, and osteoporosis — every one of cortisol's normal actions carried to a pathological extreme. **Addison disease** (cortisol deficiency) produces the mirror image: hypoglycemia, fatigue, weight loss, hypotension, and dangerous vulnerability to stress. These clinical bookends demonstrate that cortisol is not simply "the stress hormone" — it is a tightly regulated metabolic integrator whose value lies entirely in being produced in the right amount at the right time.
