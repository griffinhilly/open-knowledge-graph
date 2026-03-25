---
id: narrow-intrinsic-content-mind
title: Narrow Content and Intrinsic Mental Properties
domain: philosophy
course: philosophy-of-mind
prerequisites:
- id: content-externalism-individuation
  type: hard
- id: semantic-content-externalism
  type: soft
- id: de-re-attitudes
  type: soft
- id: intentionality-semantic-content-mind
  type: soft
- id: thought-content-aboutness
  type: soft
- id: biosemantics-evolutionary-content
  type: soft
- id: consciousness-and-representation
  type: soft
builds-toward:
- representationalism
- computational-theory-of-mind
tags:
- content
- intentionality
- semantics
- internal-properties
- representation
stage: formal-systems
status: validated
---
# Narrow Content and Intrinsic Mental Properties

## Core Idea
Narrow content is meaning a mental state has from intrinsic physical/neural properties alone, independent of external environment. Wide content depends on external factors. This distinction matters for computational theories (assuming narrow internal content) yet content also depends on causal connections to the world.

## Questions

```yaml
- question: "Oscar is on Earth; Twin-Oscar has an identical brain but lives on Twin Earth where 'water' is XYZ. Both sincerely say 'I want a glass of water.' What does the narrow/wide content distinction predict?"
  type: multiple-choice
  options:
    - "They have the same wide content but different narrow content — their environments differ"
    - "They have the same narrow content but different wide content — identical internal states, but different external referents"
    - "They have identical narrow and wide content — they are molecule-for-molecule identical"
    - "Only Oscar's belief has genuine content; Twin-Oscar's belief lacks reference because XYZ is not the real water"
  answer: 1
  explanation: "Narrow content is fixed entirely by intrinsic internal states — since Oscar and Twin-Oscar are brain-identical, their narrow content is the same. But wide content incorporates environmental context: Oscar's 'water' refers to H₂O, Twin-Oscar's 'water' refers to XYZ. Same narrow content, different wide content. This is exactly the point of the Twin Earth thought experiment: it shows that two internally identical people can mean different things by the same words, which motivates distinguishing the two kinds of content."

- question: "Why did Fodor argue that computational theories of mind require narrow rather than wide content?"
  type: multiple-choice
  options:
    - "Because computers operate without any environment, making environmental content irrelevant by definition"
    - "Because narrow content is causally efficacious through internal states alone — a computation's next step is determined by its internal state, not by what that state refers to externally"
    - "Because wide content requires too much memory storage to represent computationally"
    - "Because experimental psychology has confirmed that human behavior is determined by wide content alone"
  answer: 1
  explanation: "The key is causal efficacy. A computational system operates over internal states: the Turing machine reads a symbol and transitions based on its internal configuration, regardless of what that symbol refers to in the world. Similarly, Fodor argued, mental causation must be determined by internal states — if you believe there is a tiger in front of you (even when there isn't), you run, because it is the internal state that causes the behavior, not the actual tiger. Wide content, which depends on external facts, would make mental states the wrong kind of thing to figure in causal laws. Narrow content, fixed by internal states, is what a scientific psychology needs."

- question: "If two individuals have molecule-for-molecule identical brains, they necessarily have identical wide content for all their mental states."
  type: true-false
  answer: false
  explanation: "The Twin Earth case shows this is false. Oscar and Twin-Oscar are brain-identical but have different wide content: Oscar's 'water' refers to H₂O, Twin-Oscar's to XYZ. Wide content depends on external, environmental factors — what the internal states are causally connected to in the world — not just on intrinsic physical constitution. That is precisely the externalist insight: environment partially determines content."

- question: "Narrow content has been criticized for being too thin to count as genuine content, because it may amount to mere formal syntax without referential significance."
  type: true-false
  answer: true
  explanation: "This is one of the central objections to the narrow content program. Critics argue that if narrow content is fixed entirely by internal functional or computational structure, it describes a formal role — how a symbol behaves in inference and processing — without specifying what it is about. Genuine intentional content, the objection goes, is constitutively relational: it is content-of-something. A purely internal 'narrow content' might be syntax masquerading as semantics. Fodor tried to define narrow content as a function from environments to wide contents, but critics question whether this function itself has genuine referential significance."

- question: "Explain the analogy between narrow content and a recipe. What does the analogy reveal about the relationship between narrow and wide content?"
  type: short-answer
  answer: "Narrow content is like a recipe: it specifies a procedure or functional structure that, combined with particular environmental ingredients (the actual external referents), produces wide content — the finished dish. The same recipe in different kitchens (environments) yields different dishes, just as the same internal state in different environments yields different wide contents. The analogy reveals that narrow content is not nothing — it is a real structure that systematically determines wide content once the environment is specified — while clarifying that narrow content alone does not fix what the mental state is about."
  explanation: "The recipe analogy captures why narrow content defenders think it is genuinely content-like: it has determinate structure that constrains what wide contents can be produced from it. But it also shows narrow content's limitation: you cannot say what a recipe 'means' without specifying the ingredients. Externalists seize on this to argue that narrow content is not genuine content at all — only the finished dish (wide content) is really 'about' something. The analogy thus crystallizes the central dispute rather than resolving it."
```

## Explainer

From content externalism, you know the Twin Earth thought experiment: Oscar and Twin-Oscar have molecule-for-molecule identical brains, yet their mental states have different contents — "water" picks out H₂O for Oscar and XYZ for his twin. Content, on the externalist view, is **wide**: it depends on factors outside the skin. This creates a puzzle. If cognition is computation defined over internal states, and if content is what those states are *about*, then wide content seems wrong for computational purposes — two physically identical systems would have different contents depending on their environment.

**Narrow content** is the proposed solution: a type of mental content fixed entirely by intrinsic physical or functional states, independent of environment. Whatever Oscar and Twin-Oscar share — their identical computational structure — constitutes their narrow content. Wide content then adds environmental context on top. Think of narrow content as a function: given the same internal state in different environments, you get different wide contents. Narrow content is like a recipe; wide content is the finished dish when you supply the actual ingredients (the environment).

The motivation is strongest in computational theories of mind. If the mind is a computing machine, then its operations must be determined by internal states alone — a Turing machine does not need to know whether its symbols refer to real-world objects to run its program. Jerry Fodor argued that a scientific psychology needed narrow, causally efficacious content to explain behavior. Behavior seems to track internal states more tightly than external referents: if you believe there's a tiger in front of you (even when there isn't), you run — the behavior is caused by the internal state, not by the actual tiger.

The difficulties are significant. Critics argue that narrow content is either too thin to be genuine *content* (a mere formal structure without referential significance) or cannot be non-trivially specified without appealing to wide content. If narrow content is just syntax — a formal role unconnected to the world — it is unclear what work it does in explaining intentionality. The **de re attitudes** you have studied illustrate this tension: to believe that *that man* is a thief, the very individuation of "that man" seems to require an environmental relation, not just an internal state.

The narrow-wide distinction marks a fault line between internalists (the mind's contents are fixed by what is inside the skull) and externalists (the mind's contents reach out into the world). How you resolve this question has downstream consequences for computational theories of mind, for debates about mental causation, and for what a complete science of the mind would look like.
