---
id: forgetting-and-interference
title: Forgetting and Interference Theory
domain: psychology
course: cognitive-psychology
prerequisites:
- id: memory-encoding-strategies
  type: hard
- id: memory-retrieval-cues
  type: hard
- id: retrieval-cues-encoding-specificity
  type: soft
tags:
- memory
- forgetting
- interference
- decay
stage: formal-systems
status: validated
---

# Forgetting and Interference Theory

## Core Idea
Forgetting occurs through several mechanisms: decay (trace fading over time without rehearsal), retroactive interference (new learning impairs recall of older memories), and proactive interference (old memories impair recall of newer ones). Ebbinghaus's forgetting curve shows that forgetting is rapid initially and then slows — a pattern replicated consistently across materials and populations. Retrieval-induced forgetting (practicing some items impairs recall of related unpracticed items) reveals an active suppression mechanism.

## How It's Best Learned
Study the AB-AC interference paradigm: learn list A, then a conflicting list C, then test list A. Comparing proactive versus retroactive directions makes interference intuitive by showing which temporal direction causes interference.

## Common Misconceptions
- Decay alone is insufficient to explain most forgetting — interference and retrieval failure are stronger and better-supported factors.
- Forgetting is not always maladaptive; suppressing irrelevant or conflicting memories helps prioritize relevant information and reduces interference in ongoing cognition.

## Questions

```yaml
- question: "A student studies French vocabulary in the morning, then attends a Spanish class in the afternoon (no self-testing), and that evening quizzes herself on French — scoring much worse than expected. Which mechanism best explains her poor French recall?"
  type: multiple-choice
  options:
    - "Decay — French memories faded naturally over the course of the day without rehearsal"
    - "Retroactive interference — the Spanish learning competed with French memory traces for the same retrieval cues"
    - "Proactive interference — the French learning was too strongly encoded and blocked the Spanish class"
    - "Retrieval-induced forgetting — practicing Spanish vocabulary suppressed unpracticed French items"
  answer: 1
  explanation: "This is the AB-AC interference paradigm: learn List A (French), then learn a conflicting List C (Spanish), then test List A. Retroactive interference occurs when *newer* learning disrupts recall of *older* material by competing for the same retrieval cues. Decay alone cannot explain the size of typical forgetting effects, and proactive interference runs in the opposite direction (old disrupting new). Retrieval-induced forgetting requires actual retrieval practice of the competing material — which the scenario explicitly excludes."

- question: "You memorized a new phone number last week. Now you keep accidentally dialing your old number instead. Which type of interference does this demonstrate?"
  type: multiple-choice
  options:
    - "Proactive interference — old memories are interfering with recall of the new number"
    - "Retroactive interference — the new number is suppressing retrieval of the old one"
    - "Retrieval-induced forgetting — practicing the old number caused active suppression of the new one"
    - "Decay — the new number has not been rehearsed enough to consolidate into long-term memory"
  answer: 0
  explanation: "Proactive interference (PI) occurs when *older* memories disrupt recall of *newer* material. Here, the old phone number (learned first) is intruding on attempts to recall the new one. Retroactive interference would be the reverse: if learning the new number was somehow causing you to forget the old one. The key diagnostic question is temporal direction: which memory is older, and which is being disrupted?"

- question: "Interference is strongest when two sets of memories are associated with highly similar retrieval cues."
  type: true-false
  answer: true
  explanation: "Interference occurs because memories compete for the same retrieval cues at the moment of recall. When two memories share cues (the same context, the same stimulus words, the same setting), competition is greatest — each cue activates both memories simultaneously, increasing interference. This is why the AB-AC paradigm produces strong RI: the same first words (List A cues) now retrieve competing second words from List C."

- question: "Decay — the natural fading of memory traces over time without rehearsal — is the primary explanation for most everyday forgetting."
  type: true-false
  answer: false
  explanation: "Although decay is a real phenomenon, interference theory and retrieval failure are better-supported explanations for most forgetting. Evidence against pure decay includes the finding that forgetting rates depend on what happens *during* the interval, not just how long it is — interpolated learning increases forgetting, while a 'quiet' interval (such as sleep) reduces it. If decay were primary, the interval's content shouldn't matter. Most forgetting appears to result from retrieval competition and the unavailability of effective retrieval cues."

- question: "Why does practicing retrieval of some items from a category sometimes make it harder to recall related items from the same category that you didn't practice?"
  type: short-answer
  answer: "When you retrieve a practiced item, the memory system must inhibit competing memories that are associated with the same retrieval cues — including related, unpracticed items from the same category. This active suppression (retrieval-induced forgetting) reduces the accessibility of those unpracticed items in subsequent tests. The inhibition is a feature, not a bug: it allows the currently-relevant memory to win the retrieval competition without interference from associated competitors."
  explanation: "This is retrieval-induced forgetting (RIF), which reveals that memory retrieval is an active, competitive process rather than a passive readout. The same inhibitory mechanism that makes RIF possible is what allows fluid cognition: without the ability to suppress currently-irrelevant associated memories, every attempt at retrieval would activate a flood of competitors. The practical implication is that interleaved practice — mixing categories — reduces contextual overlap and therefore reduces how much retrieval practice of one item suppresses others."
```

## Explainer

You already know from your memory prerequisites that encoding requires elaboration and that retrieval depends critically on cues — that memories are not stored and replayed like recordings, but reconstructed at retrieval using whatever cues are available. **Interference theory** builds directly on this understanding: if retrieval is cue-dependent, then having multiple memories associated with the same cue creates competition, and competition causes forgetting.

The two main interference types can be understood by their temporal direction relative to the target memory. **Retroactive interference (RI)** occurs when *newer* learning disrupts recall of *older* material. If you learn Spanish vocabulary this week and try to recall the French vocabulary you studied last month, the newer Spanish material competes for retrieval. **Proactive interference (PI)** is the opposite: *older* learning disrupts recall of *newer* material. If you've driven a rental car for a week and just switched back to your own car, old habits (old memories) produce errors in the new context. The AB-AC paradigm makes this concrete: learn List A (word pairs), then learn a conflicting List C (same first words, different second words), then test List A — the RI effect is the decrement in A recall due to C. The critical variable is similarity: more similar materials compete harder for the same retrieval cues, producing more interference.

**Ebbinghaus's forgetting curve** describes the empirical shape of forgetting over time: rapid loss initially, then a flattening as the remaining memories become more consolidated. The curve is best understood not as passive decay but as the accumulating effect of interference from new experience plus the gradual weakening of traces that are never retrieved. **Retrieval-induced forgetting (RIF)** reveals that forgetting has an active mechanism: when you practice retrieving some items from a category, recall of *related, unpracticed* items from the same category gets *worse*. The act of retrieval suppresses competitors. This is not an accident — it is the same inhibitory mechanism that keeps your current thoughts from being overwhelmed by associated memories you are not trying to retrieve.

The practical upshot for learning is that interference and retrieval-induced forgetting imply both dangers and tools. The danger: studying similar materials in close succession increases competition and forgetting. The tool: the same retrieval competition that causes RIF can be harnessed through **interleaved practice** — mixing categories during study reduces the contextual overlap between competing memories, and **retrieval practice** itself (testing yourself) strengthens target memories via the same mechanism that inhibits competitors. From your encoding strategies prerequisite, you know that testing beats restudying; interference theory explains part of why — retrieval suppresses irrelevant associations, leaving the practiced memory more cleanly accessible.
