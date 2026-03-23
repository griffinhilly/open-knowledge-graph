---
id: sentence-comprehension-parsing
title: Sentence Comprehension and Parsing
domain: psychology
course: cognitive-psychology
prerequisites:
- id: word-recognition-lexical-access
  type: hard
- id: syntax-and-grammar-acquisition
  type: hard
builds-toward:
- mental-model-construction
tags:
- language
- comprehension
- parsing
- syntax
stage: formal-systems
status: validated
---

# Sentence Comprehension and Parsing

## Core Idea
Sentence comprehension involves parsing grammatical structure and integrating meaning. Garden-path sentences reveal that parsing is not always optimal: readers initially commit to one structural interpretation, then must revise when encountering contradictory information. This demonstrates the role of expectancy and immediate processing in comprehension.

## Questions

```yaml
- question: "Most readers stumble on the final word of 'The horse raced past the barn fell.' What does this garden-path effect reveal about sentence parsing?"
  type: multiple-choice
  options:
    - "Readers wait until the sentence is fully heard before assigning grammatical structure"
    - "The parser immediately commits to one structural interpretation and must expensively reanalyze when that interpretation fails"
    - "Readers rely on semantic plausibility to correctly assign structure in real time, preventing such errors"
    - "The sentence violates universal grammar constraints and is therefore unprocessable"
  answer: 1
  explanation: "The garden-path effect is direct evidence that parsing is incremental and immediate, not optimal and wait-and-see. The parser applies a minimal-attachment heuristic — treating 'raced' as the main verb — before reaching 'fell,' which makes that analysis impossible. At 'fell,' costly reanalysis must occur, producing the characteristic reading disruption. If readers waited for all input before assigning structure, garden-path effects would not exist. Eye-tracking confirms this: fixation times and regressions spike at the disambiguating word."

- question: "Center-embedded sentences like 'The reporter that the senator that the lobbyist attacked praised wrote the story' are nearly incomprehensible despite being grammatical. The best explanation is:"
  type: multiple-choice
  options:
    - "They use unusual vocabulary that readers haven't encountered before"
    - "The parser applies different grammatical rules to multiple levels of embedding"
    - "Maintaining partially-built syntactic structures across multiple interrupting clauses exhausts working memory capacity"
    - "Center-embedding beyond one level violates syntactic rules in most languages"
  answer: 2
  explanation: "Center-embedding requires holding the first noun phrase ('reporter') available in working memory across two interrupting clauses before the main verb ('wrote') finally arrives. Each additional level of embedding adds another unresolved dependency that must be maintained simultaneously. This rapidly exceeds the capacity of working memory — not because anything is grammatically wrong, but because the parser's workspace has finite capacity. Right-branching sentences with equivalent complexity are easy because each clause can be resolved before the next begins, avoiding simultaneous storage demands."

- question: "Syntax-first models of parsing (like Frazier's garden-path theory) claim that the parser initially uses all available information — including semantic plausibility, discourse context, and word frequency — to build sentence structure."
  type: true-false
  answer: false
  explanation: "Syntax-first models claim the opposite: the parser uses only syntactic information to build an initial structure, applying heuristics like minimal attachment without consulting semantics or context. Semantic plausibility and context are consulted only after an initial structural analysis is complete. This is exactly what produces garden-path effects in semantically implausible or contextually inappropriate sentences. Interactive models challenge this by arguing that all information is used simultaneously from the start — but evidence supports a nuanced middle ground where syntax has priority, not exclusivity."

- question: "Garden-path effects, as measured by longer fixation times and backward regressions in eye-tracking studies, provide evidence that the parser commits to an initial structural interpretation before the sentence is complete."
  type: true-false
  answer: true
  explanation: "Eye-tracking during reading allows millisecond-level measurement of where readers look and for how long. At the disambiguating word in a garden-path sentence, fixation times spike and regressions (backward eye movements) increase — behavioral signatures of reanalysis. If the parser held multiple interpretations open simultaneously (a parallel parser), we would expect little or no disruption at the disambiguating word. The consistent disruption is strong evidence for serial commitment to an initial parse followed by effortful reanalysis."

- question: "Why does the garden-path effect challenge the idea that sentence parsing is an optimal, wait-and-see process? What does it reveal about how the parser actually works?"
  type: short-answer
  answer: "The garden-path effect shows that the parser commits to one structural interpretation immediately, before sufficient information is available to guarantee that interpretation is correct. It applies syntactic heuristics (like minimal attachment) incrementally, word by word, rather than waiting for more input. When the initial interpretation turns out to be wrong — as 'fell' reveals in 'The horse raced past the barn fell' — the parser must abandon its committed analysis and reanalyze from scratch, a cognitively costly process. An optimal, wait-and-see parser would hold multiple structural hypotheses open until disambiguating information arrived, and would therefore show no disruption at the disambiguating word. Garden-path effects prove this doesn't happen."
  explanation: "The deeper implication is that the parser trades correctness for speed: immediate commitment is faster and requires less memory than holding multiple parses open, but it fails on structurally unusual sentences. This reflects a general principle in cognitive psychology — the mind uses heuristics that are fast and usually right, at the cost of systematic errors in specific cases. The garden-path effect is one of the cleanest demonstrations of this tradeoff in language processing."
```

## Explainer

From your word recognition prerequisite, you know how the mind accesses individual words from the mental lexicon — recognizing form, retrieving meaning, and activating syntactic information within a few hundred milliseconds. But understanding language involves far more than recognizing words in sequence: the meaning of a sentence is not a sum of word meanings, but a function of *structure*. "The dog bit the man" and "The man bit the dog" use the same words to mean different things. **Parsing** is the process of assigning grammatical structure to incoming words — identifying which noun phrase is the subject, which verb is the main verb, which clause modifies which — and doing so incrementally as each word arrives, before the sentence is complete.

The **garden-path effect** is the signature phenomenon showing that parsing commits to one interpretation immediately rather than waiting for more information. Consider: *"The horse raced past the barn fell."* Most readers stumble at "fell" — this is a grammatically correct sentence (reduced relative clause: "The horse [that was] raced past the barn fell"), but the parser had committed to analyzing "raced" as the main verb, not as a participle. When "fell" arrives and is uninterpretable under the initial analysis, the parser must **reanalyze** — a cognitively effortful, time-consuming process that produces characteristic delays measurable in eye-tracking studies as longer fixation times and regressions (backward re-reading). The reader was led down the garden path by the parser's initial (wrong) commitment. Simple examples include: *"The old man the boats"* (where "man" is the verb) or *"Fat people eat accumulates"* (where "eat" is not the main verb).

The core theoretical debate is between **syntax-first (serial) models** and **interactive models**. Syntax-first models (Frazier's garden-path theory) claim that the parser uses only syntactic information to build an initial structure — it applies heuristics like "minimal attachment" (attach each new word with the fewest syntactic nodes) and ignores semantic plausibility and contextual information until structural analysis is complete. If the initial structure fails, reanalysis follows. Interactive models claim that the parser uses all available information simultaneously — syntax, semantics, plausibility, frequency of structural patterns, and discourse context — and so rarely commits to an unambiguously wrong interpretation when plausible alternatives are available. The evidence favors a nuanced middle ground: syntax does constrain early parsing, but discourse context and lexical probabilities (knowing that "raced" rarely introduces a relative clause) bias the initial analysis and can prevent garden-pathing in rich enough contexts.

Working memory plays a crucial role in parsing complex structures. **Center-embedded sentences** — those with a relative clause that interrupts the main clause, which can itself be interrupted — rapidly exceed parsing capacity: "The reporter [that the senator [that the lobbyist attacked] praised] wrote the story." Understanding this sentence requires keeping the first subject ("reporter") available across two interrupting clauses before the main verb ("wrote") finally arrives. Capacity-limited working memory is why center-embedding beyond one or two levels becomes nearly incomprehensible even for speakers who understand all the words and know the grammatical rules. This connects your syntax knowledge to the working memory model: parsing is an on-line process that must hold partially built structures in working memory while integrating each new word, and the same capacity constraints that limit other cognitive operations limit comprehension of structurally complex language.
