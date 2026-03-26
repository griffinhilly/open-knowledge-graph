---
id: lexical-access-word-recognition
title: Lexical Access and Word Recognition in Real Time
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: psycholinguistics-intro
  type: hard
- id: language-and-the-brain
  type: hard
tags:
- psycholinguistics
- lexical-access
- word-recognition
stage: expert
status: validated
---

# Lexical Access and Word Recognition in Real Time

## Core Idea
Lexical access retrieves word meanings and phonological forms from memory during comprehension and production. Eye-tracking and priming studies reveal that access begins immediately upon encountering partial word information and is initially automatic, with competing candidates activated in parallel.

## How It's Best Learned
Review eye-tracking experiments tracking lexical access during reading; conduct or study priming experiments showing automatic activation of semantic and phonological neighbors.

## Common Misconceptions
Lexical access is not conscious deliberate lookup but rapid automatic activation of competing candidates; later stages filter implausible meanings based on context.

## Questions

```yaml
- question: "According to the cohort model of spoken word recognition, what happens in the mind of a listener who hears the syllables 'cap-' at the start of a spoken word?"
  type: multiple-choice
  options:
    - "The listener waits for the complete word before activating any candidates"
    - "The listener retrieves a single best-guess candidate based on prior context"
    - "The listener automatically activates all words beginning with 'cap' in parallel — captain, capsule, capture — and progressively eliminates them as more acoustic signal arrives"
    - "The listener identifies the word only after the sentence ends and context disambiguates meaning"
  answer: 2
  explanation: "The cohort model's central claim is that lexical access begins immediately upon encountering partial acoustic input, activating a cohort of all matching candidates in parallel. As the acoustic signal continues, candidates inconsistent with the input are eliminated. This process is automatic, not deliberate — listeners do not consciously consider and reject candidates. Option A (waiting for full word) and Option D (waiting for sentence end) both contradict the evidence that recognition begins with partial information. Option B describes a single candidate, but the model specifically requires parallel activation of multiple candidates."

- question: "In a semantic priming experiment, participants recognize the word BUTTER faster after seeing BREAD than after seeing an unrelated word. What does this finding reveal about lexical access?"
  type: multiple-choice
  options:
    - "Readers consciously search for related words after recognizing BREAD, which speeds access to BUTTER"
    - "Activating a word automatically spreads activation to semantically related entries in the mental lexicon, facilitating their recognition before any deliberate search begins"
    - "The effect only occurs because BREAD and BUTTER are commonly seen adjacent to each other in written text"
    - "Semantic priming shows that reading is slower and more serial than spoken language comprehension"
  answer: 1
  explanation: "Semantic priming occurs at very short stimulus-onset asynchronies — sometimes under 100ms — far too fast for conscious deliberate search. This confirms that activation spreads automatically through the lexical network: recognizing BREAD activates its semantic neighbors, lowering the threshold for recognizing related words. Option A describes a slower, deliberate process that the reaction-time data rules out. The priming effect is automatic — it happens before deliberation can intervene, which is why it provides evidence about the architecture of lexical memory rather than about strategic reading behavior."

- question: "When a fluent reader encounters the word 'bank' in a sentence strongly disambiguated toward the river meaning, mainly the river meaning is activated — context prevents the financial meaning from being retrieved at most."
  type: true-false
  answer: false
  explanation: "Most evidence supports weak modularity: early lexical access is largely automatic and parallel, activating multiple meanings of ambiguous words regardless of context. Context operates at a rapid selection stage, suppressing the inappropriate meaning so quickly that readers rarely notice both meanings were activated. But reaction-time and eye-tracking studies show transient activation of the contextually inappropriate meaning even in biasing sentences. The misconception — that context prevents irrelevant meanings from being activated — describes the interactive view, which is not well supported by the evidence. The process feels seamless because selection is very rapid, not because access was selective to begin with."

- question: "The cohort model predicts that spoken words can be recognized before the speaker finishes producing them, at the 'uniqueness point' where only one candidate remains consistent with the acoustic signal."
  type: true-false
  answer: true
  explanation: "This is a core empirical prediction of the cohort model, and it has been confirmed by eye-tracking experiments. As candidates in the initial cohort are eliminated when they no longer match the incoming sound, a uniqueness point is reached when only one word in the mental lexicon is consistent with what has been heard. At that moment, identification is complete — before the final phoneme is produced. Eye-tracking studies show listeners fixating on the correct picture in a visual display at sub-syllabic timescales, and in conversation, people begin planning responses before their interlocutor has finished speaking. This early recognition is possible precisely because access is parallel and competitive."

- question: "Why do psycholinguists care whether lexical access is 'modular' (context-free at the initial stage) or 'interactive' (context-penetrable from the start)?"
  type: short-answer
  answer: "The distinction describes the fundamental architecture of language comprehension — specifically, whether meaning retrieval is an autonomous process or whether top-down knowledge (context, expectations, prior text) penetrates the earliest stages of word recognition. If access is modular, all meanings of ambiguous words are initially retrieved and errors or biases in comprehension must arise at later selection stages; the access system cannot be 'tuned' by context. If access is interactive, context can bias which candidates are most strongly activated from the start, explaining the rarity of garden-path confusion with ambiguous words. Beyond theory, the distinction matters practically: for aphasia rehabilitation, reading instruction, and understanding language breakdowns, knowing where in processing context operates informs where interventions should target. Current evidence supports weak modularity — early access is largely parallel and automatic, but context-driven selection is so rapid that the two stages blur in real-time comprehension."
  explanation: "This is not just a theoretical debate — it bears on how language breakdowns occur and what makes comprehension effortful. If the initial access stage is autonomous, then access errors (activating the wrong meaning) require later-stage correction, whereas if access is interactive, impoverished context could directly impair which candidates become available."
```

## Explainer

From your study of psycholinguistics and the neuroscience of language, you know that the brain processes language rapidly and in real time — comprehension doesn't wait for a sentence to end before beginning. **Lexical access** is the subprocess of retrieval: given some acoustic or visual input, the cognitive system must locate the corresponding entry in the **mental lexicon** — the internal repository of words with their phonological forms, meanings, grammatical categories, and typical syntactic contexts. The central finding from decades of research is that this retrieval is not a deliberate lookup (like searching a dictionary) but a massively parallel, automatic process that begins with partial information and resolves competition over milliseconds.

The **cohort model** captures how spoken word recognition unfolds. When you hear "cap-", you automatically activate all words in your mental lexicon that begin with that sound: *cap*, *captain*, *capture*, *capsule*, and so on. This is the initial **cohort**. As more of the acoustic signal arrives, cohort members that no longer match are eliminated, until at some point — the **uniqueness point** — only one candidate remains and the word is identified. The cohort model predicts that words are recognized before their acoustic offset, which eye-tracking and priming experiments confirm: listeners can begin planning responses to a word before the speaker has finished producing it. For reading, the analogous process uses orthographic input rather than phonological, but the parallel activation logic is the same.

**Priming** experiments are the main empirical tool for studying what gets activated and when. In a **semantic priming** paradigm, seeing the word BREAD makes you faster to recognize BUTTER — because activating *bread* also spreads activation to semantically related nodes in the lexical network. In **phonological priming**, hearing "cat" facilitates recognition of "cap" — evidence that phonological neighbors are co-activated even when they are semantically unrelated. These effects occur at very short stimulus-onset asynchronies (sometimes under 100ms), confirming that the activation is **automatic** — it happens before conscious deliberation can intervene.

The key theoretical question is when and how context constrains this initially unconstrained activation. The **modular view** holds that initial lexical access is autonomous and context-free: the word BANK activates both its financial and riverbank meanings regardless of prior context, and only a later stage selects the contextually appropriate meaning. The **interactive view** holds that context can penetrate even early access, biasing which candidates are most strongly activated. Most current evidence favors a weak modularity: initial access is largely automatic and parallel, but context speeds selection so rapidly that only the appropriate meaning appears to reach awareness. This is why the misconception matters: readers who encounter an ambiguous word like *bank* in a disambiguating context may never consciously notice both meanings were activated, yet the transient activation of the inappropriate meaning has measurable effects on reaction time and eye movements.
