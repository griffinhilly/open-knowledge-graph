---
id: luminosity-introspection
title: Luminosity and the KK Principle
domain: philosophy
course: epistemology
prerequisites:
- id: justified-true-belief
  type: soft
- id: higher-order-evidence-justification
  type: hard
tags:
- luminosity
- introspection
- KK-principle
- higher-order
- williamson
stage: formal-systems
status: draft
---

# Luminosity and the KK Principle

## Core Idea
The luminosity thesis holds that whenever one has a mental state, one is in a position to know that one has that state. Closely related is the KK principle: if you know something, you know that you know it. Williamson argues both principles face insurmountable obstacles given the margin-for-error account of knowledge and the vagueness of mental state boundaries.

## How It's Best Learned
Test luminosity with subtle mental state differences: can you always detect when you're certain versus almost certain? When you believe something, are you always positioned to know you believe it? Examine Williamson's margins-for-error argument against these principles.

## Common Misconceptions
- Rejecting luminosity doesn't mean introspection is entirely unreliable. - The KK principle is stronger than simple reflection; it requires knowledge of knowledge, not just awareness. - Luminosity concerns only whether one is 'in a position' to know; it doesn't claim such knowledge is easily obtained.

## Questions

```yaml
- question: "Williamson's argument against luminosity relies on which key feature of mental states?"
  type: multiple-choice
  options:
    - "Mental states are completely inaccessible to introspection in all cases"
    - "Mental states change gradually, so at any boundary point nearby situations include states where the belief is wrong"
    - "Mental states are too fast-changing for the brain to track accurately"
    - "Introspection requires language, but mental states are pre-linguistic"
  answer: 1
  explanation: "Williamson's margins-for-error argument targets the gradual nature of mental state change. Consider warmth: as you cool imperceptibly, at every point your current feeling is so similar to adjacent moments that knowing you feel warm would require being reliably right in nearby situations — but in nearby situations you no longer feel warm. Knowledge requires safety (being right not just now but in nearby cases), and gradual change guarantees nearby cases where your belief would be wrong. This argument applies to any mental state that can change gradually."

- question: "You are experiencing a slowly decreasing level of warmth, imperceptible from moment to moment. At the threshold between 'warm' and 'not warm,' Williamson's argument says you cannot know you feel warm. The best explanation for this is:"
  type: multiple-choice
  options:
    - "You are temporarily unconscious at the threshold and cannot form beliefs"
    - "The concept of 'warm' is too vague to have a determinate truth condition"
    - "Knowledge requires a margin for error — nearby situations are ones where you're no longer warm but still believe you are"
    - "At the threshold, the feeling itself does not exist and so cannot be known"
  answer: 2
  explanation: "Williamson's key move is the margin-for-error requirement: you know P only if, in situations relevantly similar to the current one, you would still believe P and it would still be true. At the threshold of warmth, the immediately adjacent moments are ones where you are no longer warm — but by hypothesis, you cannot detect the difference, so you still believe you are warm. This means your belief is unsafe: nearby it is false while you still hold it. Therefore it doesn't qualify as knowledge, even though in this very moment it happens to be true."

- question: "Rejecting luminosity entails that introspection is entirely unreliable and provides no epistemic access to one's own mental states."
  type: true-false
  answer: false
  explanation: "This is an overreaction that Williamson explicitly avoids. Rejecting luminosity means only that introspection is not *infallible* or *perfectly privileged* — it is subject to the same kinds of margins-for-error and reliability constraints as perception. Introspection can still be a generally reliable guide to one's mental states without being an authoritative, error-proof source. The result is that self-knowledge is more like perceptual knowledge than traditional epistemology assumed, not that it is useless."

- question: "The KK principle states: if you know that P, then you know that you know that P."
  type: true-false
  answer: true
  explanation: "This is the correct statement of the KK principle. It says epistemic states are transparent: knowing P automatically puts you in a position to know your own knowledge state. Williamson's argument against KK parallels his luminosity argument — knowing that you know requires satisfying the conditions for knowledge at a higher order, and the margin-for-error argument shows those conditions may fail even when first-order knowledge obtains. The KK principle fails for the same reason luminosity fails: safety conditions at the second order are not automatically satisfied by safety conditions at the first."

- question: "Why does Williamson use a case of gradually changing mental states (like slowly cooling down) to argue against luminosity, rather than focusing on cases of dramatic mental state change?"
  type: short-answer
  answer: "Gradual change is what generates the margin-for-error problem. If states changed abruptly, there would be a clear before-and-after with no ambiguous intermediate cases. But with imperceptible gradual change, at every moment your current state is extremely similar to the adjacent moments — some of which have crossed the threshold. Knowledge requires safety (being right in nearby situations), and gradual change ensures that nearby situations include ones where the state has changed but your belief hasn't. Cases of dramatic change wouldn't create this structural problem."
  explanation: "The force of the argument depends on the inability to detect fine-grained differences. The gradual-change scenario creates a series of adjacent cases across which the mental state shifts while the introspective belief stays constant — and this is exactly what knowledge requires you not to do. Williamson's genius is recognizing that this pattern is not a special edge case but a structural feature of any mental state that admits of degrees, which is most of them."
```

## Explainer

The **luminosity thesis** captures an intuitive picture of the mind as self-transparent: mental states are "lit from within," fully available to the subject who has them. Whenever you are in pain, you know you are in pain. Whenever you believe something, you know you believe it. Whenever you feel certain, you know you feel certain. This seems to capture something important about the first-person perspective — unlike the external world, where evidence can be misleading or incomplete, your own mental states seem directly accessible in a way nothing else is. The closely related **KK principle** (if you know P, you know that you know P) extends this to knowledge itself: your epistemic states are also transparent to you.

Your background in justified true belief gives you the resources to see why luminosity is philosophically significant. If knowledge requires justification, and you can always know whether you have a mental state, then your beliefs about your own mental states are always justified from the inside. This would mean introspection is a privileged epistemic method — not infallible, perhaps, but systematically more reliable than perception of the external world. Many traditional epistemological frameworks assume something like this: Descartes' cogito and Locke's inner sense both presuppose that the mind has special access to itself. Luminosity is the contemporary formulation of this assumption.

Timothy **Williamson's** argument against luminosity in *Knowledge and Its Limits* (2000) is the most influential challenge. He uses a **margins-for-error** argument built on the gradual change of mental states. Consider warmth: imagine you cool down very slowly over many hours, one imperceptible degree at a time. At the start you feel warm; at the end you feel cold. At every intermediate point, your feeling is so close to the adjacent states that you cannot reliably distinguish "I feel warm" from "I feel slightly-less-warm-than-warm." Williamson argues that knowledge requires a safety margin — you can only know P if, in nearby possible situations, you also believe P and it is true. But given the gradual change, at every point where you believe you feel warm, nearby situations include ones where you no longer feel warm but still believe you do. So you never *know* that you feel warm; you only believe it. Since this argument applies to any gradually-changing mental state, luminosity fails generally.

The implications are striking: your higher-order evidence about your own mental states is not automatically authoritative. You might believe you are certain of something when you are actually only fairly confident; you might believe you are experiencing pain when you are experiencing something that would not quite count. This does not mean introspection is worthless — it means introspection is more like perception than traditional epistemology assumed, subject to the same kinds of margins for error and reliability constraints. The KK principle falls for the same reason: knowing P does not guarantee knowing you know P, because the standards for second-order knowledge may not be met even when first-order knowledge is. The luminosity debate thus reopens questions about what is distinctive about self-knowledge and whether the first-person perspective really does carry any special epistemic privilege.
