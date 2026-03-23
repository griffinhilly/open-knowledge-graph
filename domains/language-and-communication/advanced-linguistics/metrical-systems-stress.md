---
id: metrical-systems-stress
title: Metrical Feet and Stress Systems
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: suprasegmental-phonology
  type: hard
- id: syllable-structure-prosody
  type: soft
tags:
- stress
- meter
- prosody
stage: expert
status: validated
---

# Metrical Feet and Stress Systems

## Core Idea
Metrical phonology organizes syllables into feet (binary or ternary units) that carry stress. Trees represent relative prominence, with stressed syllables dominating unstressed ones. Feet are constructed left-to-right or right-to-left depending on the language, building successively larger prosodic domains. This account explains stress patterns, secondary stress, and the phonological effects of stress without needing language-specific stress rules.

## How It's Best Learned
Build metrical trees for words in several stress systems (English, Spanish, Finnish) and verify that the foot structure correctly predicts which syllables bear stress. Examine how foot type (iambic, trochaic) and directionality vary across languages.

## Common Misconceptions
- Metrical feet are not arbitrary units; they reflect real phonological structure with phonetic consequences (duration, pitch).
- Stress systems are not always easy to describe with rule-based accounts; metrical structure provides a more elegant explanation.

## Questions

```yaml
- question: "In a language where primary stress always falls on the first syllable, long words like 'Alabama' also carry secondary stress on the third syllable. What does metrical theory predict about why secondary stress occurs at that position?"
  type: multiple-choice
  options:
    - "Secondary stress is stored as a lexical property of 'Alabama' in the mental lexicon, independent of any systematic rule"
    - "Secondary stress results from a separate phonological rule triggered by word length"
    - "The language builds trochaic feet left-to-right; every foot has a head, so the strong syllable of each non-primary foot automatically receives secondary stress — it is a structural consequence, not a separate stipulation"
    - "Secondary stress marks syllables that historically had primary stress before the first-syllable rule was applied"
  answer: 2
  explanation: "This is the explanatory payoff of metrical theory. If the language builds SW (trochaic) feet left to right, 'Alabama' parses into feet across its four syllables. Each foot has a strong (stressed) syllable. The foot containing the first syllable has its head designated as the primary stress domain; the remaining feet still have heads, producing secondary stress at predictable positions. The theory derives secondary stress from the same mechanism that produces primary stress — no additional rule is needed. This is far more economical than listing secondary stress separately for every long word."

- question: "A linguist proposes that English stress could be described by the rule: 'stress the first syllable of every word.' This works for 'table', 'window', and 'peanut'. What does metrical theory reveal that this rule misses?"
  type: multiple-choice
  options:
    - "Nothing significant — this rule is a good approximation for all English words, and metrical theory merely formalizes the same generalization"
    - "The rule fails entirely for monosyllabic words, which are common in English"
    - "The rule cannot predict stress in polysyllabic words like 'understand', 'Tennessee', or 'Alabama', where syllables beyond the first also bear stress, nor does it explain stress in words borrowed from French where the pattern differs — metrical theory generates these as outputs of foot structure"
    - "English is actually a right-to-left stress language, so the first-syllable rule has the directionality backwards"
  answer: 2
  explanation: "A simple first-syllable rule works for basic trochees but immediately fails for longer words where multiple stress-bearing syllables appear, and for words that follow different patterns. The first-syllable rule also gives no account of WHY the first syllable is stressed — it is just stipulated. Metrical theory provides an explanation: English builds trochaic feet from the left, so the first syllable is naturally the head of the first foot, and subsequent feet generate secondary stresses. The rule is a surface description; metrical structure is the underlying generalization."

- question: "A syllable with a long vowel or a coda consonant (a 'heavy' syllable) tends to attract stress more than an open syllable with a short vowel (a 'light' syllable) in weight-sensitive stress languages."
  type: true-false
  answer: true
  explanation: "Weight-sensitivity is a pervasive feature of stress systems: heavy syllables (CVC, CVV) have greater phonological 'mass' that makes them preferred as foot heads. In Latin, stress falls on the penultimate syllable if it is heavy, but on the antepenult if the penult is light — the rule is directly sensitive to weight. In metrical theory, this falls out from the claim that heavy syllables are metrically stronger and can function as foot heads more readily than light ones. Weight-sensitivity is not an add-on rule but a consequence of how syllable structure interacts with foot structure."

- question: "Metrical feet are purely theoretical constructs — they are a convenient notation for describing stress patterns but have no phonetic reality or consequences beyond stress placement."
  type: true-false
  answer: false
  explanation: "Metrical structure has real phonetic consequences beyond just marking which syllable is louder. It governs phenomena like syncope (vowel deletion in unstressed syllables — 'every' often realized as 'ev-ry'), consonant alternations like flapping in American English (the /t/ in 'butter' becomes a flap partly because it is in a weak syllable between two vowels), and the environments for many other phonological rules. The foot is not just an annotation — it is a domain that triggers and constrains phonological processes. This is evidence that the structure is psychologically real, not merely descriptive shorthand."

- question: "Why does metrical theory provide a more explanatory account of stress than a list of language-specific stress rules?"
  type: short-answer
  answer: "A list of rules describes what happens (e.g., 'stress the third-to-last syllable') without explaining why. Metrical theory derives stress from two general parameters — foot type (trochee or iamb) and directionality (left-to-right or right-to-left) — that interact with syllable weight. This predicts not just primary stress but secondary stress, the behavior of exceptional words, and phonological processes conditioned on stress, all from the same underlying structure."
  explanation: "Rule-list approaches face a compounding problem: each exception requires a new stipulation, and exceptions often cluster in ways the rules don't explain. Metrical theory shows these clusters are systematic — they follow from the interaction of foot structure with syllable weight. For example, the Latin penultimate stress rule is not arbitrary; it falls out from how Latin builds feet combined with the metrically strong status of heavy syllables. The theory also makes cross-linguistic predictions: languages that share a foot type and directionality should share stress patterns, which is empirically testable in a way that language-specific rule lists are not."
```

## Explainer

From suprasegmental phonology, you know that stress is a property of syllables that involves a cluster of phonetic features — greater loudness, longer duration, and often higher pitch — and that stress patterns vary systematically across languages. You also know from syllable structure that syllables are organized into hierarchical constituents (onset, nucleus, coda) with the nucleus as the head. Metrical theory takes this hierarchical intuition and extends it upward: syllables group into **feet**, feet group into **prosodic words**, and prosodic words group into larger units. Stress, in this view, is not a rule-stipulated property of individual syllables but a consequence of where heads fall in this hierarchical structure.

The foundational unit is the **metrical foot** — a grouping of two (or sometimes three) syllables with one head (the strong or stressed syllable) and one or more dependents (weak or unstressed syllables). Two fundamental foot types are the **trochee** (strong-weak, SW) and the **iamb** (weak-strong, WS). English is predominantly trochaic: *PEA-nut*, *TA-ble*, *WIN-dow* all have the strong syllable first. Latin and Arabic stress systems are more iambic. The foot type is a property of the language's phonology, not of individual words, and it determines the default rhythm of the whole language.

Directionality of foot-building is the second key parameter. Languages construct feet either left-to-right or right-to-left from the edge of the word. English, for example, builds trochees from left to right: *ÁLA-bama* parses as (ÁLA)-(ba-MA) where the first foot is strong-weak and the second is weak-strong (actually English metrical structure is more complex, but the leftward bias is real). The combination of foot type and directionality predicts where primary stress falls in most words, and where **secondary stress** falls in longer words. Secondary stress arises because every foot has a head — even non-primary feet contribute a weaker beat. This is why *Ála-bàma* has both primary stress on the first syllable and a secondary stress on the third: the prosodic structure requires it, not an arbitrary rule.

The explanatory power of the metrical approach becomes clear when you compare it to the alternative: a list of stress rules. A purely rule-based account might say "stress the third-to-last syllable in Spanish" or "stress the antepenult if the penult is light." These rules work for regular cases but require additional stipulations for every exception, and they don't explain why the exceptions cluster the way they do. Metrical theory shows that most "exceptions" are not really exceptions — they reflect interaction between the regular foot structure and other phonological factors like **syllable weight** (the distinction between heavy syllables with long vowels or codas, and light syllables with short vowels). Heavy syllables attract stress because they are metrically stronger — they can function as the head of a foot more readily than light syllables. This weight-sensitivity is not a separate rule but a consequence of foot structure.

**Metrical trees** make the hierarchical relationships explicit. At the bottom, syllables are labeled strong (S) or weak (W) within feet. At the next level, feet are labeled strong or weak within the prosodic word. Primary stress falls on the strong syllable of the strong foot; secondary stress falls on the strong syllable of weak feet. The tree is a visual representation of the claim that stress is relational and hierarchical, not a fixed phonetic property. This has consequences beyond stress: the same metrical structure governs phenomena like **syncope** (vowel deletion in unstressed syllables), **flapping** in American English (where the /t/ in *butter* becomes a flap partly because it is in a weak syllable), and the prosodic environments for various phonological rules. Stress, in metrical theory, is not just about which syllables are louder — it is the organizing principle of the phonological word.
