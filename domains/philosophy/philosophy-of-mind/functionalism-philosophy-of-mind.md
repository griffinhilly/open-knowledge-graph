---
id: functionalism-philosophy-of-mind
title: Functionalism
domain: philosophy
course: philosophy-of-mind
prerequisites:
- id: philosophical-behaviorism
  type: hard
- id: identity-theory
  type: hard
- id: physicalism-about-mind
  type: soft
- id: church-turing-thesis
  type: soft
- id: lambda-calculus
  type: soft
- id: computability-models-equivalence
  type: soft
builds-toward:
- multiple-realizability
- chinese-room-argument
- turing-test-and-machine-minds
- extended-mind-thesis
- eliminative-materialism
tags:
- functionalism
- Putnam
- Turing
- computational
- mental-states
stage: advanced
status: validated
---

# Functionalism

## Core Idea
Functionalism, developed by Hilary Putnam and others in the 1960s, holds that mental states are defined by their functional roles — their causal relations to sensory inputs, behavioral outputs, and other mental states — rather than by their physical constitution. Pain is whatever state is caused by tissue damage, causes distress and avoidance behavior, and interacts with beliefs and desires in characteristic ways. Because the functional role is what matters, mental states can in principle be realized by any physical (or non-physical) substrate that plays the right causal role, making functionalism compatible with strong AI and multiple realizability.

## How It's Best Learned
Use the analogy of software and hardware: the same program can run on different physical machines. Functionalism says mental states stand to brain states as software stands to hardware. Then examine whether this analogy holds under pressure from consciousness objections (qualia, the Chinese Room).

## Common Misconceptions
- Functionalism is not the claim that minds are computers; it is the claim that mental states are individuated by causal/functional role, of which computation is one possible implementation.
- Functionalism does not entail that consciousness is explainable in functional terms; this is precisely what critics like Chalmers deny.

## Questions

```yaml
- question: "Functionalism's key advantage over identity theory is that it:"
  type: multiple-choice
  options:
    - "Identifies mental states with specific brain states, enabling precise neuroscientific investigation"
    - "Allows that the same mental state type could be realized by physically very different systems"
    - "Holds that mental states are just dispositions to behave, eliminating appeal to inner states"
    - "Proves that artificial intelligence must eventually be conscious"
  answer: 1
  explanation: "Identity theory (type physicalism) says mental state types are identical to brain state types, implying only creatures with that specific brain structure can have those mental states. Functionalism avoids this by saying what defines a mental state is its causal/functional role, which could be realized by any system — silicon chips, octopus neurons, human neurons — that plays the right role. This is multiple realizability, functionalism's main advantage over identity theory."

- question: "Functionalism entails that any machine that reliably produces outputs matching human responses to all inputs must be conscious."
  type: true-false
  answer: false
  explanation: "This is precisely what critics like Searle (Chinese Room) and Chalmers (hard problem) deny. Functionalism defines mental states by their causal/functional role, but consciousness — qualia, subjective experience — may not be fully captured by functional description alone. A system could fulfill all functional criteria while there is 'nothing it is like' to be that system. Functionalism's relationship to consciousness remains contested."

- question: "What does the software/hardware analogy explain about functionalism's claim regarding multiple realizability?"
  type: short-answer
  answer: "The analogy holds that mental states stand to brain states as software stands to hardware: the same program (functional organization) can run on different physical machines. Multiple realizability says the same mental state type can be implemented in different physical substrates — human neurons, octopus neurons, or silicon chips — so long as all play the same functional role."
  explanation: "A word processor doesn't care whether it runs on a Mac or a PC; what matters is that the hardware implements the correct functional operations. Functionalism applies the same logic to minds: what makes a state 'pain' is not the specific neuron type but the functional role (caused by damage, causes avoidance, etc.). This is why functionalism opened philosophy of mind to the serious possibility of artificial minds."
```

## Explainer

When you studied behaviorism, you encountered the view that mental states are just behavioral dispositions — to say someone is in pain is just to say they tend to wince, withdraw, and say "ouch." When you studied identity theory, you encountered the view that mental states are identical to specific brain states — pain just *is* a particular type of C-fiber firing. Functionalism emerged as a synthesis and improvement on both: it accepts behaviorism's insight that mental states are characterized by their role, but grounds that role in *internal* causal structure, not just external behavior. And it accepts identity theory's insight that mental states are physically realized, without requiring that they be realized in one specific physical way.

The core functionalist idea is that mental states are defined by **what they do**, not **what they are made of**. Pain, for example, is whatever state is typically caused by tissue damage, causes distress and avoidance behavior, causes the belief that something is wrong, and motivates the desire for relief. If something plays that exact causal role — in your neurons, in an octopus's neurons, or in principle in a future computer — it qualifies as pain. The identity theorist would say only creatures with the right neurochemistry can feel pain; the functionalist says the neurochemistry is just one way to implement the relevant causal role.

Hilary Putnam developed the **software/hardware analogy** to make this vivid. A chess program doesn't care whether it runs on a 1970s mainframe or a modern laptop; what matters is that the machine correctly implements the program's logical structure. Mental states, on this view, are like programs — abstract functional descriptions that can be realized in different physical substrates. This is why functionalism opened the door to taking artificial intelligence seriously as a route to genuine minds: if minds are functional organizations, then any system that instantiates the right organization in principle has a mind.

Functionalism also faces serious challenges that you will explore in coming topics. The most powerful involves **qualia** — the subjective, felt quality of experience. Block's "absent qualia" thought experiment asks you to imagine the entire population of China organized to implement the functional organization of a human brain: is there anything it is like to be that system? Most people's intuition is no, which suggests that functional role may not be sufficient for consciousness. These objections motivate the Chinese Room argument and Chalmers's hard problem of consciousness, both of which accept the functionalist account of cognition while questioning whether it captures experience.

A final distinction worth keeping sharp: functionalism is **not** the claim that minds are computers. It is the claim that mental states are individuated by their causal roles — computation is one possible implementation of those roles, not the definition of them. A society of neurons implementing pain is doing something computational in a loose sense, but functionalism would apply equally to a hydraulic system or an alien biology that played the same causal role. This generality is functionalism's strength, and also the source of the hardest questions it must answer.
