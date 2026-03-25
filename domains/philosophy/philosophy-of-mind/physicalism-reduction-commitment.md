---
id: physicalism-reduction-commitment
title: 'Physicalism: The Core Thesis'
domain: philosophy
course: philosophy-of-mind
prerequisites:
- id: mind-body-problem-formulation
  type: hard
- id: physicalism-about-mind
  type: soft
- id: emergence-reduction-consciousness
  type: soft
- id: token-identity-theory
  type: soft
builds-toward:
- reductive-physicalism-theory
- non-reductive-physicalism-details
- eliminative-materialism
tags:
- physicalism
- materialism
- reduction
stage: formal-systems
status: validated
---
# Physicalism: The Core Thesis

## Core Idea
Physicalism asserts that everything, including mental phenomena, is ultimately physical. The core commitment is that there are no non-physical substances or irreducible non-physical properties, though physicalists differ on whether mental properties can be reduced to neural or functional properties.

## Questions

```yaml
- question: "A philosopher claims mental properties are real and causally efficacious, but cannot be defined in terms of or identified with physical properties. What is the strongest objection to this position?"
  type: multiple-choice
  options:
    - "It implicitly denies that brain states cause behavior, which is empirically false"
    - "If physical causation is closed, mental properties appear to do no additional causal work and become epiphenomenal"
    - "It commits to substance dualism, which has already been empirically refuted"
    - "It cannot explain why mental vocabulary is useful if it doesn't reduce to physics"
  answer: 1
  explanation: "This describes non-reductive physicalism, and the causal exclusion problem is its sharpest challenge. If every physical effect has a sufficient physical cause (causal closure of the physical), then a distinct mental property can't add further causal contribution without overdetermination. Mental properties appear epiphenomenal — present but causally idle. Option A misreads the position; option C confuses non-reductive physicalism with dualism (it accepts supervenience); option D is a weaker concern."

- question: "Which of the following best distinguishes type identity theory from token identity theory?"
  type: multiple-choice
  options:
    - "Type identity allows multiple realizability; token identity does not"
    - "Token identity identifies each particular mental event with some physical event, while type identity identifies entire mental categories with physical types"
    - "Type identity is a form of dualism; token identity is a form of physicalism"
    - "Token identity requires mental descriptions to be eliminated in favor of neural ones; type identity does not"
  answer: 1
  explanation: "Token identity holds that each individual mental event (my specific pain right now) is identical to some physical event, but different instances of the same mental type may correspond to different physical types — permitting multiple realizability. Type identity makes the stronger claim: the mental type 'pain' as such is identical to a physical type like 'C-fiber firing,' so every instance of pain must be that neural state. Only token identity accommodates the fact that pain appears to occur in organisms with very different neural architectures."

- question: "Supervenience alone — the claim that there can be no mental difference without a physical difference — commits a physicalist to the view that mental properties are identical to physical properties."
  type: true-false
  answer: false
  explanation: "Supervenience is the weakest form of physicalism. It says mental facts track physical facts but is compatible with mental properties being genuinely distinct from physical properties — just dependent on them. Non-reductive physicalists accept supervenience while denying reduction or identity. Identity is a much stronger claim: two things that are identical are literally the same thing. Supervenience only requires dependence, not sameness."

- question: "Type identity theory predicts that pain in a human and pain in an octopus must involve literally the same neural state."
  type: true-false
  answer: true
  explanation: "Type identity theory holds that each mental type is numerically identical to a physical (neural) type — just as 'water' and 'H₂O' refer to the same substance. If pain = C-fiber firing, then any creature in pain must have C-fibers firing. But octopuses, humans, and hypothetical silicon systems have radically different substrates. This is precisely why multiple realizability is such a damaging objection to type identity: it seems implausible that all these realizations share a common neural type."

- question: "What is the causal exclusion problem, and why does it specifically threaten non-reductive physicalism rather than physicalism in general?"
  type: short-answer
  answer: "If physics is causally closed — every physical effect has a sufficient prior physical cause — then mental properties that are distinct from physical properties cannot do additional causal work without overdetermination. Non-reductive physicalism accepts supervenience (mental depends on physical) but denies identity (mental ≠ physical). This leaves mental properties causally redundant: everything the mental would cause is already fully caused by its physical base. Reductive physicalists dissolve the problem by identifying the mental with the physical; eliminativists dissolve it by denying mental properties exist."
  explanation: "The problem targets the specific combination of claims non-reductive physicalism holds: physical causal closure + irreducibility of mental properties. Either commitment alone is fine; holding both simultaneously creates the tension. The reductive physicalist and eliminativist each escape by abandoning one of the commitments the non-reductive physicalist insists on keeping."
```

## Explainer

Physicalism is the default ontological commitment of modern science: the world is exhausted by physical facts, and anything real — tables, cells, economies, minds — is ultimately constituted by physical entities following physical laws. The philosophical interest lies in what "ultimately physical" actually requires. The weakest version demands only **supervenience**: there can be no mental difference without a physical difference. If two possible worlds are physically identical, they must be mentally identical too. This is a constraint on dependence — mental facts track physical facts — without requiring that mental descriptions be translatable into physical ones.

Your prerequisite — the **mind-body problem** — already established why this commitment is harder to honor than it looks. Physical description, in its most austere form, talks about mass, charge, position, momentum, and their relations. Mental description talks about beliefs, desires, pains, and experiences. The philosophical challenge is explaining how mental facts can be nothing over and above physical facts when the two vocabularies seem so different. Physicalists propose several strategies, and understanding their differences is crucial for subsequent work.

**Type identity theory** is the strongest reductive form: every mental type (pain, belief, desire) is numerically identical to a neural type (C-fiber firing, such-and-such activation pattern). This predicts that mental terms and neural terms co-refer — just as "water" and "H₂O" co-refer — and thus licenses elimination or replacement of mental vocabulary in favor of neural vocabulary. The problem is **multiple realizability**: pain is realized in humans, octopuses, and possibly silicon systems, all of which differ dramatically in their neural (or non-neural) substrate. It seems wrong that all these realizations share a common neural type. **Token identity theory** weakens the claim: each particular mental event is identical to some physical event, but different instances of the same mental type may be different physical types. This permits multiple realizability but sacrifices the explanatory promise of type-level reduction.

**Non-reductive physicalism** accepts supervenience while denying that mental properties reduce to physical properties. Mental properties are real and causally efficacious, but they are not identical to nor definable in terms of physical properties. This position faces the **causal exclusion problem**: if a physical event is fully causally explained by prior physical events (as physicalism implies), how can the mental properties of those events do any additional causal work? The mental seems causally redundant — epiphenomenal in all but name. Physicalists like Jaegwon Kim have pressed this problem hard, arguing that non-reductive physicalism cannot be stably held. The alternatives are reductive physicalism (accept reduction) or eliminativism (deny that mental vocabulary tracks anything real). These positions form the landscape you will chart in subsequent topics on reductive and non-reductive physicalism.
