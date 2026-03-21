---
id: anomalous-monism
title: Anomalous Monism
domain: philosophy
course: philosophy-of-mind
prerequisites:
- id: physicalism-about-mind
  type: hard
- id: mental-causation
  type: soft
- id: identity-theory
  type: soft
- id: property-dualism
  type: soft
tags:
- anomalous-monism
- Davidson
- token-identity
- supervenience
- causation
stage: formal-systems
status: validated
---
# Anomalous Monism

## Core Idea
Donald Davidson's anomalous monism (1970) holds that mental events are identical with physical events (monism) but that mental event types cannot be systematically reduced to or correlated with physical event types (anomalism). Each mental event token is a physical event token, but there are no strict psychophysical laws connecting mental and physical descriptions. Mental descriptions are governed by norms of rationality (the principle of charity) rather than strict causal laws, making psychology 'anomalous' — it operates under different constitutive principles than physics. Davidson attempts to reconcile the causal efficacy of the mental with the autonomy of mental description, though Kim argues this leaves mental properties causally impotent.

## How It's Best Learned
Read Davidson's 'Mental Events' (1970). The key is understanding why Davidson thinks mental/physical event identity is compatible with irreducibility of mental descriptions: identity is a relation between events (particulars), while reducibility concerns types or predicates. Then trace how Kim's exclusion argument targets Davidson's position specifically.

## Common Misconceptions
- 'Anomalous' does not mean 'weird' or 'irregular'; it means that mental events, described under mental descriptions, do not fall under strict causal laws.
- Anomalous monism is not eliminativist: Davidson affirms the reality and causal efficacy of mental events — he just denies there are strict psychophysical bridge laws.

## Questions

```yaml
- question: "Davidson holds three non-negotiable claims: mental events cause physical events; causation is backed by strict laws; and there are no strict psychophysical laws. How does he resolve the apparent contradiction?"
  type: multiple-choice
  options:
    - "He denies the first claim — mental events do not genuinely cause physical events; only physical events cause physical events"
    - "He denies the second claim — mental causation is a distinct kind of causal relation that does not require backing by strict laws"
    - "He holds that each mental event token is identical to some physical event token, so mental events cause things by falling under physical causal laws under their physical description"
    - "He posits special psychophysical bridge laws that connect mental descriptions to physical descriptions, making mental causation lawful after all"
  answer: 2
  explanation: "Davidson's resolution is token-token identity: every individual mental event is identical to some individual physical event. The mental event causes things not under its mental description (where no strict laws apply) but under its physical description (where physical causal laws do apply). This preserves all three claims: mental events are causally efficacious (claim 1) because they are physical events; causation is backed by laws (claim 2) at the physical level; and no systematic psychophysical bridge laws are needed (claim 3) because the identity is at the token level, not the type level."

- question: "Jaegwon Kim's exclusion argument targets anomalous monism by arguing that:"
  type: multiple-choice
  options:
    - "Mental events cannot be identical to physical events because mental and physical predicates have incompatible logical forms"
    - "If physical causes are sufficient for physical effects, and mental properties are not identical to physical properties at the type level, then mental properties do no independent causal work and are epiphenomenal"
    - "Davidson's principle of charity makes psychological explanation circular and non-explanatory"
    - "Token identity without type identity makes event individuation indeterminate, undermining the identity claim"
  answer: 1
  explanation: "Kim's exclusion argument: physical events have sufficient physical causes. If mental properties are not type-identical to physical properties, then when a mental property (say, being a belief) coincides with a physical state, the physical state is doing all the causal work. The mental property is along for the ride — present but causally inert. Davidson insists mental event *tokens* are causally efficacious, but Kim presses that the mental *properties* — what makes the event a belief rather than just a neural firing — do nothing. This is the sense in which anomalous monism may save mental causation at the event level while losing it at the property level."

- question: "In anomalous monism, each individual mental event token is identical to some physical event token, even though mental event types cannot be reduced to physical event types."
  type: true-false
  answer: true
  explanation: "This is the defining feature of anomalous monism: monism at the token level (each mental event = some physical event), combined with irreducibility at the type level (no systematic bridge laws connecting mental types to physical types). The 'anomalous' part names the type-level irreducibility: mental descriptions are governed by norms of rationality that have no analog in physical description, making systematic psychophysical laws impossible. The 'monism' part names the token-level identity: there is only one kind of stuff (the physical), and mental events are physical events under a different description."

- question: "Anomalous monism is a version of type identity theory: it holds that mental types (like pain or belief) are identical to physical types (like C-fiber firing), while acknowledging exceptions in unusual cases."
  type: true-false
  answer: false
  explanation: "Anomalous monism explicitly rejects type identity theory. Type identity (Smart, Place) holds that mental *types* are identical to physical types — pain = C-fiber firing for all instances. Davidson denies this entirely: there are no strict psychophysical laws, no systematic mapping of mental types onto physical types. What Davidson accepts is only token identity — each individual mental event instance is identical to some physical event instance, but there is no general rule saying which mental type corresponds to which physical type. This is the core of what makes the position 'anomalous.'"

- question: "What does Davidson mean by saying that mental descriptions are 'anomalous'? Why do norms of rationality make mental description constitutively different from physical description, and what does this imply about the possibility of strict psychophysical laws?"
  type: short-answer
  answer: "Mental descriptions are 'anomalous' in the technical sense: mental events described under mental predicates do not fall under strict causal laws. Davidson's reason is that mental description is normatively constituted — to attribute beliefs, desires, and intentions to an agent, you must interpret them as broadly rational. You cannot assign mental states without making the agent's overall psychology cohere. Physical description has no such constraint: a brain state is whatever it is, regardless of whether it is rational. Because the standards governing mental and physical description are constitutively different in kind, no systematic bridge law — 'whenever mental type M, then physical type P' — can hold. The rational and the nomological operate under different principles."
  explanation: "This is the deepest commitment in Davidson's position. The argument is not empirical (we haven't found the laws yet) but conceptual (the nature of mental description makes such laws impossible in principle). Rationalizing explanation — explaining behavior by citing reasons — requires holistic interpretation under norms of coherence and rationality. Causal explanation under strict laws requires only nomological regularities, with no normative dimension. These are two distinct explanatory frameworks, and their constitutive differences prevent reduction of one to the other, no matter how detailed our neuroscience becomes."
```

## Explainer

From your study of physicalism and identity theory, you know that **type identity theory** (Smart, Place) held that mental types — pain, belief, desire — are identical to physical types: pain = C-fiber firing, for instance. This is a strongly reductive view: psychology, in principle, reduces to neuroscience. You also know that **property dualism** denies this reduction while accepting that mental properties depend on physical ones. Donald Davidson's **anomalous monism** occupies unusual ground: it is monist at the level of *tokens* (individual events) but irreducibly dualist at the level of *types* (properties and descriptions).

The position rests on three claims Davidson takes to be jointly non-negotiable. First, **mental events can cause physical events**: my belief that it's raining and my desire to stay dry can cause me to pick up an umbrella. Second, **causation is backed by strict laws**: when event A causes event B, there is some strict law under which they fall. Third, **there are no strict psychophysical laws**: there is no systematic mapping of mental types onto physical types that constitutes a genuine bridge law. The first two claims are broadly accepted; the third requires argument. Davidson's reasoning is that mental descriptions are governed by normative standards — rationality, coherence, consistency — that have no analog in physical description. To interpret a person's mental states, you must make them rational; you cannot interpret them as a mere physical mechanism. Mental and physical descriptions are *constitutively different* in kind, not just coincidentally uncorrelated.

These three claims are in tension: if causation requires strict laws, and there are no strict psychophysical laws, how can the mental cause anything? Davidson's resolution is a **token-token identity**: each individual mental event *token* is identical to some physical event token, and it is *under its physical description* that the event falls under a strict causal law. My belief-token is identical to some brain-state-token, and *qua* brain-state it enters into physical causal relations governed by neuroscientific or physical laws. Mental event causation is real, but the causal work is done by the physical description of the event.

The legacy of anomalous monism is largely shaped by Jaegwon Kim's critique. If mental properties — the properties that make an event a belief rather than just a neural firing — do no independent causal work, then they are **epiphenomenal**: present, but causally idle. Kim's **exclusion argument** presses this: given that physical causes are sufficient for physical effects, what causal role is left for mental properties? Davidson insists that mental event *tokens* are causally efficacious, but Kim argues that without type-level connections, the mental properties themselves are doing nothing. This is the central unresolved tension: anomalous monism saves mental causation at the level of events while appearing to lose it at the level of properties — which is precisely where the explanatory interest lies.
