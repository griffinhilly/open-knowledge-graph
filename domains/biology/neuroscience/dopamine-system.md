---
id: dopamine-system
title: The Dopamine System
domain: biology
course: neuroscience
prerequisites:
- id: dopamine-reward-system
  type: hard
- id: basal-ganglia-motor-selection
  type: soft
builds-toward:
- reward-motivation-circuits
- motor-learning-cerebellar
- parkinson-disease-pathology
tags:
- dopamine
- da
- reward
- motor-control
stage: advanced
status: validated
---

# The Dopamine System

## Core Idea
Dopamine is synthesized in the midbrain (VTA and SNc) and acts via D1-like and D2-like receptors to regulate reward, motivation, and motor control. Phasic dopamine release signals prediction errors; tonic dopamine sets motivational state. The nigrostriatal pathway controls movement; mesolimbic pathway mediates reward. Parkinson's involves loss of nigrostriatal dopamine neurons.

## How It's Best Learned
Record dopamine neuron responses during reward tasks. Trace VTA and SNc connections to striatum and prefrontal cortex.

## Common Misconceptions
Dopamine signals pleasure—it signals prediction error and motivation. Dopamine is depleted throughout the brain in Parkinson's—the nigrostriatal system is most affected.

## Questions

```yaml
- question: "A rat is trained to press a lever for a food reward. Initially, dopamine neurons fire strongly when the food is delivered. After weeks of training with a reliable tone that precedes food delivery, researchers record dopamine activity. Which pattern best describes the learned response?"
  type: multiple-choice
  options: ["Dopamine neurons fire strongly to food delivery and weakly to the tone, as dopamine encodes pleasure", "Dopamine neurons fire strongly to the tone and show little or no response to food delivery itself", "Dopamine neurons fire equally to both tone and food delivery, since both are rewarding", "Dopamine neurons are suppressed by the tone because it creates anticipatory anxiety"]
  answer: 1
  explanation: "Phasic dopamine release encodes reward prediction error, not pleasure. Early in training, the unpredicted food triggers a dopamine burst. As the tone becomes a reliable predictor, the dopamine response shifts to the tone (the earliest predictor of reward). Food delivery, now fully predicted, produces no additional dopamine signal — it is 'accounted for.' If the expected reward is then omitted, dopamine activity is suppressed below baseline, encoding a negative prediction error."

- question: "The motor deficits characteristic of Parkinson's disease (tremor, rigidity, bradykinesia) are primarily caused by dopamine loss in the mesolimbic pathway projecting from the VTA to the nucleus accumbens."
  type: true-false
  answer: false
  explanation: "Parkinson's disease motor symptoms result from the loss of dopamine neurons in the substantia nigra pars compacta (SNc) of the nigrostriatal pathway, which projects to the dorsal striatum (caudate and putamen). The mesolimbic pathway (VTA → nucleus accumbens) is more involved in reward, motivation, and addiction. The mesolimbic pathway is relatively spared in early Parkinson's, which is why motivational deficits emerge later in the disease than motor symptoms."

- question: "Distinguish between phasic and tonic dopamine release: how do they differ in their temporal dynamics and what distinct functional roles does each serve?"
  type: short-answer
  answer: "Phasic dopamine refers to brief, high-amplitude bursts of dopamine release (milliseconds to seconds) triggered by unexpected rewards or reward-predicting cues; it encodes reward prediction errors and drives learning about which actions and stimuli predict reward. Tonic dopamine refers to the low-level, sustained baseline dopamine concentration in the synapse maintained by ongoing spontaneous firing; it sets the general motivational state, modulates working memory in prefrontal cortex, and regulates the responsiveness of striatal circuits to phasic signals."
  explanation: "The distinction matters clinically and conceptually. Drugs of abuse (cocaine, amphetamine) primarily amplify phasic signals by blocking reuptake or forcing vesicular release, hijacking the prediction error system. Antipsychotics primarily reduce tonic D2 receptor signaling. Parkinson's treatment (L-DOPA) partly restores tonic dopamine, though it imperfectly mimics the phasic signals lost with SNc neuron death. The two modes of release are regulated differently and have distinct effects on learning versus motivational state."
```

## Explainer

When people say dopamine is the "pleasure chemical," they are telling an incomplete and somewhat misleading story. Dopamine is critical to reward processing, but what it actually encodes is more specific and more interesting than pleasure itself. Understanding the dopamine system means distinguishing between its anatomical pathways, its firing patterns, and what those patterns actually compute.

The dopamine system originates in two midbrain nuclei: the ventral tegmental area (VTA) and the substantia nigra pars compacta (SNc). These neurons project to fundamentally different targets. The nigrostriatal pathway runs from SNc to the dorsal striatum (caudate nucleus and putamen) — the part of the basal ganglia most directly involved in selecting and initiating voluntary movements. The mesolimbic pathway runs from VTA to the nucleus accumbens and other limbic structures, mediating reward learning, motivation, and goal-directed behavior. A third projection — the mesocortical pathway from VTA to prefrontal cortex — regulates working memory and executive function. These pathways are anatomically distinct and serve distinct functions, which is why Parkinson's disease (primarily a nigrostriatal disorder) causes motor problems first, while addiction and schizophrenia involve mesolimbic and mesocortical dysregulation.

The most important functional concept for understanding what dopamine neurons actually compute is the reward prediction error signal. When something unexpectedly good happens, dopamine neurons fire a brief, high-amplitude phasic burst. When a cue reliably predicts a good outcome, that burst shifts over time to the cue rather than the reward — because the reward is now expected and "priced in." If an expected reward fails to arrive, dopamine activity is suppressed below baseline. This pattern — positive burst for better-than-expected, negative dip for worse-than-expected, silence for exactly-as-expected — is precisely the prediction error signal used in reinforcement learning theory. The brain is implementing something like a temporal difference learning algorithm using phasic dopamine as the error signal.

Tonic dopamine operates on a completely different timescale. Rather than event-triggered bursts, tonic dopamine is the low-level baseline concentration in the synapse maintained by the ongoing spontaneous firing of dopamine neurons. It sets motivational state — the general drive to pursue goals — and modulates how readily the striatum and prefrontal cortex respond to phasic signals. Too little tonic dopamine produces apathy and difficulty initiating action (as in Parkinson's and some depressions); too much D2 receptor stimulation disrupts working memory and is implicated in schizophrenia.

In Parkinson's disease, the SNc dopamine neurons progressively die — typically 60-80% are lost before motor symptoms become apparent, which speaks to how much reserve the system has. L-DOPA therapy floods the system with dopamine precursor, partly restoring the tonic baseline and enabling movement, but it imperfectly mimics the precise phasic prediction error signals that healthy SNc neurons generate in response to movement context. This is why motor control in treated Parkinson's is functional but not normal. The story of the dopamine system is ultimately a story about how a small cluster of neurons in the brainstem — in the thousands, not millions — exerts outsized control over learning, motivation, and action by virtue of what their firing pattern communicates, not just how much neurotransmitter they release.
