---
id: skeptical-scenarios-knowledge-closure
title: Skeptical Scenarios and Knowledge Closure
domain: philosophy
course: epistemology
prerequisites:
- id: external-world-skepticism
  type: hard
- id: epistemic-closure
  type: hard
- id: modal-logic-intro
  type: soft
- id: possible-worlds-semantics
  type: soft
tags:
- skepticism
- scenarios
- closure
- knowledge
stage: formal-systems
status: validated
---

# Skeptical Scenarios and Knowledge Closure

## Core Idea
Skeptical scenarios (brains in vats, Descartes' demon, sophisticated simulation) challenge closure by seemingly showing we can know ordinary propositions (I have hands) without knowing we're not in skeptical scenarios (I'm not a brain in a vat), even though the former entails the latter. This forces epistemology to choose between accepting skepticism, rejecting closure, or distinguishing levels of knowledge. The tension illustrates a fundamental problem in the foundations of knowledge.

## How It's Best Learned
Examine skeptical hypotheses (brain in a vat, evil demon, simulation) and identify the intuition driving closure: if you don't know you're not in the skeptical scenario, how can you know ordinary facts? Test proposed resolutions.

## Common Misconceptions
- Thinking skeptical scenarios are genuine possibilities requiring empirical evidence to rule out.
- Assuming skepticism follows directly from closure.
- Confusing skeptical scenarios with science fiction possibilities.

## Questions

```yaml
- question: "You believe you have hands (H). A skeptic argues: H entails not-BIV; you cannot rule out BIV; therefore by modus tollens you do not know H. Fred Dretske's tracking account responds by:"
  type: multiple-choice
  options:
    - "Accepting the conclusion — we do not know ordinary propositions in the strict sense"
    - "Denying closure — your belief in H can track the truth of H without your belief in not-BIV needing to track its truth"
    - "Arguing empirically that brain-in-vat technology is impossible"
    - "Claiming the argument commits the fallacy of affirming the consequent"
  answer: 1
  explanation: "Dretske and Nozick deny that knowledge transmits through known entailment in the way closure claims. On the tracking account, you know H because there is no nearby possible world where you falsely believe you have hands. But BIV worlds are not 'nearby' — they are remote, bizarre scenarios. You need not track the truth of not-BIV to know H. This rejects closure as the premise that links ordinary knowledge to skeptical scenarios, rather than accepting skepticism or resorting to empirical arguments about technology."

- question: "A contextualist response to the skeptical argument claims that the word 'know' in 'I know I have hands' means something different in everyday conversation than in a philosophy seminar where BIV scenarios are explicitly raised. This response:"
  type: multiple-choice
  options:
    - "Denies the first premise — you actually can rule out BIV scenarios by observation"
    - "Accepts skepticism but limits its scope to philosophical contexts"
    - "Preserves ordinary knowledge claims by making knowledge-attribution context-sensitive rather than absolute"
    - "Implies that knowledge is entirely subjective and culturally determined"
  answer: 2
  explanation: "The contextualist does not deny skepticism outright, nor does the response make knowledge purely subjective. It claims the standards for 'knowing' shift with context: in ordinary conversation, the BIV scenario is not a relevant alternative, so 'I know I have hands' is true. In a seminar where the BIV scenario is explicitly raised, standards are elevated, and the same claim may be false. Knowledge attributions are context-sensitive in the same way that 'flat' or 'empty' are — the semantics shifts, not the world."

- question: "On the tracking account of knowledge, a person can know they have hands without knowing they are not a brain in a vat, because BIV worlds are not 'nearby' possible worlds where the person would falsely believe they have hands."
  type: true-false
  answer: true
  explanation: "The tracking account requires that in nearby possible worlds, you would not falsely believe P. For H (I have hands), there is no nearby world where you lack hands but still believe you have them — nearby worlds are just slight variations on actual reality. BIV worlds are highly remote. So H is tracked. For not-BIV, the BIV world is, by hypothesis, indistinguishable from actuality — it is in some sense 'as close as it gets' experientially. So not-BIV is not tracked. This is precisely what allows the tracking theorist to preserve ordinary knowledge while denying closure."

- question: "If epistemic closure is valid and you cannot know you are not a brain in a vat, then you cannot know any ordinary propositions — accepting closure forces acceptance of skepticism."
  type: true-false
  answer: false
  explanation: "Closure combined with the inability to know not-BIV does yield the skeptical conclusion by modus tollens. But contextualism accepts closure while still preserving ordinary knowledge — by arguing that in ordinary contexts, you DO know not-BIV (because the BIV scenario is not a relevant alternative in that context). So closure is compatible with rejecting skepticism if knowledge is context-sensitive. Accepting closure does not force skepticism; it forces a choice between skepticism, denying closure, or contextualizing knowledge."

- question: "Why does the skeptical argument run the closure principle via modus tollens, and what does this reveal about the relationship between ordinary knowledge and knowledge of skeptical scenarios?"
  type: short-answer
  answer: "The argument runs: (1) You cannot know not-BIV. (2) If you knew H, closure would require you to know not-BIV (since H entails not-BIV). Therefore (3) you do not know H. This is modus tollens on closure: instead of transmitting knowledge forward from H to not-BIV, it transmits ignorance backward from not-BIV to H. This reveals that ordinary knowledge and knowledge of skeptical scenarios are not independent — closure links them. You cannot comfortably say 'I know I have hands' while also saying 'I have no idea whether I'm a brain in a vat,' because the first entails the second. Any theory of knowledge must explain why ordinary knowledge is secure despite the apparent impossibility of ruling out skeptical scenarios."
  explanation: "The modus tollens move is the argument's real bite. Closure was designed as a forward principle (knowledge transmits through deduction), but it cuts both ways. The skeptic uses it backward: inability to know the entailed conclusion infects knowledge of the premise. Solutions must either block the backward transmission (deny closure), accept it but limit its scope (contextualism), or accept the full skeptical conclusion."
```

## Explainer

From your study of external world skepticism, you know the basic skeptical problem: our sensory evidence is compatible with radically different underlying realities. From your study of epistemic closure, you know the principle: if you know P, and you know that P entails Q, then you know Q (or are in a position to know Q). Skeptical scenarios with closure arguments combine these into one of the sharpest challenges in epistemology. The argument goes quickly from ordinary common sense to apparent disaster.

Here is the core inference. You believe you have hands — you can see them, feel them, you've used them all your life. Call this belief H. Now consider a skeptical scenario: a **brain in a vat** (BIV), connected to a computer that produces perfectly coherent simulated experiences of having hands and a body. If you were a BIV, your experiences would be indistinguishable from your actual experiences. Now, H (I have hands) entails not-BIV (I am not a brain in a vat), because if you're a brain in a vat, you don't actually have hands. By closure, if you know H, you must know not-BIV. But can you know not-BIV? You have no experience or evidence that discriminates between the real-hands scenario and the BIV scenario. It seems you can't rule out BIV. Therefore, by **modus tollens** running the closure argument backwards, perhaps you don't know H either. The ordinary knowledge you took for granted is apparently undermined.

Three major response strategies have been developed. The first is **accepting skepticism**: bite the bullet and acknowledge that we don't know ordinary propositions in the strict philosophical sense. This is intellectually honest but practically bizarre — we can't operate as though we don't know we have hands. The second is **rejecting closure**: some philosophers (notably Fred Dretske and Robert Nozick) argue that knowledge does not transmit through entailment in this way. On a **tracking** account, you know H because your belief in H tracks the truth — you would not believe you have hands if you didn't. But you don't need your belief in not-BIV to track its truth. Knowledge can be compartmentalized. The third strategy is **contextualism**: what counts as "knowing" depends on the context of inquiry. In an ordinary conversation, saying "I know I have hands" is true; in a skeptical philosophical seminar where BIV scenarios are explicitly raised, the standards for "knowing" are elevated and the claim might be false. Knowledge attributions are context-sensitive, not absolute.

Your soft prerequisites in possible worlds semantics are useful here. Tracking accounts can be expressed in modal terms: you know P if there is no nearby possible world in which you falsely believe P. BIV worlds are not "nearby" in the relevant sense — they are highly unusual alternative scenarios, not close variations on your actual situation. This is why the tracking theorist can say: I know I have hands (no close world where I'm wrong about this), even though I don't know I'm not a BIV (the BIV world, though distant, is indistinguishable from this one and I couldn't detect the difference). The modal framework makes precise what "relevant alternatives" means and which possibilities must be eliminated for knowledge.

The philosophical importance of this topic extends beyond academic puzzle-solving. How you resolve the tension between closure and skeptical scenarios reveals your deeper commitments about what knowledge is for. If knowledge requires ruling out every logically possible alternative, it becomes unattainable. If it requires ruling out only practically relevant alternatives, it is attainable but the notion of "relevance" needs an account. The skeptical scenarios argument is a stress test: a theory of knowledge that cannot explain why ordinary people genuinely know they have hands, while also explaining why we cannot empirically rule out BIV scenarios, is in trouble. The solutions (denying closure, contextualizing knowledge, invoking possible worlds) are also the leading positive theories of knowledge in contemporary epistemology.

