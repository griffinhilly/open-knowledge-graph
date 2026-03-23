---
id: derivational-morphology
title: Derivational Morphology
domain: language-and-communication
course: linguistics
prerequisites:
- id: morpheme-types
  type: hard
- id: morphological-structure
  type: hard
tags:
- derivation
- affixation
- compounding
- conversion
- productivity
- blocking
stage: formal-systems
status: validated
---

# Derivational Morphology

## Core Idea
Derivational morphology studies the processes by which new words are created from existing morphemes, typically changing the meaning, the lexical category, or both. Affixation is the most common strategy — prefixes (un-, re-, pre-) and suffixes (-ness, -ize, -able) attach to bases to form new lexemes. Compounding combines two or more free morphemes into a single word (blackboard, earthquake), while conversion (or zero-derivation) shifts a word's category without any overt marking (to email from email, to Google from Google). Derivational processes vary in productivity — some affixes actively generate new words (un-Xable is highly productive), while blocking prevents a derivation when an established form already fills the semantic niche (the existence of "thief" blocks "*stealer" in standard usage).

## How It's Best Learned
Take a complex derived word like "unbelievability" and peel it apart layer by layer, identifying the base and each affix in the order it was attached. Test the productivity of affixes by trying to coin new words (un-X, re-X, X-ize) and noticing which combinations feel natural and which feel strange. Compare English derivational morphology with a polysynthetic language like Mohawk to see how dramatically derivational capacity can vary.

## Common Misconceptions
- Derivational affixes do not simply add meaning mechanically — the meaning of a derived word often drifts from what the parts would predict (a "department" is not someone who departs).
- Not all derivation involves affixes — compounding and conversion are equally important word-formation processes that operate without adding bound morphemes.
- Productivity is gradient, not binary; affixes range from fully productive (creating new words freely) to completely fossilized (surviving only in existing words like the "-th" in "warmth").

## Questions

```yaml
- question: "A speaker coins '*thievage' to mean 'the practice of stealing,' but native speakers reject it in favor of 'theft.' This is best explained by:"
  type: multiple-choice
  options:
    - "The suffix -age being completely unproductive in English"
    - "Blocking — the established word 'theft' already occupies the semantic slot"
    - "Compounding being preferred over suffixation for abstract nouns"
    - "'Theft' being a converted form of the verb 'to thieve'"
  answer: 1
  explanation: "Blocking occurs when an existing word preempts a derived competitor. The derivational process that would produce '*thievage' is grammatically possible — -age is a productive suffix (drainage, seepage, breakage) — but 'theft' has already claimed the niche for 'act of stealing.' The mental lexicon acts like real estate: once a slot is taken, the derivational rule is suppressed even though it remains structurally available. Blocking explains why the morphological system is partly systematic and partly arbitrary."

- question: "Adding '-ness' to 'happy' to create 'happiness' is a derivational process rather than an inflectional one primarily because:"
  type: multiple-choice
  options:
    - "'-ness' attaches after the base rather than before it"
    - "It creates a new word (lexeme) with a different grammatical category — adjective becomes noun"
    - "Inflectional morphology only applies to verbs and nouns, not adjectives"
    - "The resulting word 'happiness' has a completely unpredictable meaning"
  answer: 1
  explanation: "The hallmark of derivational morphology is creating a new lexeme — a new word that takes its own place in the mental lexicon, often with a different grammatical category. 'Happiness' is a noun; 'happy' is an adjective. Adding -ness changes the syntactic distribution, the meaning type, and opens new morphological possibilities (e.g., you can further derive 'unhappiness'). Inflectional morphology, by contrast, marks grammatical features (tense, number, case) without changing the word's basic category or lexical identity."

- question: "The meaning of a derived word can always be reliably predicted by combining the meanings of its component morphemes."
  type: true-false
  answer: false
  explanation: "Lexicalization causes derived words to drift semantically from their compositional meaning. A 'department' is not a group of people who depart; a 'deadline' has nothing to do with death; 'understand' does not mean to stand under. Once a derived word is stored as a unit in the mental lexicon, its meaning can shift through use, metaphor, and cultural change. This semantic opacity is especially common in compounding but occurs in affixation too. Productive, newly coined forms tend to be more compositionally transparent; established, lexicalized forms often are not."

- question: "Conversion (zero-derivation) is a legitimate derivational process even though it adds no phonological material to the base form."
  type: true-false
  answer: true
  explanation: "Conversion shifts a word's grammatical category without any overt affix. 'Email' (noun) → 'to email' (verb); 'Google' (proper noun) → 'to google' (verb); 'bottle' (noun) → 'to bottle' (verb). The word gains new syntactic distribution and morphological behavior (it can now be inflected for tense: emailed, emailing) purely through a change in category assignment. Derivation is defined by the creation of a new lexeme, not by the requirement that an affix be audible — the derivation is phonologically empty but grammatically real."

- question: "What is 'blocking' in derivational morphology, and why does it mean that derivational rules don't generate all the words they theoretically could?"
  type: short-answer
  answer: "Blocking is the phenomenon where an established word in the mental lexicon prevents a derived word from being coined to fill the same semantic slot. Even when a derivational rule is productive, its output is suppressed if a pre-existing word already occupies that niche. 'Singer' exists, so '*songster' is blocked for the same meaning. 'Theft' exists, so '*stealage' is blocked. The rule remains grammatically possible — the block is lexical, not structural."
  explanation: "Blocking explains a core puzzle: if derivational rules are productive, why aren't there far more derived words in the lexicon? The answer is that productivity operates against the existing vocabulary. Every new derivation must find an unoccupied semantic slot; where one is already claimed, the derivation is preempted. This makes the lexicon feel partly rule-governed (new words can be coined) and partly arbitrary (many theoretically possible forms simply don't exist). The degree of blocking varies — it's stronger for near-synonyms and weaker when the new form adds nuance the established word lacks."
```

## Explainer

From your prerequisite study of morpheme types and morphological structure, you know that words are composed of **morphemes** — the smallest meaningful units — and that these morphemes can be free (capable of standing alone) or bound (requiring attachment to another morpheme). Derivational morphology asks: how does the language engine *create new words* by manipulating these building blocks? The answer involves three core processes, each exploiting different properties of the morphological system.

**Affixation** is the most visible process. A **prefix** attaches before the base (un-happy, re-write, pre-heat) and typically shifts meaning without changing grammatical category — "un-happy" is still an adjective, just negated. A **suffix** attaches after the base and often does change the category: the adjective "happy" becomes the noun "happiness" (adding -ness), or the noun "terror" becomes a verb "terrorize" (adding -ize). This category-changing property is the defining feature of derivational affixes — they derive a new *lexeme*, a word with its own place in the mental lexicon, its own meaning, and its own syntactic distribution. You can stack derivations: "beauty" (noun) → "beautiful" (adjective, -ful) → "beautify" (verb, -ify) → "beautification" (noun, -ation). Each step creates a new word via a new derivational rule.

**Compounding** builds words from two or more free morphemes: "black" + "board" = "blackboard," "sun" + "flower" = "sunflower," "police" + "man" = "policeman." The compound is a new lexeme with its own meaning — crucially, a meaning that is often not fully predictable from the parts. A "blackboard" need not be black; a "deadline" has nothing to do with death in most contexts. This **semantic opacity** is the signature of a compound that has been lexicalized — stored as a unit in the mental lexicon rather than computed fresh each time. **Conversion** (or zero-derivation) takes the process to its limit: the word shifts category without any overt marking at all. "Email" was a noun; now it's also a verb ("I'll email you"). "Google" became a verb ("Just Google it"). The word has gained new syntactic distribution without any morphological change — the derivation is phonologically empty but grammatically real.

**Productivity** is the measure of how freely an affix generates new words. The affix -able is highly productive: given any transitive verb, you can plausibly coin a new -able word (printable, searchable, crashable). The affix -th (as in warmth, strength, depth) is completely fossilized — you cannot coin new -th words with any expectation they'll be accepted. **Blocking** is the phenomenon that limits productivity: an established word occupying a semantic slot prevents a derived competitor from filling it. "Theft" blocks "*stealage"; "singer" might block "*songster." The mental lexicon acts like a real-estate market — once a slot is claimed, the derivational process that would create a competitor is suppressed, even though it remains grammatically possible. Blocking and productivity together explain why derivational morphology feels partly systematic and partly arbitrary: the rules are productive, but they operate against a backdrop of established vocabulary that redirects and constrains them.
