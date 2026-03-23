---
id: invertible-counterpoint-advanced
title: Invertible Counterpoint and Multiple Counterpoint
domain: music
course: advanced-music-theory
prerequisites:
- id: counterpoint-basics
  type: hard
- id: species-counterpoint
  type: hard
builds-toward:
- canon-techniques-advanced
tags:
- counterpoint
- inversion
- advanced
- voice-exchange
stage: expert
status: validated
---

# Invertible Counterpoint and Multiple Counterpoint

## Core Idea
Invertible (or double) counterpoint creates two complementary lines that can exchange register while maintaining the same harmonic content and voice-leading relationships, enabling richer developmental possibilities. Triple and quadruple counterpoint extend this principle to three or four voices, creating extraordinary compositional flexibility.

## Questions

```yaml
- question: "You are writing two voices intended for invertible counterpoint at the octave, and you use a perfect fifth between them. When the voices exchange registers, this interval becomes:"
  type: multiple-choice
  options:
    - "A perfect fifth — intervals are preserved under octave inversion"
    - "A perfect fourth — which is treated as dissonant against the bass in traditional counterpoint"
    - "A minor sixth — because inversion reverses interval quality"
    - "A tritone — because the perfect fifth and fourth differ by a tritone"
  answer: 1
  explanation: "Using the inversion rule for counterpoint at the octave — new interval = 9 − old — a perfect fifth (5) becomes 9 − 5 = 4, a perfect fourth. A fourth is treated as dissonant when it falls between the bass and an upper voice, creating voice-leading problems in the inverted arrangement. This is the central danger in invertible counterpoint: an interval that sounds fine in the original position can become problematic when the voices swap."

- question: "Why do composers writing for invertible counterpoint at the octave favor intervals of thirds and sixths?"
  type: multiple-choice
  options:
    - "Thirds and sixths are more consonant than other intervals in tonal harmony"
    - "Thirds invert to sixths and sixths invert to thirds — both remain consonant in either arrangement"
    - "Thirds and sixths eliminate parallel motion, reducing voice-leading errors"
    - "Bach's strict style allows only thirds and sixths between inner voices"
  answer: 1
  explanation: "Using the 9-minus rule: a third (3) becomes 9 − 3 = 6, a sixth; a sixth (6) becomes 9 − 6 = 3, a third. Both thirds and sixths are consonant intervals, so they remain consonant after inversion. They are the 'safe' interval choices for invertible counterpoint — whatever arrangement the voices appear in, the intervals hold up. Fifths, by contrast, become fourths, creating dissonance against the bass."

- question: "In invertible counterpoint at the octave, a major third in the original arrangement becomes a minor sixth when the voices exchange registers."
  type: true-false
  answer: true
  explanation: "Yes. The interval number transforms by the rule 9 − 3 = 6, giving a sixth. When a major interval is inverted, its quality becomes minor (and vice versa): a major third inverts to a minor sixth, a minor third to a major sixth. This quality flip is part of what makes invertible counterpoint planning non-trivial — the composer must verify that the resulting quality in the inverted arrangement still makes harmonic sense."

- question: "Any two voices that independently satisfy standard voice-leading rules can be used as invertible counterpoint, since each part is already correct on its own."
  type: true-false
  answer: false
  explanation: "This is the key misconception. Two individually correct voices may produce voice-leading problems when inverted. The most dangerous case: a perfectly consonant fifth between the voices becomes a fourth — dissonant against the bass — when the voices swap. Invertible counterpoint requires planning both arrangements simultaneously from the start, not assembling two independently correct lines and hoping they invert cleanly."

- question: "Explain why the '9 minus the original interval' transformation rule determines which intervals are safe to use in invertible counterpoint at the octave, and give an example of an interval that becomes problematic after inversion."
  type: short-answer
  answer: "When two voices exchange registers by an octave, every interval is replaced by its complement to 9 (counting from 1): a third becomes a sixth, a fifth becomes a fourth, etc. The composer must verify that the transformed interval is also acceptable voice-leading. The classic problem: a perfect fifth (consonant in any position) becomes a perfect fourth (9 − 5 = 4), which is dissonant when it falls between the bass and an upper voice. Parallel fifths are already forbidden; after inversion they become parallel fourths — equally problematic. Planning for inversion means choosing intervals whose complements to 9 are also consonant."
  explanation: "The 9-minus rule captures what happens geometrically when you flip the relative register of two voices: the interval that was above the bass is now above the soprano, and the sizes that fill an octave sum to 9 (e.g., a third and a sixth, a fourth and a fifth). This is why invertible counterpoint is considered advanced compositional skill: it requires thinking in two arrangements simultaneously — checking not just that the current layout works, but that its mirror image works too."
```

## Explainer

From species counterpoint you learned the interval rules that govern two-voice writing: which intervals are consonant, which dissonances are permitted and how they must resolve, and how to handle parallel motion. **Invertible counterpoint** takes this one step further by asking: what if I want to write two voices that can *swap registers* — the soprano becomes the bass and vice versa — and still sound correct? This is the fundamental question of double counterpoint, and answering it requires thinking about how intervals transform when two voices exchange.

The most common case is **invertible counterpoint at the octave**: one voice descends an octave (or the other ascends one) so that what was the top voice is now the bottom. When voices invert at the octave, every interval transforms according to the rule: the new interval is 9 minus the old one (counting from 1). A third becomes a sixth (9−3=6), a sixth becomes a third, a fourth becomes a fifth — and crucially, a fifth becomes a fourth. That last transformation is the danger point: perfect fifths, which are fully consonant in the original position, become perfect fourths after inversion. A fourth requires careful treatment in counterpoint (it is dissonant against the bass). This means you must avoid exposed parallel fifths in invertible counterpoint, because they will become parallel fourths — equally problematic — when the voices swap.

The practical result: when writing a pair of lines intended for invertible counterpoint, you plan for both arrangements simultaneously. You check not only that the original voice arrangement is correct, but that the inverted arrangement is also valid. The most common strategy is to favor thirds and sixths (which swap with each other) and to treat fourths as consonant only when a third voice is present to contextualize them. Bach's inventions and fugues make constant use of this technique: a subject-answer pair in a fugue is often designed so that the subject can appear above or below the countersubject, enabling varied recombination throughout the development.

**Triple and quadruple counterpoint** extend this to three or four voices, creating a combinatorial explosion of possibilities. Three voices that are mutually invertible can appear in 3! = 6 different orderings from top to bottom, while four voices yield 24 arrangements. Each arrangement must independently satisfy voice-leading rules, and the harmonic content must remain coherent in every configuration. This level of pre-compositional planning is what makes Bach's fugues feel inexhaustible: the material is engineered to combine in multiple ways, so each recombination reveals new facets of the same underlying structure. Mastering invertible counterpoint transforms counterpoint from reactive rule-following into proactive structural design.
