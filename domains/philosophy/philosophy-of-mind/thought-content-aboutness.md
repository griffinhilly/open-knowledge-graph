---
id: thought-content-aboutness
title: 'Mental Content and Aboutness: What Makes Thoughts About Things'
domain: philosophy
course: philosophy-of-mind
prerequisites:
- id: intentionality
  type: hard
- id: intentionality-aboutness
  type: hard
- id: content-externalism-individuation
  type: soft
builds-toward:
- representationalism
- semantic-content-externalism
tags:
- intentionality
- content
- representation
- meaning
- aboutness
stage: advanced
status: draft
---

# Mental Content and Aboutness: What Makes Thoughts About Things

## Core Idea
The fundamental question of mental content is: what makes a thought about the Eiffel Tower rather than something else? Competing accounts exist—causal theories (thoughts are about what causes them), teleosemantic theories (thoughts are about what they evolved to represent), and externalist theories (thoughts get content from environment).

## Questions

```yaml
- question: "You see a wolf in dim light and mistake it for a dog. Your dog-concept fires. On a naive causal theory, what does your thought represent at that moment?"
  type: multiple-choice
  options:
    - "Dogs — the causal history of the concept (being caused by dogs in the past) fixes its content"
    - "Wolves — what actually caused the concept to fire on this occasion determines its content"
    - "Dogs-or-wolves — the concept must represent the disjunction of everything that has ever caused it to fire"
    - "Nothing — mental states that misfire have no content"
  answer: 2
  explanation: "This is the 'disjunction problem' that bedevils causal theories. If content is fixed by current cause, misrepresentation is impossible (the wolf-caused thought represents wolves correctly). If content is fixed by original cause, then anything that happens to trigger the concept gets added to the content — giving an expanding disjunction. Neither option allows genuine misrepresentation where the content is 'dog' but what is present is a wolf. Solving this problem — allowing error — is the central challenge for theories of mental content."

- question: "A frog's bug-detection system fires at a black pellet rather than a fly. On a teleosemantic theory, what does the frog's neural state represent?"
  type: multiple-choice
  options:
    - "The black pellet — that is what caused the state on this occasion"
    - "Bugs — that is what the system evolved to track, fixing content independently of what caused it this time"
    - "Nothing — the state is misfiring and therefore has no representational content"
    - "Both bugs and pellets, since both reliably cause the system to fire"
  answer: 1
  explanation: "Teleosemantic theories (Millikan, Papineau) fix content through *proper function* — what the mechanism was selected to do over evolutionary history — rather than actual causes. The system was selected because it caught flies, so it represents flies. The pellet-firing is a misrepresentation: the state is about flies but was caused by a pellet. This allows genuine error, which is what simple causal theories struggle to accommodate. The cost is that content is sensitive to evolutionary history rather than current functional role."

- question: "A simple causal theory of mental content easily explains how mental states can misrepresent the world."
  type: true-false
  answer: false
  explanation: "Misrepresentation is the central challenge for causal theories. If a mental state represents X because X causes it, then a state caused by Y represents Y — not X — making error impossible by definition. The wolf-for-dog case shows the problem: the thought seems to misrepresent (it's about dogs but was caused by a wolf). Getting misrepresentation right requires either pointing to historical/evolutionary causes (teleosemantics) or to the external environment independently of individual causal history (externalism)."

- question: "Externalist theories of content hold that what a thought is about can depend on facts about the external environment, even facts the thinker does not know."
  type: true-false
  answer: true
  explanation: "This is the core externalist claim, drawing on Putnam and Burge. Your 'water' thought is about H₂O — not just about a clear drinkable liquid — partly because of what water actually is in your environment, regardless of whether you know any chemistry. Twin Earth thought experiments show that two people with qualitatively identical internal states can have thoughts with different content if their environments contain different substances. Content is 'wide': it extends beyond the skull."

- question: "Why is the possibility of misrepresentation a problem for causal theories of mental content, and what is the disjunction problem?"
  type: short-answer
  answer: "A causal theory says a mental state represents X if X causes it. But when I mistake a wolf for a dog, my dog-concept fires while being caused by a wolf. Two options: (1) Current cause fixes content — the thought represents the wolf, so I'm not misrepresenting anything; error disappears. (2) Historical causes fix content — the concept represents everything that has ever caused it (dogs, wolves, dim-light animals...), giving a widening disjunction as content rather than a specific object. Either way, genuine misrepresentation of a specific thing becomes impossible. This is the disjunction problem: content collapses into a disjunction or error becomes incoherent."
  explanation: "Both horns are unacceptable: the first denies that we ever have false beliefs; the second means concepts don't have determinate content. Teleosemantics and externalism each try to solve this by appealing to something other than token causal history — evolutionary function or broad environmental facts — to ground determinate content and genuine error."
```

## Explainer

From your study of intentionality, you know that mental states have **aboutness** — they are directed toward objects, properties, and states of affairs. A belief is always a belief *that* something, a desire is always a desire *for* something. But intentionality raises an immediate puzzle: what in the physical world could possibly constitute this directedness? What makes a neural state be *about* Paris rather than about Buenos Aires, or about nothing at all?

The **causal theory of content** offers the most intuitive starting point: a mental state represents X if X is what reliably causes that state. If your "dog"-concept fires in the presence of dogs, then dogs are what it represents. This captures something right — we do expect content to track the environment — but it faces the **problem of misrepresentation**. If a thought can be *wrong*, then a mental state can occur without its normal cause. When you mistake a wolf for a dog, your dog-concept fires, but what causes it is a wolf. Does your thought therefore represent wolves? If content is fixed by what actually causes the state on a given occasion, there can be no such thing as error, which is clearly absurd.

**Teleosemantic theories** (Ruth Millikan, David Papineau) solve misrepresentation by shifting from actual causes to *proper functions* — what a state was selected to do over evolutionary or developmental history. A frog's tongue-snapping mechanism was selected because it caught flies; that is what it *represents*, even when it misfires and snaps at a pellet of black paper. Error is now possible: the mechanism misrepresents when it fires without its historically normal cause. The cost is that content becomes sensitive to evolutionary history in ways that seem remote from ordinary thought — and it is unclear whether the theory extends to learned concepts and complex propositional thought without becoming ad hoc.

**Externalist theories** (building on Putnam and Burge, which you may have encountered) argue that content is fixed not just by internal causal history but by the nature of the external environment. What your "water" thought is about is partly fixed by what water actually *is* — H₂O — regardless of whether you know chemistry. These three families of theory are not mutually exclusive; most contemporary philosophers draw on causal, functional, and environmental factors in combination. The theoretical terrain here connects directly to debates about **narrow vs. wide content**: whether mental content can be specified purely by internal states, or whether it essentially involves the world beyond the skin.
