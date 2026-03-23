---
id: null-subject-parameter
title: The Null Subject Parameter
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: movement-and-transformations
  type: hard
- id: linguistic-typology
  type: soft
builds-toward:
- parameter-setting-acquisition
tags:
- syntax
- parameters
- universal-grammar
stage: expert
status: validated
---

# The Null Subject Parameter

## Core Idea
The null subject parameter explains why some languages (Spanish, Italian, Polish) permit sentences like 'Hablas español' (omitting 'you') while others (English, French) require overt subjects. The parameter governs whether verb morphology is rich enough to identify subjects independently, and interacts with other properties like word order freedom and subject-auxiliary inversion patterns.

## Questions

```yaml
- question: "Spanish allows 'Habla María' (subject follows the verb, no expletive filler), while English requires 'Mary speaks' and 'It is raining.' What best explains both contrasts?"
  type: multiple-choice
  options:
    - "Spanish has a richer literary tradition that tolerates more word-order variation"
    - "English requires an overt subject even in expletive constructions because English verb morphology cannot uniquely identify subjects, while Spanish verb forms carry enough agreement information to recover the subject independently"
    - "Spanish permits free word order in all sentence types, whereas English has strict SVO order due to its Germanic heritage"
    - "English pronouns are phonologically weak and must be spoken, while Spanish pronouns are phonologically strong and therefore optional"
  answer: 1
  explanation: "The null subject parameter is tied to morphological richness: Spanish 'hablas' can only mean 'you speak' — the verb form uniquely determines the person and number of the subject. English 'speak' is compatible with I/you/we/they, so an overt subject is required for referential clarity. This also explains expletives like 'It is raining': the subject position must be filled in English even when there's nothing meaningful to say about it."

- question: "Japanese and Chinese allow null subjects but lack the rich person/number verb agreement morphology that Spanish has. What does this most directly suggest?"
  type: multiple-choice
  options:
    - "Japanese and Chinese are not genuine null-subject languages — their omitted subjects are better analyzed as topic-drop"
    - "Null subject is a surface property that multiple different underlying mechanisms can produce, so 'null subject language' may cover several distinct parameter settings"
    - "Verb morphology is not actually required for the null subject parameter — the real trigger is prosodic rather than morphological"
    - "Japanese and Chinese must have covert agreement features that function like the overt agreement morphology in Spanish"
  answer: 1
  explanation: "This is a key complication: Japanese and Chinese look like null-subject languages on the surface but the mechanism differs from Spanish/Italian. Spanish null subjects are licensed by rich agreement morphology; Japanese/Chinese null subjects may reflect topic-drop, discourse-governed deletion, or different structural mechanisms. This shows that 'null subject language' is a heterogeneous category at the surface level, and the deeper parameter(s) may be distinct across language families — an active research question in syntax and typology."

- question: "In a null-subject language like Spanish, the verb form 'hablas' can uniquely identify the subject as second-person singular without any overt pronoun."
  type: true-false
  answer: true
  explanation: "'Hablas' can only mean 'you (singular) speak' — no other person-number combination maps onto this inflected form. This is what 'rich agreement morphology' means: the verb itself encodes enough grammatical information to recover the subject's reference, making an overt pronoun (tú) redundant rather than required."

- question: "English 'It is raining' shows that English is a partial null-subject language because the subject 'it' has no real referential content — it is essentially absent semantically."
  type: true-false
  answer: false
  explanation: "This is a subtle but important distinction: 'it' in English expletive constructions is an *overt* subject — it is phonologically present and fills the required subject position. English obligatorily requires something in the subject slot, even when there is no meaningful referent, which is why a semantically empty placeholder must be inserted. A true null-subject language like Italian would simply have no overt element: 'Piove' ('rains') with nothing in the subject position — not even a dummy pronoun."

- question: "Why does the null subject parameter predict not just whether pronouns can be dropped but also whether a language allows free subject-verb inversion (e.g., 'Habla María' in Spanish)?"
  type: short-answer
  answer: "If verb morphology uniquely identifies the subject, the subject's position in the sentence is not needed for reference recovery — it can appear after the verb or be absent entirely without ambiguity. English requires the subject before the verb partly because the verb form alone doesn't tell you who is speaking/doing; moving the subject post-verbally would create interpretive confusion. The parameter is a cluster: rich agreement licenses both null subjects AND free inversion because both follow from the same underlying property — that the verb carries its own referential load."
  explanation: "This cluster property is evidence that the null subject setting is a real syntactic parameter rather than an arbitrary language-specific quirk. It also predicts different behavior in that-trace constructions: Italian allows 'Chi pensi che abbia vinto?' ('Who do you think that won?') with an empty subject after the complementizer, while English disallows the equivalent because the subject position must be filled. Multiple surface contrasts follow from one binary setting."
```

## Explainer

From your work on movement and transformations, you know that syntactic structures involve more than the words you hear — positions can be filled by empty elements whose presence is inferred from morphological and syntactic evidence. The null subject parameter is the best-studied example of a **syntactic parameter**: a binary grammatical setting that generates a cluster of surface differences between languages, all deriving from a single underlying property.

The core claim is that languages divide into two types depending on whether they allow **pro** ("small pro") — a phonologically empty pronoun that can occupy the subject position. In **pro-drop** or **null subject** languages like Spanish, Italian, Japanese, and Turkish, the verb morphology is rich enough to uniquely identify the grammatical person and number of the subject. Spanish *hablas* can only mean "you speak" (second person singular); no other reading is possible. Because the verb form itself carries enough information to recover the subject's reference, an overt subject pronoun (*tú*) is optional. English verbs do not have this property: *speak* is compatible with *I*, *you*, *we*, and *they*, so the subject pronoun cannot be omitted without loss of referential content. English **requires** an overt subject — even in expletive constructions like *It is raining* and *There is a problem*, where the subject position must be filled by a semantically empty placeholder.

The parameter is interesting not just because it explains the presence or absence of overt subjects, but because it predicts a **cluster** of correlated properties. Languages that allow null subjects also tend to permit **free inversion** — placing the subject after the verb (*Habla María* "speaks Maria / Maria speaks" in Spanish) without the subject-auxiliary inversion that English uses for questions. They also show **that-trace effects** differently: English disallows *"Who do you think that _ left early?"* (where the empty subject trace follows *that*), while Italian and Spanish allow equivalent constructions. These correlations suggest that null subject status is a coherent parameter of Universal Grammar rather than an arbitrary collection of unrelated facts.

The acquisition of the null subject parameter is itself illuminating. Children acquiring Spanish begin producing null subjects earlier than children acquiring English produce overt subjects, suggesting the parameter is set quickly once positive evidence arrives — a single clear instance of a null subject licenses the pro-drop setting. Cross-linguistic typology adds further complexity: Japanese and Chinese allow null subjects but for different structural reasons than Spanish (without the rich agreement morphology), suggesting that "null subject language" may be a surface property that multiple parameter settings can produce through different underlying mechanisms. This is a productive area of ongoing research at the intersection of syntax and typology that you can explore once you understand parameter-setting in acquisition.
