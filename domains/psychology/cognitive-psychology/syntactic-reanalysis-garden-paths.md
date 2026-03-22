---
id: syntactic-reanalysis-garden-paths
title: Syntactic Reanalysis and Garden-Path Phenomena
domain: psychology
course: cognitive-psychology
prerequisites:
- id: language-comprehension
  type: hard
- id: sentence-comprehension-parsing
  type: hard
builds-toward:
- pragmatic-implicature-context
tags:
- language
- syntax
- parsing
- reanalysis
stage: advanced
status: draft
---

# Syntactic Reanalysis and Garden-Path Phenomena

## Core Idea
In garden-path sentences (e.g., 'The horse raced past the barn fell'), initial parsing commits to an incorrect syntactic structure ('the horse raced past the barn' as the main clause) only to require reanalysis when new evidence mounts ('fell' indicates the horse is the subject of a reduced relative clause). Garden-path effects reveal that parsing is incremental and initially commits to the most frequent or simple interpretations, later correcting when evidence mandates. The revision process shows parsing is not purely bottom-up or top-down but interactive.

## How It's Best Learned
Use self-paced reading where participants advance through garden-path sentences word-by-word, showing increased reading times at reanalysis points. Contrast with non-ambiguous control sentences and sentences biasing the correct initial parse to isolate reanalysis costs.

## Common Misconceptions
- Assuming the parser considers all syntactically possible interpretations simultaneously; the garden-path effect shows the parser commits early.
- Treating reanalysis failures as processing deficits; garden-path phenomena occur in skilled readers and reflect optimal strategies given frequency distributions.

## Questions

```yaml
- question: "A researcher measures reading times for 'The horse raced past the barn fell' vs. 'The horse that was raced past the barn fell.' What result is expected and what does it reveal about the parser?"
  type: multiple-choice
  options:
    - "Longer reading times specifically at 'fell' in the garden-path version, showing the parser had committed to an incorrect early parse that must be rebuilt"
    - "Shorter reading times on the garden-path version, because it is syntactically simpler"
    - "Equal reading times on both, because skilled readers consider all possible parses simultaneously until disambiguated"
    - "Slower reading times throughout the garden-path version, because reduced relative clauses are uniformly harder"
  answer: 0
  explanation: "The reading-time spike specifically at 'fell' — the disambiguating word — is the signature of reanalysis. By 'barn,' the parser had committed to 'The horse raced past the barn' as a complete simple sentence; 'fell' then forces a total structural rebuild. The control sentence ('that was raced') explicitly marks the relative clause from the start, so no reanalysis is required and reading time at 'fell' is normal. The localization of difficulty at the disambiguation point proves the parser committed early rather than tracking all parses in parallel."

- question: "Why do garden-path processing failures occur even in highly skilled, expert readers?"
  type: multiple-choice
  options:
    - "Skilled readers are overconfident and skip re-reading; less skilled readers slow down and avoid the garden path"
    - "The parser uses a frequency-based greedy strategy that bets on the most probable parse at each decision point — a strategy that is efficient overall despite occasional errors on rare constructions"
    - "The parser is a purely syntactic module that ignores meaning and context until the full sentence is available"
    - "Garden-path errors reflect short-term memory limitations that expert readers overcome with practice"
  answer: 1
  explanation: "Simple active constructions like 'The horse raced past the barn [and stopped]' are far more frequent in natural language than reduced relative constructions. The parser has internalized these statistics and commits to the most probable parse at each word — a strategy that is correct the overwhelming majority of the time. Garden-path sentences are the rare cases where this bet loses. The effect in skilled readers is not a failure of skill; it is the measurable cost of an efficient probabilistic strategy that cannot be eliminated without sacrificing its benefits on the common case."

- question: "Garden-path effects reveal that the language parser commits to a specific syntactic interpretation incrementally rather than maintaining all possible parses in parallel."
  type: true-false
  answer: true
  explanation: "If the parser held all syntactic possibilities open simultaneously, there would be no special processing cost when the disambiguating word arrived — the system would simply select the correct parse from already-active candidates. The empirically observed spike in reading time specifically at the disambiguation point is direct evidence of prior commitment to a single parse. That commitment is what makes reanalysis costly: the parser must discard the invested structure and rebuild."

- question: "Garden-path sentence failures in skilled readers indicate that the human parsing system is poorly designed, since an optimal system would never require reanalysis."
  type: true-false
  answer: false
  explanation: "Garden-path effects are a consequence of an efficient, well-calibrated probabilistic strategy — not a design flaw. A parser that considered all possible syntactic interpretations at every word to avoid any reanalysis would be computationally far more expensive for the vast majority of sentences, which are unambiguous or resolved by context. The garden-path effect is the small, tolerable cost of a greedy strategy that is correct the overwhelming majority of the time. Skilled readers show the effect because the strategy is working as intended."

- question: "A sentence is syntactically ambiguous until its final word. Explain why this surface ambiguity does not mean the parser suspends judgment — and what experimental evidence demonstrates this."
  type: short-answer
  answer: "Despite ambiguity, the parser commits immediately to the most probable parse rather than tracking multiple interpretations. The evidence: reading time increases are localized specifically at the disambiguating word (e.g., 'fell' in 'The horse raced past the barn fell'), not distributed across the whole sentence. If the parser had kept both parses active throughout, disambiguation would require no extra processing — it would simply select among already-computed options. The concentrated difficulty at the disambiguation point shows commitment occurred earlier, before the disambiguating information arrived."
  explanation: "This is the central diagnostic logic of garden-path research: the timing of the reading-time increase isolates exactly when commitment occurred and confirms that the parser does not behave like an exhaustive search algorithm. Early commitment is the computationally efficient choice given natural language statistics; garden-path sentences are the rare cases engineered to make that commitment costly."
```

## Explainer

From sentence comprehension and parsing, you know that the language comprehension system assigns syntactic structure to incoming words incrementally — it doesn't wait for the full sentence before beginning to build a parse. This incremental commitment is normally efficient because most sentences are unambiguous, and starting to build structure early means that by the time the sentence ends, processing is nearly complete. **Garden-path sentences** are the diagnostic case that reveals the cost of this strategy: they are constructed so that the most probable early parse turns out to be wrong, forcing the system to backtrack and rebuild.

The canonical example deserves careful unpacking word by word. *"The horse raced past the barn fell."* The parser begins: "The horse" → noun phrase, subject of the sentence. "raced" → simple past verb; "The horse raced..." looks like the main clause structure is underway. "past the barn" → prepositional phrase modifying the path of racing. By "barn," the parser has constructed a complete sentence: *The horse raced past the barn.* Then "fell" arrives. This is catastrophic: "fell" is a verb that needs a subject, and "the horse" is already taken as the agent of "raced." The parser must radically revise its analysis: "raced past the barn" is not the main predicate — it is a **reduced relative clause** (equivalent to "that was raced past the barn"), and "the horse" is not the agent of racing but the subject of the main verb "fell." The horse fell. It was the horse that was raced. This reanalysis is cognitively expensive and measurable.

Why does the parser commit to the wrong analysis in the first place? Because it is implementing a **frequency-based greedy strategy**. Simple active sentences ("The horse raced past the barn [and then stopped]") are far more common in natural language than reduced relative clause constructions ("The horse [that was] raced past the barn [by the jockey] fell"). The parser has internalized these frequency statistics and bets on the most probable parse at each decision point. This strategy is correct the overwhelming majority of the time — the cost of occasionally being wrong on garden-path sentences is outweighed by the efficiency gained on the far more common simple sentences. The garden-path effect is not a bug; it is the price of a well-calibrated probabilistic strategy operating on the rare case where its bet turns out to be wrong.

The **reanalysis process** itself is revealing. Self-paced reading studies show elevated reading times specifically at the disambiguating word ("fell") — sometimes 200–400 ms longer than on matched non-ambiguous controls. This is the measurable signature of the parser backtracking, discarding its previous structure, and rebuilding. Not all garden paths are equally costly: reanalysis is easier when the revision is local (affecting only the most recent phrase) and harder when it requires restructuring the entire sentence. Some garden-path sentences are so difficult that they remain partially unintelligible even after extended processing — readers can tell something is wrong without fully recovering the correct structure. This asymmetry tells us that reanalysis is not free, unlimited re-parsing but a costly, sometimes incomplete process.

Parsing is not purely syntactic — **contextual and semantic information modulates garden-path strength**. If preceding context makes the reduced relative reading more probable (you've been reading a story about horse racing), the garden-path effect is attenuated. If lexical information makes the verb more likely to appear in relative clauses (verbs with passive-favorable semantics), the effect is smaller. This interactivity shows that the parser is not an isolated syntactic module but a probabilistic system integrating multiple information sources simultaneously. The garden-path paradigm contributed to a decades-long debate about whether parsing is initially modular (pure syntax first, then semantics) or interactive (all information in parallel from the start). Current consensus favors interactive accounts: the parser is a flexible probabilistic machine, and the "commitment" to an early parse is not a hard syntactic rule but a weighted bet that stronger contextual evidence can override.
