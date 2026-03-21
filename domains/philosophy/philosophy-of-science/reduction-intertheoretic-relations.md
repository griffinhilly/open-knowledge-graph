---
id: reduction-intertheoretic-relations
title: Reduction and Emergence
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: laws-of-nature-metaphysics
  type: soft
- id: natural-kinds-classification
  type: soft
builds-toward:
- scientific-progress-and-convergence
tags:
- reduction
- emergence
- levels
stage: advanced
status: draft
---

# Reduction and Emergence

## Core Idea
Reduction holds that theories of higher levels (psychology, biology) reduce to lower levels (physics, chemistry), explaining higher-level phenomena through lower-level mechanisms. Emergence denies this, claiming higher levels have novel, irreducible properties. This debate shapes understanding of science's unity and whether all phenomena ultimately reduce to physics.

## Questions

```yaml
- question: "Pain is a psychological state that is realized by C-fiber stimulation in humans, but may be realized by entirely different physical structures in octopuses. According to the multiple realizability objection, what does this imply for Nagelian reduction of psychology to physics?"
  type: multiple-choice
  options:
    - "Psychology reduces successfully because there is always *some* physical realizer, even if different species have different ones"
    - "The bridge law for 'pain' must be a disjunction of all possible physical realizers — which may be open-ended and not a genuine natural kind"
    - "Multiple realizability shows that psychology is not a genuine science, since its categories are too vague"
    - "Nagelian reduction still works as long as we restrict bridge laws to a single species"
  answer: 1
  explanation: "Putnam's multiple realizability objection holds that if 'pain' can be realized by arbitrarily many different physical configurations, then the bridge law connecting 'pain' to a physical predicate would have to be an open-ended disjunction. But an infinite or open-ended disjunction is not a natural kind in physics — physics does not group C-fibers, silicon circuits, and cephalopod neurons under a single natural category. Without a genuine physical predicate on the right side of the bridge law, Nagelian reduction cannot proceed. The higher-level kind 'pain' carves nature at functional joints that are invisible to physics."

- question: "The game of life produces 'gliders' — patterns that move coherently across the grid. Gliders are nothing more than cell states, yet 'glider' is not a concept of cellular automaton theory. What kind of emergence does this illustrate?"
  type: multiple-choice
  options:
    - "Strong emergence — gliders have properties that cannot in principle be derived from cell states"
    - "Weak emergence — gliders are in principle derivable from the lower-level rules but are not concepts of that lower-level theory"
    - "Nagelian reduction — gliders reduce to cell states via bridge laws"
    - "Multiple realizability — the same glider pattern can be realized by different cell configurations"
  answer: 1
  explanation: "Weak emergence holds that a higher-level property is ontologically nothing over and above the lower-level constituents (gliders *are* cell states) but belongs to a different conceptual level — 'glider' is not a concept of cellular automaton theory, yet it picks out a real, stable pattern. The glider pattern is in principle derivable from the rules if you ran the simulation; the emergence is epistemic and conceptual, not ontological. Strong emergence would require that gliders have properties that *cannot even in principle* be derived from cell states — which is not the case here."

- question: "Multiple realizability is the central objection to Nagelian reduction: it argues that the same higher-level property can be realized by many different lower-level configurations, making it impossible to formulate the bridge laws reduction requires."
  type: true-false
  answer: true
  explanation: "Nagelian reduction requires bridge laws connecting each higher-level predicate to a lower-level one. Multiple realizability (Putnam) argues that psychological predicates like 'pain' or biological predicates like 'gene' can be realized by physically heterogeneous substrates, so there is no single physical predicate to put in the bridge law. At best, the law becomes a disjunction — but a wildly disjunctive predicate is not a natural kind and not a law of physics. This is widely regarded as the most powerful objection to classical reductionism."

- question: "If reduction succeeds — if all higher-level theories can in principle be derived from physics — then the special sciences (psychology, biology, economics) lose their explanatory authority and become redundant."
  type: true-false
  answer: false
  explanation: "This is Fodor's point about the autonomy of the special sciences. Even if higher-level phenomena are ontologically grounded in physics, the special sciences use concepts that carve nature at real, causally relevant joints that physics does not recognize. The law 'organisms reproduce to maximize fitness' captures genuine regularities that would be invisible if described purely in physical terms — the physical description would be astronomically complex and would obscure the explanatory pattern. Reduction, if it succeeded, would show that physics underlies everything; it would not show that other levels of description are explanatorily idle."

- question: "Why does multiple realizability pose a problem specifically for bridge laws in Nagelian reduction, rather than just showing that different species have different neuroscience?"
  type: short-answer
  answer: "Nagelian reduction requires that for every predicate of the higher-level theory, there is a *corresponding* predicate in the lower-level theory, connected by a bridge law (a biconditional or identity). Multiple realizability shows that higher-level predicates like 'pain' pick out a functional kind — defined by causal role (caused by damage, causes withdrawal) — that can be physically realized in indefinitely many ways. There is no single physical predicate that captures all and only the realizers of pain across all possible creatures. The bridge law would have to be an open-ended disjunction, which is not a natural kind and not a law. The problem is structural: functional classification and physical classification cross-cut each other, so the bridge laws cannot be formulated."
  explanation: "This is why many philosophers conclude that the special sciences are irreducibly autonomous — their categories are real and causally efficacious but not reducible to physical natural kinds. The alternative is to accept that reduction must be species-specific (or system-specific), which saves reduction at the cost of making it far less ambitious than its proponents intended."
```

## Explainer

The sciences are organized in levels. Physics describes fundamental particles and forces. Chemistry describes molecular structures and reactions built from those particles. Biology describes living systems built from molecules. Psychology describes mental states built from neural processes. Each level has its own laws, concepts, and natural kinds. The question of **intertheoretic reduction** is whether this hierarchy is merely organizational convenience or whether higher-level theories are in principle derivable from lower-level ones — and whether we should expect the sciences ultimately to unify under physics.

Nagel's classic **model of reduction** (1961) specifies two conditions. First, **connectability**: for every predicate of the higher-level theory (e.g., "gene" in genetics), there must be a corresponding predicate in the lower-level theory (e.g., a description in molecular biology), linked by **bridge laws** — biconditionals or identities connecting the vocabularies. Second, **derivability**: once bridge laws are in place, the laws of the higher-level theory must be logically derivable from the lower-level theory plus the bridge laws. On this model, the reduction of genetics to molecular biology would require showing that every genetic property corresponds to some molecular property, and that Mendel's laws follow from the chemistry of DNA and cell division.

The most important objection to Nagel-style reduction is **multiple realizability**, developed by Putnam. Consider the psychological state of pain. Pain is realized by C-fiber stimulation in humans — but the same functional state (being caused by damage, causing withdrawal, triggering distress) might be realized by completely different physical structures in octopuses, robots, or aliens. If "pain" picks out a real psychological kind, and if that kind can be realized by arbitrarily many physical configurations, then there is no single physical predicate to put in the bridge law. The higher-level concept carves nature at joints that are invisible at the lower level. This is a problem for reductionism: the special sciences classify phenomena by their functional or causal profiles, not by their physical constitution, and these classifications cut across physical kinds.

**Emergence** comes in two varieties. **Weak emergence** holds that higher-level properties are in principle derivable from lower-level ones but are not practically predictable from them — complexity makes them epistemically irreducible even if ontologically grounded in the lower level. The game of life's gliders are weakly emergent: they are nothing but cell states, but "glider" is not a concept of cellular automaton theory; it emerges at a higher level of description. **Strong emergence** makes the stronger claim that higher-level properties are not even in principle derivable from lower-level ones — they are genuinely novel, irreducible features of reality. Consciousness is frequently cited as a candidate for strong emergence: many philosophers believe that even complete physical knowledge would not let you derive the phenomenal character of experience (see the knowledge argument).

The practical import of this debate concerns the unity of science and the authority of different disciplines. Reductionists hold that biology is ultimately applied chemistry, chemistry is applied physics, and all explanatory authority flows upward from the base. Anti-reductionists like Fodor argue that the special sciences are autonomous: they carve nature at real, irreducible joints, and their laws are genuine even if they cannot be deduced from physics. This is not a merely semantic question — it bears on whether psychology can be a rigorous science in its own right, whether biological functions have genuine explanatory force, and whether understanding a phenomenon always requires understanding its physical constituents.


