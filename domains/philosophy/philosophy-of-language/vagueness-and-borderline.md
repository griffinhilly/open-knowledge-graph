---
id: vagueness-and-borderline
title: Vagueness and Borderline Cases
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: vagueness-sorites-paradox
  type: hard
- id: logical-form
  type: soft
builds-toward:
- compositionality-semantic-limits
tags:
- vagueness
- sorites
- semantics
- logic
stage: formal-systems
status: draft
---

# Vagueness and Borderline Cases

## Core Idea
Vagueness is ubiquitous (is someone with 1,000,001 hairs bald?), yet traditional logic assumes precise truth-conditions. Sorites arguments show how innocent-seeming principles lead to paradox. Supervaluationism, degree semantics, and epistemicism offer competing solutions with different implications for meaning and logic.

## Questions

```yaml
- question: "Under supervaluationism, John is borderline tall — 'John is tall' is neither true nor false on any single precisification. What is the truth value of 'John is tall or John is not tall'?"
  type: multiple-choice
  options:
    - "Indeterminate, because the disjunction inherits the indeterminacy of both disjuncts"
    - "False, because neither disjunct is true"
    - "Supertrue — true on every precisification, even though neither disjunct has a determinate truth value"
    - "Only true if we first settle on a single precisification and evaluate the disjunction within it"
  answer: 2
  explanation: "This is the signature consequence of supervaluationism. On any single precisification, John either counts as tall (making 'John is tall' true) or doesn't (making 'John is not tall' true). So 'John is tall or John is not tall' is true on EVERY precisification — supertrue — even though 'John is tall' and 'John is not tall' are each indeterminate. Classical tautologies are preserved. The cost is that we can have a true disjunction where neither disjunct is true, which violates classical inference rules like disjunction elimination."

- question: "Epistemicism handles the sorites paradox by claiming that vague predicates like 'bald' actually have sharp, precise extensions. What is the epistemicist explanation for why we cannot identify the boundary?"
  type: multiple-choice
  options:
    - "The boundary is determined by social convention and shifts depending on context, making it impossible to pin down"
    - "There is no fact of the matter about where the boundary falls — the predicate is genuinely borderless, but we can pretend there's a boundary for logical purposes"
    - "The boundary exists and is perfectly sharp, but our concepts and linguistic practices are not fine-grained enough to detect exactly where it falls"
    - "Vague predicates refer to continuous physical properties, and boundaries in continuous domains are always physically indeterminate"
  answer: 2
  explanation: "Williamson's epistemicism holds that 'bald' has a precise extension — there is a specific number of hairs below which someone is bald — but we cannot know where this threshold is because our knowledge of word meanings is limited by how we learned them. Semantic facts outstrip epistemic access. This preserves classical bivalence (every statement is true or false) and classical logic fully, but at a steep cost: it implies that removing a single hair sometimes changes someone from not-bald to bald, we just can't tell when. Many find this counterintuitive."

- question: "On the supervaluationist account, a disjunction can be true (supertrue) even when neither of its disjuncts has a truth value."
  type: true-false
  answer: true
  explanation: "This is the defining and controversial feature of supervaluationism. 'P or not-P' is a classical tautology that remains supertrue even when P is borderline (indeterminate), because on every precisification either P or not-P is true. But neither P nor not-P is supertrue when P is indeterminate. This preserves the law of excluded middle as a logical law while creating truth-value gaps for individual borderline sentences. The cost is that classical inference rules like 'from P-or-Q and not-P, infer Q' can fail."

- question: "Degree semantics resolves the problem of higher-order vagueness, because assigning a precise numerical degree (like 0.7) to a borderline sentence gives it a determinate truth value."
  type: true-false
  answer: false
  explanation: "Degree semantics faces the higher-order vagueness problem directly. Even if we assign 'John is tall' a degree of 0.7, the boundary between 'clearly tall' (degree ≈ 1) and 'borderline tall' (intermediate degree) is itself vague — there's no sharp line between degree 0.9 (clearly tall) and degree 0.7 (borderline tall). This generates vagueness about the degrees themselves, threatening an infinite regress: vagueness about vagueness, and then vagueness about that, and so on. The numerical assignment appears precise but doesn't eliminate the underlying gradience."

- question: "Epistemicism fully preserves classical two-valued logic. What does it sacrifice to do so, and why do many philosophers find that cost too high?"
  type: short-answer
  answer: "Epistemicism preserves bivalence by positing that vague predicates have perfectly sharp extensions that we simply cannot know. The cost is making meaning radically inaccessible: there is a precise hair-count threshold for baldness, but no amount of linguistic analysis or empirical investigation can identify it. This seems to sever meaning from use — the meaning of 'bald' is fixed by something beyond our grasp, not by the practices and contexts in which we use the word. Many philosophers find it implausible that meaning could be so epistemically opaque to the very speakers who deploy it."
  explanation: "The deeper objection is that epistemicism seems to generate sharp facts from nowhere. If our use of 'bald' is necessarily imprecise — no community ever drew a sharp line at exactly 1,047 hairs — then what could possibly fix such a boundary? Williamson argues that meaning supervenes on use in a way that produces sharp extensions even without explicit boundary-fixing, but this remains contested. The debate connects to broader questions about semantic externalism and the relationship between meaning, use, and knowledge."
```

## Explainer

You already understand the Sorites paradox: take a heap of sand, remove one grain — still a heap. Repeat a thousand times. At no point does a single grain make the difference between heap and non-heap, yet we end with one grain and the argument forces us to call it a heap. The paradox arises because "heap" is **vague**: there is no sharp boundary between heaps and non-heaps, and cases in the middle — a hundred grains, perhaps — are **borderline cases** where it is genuinely unclear whether the term applies. The challenge is to explain what's happening in borderline cases without accepting the paradox.

The simplest response is **epistemicism**, defended by Timothy Williamson. Vague predicates actually have perfectly sharp extensions — there really is a precise number of hairs below which someone is bald — but we cannot know where the boundary falls because our concepts are not precise enough to detect it. On this view, classical logic is fully preserved: every statement is either true or false; it's just that we can't always know which. The counterintuitive implication is that removing a single hair sometimes makes someone bald, we just can't tell when. Epistemicism saves logic at the cost of making meaning radically inaccessible.

**Supervaluationism** takes a different route. A vague predicate like "tall" can be "precisified" — made arbitrarily sharp — in many different ways. Someone 5'10" might count as tall on some precisifications and not tall on others. Supervaluationism says a sentence is **supertrue** if it is true on all precisifications, **superfalse** if false on all, and **indeterminate** (neither true nor false) if it varies. Classical tautologies like "John is tall or not tall" remain supertrue — true on every precisification — even when "John is tall" is indeterminate. This preserves classical logical laws while allowing truth-value gaps at borderline cases. The cost: some instances of classical inference fail; you can have a disjunction that is supertrue even though neither disjunct is true.

**Degree semantics** (developed by Kamp, Fine, and others) assigns sentences involving vague predicates **degrees of truth** between 0 and 1, rather than just true or false. "John is tall" might have a degree of 0.7 if he's 5'11". Logical connectives then operate on degrees: "not" inverts, "and" takes the minimum, "or" takes the maximum. Borderline cases are cases with intermediate degree, not missing truth values. The challenge for degree semantics is explaining what these degrees represent — are they objective features of the world, facts about our dispositions, or something else? — and handling higher-order vagueness: the boundary between "clearly tall" and "borderline tall" is itself vague, threatening an infinite regress of borderlines. Each theory reveals something important: vagueness is not merely a linguistic imprecision to be cleaned up, but a deep feature of how language engages with a continuous world.
