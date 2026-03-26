---
id: causal-order-temporal-order
title: Causal Order and Temporal Order
domain: philosophy
course: metaphysics
prerequisites:
- id: causation-and-causal-relations
  type: hard
- id: philosophy-of-time
  type: hard
- id: counterfactual-causation
  type: soft
- id: causal-closure-principle
  type: soft
builds-toward:
- counterfactual-truth-modality
tags:
- causation
- time
- order
- temporal
- metaphysics
stage: formal-systems
status: validated
---
# Causal Order and Temporal Order

## Core Idea
Do causal relations presuppose temporal order, or is temporal order derivative of causal structure? Standard metaphysics assumes causes precede effects temporally, but some theories reverse this. Others argue causation and temporal direction are asymmetric for distinct reasons (causation involves counterfactual dependence, time has entropic direction). Understanding this relationship is crucial for philosophy of time and causation.

## Questions

```yaml
- question: "According to the causal theory of time, what does it mean for event A to occur 'before' event B?"
  type: multiple-choice
  options:
    - "A has higher entropy than B, reflecting the thermodynamic arrow of time"
    - "A and B are connected by a continuous chain of physical events"
    - "A can causally influence B, but B cannot causally influence A"
    - "A is closer in space to the observer's reference frame than B"
  answer: 2
  explanation: "The causal theory of time (associated with Reichenbach) identifies temporal order with the direction of causal influence: 'A is earlier than B' just means A is the kind of event that can affect B, while B cannot affect A. This reduces temporal order to causal structure, avoiding a primitive unexplained 'arrow of time.' The problem is that this threatens circularity: our best analyses of causation (especially counterfactual analyses) typically presuppose which event is 'earlier,' so defining temporal order in terms of causal order and causal order in terms of temporal order goes in circles."

- question: "A physicist proposes a theory in which a measurement outcome can causally influence the earlier experimental setup via a retrocausal quantum mechanism. If such backward causation is coherent, this most directly suggests:"
  type: multiple-choice
  options:
    - "The causal theory of time must be correct — backward causation confirms that causes always define temporal direction"
    - "Causal order and temporal order are conceptually separable — an event can be a cause even if it is temporally later than its effect"
    - "The second law of thermodynamics would necessarily be violated by any retrocausal process"
    - "Counterfactual analyses of causation are refuted because they cannot accommodate backward causation"
  answer: 1
  explanation: "If backward causation is coherent — a later event causing an earlier one — then causal order and temporal order are not the same concept: 'cause' does not simply mean 'earlier.' The two asymmetries can come apart, showing they are conceptually independent. Fundamental physics is time-symmetric at the level of equations, so backward causation is not ruled out by physics. Whether it would violate the second law depends on the specific mechanism; the key philosophical point is the conceptual separability of the two asymmetries."

- question: "If backward causation is genuinely possible, this demonstrates that causal order and temporal order cannot be identified with each other."
  type: true-false
  answer: true
  explanation: "Backward causation means an effect temporally precedes its cause. If such cases are possible, then we have causes that are later than their effects in time — which means causal order and temporal order come apart. This undermines any simple identification of 'A causes B' with 'A is earlier than B,' since backward causation is precisely a counterexample to that identification. The possibility of backward causation shows the two concepts are logically distinct even if they typically align."

- question: "The fundamental laws of classical mechanics and quantum mechanics are time-asymmetric — they describe processes that can unfold mainly in the forward temporal direction."
  type: true-false
  answer: false
  explanation: "This is false, and it is central to the puzzle of causal-temporal order. Newton's laws, electrodynamics, and the Schrödinger equation are all time-symmetric: reversing the time variable (and, in quantum mechanics, taking the complex conjugate) yields equally valid solutions running backward. The apparent asymmetry of the world — causes preceding effects, entropy increasing — is not a direct consequence of the fundamental laws themselves. It requires additional statistical or initial-condition explanations (such as the entropic arrow of time) that are not built into the equations."

- question: "Why does the causal theory of time — the view that temporal order is grounded in causal order — face a circularity problem?"
  type: short-answer
  answer: "The causal theory wants to define 'A is earlier than B' in terms of 'A can causally affect B but not vice versa.' But our best analyses of causation — especially counterfactual analyses — themselves rely on temporal notions: they say something like 'if A hadn't occurred, B wouldn't have occurred,' and they typically restrict this to cases where A is earlier than B. If temporal order is defined using causal order, and causal order is defined using temporal order, neither concept is independently grounded. The circle is vicious if we want a reductive account."
  explanation: "The circularity problem shows that causal and temporal asymmetries cannot both be reduced to each other simultaneously. The alternative is to ground both in a third factor — most commonly the entropic arrow (the second law of thermodynamics) — which explains why causes precede effects and why entropy increases without deriving one from the other. This avoids circularity but treats both arrows as consequences of something deeper (statistical mechanics and initial conditions) rather than as one reducing to the other."
```

## Explainer

The commonsense picture is straightforward: causes come before effects, and "before" is defined by the direction of time. But once you've studied causation and the philosophy of time separately, a deeper puzzle emerges: how exactly do these two asymmetries — causal and temporal — relate to each other? Are they the same asymmetry, or are they independent features of the world that merely happen to align?

One position is that **causal order is prior to temporal order** — that what we call "earlier" and "later" is actually constituted by the direction of causal influence. On this view, to say event A is earlier than event B just is to say something like "A can causally affect B but not vice versa." This is the causal theory of time, associated with philosophers like Reichenbach. It has a certain economy: it reduces temporal direction to causal direction, avoiding a primitive "arrow of time." But it faces a serious challenge: it threatens circularity. Our analyses of causation — including the counterfactual analysis you've already studied — typically presuppose temporal direction. If causes are defined in terms of counterfactual dependence and counterfactuals already assume "earlier" and "later," then we can't also define temporal order in terms of causes without going in a circle.

The alternative is to treat the **temporal asymmetry as prior** or as grounded in something independent — most commonly, thermodynamics. The second law of thermodynamics says entropy increases in the forward time direction. Low-entropy states are vastly outnumbered by high-entropy states, so systems naturally evolve toward disorder. This **entropic arrow of time** can explain why causes precede effects statistically without needing causal order to ground temporal order. On this picture, time's direction and causation's direction are both grounded in the same underlying fact about entropy and probability, but they are not identical.

A third wrinkle involves **backward causation** — the possibility that effects could precede their causes. Standard physics is time-symmetric at the fundamental level; the laws of mechanics work equally well in both temporal directions. Some interpretations of quantum mechanics and certain theoretical proposals in physics allow for retrocausal influence. If backward causation is genuinely possible, this suggests that causal order and temporal order are conceptually separable: we can coherently imagine a cause that comes after its effect, which means neither concept fully reduces to the other. The relationship between causal and temporal asymmetry thus sits at the intersection of metaphysics, physics, and the analysis of counterfactuals — a point where the questions you've studied in each domain converge on a single deep puzzle about the structure of reality.

