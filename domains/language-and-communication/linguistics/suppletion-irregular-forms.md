---
id: suppletion-irregular-forms
title: Suppletion (Irregular Forms)
domain: language-and-communication
course: linguistics
prerequisites:
- id: inflectional-morphology
  type: hard
- id: morpheme-types
  type: hard
tags:
- morphology
- inflection
- allomorphy
- paradigms
stage: formal-systems
status: draft
---

# Suppletion (Irregular Forms)

## Core Idea
Suppletion is extreme allomorphy in which a root is replaced by a form from a different etymological source in specific grammatical contexts. English go/went (from 'go' and archaic 'wend') is the classic example. Suppletion typically affects high-frequency words in inflectional paradigms (person, number, tense).

## Questions

```yaml
- question: "A child says 'I goed to the store.' This error most directly demonstrates:"
  type: multiple-choice
  options:
    - "That the child has not yet learned the irregular past tense, indicating a developmental delay"
    - "That the productive past tense rule (-ed) is being applied to a lexical item that requires a stored suppletive form"
    - "That 'went' is a spelling variant of 'go' that the child hasn't memorized yet"
    - "That suppletion breaks down in child language because children learn rules before exceptions"
  answer: 1
  explanation: "The child has learned the regular past tense rule (-ed suffix) and is applying it productively. This overrides the suppletive form 'went,' which must be memorized as a lexical exception rather than derived by rule. This is called 'overregularization' — a normal developmental stage demonstrating active rule learning. Far from indicating delay, it shows the child understands the morphological system. The suppletive form 'went' requires sufficient exposure for entrenchment in the mental lexicon."

- question: "Which of the following is the clearest example of suppletion, as opposed to ordinary irregular inflection?"
  type: multiple-choice
  options:
    - "run → ran (vowel change within the same root)"
    - "go → went (present and past tense derive from historically different verbs)"
    - "goose → geese (vowel alternation for plural)"
    - "child → children (irregular plural with suffix replacement)"
  answer: 1
  explanation: "Suppletion requires that the two forms share no phonological material and come from historically distinct roots. 'Go' and 'went' share no phonological similarity: 'went' was historically the past tense of 'wend' (to travel), borrowed into the 'go' paradigm. 'Run/ran,' 'goose/geese,' and 'child/children' all involve alternations on a single root (ablaut, vowel alternation, modified suffix) — irregular, but still phonologically related to the same root. Suppletion is the extreme end of allomorphy where etymological sources differ entirely."

- question: "Suppletion occurs only in verb paradigms because verbs have more complex inflectional requirements than nouns or adjectives."
  type: true-false
  answer: false
  explanation: "English has suppletive adjective paradigms: 'good/better/best' and 'bad/worse/worst' both replace the root entirely in comparative and superlative forms rather than adding -er/-est to the base form. 'Better' is not derived from 'good' by any phonological rule; it comes from a distinct Proto-Germanic root. The topic notes verb examples (go/went, the multiple roots of 'be'), but suppletion is not restricted to verbs — it appears wherever frequency effects are strong enough to entrench non-productive forms in the mental lexicon."

- question: "Low-frequency verbs in English are more likely to have suppletive past tense forms than high-frequency verbs because they've had more time to develop historical irregularities."
  type: true-false
  answer: false
  explanation: "This reverses the actual relationship. Suppletive and irregular forms concentrate in HIGH-frequency words, not low-frequency ones. High-frequency words are used constantly, so their irregular forms are reinforced through repeated exposure and stored whole in the mental lexicon. Low-frequency words are encountered rarely, so their forms are not deeply entrenched — speakers regularize them by analogy (applying the productive -ed rule). When a low-frequency word's suppletive form falls out of use, it typically disappears as speakers default to the regular form."

- question: "Why do suppletive forms persist in high-frequency words while low-frequency words tend to get regularized, even though high-frequency words are used and 'heard more often'?"
  type: short-answer
  answer: "High-frequency words are stored as whole forms in the mental lexicon rather than being assembled from morphemes each time. Because speakers hear and produce 'went' hundreds of times in childhood, the suppletive form is deeply entrenched as the stored past tense of 'go' — any deviation sounds immediately wrong. Low-frequency words lack this entrenchment: speakers encounter them rarely enough that the irregular form isn't strongly memorized, so when the past tense is needed, they fall back on the productive rule (-ed). High frequency protects suppletive forms from regularization by analogy."
  explanation: "The theoretical implication is significant: morphology is not purely compositional (applying rules to roots). High-frequency paradigms are stored as wholes, with individual suppletive cells filled by whatever historically available form was learned. This supports a 'dual-route' or lexicalist model: productive rules generate regular forms; the lexicon stores irregular paradigms. Suppletion is the extreme evidence for the lexical storage route, because the stored form and the root share nothing phonological — only their paradigmatic relationship links them."
```

## Explainer

From your study of inflectional morphology, you know that regular inflection works by attaching morphemes to a stable root: *walk* → *walked*, *dog* → *dogs*, *fast* → *fastest*. The root stays constant; the affixes signal grammatical distinctions like tense, number, and degree. You also know from morpheme types that **allomorphy** — variation in the form of a morpheme — is common. The plural morpheme has allomorphs /s/, /z/, and /ɪz/ depending on the preceding sound (*cats*, *dogs*, *buses*), but the plural morpheme itself is still recognizably present in all three. Suppletion is what happens when this variation becomes so extreme that the root itself is unrecognizable: the connection between forms is paradigmatic (grammatically linked) but phonologically opaque.

The paradigm case is **go/went**. No phonological process derives *went* from *go* — the two forms share no phonological material. Historically, *went* is the past tense of *wend* (an archaic verb meaning to travel), which was borrowed into the *go* paradigm because *go* lacked a past tense form. This is **suppletion**: different etymological roots occupying different cells of the same inflectional paradigm. English has several more examples. *Be* is the most extreme: *am*, *is*, *are*, *was*, *were*, *be*, and *been* all fill cells of a single verb's paradigm while deriving from three different Proto-Indo-European roots. *Good/better/best* replaces the root entirely in the comparative and superlative rather than adding *-er* and *-est* to *good*. *Bad/worse/worst* does the same.

The **frequency effect** is striking and well-documented: suppletive forms are almost exclusively found among the most frequent words in a language. This is not coincidence. High-frequency words are acquired early, used constantly, and stored whole in the mental lexicon rather than being assembled from morphemes each time. Their irregular forms are reinforced through repeated exposure, so they don't get regularized by analogy (*I goed* is a child's error, not an adult's). Low-frequency words, by contrast, tend to be regularized because speakers encounter them rarely enough that the irregular form isn't entrenched in memory. When a language loses a word from active use, its suppletive forms are usually the first to disappear, as speakers regularize by analogy.

Suppletion matters theoretically because it challenges the view of morphology as a purely compositional, rule-based system. If words were always built by combining a root with affixes according to rules, suppletion would be impossible — the rules would require a stable root to work on. Instead, suppletion shows that paradigms (sets of grammatically related forms) can be stored and learned as wholes, with individual cells filled by whatever form is historically available, regardless of phonological relationship. This points toward a **lexicalist** view of morphology, where the lexicon stores not just roots but full paradigms for frequent and irregular items, alongside productive rules that generate regular forms for everything else.
