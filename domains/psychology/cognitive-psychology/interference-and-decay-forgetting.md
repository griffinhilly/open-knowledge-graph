---
id: interference-and-decay-forgetting
title: Interference and Decay in Forgetting
domain: psychology
course: cognitive-psychology
prerequisites:
- id: memory-consolidation-systems
  type: hard
- id: retrieval-cues-encoding-specificity
  type: soft
tags:
- forgetting
- interference
- decay
- memory
stage: formal-systems
status: draft
---

# Interference and Decay in Forgetting

## Core Idea
Forgetting results from two main mechanisms: interference (competing memories disrupt retrieval) and decay (memories fade with time). Proactive interference occurs when prior learning interferes with new learning, while retroactive interference occurs when new learning interferes with retrieving old memories. Ebbinghaus's forgetting curve demonstrates systematic forgetting patterns.

## Questions

```yaml
- question: "After years of using the same phone number, a person gets a new one and soon struggles to recall the old number. Which explanation best fits interference theory?"
  type: multiple-choice
  options:
    - "The old memory decayed from disuse after the number was abandoned"
    - "The new phone number competes with the old one as a retrieval cue, making the old number less accessible"
    - "The old number was never deeply encoded to begin with"
    - "Recognition of the old number would also fail because the memory is gone"
  answer: 1
  explanation: "Interference theory attributes forgetting to cue competition, not storage erasure. The cue 'my phone number' once uniquely retrieved the old number; now it competes with the new number, degrading retrieval. Crucially, the old memory is likely still stored — a recognition test (seeing both numbers) would probably succeed, confirming it's an access failure. Decay theory (option A) would predict fading over time, but that can't explain why the old number is harder to recall precisely after learning the new one."

- question: "Participants who sleep immediately after learning a word list remember significantly more than those who stay awake for the same number of hours. What does this finding most directly challenge?"
  type: multiple-choice
  options:
    - "The encoding specificity principle"
    - "Pure decay theory as an account of forgetting"
    - "The spacing effect in memory consolidation"
    - "Proactive interference from prior learning"
  answer: 1
  explanation: "Pure decay theory predicts that memory fades with time regardless of what fills that time. But both groups experienced the same elapsed time — only the content differed (sleep vs. wakeful experience). The superior retention of the sleep group implicates accumulated interference from waking experiences as the culprit, not time itself. This is the key evidence that what looks like decay may often be interference in disguise."

- question: "Most forgetting represents a failure to access memories that are still stored, rather than permanent erasure of those memories."
  type: true-false
  answer: true
  explanation: "This is the central claim of interference theory. The cue overload principle explains why: retrieval cues that once uniquely identified a memory become degraded when many competing memories share the same cue. The memory persists in storage but becomes inaccessible. The best evidence is that recognition typically recovers memories that free recall fails to retrieve — the original item acts as a specific cue that bypasses competition and restores access."

- question: "Proactive interference occurs when newly learned material disrupts memory for information learned earlier."
  type: true-false
  answer: false
  explanation: "This describes retroactive interference (RI) — new learning interfering backward with old memories. Proactive interference (PI) runs in the opposite direction: old learning interferes forward with the retention of new material. A classic example: learning a new language is harder because vocabulary from a previously learned language proactively interferes with the new one. The directionality is the key distinction — PI = old disrupts new; RI = new disrupts old."

- question: "Why does recognition memory typically outperform free recall for the same information, and what does this tell us about the nature of forgetting?"
  type: short-answer
  answer: "Recognition provides the original item as a retrieval cue, bypassing the cue overload problem that plagues free recall. In free recall, an overloaded cue must discriminate among many competing memories; in recognition, seeing the item itself is a maximally specific cue that can recover access even when free recall fails entirely."
  explanation: "This asymmetry is diagnostic: if forgetting were storage loss, recognition would fail too. The fact that recognition succeeds when recall fails reveals that the information is still encoded — the problem is retrieval, not storage. This is why interference theory (which locates forgetting in cue competition) is more supported than decay theory (which implies actual erasure). It also explains the spacing effect: distributed practice forces repeated effortful retrieval, each successful recovery strengthening resistance to future cue competition."
```

## Explainer

From your study of memory consolidation, you understand that newly formed memories pass through a vulnerable period—synaptic consolidation over minutes to hours stabilizes the molecular changes at individual synapses, while systems consolidation over days to years gradually transfers memories to distributed cortical networks. From your study of retrieval cues and encoding specificity, you know that memories are context-sensitive: retrieval is most successful when conditions at recall match the conditions at encoding. Forgetting, viewed through this lens, is often not memories disappearing but memories failing to be retrieved because the right conditions aren't met.

**Decay theory** proposes that memory traces weaken over time simply through disuse. Ebbinghaus's forgetting curve—arguably the first precise quantitative result in experimental psychology—showed that memory for nonsense syllables drops steeply in the first hour after learning and then levels off, following a power function. This curve pattern is consistent with decay. However, decay theory is difficult to test cleanly because time cannot pass without also allowing for new experiences. The most telling evidence against pure decay comes from sleep studies: participants who sleep immediately after learning remember substantially more than those who stay awake the same number of hours—the difference between the groups is not time, but the interference accumulated during wakeful experience. This suggests that what looks like decay may often be accumulated interference in disguise.

**Interference theory** provides a more mechanistically grounded account organized around competing memories at retrieval. **Proactive interference (PI)** occurs when prior learning disrupts the retention of newer material: if you've learned Spanish vocabulary for years, learning Italian vocabulary today is harder because similar Spanish words proactively interfere with the new Italian ones. **Retroactive interference (RI)** runs in the opposite direction: new learning interferes with retrieving older material. The **cue overload principle** gives interference a precise mechanism: a retrieval cue that once uniquely pointed to a specific memory becomes degraded when many competing memories have been associated with that same cue. If "hotel" once retrieved only one memory, but over time becomes associated with dozens of hotel stays, the cue loses its specificity and retrieval becomes unreliable—not because the original memory decayed but because the cue can no longer uniquely identify it.

The practical upshot connects back to encoding specificity: most "forgetting" reflects an access failure rather than a storage failure. Proactively and retroactively interfering memories are not erased—they are rendered less accessible by cue competition. This explains why recognition typically exceeds free recall: recognition provides the original item as a retrieval cue, bypassing the cue overload problem, allowing recovery of memories that cannot be freely recalled at all. It also explains the **spacing effect**: distributing practice over time, allowing some forgetting between sessions, strengthens long-term retention because each retrieval practice episode requires effortful cue-based search that strengthens the memory trace and reduces susceptibility to interference. The hardest retrievals—the ones that feel like they're on the tip of your tongue—are precisely the ones most likely to consolidate the memory durably when they succeed.
