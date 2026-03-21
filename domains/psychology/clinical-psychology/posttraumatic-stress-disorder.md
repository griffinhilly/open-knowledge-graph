---
id: posttraumatic-stress-disorder
title: Posttraumatic Stress Disorder
domain: psychology
course: clinical-psychology
prerequisites:
- id: dsm-5-diagnostic-criteria-and-classification
  type: hard
- id: amygdala-emotion
  type: soft
builds-toward:
- exposure-therapy-and-cbt
- antidepressant-medications-ssris
tags:
- PTSD
- trauma
stage: advanced
status: draft
---

# Posttraumatic Stress Disorder

## Core Idea
Posttraumatic Stress Disorder develops after trauma exposure and involves re-experiencing symptoms (flashbacks, nightmares), avoidance, negative mood/cognition changes, and hyperarousal. PTSD reflects abnormalities in fear processing and memory consolidation. The disorder maintains through avoidance that prevents habituation and maladaptive trauma memory processing.

## Questions

```yaml
- question: "A person with PTSD consistently avoids driving past the intersection where their accident occurred. Their therapist explains that this avoidance is the main reason the disorder persists. Why would avoidance maintain PTSD rather than help it resolve?"
  type: multiple-choice
  options:
    - "Avoidance suppresses the traumatic memory entirely, preventing the brain from processing it"
    - "Avoidance prevents the extinction learning that requires safe exposure to feared stimuli to form a new 'this is safe' association"
    - "Avoidance raises cortisol levels, which directly strengthens the original fear memory"
    - "Avoidance is only harmful if the original trauma was severe; for mild traumas it promotes recovery"
  answer: 1
  explanation: "Extinction is not forgetting — it is the formation of a new competing association ('the stimulus is now safe') that inhibits the original fear response. For extinction to occur, the person must encounter the feared stimulus in a safe context, allowing the nervous system to learn that the cue no longer predicts danger. Avoidance prevents this encounter entirely, so the fear memory remains unchallenged and the disorder is maintained indefinitely. This is why exposure-based therapies like Prolonged Exposure are first-line treatments: they systematically reverse avoidance."

- question: "Why do flashbacks in PTSD feel phenomenologically present-tense — as if the event is happening *now* rather than being remembered from the past?"
  type: multiple-choice
  options:
    - "PTSD erases the original memory and replaces it with a fabricated re-creation that runs as a new experience"
    - "High cortisol during trauma massively activates the amygdala while impairing hippocampal contextual encoding, leaving strong fear responses without temporal-contextual tags"
    - "Flashbacks occur only during sleep, when the prefrontal cortex is offline and cannot distinguish past from present"
    - "Re-experiencing symptoms are simply conditioned behavioral responses, not memory phenomena at all"
  answer: 1
  explanation: "Normal episodic memories are consolidated with contextual information (when, where, what came after) largely encoded by the hippocampus. During extreme stress, the amygdala is massively activated while cortisol impairs hippocampal function — resulting in a vivid, strongly encoded fear response with poor contextual anchoring. The result is a memory that activates like a present-tense alarm rather than a past-tense narrative. This is why flashbacks are triggered by sensory cues (smells, sounds) that bypass conscious recollection and activate the fear response directly."

- question: "Social support after trauma dramatically reduces the likelihood of developing PTSD."
  type: true-false
  answer: true
  explanation: "PTSD is not purely an internal neurobiological disorder — it is profoundly shaped by the social context in which recovery occurs. Having people who validate the experience, provide safety, and help the survivor make meaning of what happened is strongly protective. Social isolation after trauma is a major risk factor. This is why effective treatments often include relational components, and why community-level factors (e.g., unit cohesion in combat veterans) predict PTSD rates."

- question: "Avoidance of trauma reminders is an adaptive short-term coping strategy that, if sustained long enough, eventually leads to natural recovery from PTSD."
  type: true-false
  answer: false
  explanation: "This is the central misconception about PTSD maintenance. While avoidance provides immediate relief by preventing the fear response from firing, it also prevents the extinction learning that resolves the disorder. Sustained avoidance keeps the fear memory intact and unchallenged. Recovery requires the opposite: systematic approach to feared memories and situations (as in Prolonged Exposure) or direct processing of the traumatic memory (as in EMDR or Cognitive Processing Therapy). Avoidance is the perpetuating mechanism, not the cure."

- question: "Why is avoidance considered the central *maintaining* mechanism of PTSD rather than simply a symptom of it?"
  type: short-answer
  answer: "Avoidance prevents the extinction learning needed to resolve the conditioned fear response. Extinction requires that the feared stimulus be encountered in a safe context so the nervous system can learn a new association ('this is now safe'). By avoiding trauma reminders, the person with PTSD ensures this learning never occurs — the original fear memory remains active and unchecked. Avoidance is thus not just a downstream effect of fear; it is the behavioral loop that keeps the fear alive."
  explanation: "This distinction matters clinically: if avoidance were merely a symptom, treating the underlying fear might be sufficient. But because avoidance actively perpetuates the disorder by blocking extinction, treatment must directly target and reverse the avoidance — which is exactly what Prolonged Exposure therapy does. Understanding avoidance as a maintaining mechanism explains why the disorder can persist for decades in the absence of any ongoing threat."
```

## Explainer

From your familiarity with DSM-5 classification, you know that PTSD is unusual among psychiatric diagnoses in having an explicit etiology built into its criteria: it requires exposure to actual or threatened death, serious injury, or sexual violence. But not everyone who experiences trauma develops PTSD — only about 10–20% do after most traumas, rising to higher rates after rape or combat. The question PTSD theory must answer is not just *what the symptoms are* but *why this particular constellation of symptoms forms* and *what maintains them*.

The **four symptom clusters** in DSM-5 are not arbitrary. **Re-experiencing** (intrusive memories, flashbacks, nightmares) reflects a failure of normal memory processing. Ordinary episodic memories are consolidated into narrative form — temporally tagged, integrated with context, clearly belonging to the past. Traumatic memories in PTSD are poorly consolidated: they remain fragmented, highly sensory (triggered by smells, sounds, bodily sensations), and phenomenologically present-tense, as if the event is happening now rather than remembered. From your study of amygdala function, you can see why: extreme stress activates the amygdala massively while impairing hippocampal function (via cortisol's effects on hippocampal neurons), resulting in strong **conditioned fear responses** with weak contextual encoding. The flashback is a fear response without adequate contextual information telling the brain "this was then, not now."

**Avoidance** is the central maintaining mechanism. By avoiding trauma reminders — places, people, feelings, thoughts — the person with PTSD prevents the fear response from occurring, which provides immediate relief. But avoidance also prevents the extinction learning that normal fear processing requires. Extinction is not forgetting; it is the learning of a new association ("the stimulus is now safe") that inhibits the original fear memory. Without exposure to the feared stimulus in a safe context, this new learning never occurs. The **hyperarousal** cluster (exaggerated startle, sleep disturbance, hypervigilance) reflects a nervous system calibrated for a dangerous environment — a threat-detection system stuck in the on position long after the original threat has passed.

The **negative cognitions and mood** cluster — guilt, shame, distorted blame, emotional numbing, estrangement from others — represents the cognitive elaboration of the trauma. Many people with PTSD develop appraisals like "I am permanently damaged," "The world is completely dangerous," or "I am responsible for what happened." These appraisals are not simply symptoms to remove; they are attempts to make sense of an overwhelming experience, often in ways that preserve some feeling of control (if I caused it, I can prevent the next one) even at tremendous emotional cost. **Cognitive Processing Therapy** directly targets these stuck points. **Prolonged Exposure** targets the avoidance maintaining the disorder by systematically approaching feared memories and situations until extinction learning can proceed.

A final important point: PTSD is a diagnosis with real neurobiological correlates — elevated amygdala reactivity, reduced hippocampal volume, altered prefrontal regulation — but it is also a socially shaped experience. The same event causes different rates of PTSD across different cultural contexts and social support conditions. Having people around you who validate your experience, provide safety, and help you make meaning of what happened is enormously protective. Social isolation after trauma dramatically increases risk. This is why treatment focuses not just on the internal machinery of fear processing but on the relational and meaning-making context in which recovery happens.
