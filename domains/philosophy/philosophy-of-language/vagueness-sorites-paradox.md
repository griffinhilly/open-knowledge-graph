---
id: vagueness-sorites-paradox
title: Vagueness and the Sorites Paradox
domain: philosophy
course: philosophy-of-language
prerequisites: []
builds-toward:
- compositionality-principle
tags:
- vagueness
- sorites-paradox
- truth
- semantics
stage: abstract-reasoning
status: validated
---

# Vagueness and the Sorites Paradox

## Core Idea
Many natural language predicates are vague: 'bald,' 'tall,' 'red' have no sharp boundary between instances and non-instances. The sorites paradox exploits vagueness: if removing one hair doesn't make a non-bald person bald, then no number of removals can; yet some people are bald and some are not. This seems paradoxical. Responses include epistemicism (facts are precise but unknowable), semantic approaches (vagueness is semantic indeterminacy), degree-theoretic accounts (truth comes in degrees), and contextualism (what counts as bald varies with context).

## How It's Best Learned
Derive the sorites paradox carefully and see why classical logic seems to yield a contradiction. Study different responses and their trade-offs. Consider whether vagueness is linguistic, conceptual, or metaphysical.

## Common Misconceptions
Vagueness is just ignorance about precise facts—epistemicists say this, but contextualists and fuzzy-logic theorists deny it. Vagueness shows language is defective—many argue it's a feature, allowing flexible, context-responsive reference.

## Questions

```yaml
- question: "A philosopher argues: 'There IS a precise number of grains that separates a heap from a non-heap — we simply cannot know what that number is.' Which response to the sorites paradox does this represent?"
  type: multiple-choice
  options:
    - "Degree-theoretic (fuzzy logic) — truth comes in gradations rather than sharp cutoffs"
    - "Contextualism — the threshold shifts depending on the conversational context"
    - "Semantic indeterminacy — 'heap' has no determinate extension in borderline cases"
    - "Epistemicism — sharp thresholds exist but are unknowable in principle"
  answer: 3
  explanation: "This is epistemicism (associated with Tim Williamson). It preserves classical logic by insisting that every predicate has a precise extension — including vague ones. The vagueness is in our epistemic access, not in reality or meaning. This is the only response that leaves classical logic fully intact, but at the cost of postulating precise thresholds that seem metaphysically arbitrary and permanently unknowable."

- question: "What makes the sorites paradox a genuine paradox rather than just a bad argument?"
  type: multiple-choice
  options:
    - "The conclusion is obviously false, so the premises must also be false"
    - "The argument is logically valid and the premises seem plausible, yet the conclusion is absurd"
    - "The argument relies on circular reasoning that most people fail to notice"
    - "The paradox only applies to physical objects, not abstract predicates"
  answer: 1
  explanation: "A paradox is a valid argument with apparently true premises that yields an unacceptable conclusion. The sorites has valid logical form (modus ponens applied repeatedly) and both premises seem reasonable: 10,000 grains is a heap, and removing one grain cannot make the difference. Yet the conclusion — that one grain is a heap — is clearly false. The paradox forces us to reject at least one premise or classical logic itself, but none of the options is obviously wrong. That tension is what makes it genuinely paradoxical."

- question: "Epistemicism preserves classical logic by accepting that vague predicates have sharp, determinate extensions even if those boundaries cannot be known."
  type: true-false
  answer: true
  explanation: "Epistemicism (Williamson) holds that 'bald' has a precise threshold — some exact hair count — but that this threshold is unknowable, even in principle. This lets epistemicists keep the law of excluded middle and bivalence intact: every person is either bald or not bald. The cost is metaphysical: it requires postulating precise thresholds that nothing in our linguistic practices seems to fix."

- question: "Vagueness and ambiguity are the same phenomenon: both arise when a word's meaning is unclear."
  type: true-false
  answer: false
  explanation: "Vagueness and ambiguity are distinct. Ambiguity means a word has multiple distinct meanings (e.g., 'bank' means river bank or financial institution). Vagueness means a word has ONE meaning that lacks a sharp boundary between cases where it applies and cases where it doesn't. 'Bald' is vague — it has one meaning, but no precise cutoff. 'Bank' is ambiguous — it has two meanings. The philosophical problems they pose are entirely different."

- question: "Why is the sorites paradox philosophically troubling, and what does it reveal about the classical semantic picture of language?"
  type: short-answer
  answer: "The sorites paradox is troubling because it forces a choice between rejecting a plausible premise (the tolerance principle: one hair cannot make the difference between bald and not bald) and accepting an absurd conclusion (a single grain is a heap). The classical semantic picture assumes every predicate has a sharp extension and every statement is determinately true or false (bivalence). Vagueness challenges this: natural language predicates seem to genuinely lack sharp boundaries, yet the classical picture cannot accommodate borderline cases without either positing unknowable thresholds or abandoning bivalence."
  explanation: "Each response to the paradox pays a cost: epistemicism gets unknowable thresholds; semantic indeterminacy gives up bivalence; degree theory must explain why accumulated tiny truth-value drops eventually license a clearly false conclusion; contextualism must explain whether threshold shifts are principled. No response is cost-free, which reveals that the classical framework may simply not fit the structure of natural language vague predicates."
```

## Explainer

Many predicates in natural language — "bald," "tall," "red," "old," "heap," "rich" — admit of clear positive cases, clear negative cases, and a murky borderline region in between. A man with no hair at all is definitely bald; a man with a full head of hair is definitely not bald; a man with thinning hair at the crown is... unclear. This characteristic of predicates is called **vagueness**: the predicate does not draw a sharp line dividing the world into cases where it applies and cases where it does not. Notice that this is different from ambiguity — "bald" has one meaning, not two — but the single meaning does not determine a precise boundary.

The **Sorites Paradox** (from *soros*, Greek for "heap") exploits vagueness to generate a contradiction. Take the predicate "is a heap." Consider a pile of 10,000 grains of sand — clearly a heap. Now apply the following plausible principle: *if something is a heap, removing one grain of sand still leaves a heap.* One grain makes no perceptible difference; surely that cannot be the grain that turns a heap into a non-heap. Applying this principle 9,999 times, we conclude that a single grain of sand is a heap — which is absurd. The argument is logically valid given its premises, and both premises seem highly reasonable. Yet the conclusion is false. Something must go, but it is not clear what.

The possible responses each pay a different philosophical price. **Epistemicism** (Tim Williamson's position) bites the bullet on sharp boundaries: there *is* a precise number of hairs that separates the bald from the non-bald — we just cannot know what it is, and cannot know it even in principle. Vagueness is not a feature of the world or of meaning; it is pure **ignorance** about a precise fact. This preserves classical logic but at the cost of postulating unknowable sharp thresholds that seem metaphysically weird. **Semantic indeterminacy** approaches deny that there is any precise fact: the word "bald" does not have a determinate extension in borderline cases. But then the sorites premise — "removing one grain leaves a heap" — cannot be straightforwardly true, because truth requires determinacy.

**Degree-theoretic** approaches (fuzzy logic) replace the binary true/false with a continuum of truth values between 0 and 1. "Bald" is true to degree 0.9 of a nearly-hairless person, true to degree 0.4 of a moderately thinning person, and true to degree 0 of someone with thick hair. The sorites premise is then almost-but-not-exactly true at every step — close enough to seem plausible, but the accumulated error eventually adds up to permit a clearly false conclusion. **Contextualism** takes a different tack: what counts as bald varies with the context of conversation, the conversational standards in play. When we are talking about cancer patients, the threshold for "bald" shifts relative to a conversation about competitive swimmers. The paradox is blocked because the standard shifts as the series progresses.

Each response raises further questions. The epistemicist owes us an account of what fixes the precise threshold given that we cannot know it. The indeterminist must explain what happens to the law of excluded middle (every proposition is either true or not). The degree theorist must explain why we should not then be satisfied calling a single grain a heap to degree 0.00001. The contextualist must explain whether the shifts are arbitrary or principled. What the Sorites Paradox ultimately reveals is that the classical semantic picture — every predicate has a sharp extension, every statement is determinately true or false — may not fit natural language as well as we assumed. Whether vagueness is a defect to be engineered away or a feature that makes language usefully flexible is itself a question worth taking seriously.

