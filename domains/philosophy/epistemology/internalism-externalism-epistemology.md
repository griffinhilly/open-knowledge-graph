---
id: internalism-externalism-epistemology
title: Internalism and Externalism in Epistemology
domain: philosophy
course: epistemology
prerequisites:
- id: justified-true-belief
  type: hard
builds-toward:
- reliabilism
tags:
- internal-states
- external-world
- justification-sources
stage: formal-systems
status: validated
---

# Internalism and Externalism in Epistemology

## Core Idea
Internalism holds that a belief's justification status depends only on the agent's internal mental states (introspectible reasons, experiences, coherence). Externalism allows justification to depend on external facts: the reliable origin of the belief, proper causal history, or conformity to the world. Formally: internalists quantify only over internal properties of the belief-forming process; externalists quantify over the actual world and its objective facts about reliability.

## Questions

```yaml
- question: "A person has a reliable clairvoyant faculty that genuinely gives accurate information about distant events. They form a belief about a distant city using this faculty, but have no evidence it is reliable and cannot explain why they believe what they do. Is this belief justified, and why do internalists and reliabilists disagree?"
  type: multiple-choice
  options:
    - "Both views agree the belief is justified, since the clairvoyant has access to the right information"
    - "Both views agree the belief is unjustified, since there is no causal pathway linking the belief to the facts"
    - "Reliabilists say the belief is justified because the faculty reliably produces true beliefs; internalists say it is not because the believer cannot access or articulate any reason for it"
    - "Internalists say it is justified because the belief is accurate; reliabilists say it is not because no formal verification was performed"
  answer: 2
  explanation: "The clairvoyant case is the sharpest test case in the internalism-externalism debate. The reliabilist says: justification is about whether the belief-forming process reliably produces true beliefs — and here it does — so the belief is justified regardless of whether the believer can access that reliability. The internalist says: justification requires that the believer have reasons they can recognize on reflection. Since the clairvoyant has no accessible evidence and cannot explain their belief, there are no internal justifying factors, and the belief is unjustified no matter how reliable the faculty actually is. Your intuitions about this case reveal which framework you implicitly adopt."

- question: "What is the central commitment of access internalism?"
  type: multiple-choice
  options:
    - "Justification depends only on the external facts about how the belief was formed — specifically whether it was formed through perception or testimony"
    - "A factor justifies a belief only if the believer can recognize on reflection that it is a reason for that belief — justification requires in-principle accessibility to the believer"
    - "Any belief that tracks the truth reliably is automatically justified, as long as the believer is in a normal environment"
    - "Justification is determined by whether the community of experts would endorse the belief-forming process"
  answer: 1
  explanation: "Access internalism holds that what makes a belief justified must be accessible to the believer through introspection or reflection. The motivation is epistemic responsibility: if you can be asked 'why do you believe that?' and are expected to produce reasons, then justification must consist of things you can in principle articulate. Factors that influence your belief but that you cannot recognize as reasons — like the reliability of an unconscious process — do not count as justifiers on this view. This preserves the intuition that justified belief is something you are responsible for in a way that unjustified belief is not."

- question: "On a reliabilist account, a belief formed through a process that reliably produces true beliefs is justified even if the believer cannot articulate why they hold it or explain the process that produced it."
  type: true-false
  answer: true
  explanation: "This is the defining claim of reliabilism, the most prominent externalist theory. Reliabilism locates justification in the objective track record of the belief-forming process, not in the believer's subjective evidence or self-knowledge. A person who accurately reads environmental cues they cannot explicitly describe, a child who forms correct beliefs through testimony without understanding what testimony is, or a person using perceptual faculties they have never analyzed — all count as having justified beliefs on a reliabilist view, as long as the underlying process reliably produces true beliefs. The believer's access to that reliability is irrelevant."

- question: "Internalists and externalists agree on what justification is but disagree mainly about which specific beliefs happen to be justified."
  type: true-false
  answer: false
  explanation: "The disagreement is far deeper than that — it is about what justification fundamentally is, not just which beliefs have it. Internalists hold that justification is constituted by internal, accessible mental states (reasons, evidence, coherence). Externalists hold that justification is constituted by objective, external facts about the belief-forming process (reliability, causal history, tracking truth). These are competing accounts of justification's nature, not competing lists of justified beliefs. Cases like the clairvoyant show they can give opposing verdicts on specific beliefs, precisely because they define justification differently."

- question: "A person raised in isolation develops highly accurate beliefs about animal behavior through unconscious pattern recognition they cannot consciously articulate. How would an internalist and a reliabilist each evaluate whether these beliefs are justified?"
  type: short-answer
  answer: "The reliabilist would say the beliefs are justified: the belief-forming process (unconscious pattern recognition) reliably produces true beliefs about animal behavior, and that is what justification consists in. The fact that the person cannot articulate their process is irrelevant to the reliabilist. The internalist would say the beliefs may not be justified: justification requires accessible reasons the believer can recognize on reflection. If the person cannot point to any reason for their belief — cannot say 'I believe this because I noticed X, Y, Z' — then there are no internal justifying factors, even if the belief happens to be accurate. The internalist might acknowledge the beliefs track truth but deny that this alone constitutes justification."
  explanation: "This case parallels both Spivak's native tribesperson example and the broader internalism-externalism debate. The key philosophical issue is whether epistemic responsibility (being able to answer 'why do you believe that?') is essential to justification, or whether justification is a more objective, third-personal property that you have or lack independent of self-awareness. The answer determines whether knowledge requires a reflective, self-knowing epistemic subject or merely a reliable truth-tracking system."
```

## Explainer

From your study of justified true belief, you know that knowledge requires more than accidentally true belief — the belief must be **justified**, held for the right reasons. But what exactly makes a belief justified? The internalism-externalism debate is about the location and nature of the justification-conferring factors. It is one of the deepest structural disputes in epistemology, and understanding it clarifies why seemingly similar accounts of knowledge have radically different implications.

**Internalism** holds that all justification-conferring factors are internal to the believer — accessible through introspection or reflection. If you're justified in believing it will rain, you are justified because you can be aware of your evidence: you see dark clouds, you remember a weather forecast, you feel the humidity. The justification lives in your mental states, and you could in principle articulate it. The clearest internalist doctrine is **access internalism**: a factor justifies your belief only if you can recognize, on reflection, that it's a reason for that belief. This preserves the intuition that justification is something you are epistemically responsible for — you can be asked "why do you believe that?" and expected to produce your reasons.

**Externalism** challenges this picture. Consider a native tribesperson who has no concept of thermometers, but who forms accurate beliefs about temperature by unconsciously reading subtle environmental cues — skin sensations, plant behaviors, animal sounds — that are in fact highly reliable temperature indicators. On an internalist view, this person's beliefs might not be justified, because they cannot articulate their reasons. Yet intuitively, the beliefs are not guesses; they reliably track the truth through a sophisticated information-processing system. **Reliabilism**, the most prominent externalist theory, says justification depends on whether the belief-forming process is reliable — actually produces a high ratio of true beliefs — regardless of whether the believer can access or articulate that reliability. What matters is not your subjective evidence but the objective track record of your belief-formation method.

The sharpest test case is the **Clairvoyant scenario**: imagine someone who has a reliable clairvoyant faculty — it truly does give them accurate information about distant events — but who has no evidence this faculty is reliable and no reason to trust it. The clairvoyant forms a belief with no accessible internal justification, but the belief is produced by a reliable process. Internalists say the clairvoyant is not justified — they have no reasons to trust this inexplicable feeling. Externalists (reliabilists) say they are justified, because justification is about reliable truth-tracking, not conscious access to reasons. Your intuitions about this case reveal your implicit commitments.

There are hybrid positions. **Weak internalism** requires only that justifying factors not be inaccessible, not that the believer actually access them. **Virtue epistemology** tries to integrate both: knowledge requires reliable faculties (externalist) that are also characteristically exercised well by the agent (internalist-adjacent). The debate matters practically because it determines whether epistemic responsibility and self-knowledge are essential to justified belief, or whether justification is a more objective, third-personal property — something you either have or lack based on how the world is, independently of your self-awareness.

