---
id: reliabilism
title: Process Reliabilism
domain: philosophy
course: epistemology
prerequisites:
- id: justified-true-belief
  type: hard
- id: gettier-problems
  type: soft
- id: foundationalism
  type: soft
- id: epistemic-luck
  type: soft
- id: responses-to-gettier
  type: soft
builds-toward:
- internalism-vs-externalism
- epistemic-virtues
tags:
- reliabilism
- Goldman
- process
- externalism
- generality-problem
stage: formal-systems
status: validated
---
# Process Reliabilism

## Core Idea
Alvin Goldman's process reliabilism holds that a belief is justified if and only if it is produced by a reliable cognitive process — a process that tends to produce true beliefs in the actual world and in nearby possible worlds. Perception, memory, and valid deductive inference count as reliable processes; wishful thinking, astrology, and hasty generalization do not. Reliabilism is an externalist theory: the agent need not be aware that the process is reliable for the belief to count as justified. This approach promises to handle Gettier cases (Gettier beliefs arise from processes that fail to reliably track truth in the relevant case) and explain why children and animals can have knowledge.

## How It's Best Learned
Apply reliabilism to a range of cases: perceptual beliefs, clairvoyance, testimony, inference to the best explanation. The generality problem — how to individuate the relevant process type — is the central technical challenge to work through.

## Common Misconceptions
- Reliabilism does not say that a reliable process must succeed in every case, only that it has a sufficiently high success rate in the relevant reference class.
- The generality problem is not solved by appealing to common sense; it requires a principled criterion for which process description is the relevant one.

## Questions

```yaml
- question: "Maria grew up in a normal environment and forms accurate visual beliefs about her surroundings. She has never studied optics or cognitive science and cannot explain why vision is reliable. According to reliabilism, are her visual beliefs justified?"
  type: multiple-choice
  options:
    - "No — she cannot articulate reasons or evidence for her beliefs, so they lack justification by definition"
    - "Yes — if her visual system reliably produces true beliefs, the beliefs are justified regardless of whether she can access or explain the reliability facts"
    - "Only partially — she needs at least some introspective awareness of what makes her perception reliable"
    - "No — justification requires that the believer be able to provide a defense of their belief if challenged"
  answer: 1
  explanation: "This is the core externalist claim of reliabilism: justification is constituted by the actual relationship between the cognitive process and truth, not by what the believer can introspect or articulate. Maria's visual system reliably tracks features of her environment — that fact holds regardless of whether she knows it. Options A, C, and D all require the believer to have internal access to something (reasons, evidence, awareness, the ability to defend). These are internalist requirements that reliabilism explicitly rejects. Externalism explains how children and animals can have justified beliefs without any capacity for epistemic self-reflection."

- question: "The generality problem challenges reliabilism because:"
  type: multiple-choice
  options:
    - "Reliable processes sometimes produce false beliefs, which shows reliability isn't sufficient for justification"
    - "Any token belief-forming event can be described at many levels of generality — different descriptions yield different reliability assessments, and reliabilism provides no principled way to pick the right one"
    - "Reliabilism cannot explain how we know which of our cognitive processes to trust without circular reasoning"
    - "The theory depends on possible-worlds semantics, which cannot be empirically verified"
  answer: 1
  explanation: "The generality problem arises because process types are not given by nature — they are individuated by description. My current visual belief was produced by 'using perception,' 'using vision in good lighting,' 'using vision while wearing my glasses,' 'using vision in this room on this day,' etc. These differ in reliability: 'perception in general' is highly reliable; 'perception under these specific unusual conditions' might not be. Without a principled criterion for which description is the relevant one, reliabilism cannot deliver a determinate verdict on whether any particular belief is justified. This is a technical gap in the theory, not necessarily a fatal refutation."

- question: "Reliabilism is an internalist theory of justification because it focuses on the reliability of cognitive processes, which the believer can introspect and verify."
  type: true-false
  answer: false
  explanation: "Reliabilism is explicitly externalist. Justification depends on whether the belief-producing process is actually reliable in the world — a fact the believer need not and often cannot access. Goldman's own examples make this clear: a clairvoyant who produces reliably true beliefs about distant events is justified (on reliabilism) even if she doesn't know why she has these beliefs or what process produces them. This contrasts with internalist theories (like classical foundationalism or coherentism) that require justification to supervene on facts the believer can in principle recognize from their first-person perspective."

- question: "Process reliabilism can in principle explain why both a child perceiving the world accurately and a logician applying valid deductive inference both count as having justified beliefs, because in both cases the relevant cognitive process tends to produce true beliefs."
  type: true-false
  answer: true
  explanation: "This is one of reliabilism's genuine advantages over internalist theories. The child's perceptual system reliably tracks environmental features even though the child cannot articulate why. The logician's deductive inference preserves truth necessarily (if premises are true and the inference valid, the conclusion must be true — maximum reliability). Both processes satisfy the reliability criterion. Classical internalist accounts struggled with children and animals because they couldn't provide reasons or engage in epistemic reflection; reliabilism handles both naturally by shifting focus from the believer's introspective access to the actual truth-tracking properties of the process."

- question: "What does it mean to say that reliabilism is an 'externalist' theory of justification, and why is this a departure from classical accounts like foundationalism?"
  type: short-answer
  answer: "Externalism means that the facts that constitute justification — specifically, whether the belief-forming process is reliable — are not required to be accessible to the believer from their first-person perspective. A belief can be justified even if the believer has no idea that the process that produced it is reliable. Classical foundationalism is internalist: it requires that basic beliefs be self-evident or incorrigible to the believer, and that inferential beliefs trace their justification to foundations the believer can recognize. Reliabilism replaces this first-person accessibility requirement with a third-person, world-involving condition: does the process actually track truth?"
  explanation: "The externalist move is motivated by real problems with internalism. Internalism struggles to explain animal and infant knowledge (they can't access justificatory reasons), and it risks skeptical regress (how do you justify your justifiers?). By grounding justification in the actual reliability of processes rather than in the believer's reflective access, reliabilism avoids these problems. The trade-off is that reliability is a fact about the external world, raising new questions: reliable in what environment? Across what reference class of situations? These questions animate the generality problem and subsequent reliabilist literature."
```

## Explainer

From your work on **justified true belief**, you know the classical account: knowledge is believing something true for good reasons. From **Gettier problems**, you know that account fails because good reasons can lead to true beliefs by accident. Various **responses to Gettier** tried to patch the definition — adding a "no false lemmas" clause, requiring causal connections to the fact — but each patch faced new counterexamples. **Process reliabilism**, developed by Alvin Goldman, steps back and asks a different question: instead of analyzing what makes a *belief* justified, what makes the *cognitive process that produced it* a good one?

Goldman's answer is **reliability**: a cognitive process is epistemically good if it tends to produce true beliefs. Perception counts — your visual system reliably tracks features of the physical environment. Memory counts — it reliably preserves information about your past experiences. Valid deductive inference counts — if your premises are true and the inference is valid, the conclusion must be true; reliability is maximal. What doesn't count: wishful thinking (wanting something to be true is no guide to whether it is), reading horoscopes, or forming beliefs through pure random guessing. These processes have low truth-producing ratios in the actual world, so beliefs produced by them lack justification.

The critical innovation is **externalism**: you don't have to know that your belief-forming process is reliable for your belief to be justified. A child who forms accurate perceptual beliefs doesn't need to understand optics or neuroscience; a dog that correctly identifies its owner doesn't need to reflect on the reliability of its nose. Justification is constituted by the actual relationship between the process and truth — it's a fact about the world, not about what the agent can introspect. This contrasts with **internalist** theories (like classical foundationalism), which require justification to be accessible from the agent's first-person perspective. Internalism struggled to explain how children and animals could count as knowing anything; reliabilism handles them naturally.

The main technical challenge for reliabilism is the **generality problem**: every token belief is produced by a process that can be described at many levels of generality. My current visual belief was produced by "using my eyes," but also by "using my eyes in good lighting," and also by "using my eyes while sitting in this chair in this building on this day." Which description picks out the relevant process type for evaluating reliability? "Using eyes" is reliable; "using eyes under certain specific conditions on a specific day" might be reliable or unreliable depending on how narrowly we define it. There is no principled answer that Goldman's original formulation provides. This doesn't refute reliabilism, but it means the theory is incomplete until we can say, non-arbitrarily, which process description is the right one to evaluate. Working through this problem is the central task of reliabilist epistemology beyond the introductory level.
