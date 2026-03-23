---
id: parsing-preferences-complexity
title: Parsing Preferences and Computational Complexity
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: psycholinguistics-intro
  type: hard
- id: sentence-parsing-garden-paths
  type: soft
tags:
- parsing
- preferences
- complexity
stage: expert
status: draft
---

# Parsing Preferences and Computational Complexity

## Core Idea
Parsers exhibit biases toward simpler structures and frequent constructions. Minimal attachment (attaching phrases as low as possible) and late closure (attaching new material to recent constituents) govern initial parsing. Working memory limitations affect how many open dependencies can be maintained; high dependencies (long-distance relative clauses) are harder than low dependencies. Parsing preferences interact with grammatical constraints and input frequency to determine comprehension difficulty.

## How It's Best Learned
Predict parsing preferences for ambiguous sentences and test with reading-time experiments. Manipulate complexity factors (embedding depth, number of dependencies) and measure comprehension difficulty.

## Common Misconceptions
- Parsing preferences are not hard constraints; they bias initial analysis but can be overcome by strong cues.
- Working memory limitations are not absolute; they vary by individual and interact with linguistic factors.

## Questions

```yaml
- question: "Consider two sentences: (A) 'The reporter who attacked the senator resigned.' (B) 'The reporter that the senator attacked resigned.' Both are grammatical. Research consistently shows sentence (A) is processed faster. What is the primary reason?"
  type: multiple-choice
  options:
    - "Sentence (A) uses 'who' while (B) uses 'that,' and 'who' is a simpler relative pronoun."
    - "Sentence (A) is a subject relative clause where the dependency is shorter and more frequent; sentence (B) is an object relative clause with a longer dependency and an intervening noun phrase."
    - "Sentence (B) is grammatically marked as passive voice, which always increases processing difficulty."
    - "Sentence (A) follows late closure more strictly, while (B) violates it, causing a reanalysis penalty."
  answer: 1
  explanation: "This is the classic subject-relative vs. object-relative asymmetry. In (A), 'reporter' is the subject of the relative clause ('reporter attacked senator') — short dependency, frequent structure. In (B), 'reporter' is the object of 'attacked' while 'senator' intervenes as subject — a longer dependency that must be held in working memory while more material is processed. The difficulty is driven by dependency distance and structural frequency, not the relative pronoun used or voice."

- question: "Which principle best explains why a parser initially analyzes 'The horse raced past the barn fell' as meaning the horse raced past the barn, rather than recognizing it as a passive reduced relative clause?"
  type: multiple-choice
  options:
    - "The parser applies minimal attachment, preferring 'raced' as the main verb requiring no additional syntactic structure."
    - "The parser applies late closure, attaching 'barn' to the most recently opened noun phrase."
    - "The parser has insufficient working memory to track the subject 'horse' while processing 'raced.'"
    - "The parser expects passive voice to be marked overtly, and reduced relatives violate this expectation."
  answer: 0
  explanation: "Minimal attachment drives the initial misanalysis: the parser attaches 'raced' as the main verb (the simplest structure, requiring the fewest syntactic nodes) rather than as the beginning of a reduced relative clause. The reduced relative clause analysis requires opening an additional S-node for the embedded clause, which minimal attachment avoids unless forced. When 'fell' arrives, it cannot be the main verb because 'raced' already filled that role — the parser must revise, producing the garden-path effect."

- question: "Object relative clauses are harder to process than subject relative clauses because they are grammatically incorrect in standard English."
  type: true-false
  answer: false
  explanation: "Both subject and object relative clauses are grammatically well-formed. The difficulty is a processing phenomenon, not a grammaticality judgment. Object relative clauses are harder because they create a longer dependency distance — the relativized element is in object position, separated from the head noun by an intervening subject NP — and are less frequent in natural language. The parser experiences measurable reading-time increases and higher error rates, but not because they violate grammar."

- question: "Center-embedded sentences like 'The reporter that the senator that the lobbyist attacked accused ran' are difficult to process because maintaining multiple open dependencies simultaneously exhausts working memory."
  type: true-false
  answer: true
  explanation: "Center-embedding stacks relative clauses inside each other, forcing the parser to hold multiple incomplete dependencies open simultaneously: 'reporter' waits for its verb ('ran'), 'senator' waits for its verb ('accused'), and 'lobbyist attacked' must be resolved — all before any of the main clause verbs arrive. Working memory capacity limits how many open dependencies can be maintained. Native speakers typically fail to process more than two levels of center-embedding, demonstrating that grammatical competence does not predict processing ease."

- question: "Why does dependency distance predict parsing difficulty better than sentence length alone?"
  type: short-answer
  answer: "Sentence length doesn't capture what actually strains the parsing system: the burden of holding an open, unresolved dependency in working memory while processing intervening material. A long sentence where each dependency is quickly resolved is easy; a short sentence where a single dependency spans many intervening words is hard. Dependency distance measures the actual memory load — how many words must be processed between an element and the word it depends on. Long-distance dependencies are hard because they force the parser to maintain incomplete structures in memory for longer."
  explanation: "This is why the subject/object relative clause asymmetry is such a clean demonstration: both sentence types have very similar lengths, but their dependency structures differ — subject relatives resolve the dependency quickly, object relatives stretch it across an intervening noun phrase. The processing cost maps onto the dependency structure, not the surface length. This also explains why scrambled or topicalized constructions in flexible word-order languages create processing costs without adding words."
```

## Explainer

From your psycholinguistics background and work with garden-path sentences, you know that parsing is not a neutral process of recovering structure — the parser has preferences, and those preferences create predictable patterns of difficulty. The study of parsing preferences and computational complexity maps those patterns systematically: why are some sentences easy to understand even when they are long, while others are difficult even when they are short?

The two most studied parsing preferences are **minimal attachment** and **late closure**. Minimal attachment means the parser attaches incoming material using the fewest additional syntactic nodes possible — preferring to extend an existing phrase rather than open a new one. Late closure means the parser prefers to attach new words to the most recently opened syntactic constituent rather than closing it and opening a new phrase. These are both efficiency heuristics: they minimize the structural complexity the parser must track at any moment. The preferences usually produce correct results, but when they lead to the wrong analysis (as in garden paths), the parser must revise — and the cost of revision is what makes complexity measurable.

**Working memory** is the resource constraint that underlies many complexity effects. Parsing requires simultaneously maintaining an incomplete structure in memory while integrating new words into it. The key variable is **dependency distance**: how far apart are the words that must be linked for the sentence to be understood? In a simple sentence (*The cat chased the mouse*), the verb and its arguments are close together. In a **center-embedded** clause (*The reporter that the senator that the lobbyist attacked accused ran*), the main verb *ran* is separated from its subject *reporter* by two intervening clauses — the dependency must be held open across multiple intervening words. Sentences with long, overlapping dependencies are dramatically harder to process than sentences where dependencies are short and resolved quickly, even when both are grammatical.

This explains an otherwise puzzling asymmetry: **subject relative clauses** (*The reporter who attacked the senator*) are consistently easier than **object relative clauses** (*The reporter that the senator attacked*), even though both are grammatical. In the subject relative, the relativized element (*reporter*) is in the same position it would occupy in a simple sentence (subject). In the object relative, the relativized element is in the object position while the subject of the relative clause intervenes — creating a longer dependency and a less frequent structural pattern. Processing difficulty tracks both **dependency length** (how long a gap must be held in memory) and **frequency** (how often this structure type appears in input). High-frequency structures are faster because the parser has acquired stronger expectations for them. This interaction between memory constraints and input statistics makes parsing complexity a window into both the architecture of the parsing system and the statistical structure of the language learner's environment.
