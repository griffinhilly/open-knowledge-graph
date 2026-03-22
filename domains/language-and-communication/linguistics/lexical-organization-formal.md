---
id: lexical-organization-formal
title: Formal Structure of the Mental Lexicon
domain: language-and-communication
course: linguistics
prerequisites:
- id: lexical-semantics
  type: hard
builds-toward:
- lexical-access-word-recognition
tags:
- lexicon
- mental-lexicon
- organization
- structure
stage: formal-systems
status: draft
---

# Formal Structure of the Mental Lexicon

## Core Idea
The mental lexicon formally stores semantic, phonological, syntactic, and pragmatic properties of words. Words are organized by morphological family (run, running, runner), semantic field (emotions: angry, sad, happy), and phonological similarity (rhyming words). Psycholinguistic evidence reveals that lexical entries contain subcategorization frames, argument structures, and selectional restrictions.

## Questions

```yaml
- question: "A fluent English speaker finds 'She persuaded enthusiastically' awkward, even though it's a verb followed by an adverb — a legal grammatical pattern. What explains this?"
  type: multiple-choice
  options:
    - "The sentence is ungrammatical because adverbs cannot follow verbs in English"
    - "The word 'persuade' carries a negative connotation that conflicts with 'enthusiastically'"
    - "The subcategorization frame stored in 'persuade's' lexical entry requires a direct object and complement; an adverb alone cannot satisfy it, making the sentence feel incomplete"
    - "This is a pragmatic oddity — the sentence is grammatically fine but unusual in real contexts"
  answer: 2
  explanation: "Subcategorization frames are part of each verb's lexical entry and specify what complements the verb requires. 'Persuade' demands a direct object (a person) and typically a clausal complement or infinitive — 'I persuaded her to leave.' An adverb alone doesn't fill those slots. The result isn't ungrammatical in a formal sense, but feels broken because the frame is unsatisfied. This is distinct from a pragmatic issue — it stems directly from stored syntactic-semantic information in the lexical entry."

- question: "A speaker experiencing a tip-of-the-tongue state for the word 'cathedral' produces 'catapult' and 'cafeteria' before recovering the target. What does this reveal about the mental lexicon?"
  type: multiple-choice
  options:
    - "The lexicon organizes words by semantic field — cathedrals, catapults, and cafeterias are conceptually related"
    - "The lexicon has a phonological dimension — words sharing onset sounds and stress patterns are linked and can be co-activated during retrieval"
    - "The lexicon organizes words by morphological family — all three words share a common root"
    - "The tip-of-the-tongue state indicates a disorder affecting words beginning with 'ca-'"
  answer: 1
  explanation: "Tip-of-the-tongue states are a window into lexical organization. The words retrieved are phonologically similar (same onset, similar stress and syllable count), not semantically related. 'Catapult' and 'cafeteria' are not in the same semantic field as 'cathedral,' but they share surface sound properties. This reveals that the mental lexicon has an independent phonological organizational layer, and accessing one phonological neighborhood can activate neighboring entries — even when the semantic properties of the target are fully known."

- question: "A verb's selectional restrictions specify which syntactic structures it can appear in — for example, whether it takes a direct object or a complement clause."
  type: true-false
  answer: false
  explanation: "Selectional restrictions are *semantic* constraints on the types of entities that can fill a verb's argument roles — 'devour' requires its patient to be something edible; 'elapse' requires a time subject. Syntactic structural requirements (which complements a verb can take) are encoded in subcategorization frames. The distinction matters because violating a subcategorization frame produces syntactic infelicity, while violating selectional restrictions produces semantic anomaly — which can often be rescued by metaphor ('She devoured the book') in a way that syntactic violations cannot."

- question: "The mental lexicon encodes multiple types of information simultaneously for each word — phonological, morphological, syntactic, and semantic — all of which can influence how words are recognized and retrieved."
  type: true-false
  answer: true
  explanation: "Psycholinguistic evidence from priming studies, tip-of-the-tongue states, and speech errors converges on a multi-dimensional view of the lexicon. Phonological priming (similar-sounding words speed each other's recognition), morphological priming (seeing 'run' speeds recognition of 'runner'), and semantic priming (seeing 'doctor' speeds recognition of 'nurse') all operate in parallel. The mental lexicon is not a dictionary indexed only by meaning — it is cross-indexed along all these dimensions simultaneously."

- question: "What is the difference between subcategorization frames and selectional restrictions, and why does maintaining this distinction matter for understanding lexical knowledge?"
  type: short-answer
  answer: "A subcategorization frame specifies the syntactic complements a verb requires — 'persuade' needs a direct object NP and a clausal complement or infinitive. Selectional restrictions specify semantic requirements on argument fillers — 'devour' requires its patient to be edible, 'elapse' requires a time-interval subject. The distinction matters because violations have different linguistic status: subcategorization violations produce syntactic infelicity ('She persuaded'), while selectional violations produce semantic anomaly ('She devoured the idea') — the latter is often interpretable as metaphor, the former typically cannot be rescued this way."
  explanation: "Both are encoded in lexical entries, but they operate at different levels. Subcategorization is a syntactic fact about a word's grammatical environment; selectional restrictions are semantic facts about the kinds of things that can participate in the event the verb describes. Understanding both helps explain how language processing is so fast and accurate: accessing a word immediately delivers not just its meaning but the full package of syntactic and semantic constraints that govern how it combines with surrounding material."
```

## Explainer

From your study of lexical semantics, you understand that word meaning is richly structured — words exist in semantic fields, relate through hyponymy and antonymy, and have componential meanings that distinguish, say, *kill* from *cause to die*. But a word is more than its meaning. The **mental lexicon** is not a dictionary of definitions; it is a structured database where each entry stores multiple types of information simultaneously: what the word means, how it sounds, how it is spelled, what grammatical category it belongs to, and what syntactic environments it fits into. The formal structure of this database is what we're examining here.

Consider what you know about the word *persuade*. You know its meaning — causing someone to believe something through argument. But your lexical entry also encodes its phonological form (/pɚˈsweɪd/), its grammatical category (verb), and crucially its **subcategorization frame**: *persuade* requires a direct object (a person) and typically a complement clause or infinitive — *I persuaded her that X* or *I persuaded her to do X*. This subcategorization frame is part of the lexical entry, not learned anew each time the word is encountered. It's why "She persuaded enthusiastically" sounds wrong even though *persuade* is a verb and *enthusiastically* is a legitimate adverb — the frame specifies what complements the verb requires.

Words are also cross-indexed by multiple organizing principles simultaneously. **Morphological family** links *run*, *running*, *runner*, *ran*, and *outrun* — accessing one can prime the others. **Semantic field** clusters words by conceptual domain: the emotion field contains *angry*, *sad*, *happy*, *fearful*, *disgusted*, each related to the others through shared features and contrasts you studied in lexical semantics. **Phonological similarity** creates a separate organizational layer: *cat*, *bat*, *hat*, *sat* are linked by rhyme, which is why tip-of-the-tongue states often produce phonologically similar words rather than semantically similar ones. Psycholinguistic experiments — particularly priming studies, where seeing one word speeds recognition of related words — reveal all three organizational dimensions operating in parallel.

The formal concepts of **argument structure** and **selectional restrictions** extend the subcategorization frame into semantic territory. A verb like *devour* takes an agent subject and a patient object; but selectional restrictions further specify that the patient must be something edible (*She devoured the meal*; *?She devoured the idea* is odd, though acceptable metaphorically). These restrictions are not syntactic rules — they are semantic properties encoded in the lexical entry. When they're violated, the result isn't ungrammatical but semantically anomalous, as in Chomsky's famous "colorless green ideas sleep furiously" — syntactically impeccable, semantically incoherent. Understanding the mental lexicon as a multi-dimensional formal structure helps explain why language processing is so fast and accurate: the parser doesn't just look up a word's meaning, it immediately retrieves the full package of phonological, syntactic, and semantic constraints that govern how the word will combine with everything around it.
