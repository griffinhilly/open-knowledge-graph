---
id: major-depressive-disorder-mdd
title: Major Depressive Disorder
domain: psychology
course: clinical-psychology
prerequisites:
- id: dsm-5-diagnostic-criteria-and-classification
  type: hard
- id: serotonin-system
  type: soft
- id: schizoaffective-disorder
  type: soft
builds-toward:
- behavioral-activation-depression
- cognitive-behavioral-therapy-cbt
tags:
- depression
- mood
stage: expert
status: validated
---
# Major Depressive Disorder

## Core Idea
Major Depressive Disorder is characterized by depressed mood or anhedonia lasting at least 2 weeks with changes in sleep, appetite, energy, concentration, guilt, and suicidal ideation. Depression involves cognitive distortions, physiological changes including HPA axis dysregulation, and behavioral withdrawal.

## Questions

```yaml
- question: "A patient tells her therapist: 'I don't feel sad exactly — food just doesn't taste good anymore, I've stopped listening to music, and I don't look forward to anything.' She denies depressed mood. Which of the following best applies?"
  type: multiple-choice
  options:
    - "She cannot be diagnosed with MDD because depressed mood is required"
    - "She meets criteria for anhedonia, which is sufficient as the core MDD symptom alongside other criteria"
    - "This pattern suggests anxiety rather than depression"
    - "She may have MDD only if she also reports sadness later in the episode"
  answer: 1
  explanation: "DSM-5 requires EITHER depressed mood OR anhedonia as the core feature — not both. Anhedonia (loss of pleasure or interest) is a fully valid primary symptom and may actually reflect dopamine reward-circuit dysfunction more than serotonin dysregulation. The common misconception is that depression always means sadness; many patients present primarily through anhedonia."

- question: "A therapist using behavioral activation asks a depressed patient to schedule a walk with a friend even though the patient feels no desire to do so. The patient protests: 'What's the point if I won't enjoy it?' What is the correct clinical response grounded in behavioral theory?"
  type: multiple-choice
  options:
    - "The patient is right — engaging without motivation is unlikely to help and may reinforce hopelessness"
    - "Motivation is required first; the therapist should work on motivational interviewing before scheduling activities"
    - "Action precedes motivation in depression; engaging in the activity can restore positive reinforcement and begin to shift mood"
    - "The scheduled activity will only help if the patient chooses it spontaneously rather than being prompted"
  answer: 2
  explanation: "Behavioral activation is built on the insight that in depression, the normal sequence is reversed: people wait for motivation before acting, but the withdrawal that follows removes the activities that would restore motivation. The withdrawal spiral — reduced activity → less positive reinforcement → worsening mood → further withdrawal — must be broken by scheduling activity regardless of motivation level. Action precedes motivation, not the other way around."

- question: "Anhedonia in MDD can occur independently of depressed mood, and is linked more closely to dopamine reward-circuit dysfunction than to serotonin dysregulation."
  type: true-false
  answer: true
  explanation: "True. The Explainer notes that anhedonia implicates the reward system and is more closely linked to reduced dopamine signaling, while serotonin is more central to mood regulation. This neurobiological distinction helps explain why SSRIs — which primarily target serotonin — work well for some patients but are less effective for those whose MDD is dominated by anhedonia."

- question: "Elevated cortisol in MDD is the initial cause of the disorder; once cortisol normalizes, depression reliably resolves."
  type: true-false
  answer: false
  explanation: "False. The relationship between cortisol and depression is bidirectional, not unidirectional. Chronic stress activates the HPA axis and elevates cortisol, which can contribute to depression — but the depressive state itself perpetuates the biological stress response. Moreover, HPA dysregulation is one of several pathophysiological threads in MDD (alongside dopamine, serotonin, behavioral, and cognitive factors), and MDD is neurobiologically heterogeneous. Normalizing cortisol alone does not reliably resolve the full disorder."

- question: "Why does behavioral withdrawal worsen depression rather than protecting a person from further distress?"
  type: short-answer
  answer: "Behavioral withdrawal removes the activities that provide positive reinforcement — social contact, accomplishment, pleasure. By withdrawing, the person eliminates the very experiences that could improve mood, creating a self-reinforcing spiral: less activity leads to less reinforcement, which deepens the depression, which further reduces motivation to engage. The withdrawal feels protective but actually accelerates decline by cutting off the inputs the mood system depends on."
  explanation: "This is the core logic behind behavioral activation therapy. The insight is counterintuitive: depressed people reduce activity because they expect it to be unrewarding — and in doing so, they guarantee it will be. Breaking the spiral requires acting before motivation returns, trusting that engagement itself will begin to restore the reinforcement that motivation depends on."
```

## Explainer

From your work with DSM-5 diagnostic criteria, you understand that psychiatric diagnoses require a specific symptom cluster persisting above a duration and severity threshold. MDD exemplifies this structure: the diagnosis requires either **depressed mood** or **anhedonia** (loss of pleasure or interest in activities previously enjoyed) as a core feature, plus at least five total symptoms from a list that includes sleep disturbance, appetite and weight changes, psychomotor retardation or agitation, fatigue, feelings of worthlessness or excessive guilt, diminished concentration, and recurrent thoughts of death or suicidal ideation. All symptoms must persist for at least two weeks and represent a change from prior functioning. The two-week criterion distinguishes an episode from normal grief or transient low mood.

The most clinically important distinction is between depressed mood and **anhedonia**. Some patients describe sadness clearly; others deny feeling sad but report that nothing brings pleasure — food doesn't taste good, music sounds flat, social interactions feel effortless but pointless. Anhedonia is particularly important because it implicates the reward system: serotonin (your soft prerequisite) is involved in mood regulation, but anhedonia is more closely linked to reduced dopamine signaling in reward circuits. This helps explain why antidepressants that primarily target serotonin (SSRIs) work well for some patients but poorly for others — MDD is neurobiologically heterogeneous, and different patients likely have different dominant pathophysiology.

The **HPA axis dysregulation** in MDD illustrates how the disorder crosses from psychology into physiology. Chronic stress activates the hypothalamic-pituitary-adrenal axis, releasing cortisol. In many depressed patients, this system becomes dysregulated: cortisol levels are elevated, and the normal feedback suppression that would turn off the stress response is blunted. Elevated cortisol harms hippocampal neurons (hippocampal volume is measurably reduced in MDD), disrupts sleep architecture, suppresses immune function, and further impairs mood. This creates a bidirectional relationship: stress causes depression, and depression perpetuates the biological stress response.

The behavioral dimension of MDD is captured by the concept of a **withdrawal spiral**. When depressed, individuals lose motivation and withdraw from activities. But those activities were providing positive reinforcement — social contact, accomplishment, pleasure. By withdrawing, the person removes the very experiences that could improve mood, accelerating the decline. Behavioral activation therapy, a component of CBT, directly targets this spiral by scheduling pleasurable and meaningful activities even before motivation returns — the insight being that action precedes motivation in depression, not the other way around. Understanding MDD as simultaneously a neurobiological, cognitive, and behavioral condition is what the biopsychosocial model requires: single-level explanations consistently underpredict both symptom presentation and treatment response.
