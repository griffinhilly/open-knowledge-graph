---
id: meaning-convention-vs-intention
title: 'Linguistic Meaning: Convention Versus Intention'
domain: philosophy
course: philosophy-of-language
prerequisites:
- id: grice-cooperative-principle-maxims
  type: hard
- id: speaker-meaning
  type: hard
builds-toward:
- literal-meaning-speaker-meaning
tags:
- meaning
- convention
- intention
stage: formal-systems
status: validated
---

# Linguistic Meaning: Convention Versus Intention

## Core Idea
Linguistic meaning involves two dimensions: conventional meaning (what sentences mean by shared language rules) and speaker meaning (what individual speakers intend to communicate). Neither convention nor intention alone suffices; both are necessary for a complete account of meaning.

## Questions

```yaml
- question: "Alex says 'Nice weather' while pointing at a thunderstorm, with an obviously sarcastic tone. The conventional meaning of 'nice weather' describes pleasant conditions. What does this example illustrate about linguistic meaning?"
  type: multiple-choice
  options:
    - "Conventional meaning breaks down during irony, making speaker meaning the only operative level"
    - "Speaker meaning can diverge systematically from conventional meaning, and listeners use pragmatic inference — not just convention — to recover what the speaker intends"
    - "Conventions are insufficient to establish any meaning; all meaning is ultimately determined by individual speaker intention"
    - "Because the conventional meaning is false (it's not nice weather), the utterance has no meaning"
  answer: 1
  explanation: "Irony is a paradigm case of the gap between conventional and speaker meaning. The conventional meaning of 'nice weather' (pleasant conditions) is compositionally determined by grammar and lexicon — Alex hasn't broken any linguistic convention in the strict sense. What changes is what Alex *means by* the utterance in context: the speaker meaning is the opposite of the conventional meaning. Listeners bridge this gap using Gricean inference — recognizing that a cooperative speaker saying something obviously false must intend to communicate something else. Neither convention nor intention alone does all the work."

- question: "Kripke's reading of Wittgenstein's rule-following argument aims to show that a speaker cannot fix the meaning of a word by a private mental act alone. What follows?"
  type: multiple-choice
  options:
    - "Words have no determinate meanings — radical semantic indeterminacy is unavoidable"
    - "Meaning requires a public standard or community practice that determines correctness independently of any individual's private intentions"
    - "Grice's account of speaker meaning is the correct and complete account of all linguistic meaning"
    - "Only conventions, never speaker intentions, play any role in what utterances communicate"
  answer: 1
  explanation: "The rule-following argument targets the idea that meaning could be settled by a private mental item (an image, a feeling of intended use, a disposition). The scenario: what makes it the case that by 'plus' you mean addition rather than 'quaddition' (a deviant function agreeing with addition on all past cases)? No private mental state can distinguish these, because any mental state is compatible with either interpretation. Only *community practice* — shared use over time — provides a standard against which answers can be correct or incorrect. This doesn't eliminate speaker meaning; it shows that speaker meaning presupposes, rather than replaces, a publicly grounded conventional backdrop."

- question: "When speaker meaning diverges from conventional meaning — as in irony or implicature — communication has failed."
  type: true-false
  answer: false
  explanation: "Divergence between speaker meaning and conventional meaning is not failure but a normal, highly productive feature of language. Irony, metaphor, understatement, and implicature all involve intentional divergence — and they are understood successfully by interlocutors using Gricean inference. Communication succeeds when the listener correctly recovers the speaker's intended meaning, regardless of whether it matches the conventional content. The conventional meaning often serves as the background the speaker exploits (by violating it, as in irony) to convey the intended meaning more forcefully."

- question: "On Grice's intentionalist account, the conventional meaning of a sentence is ultimately grounded in patterns of communicative intention across a linguistic community."
  type: true-false
  answer: true
  explanation: "Grice's program is to derive conventional (sentence) meaning from speaker meaning. The idea: a word or expression comes to mean what it does because speakers repeatedly use it with certain intentions, those uses succeed, and over time the pattern stabilizes into a convention. Convention is the *sediment* of successful communicative intentions. Lewis's coordination-solution account of convention is compatible with this picture: conventions solve repeated coordination problems (how to communicate reliably), and they originate in the intentions of community members. This bottom-up derivation of conventional from intentional meaning is the hallmark of intentionalism."

- question: "Why is neither convention alone nor intention alone sufficient for a complete account of linguistic meaning? What does each dimension contribute?"
  type: short-answer
  answer: "Convention alone fails because conventional meaning fixes only a semantic baseline — irony, implicature, and metaphor all involve speakers meaning something different from (or beyond) the conventional content, and understanding them requires inferring the speaker's intention. Intention alone fails because private intention cannot fix meaning without a public standard: the rule-following argument shows that no private mental state distinguishes the intended meaning from an indefinite range of alternative interpretations — only community practice provides the normative standard of correctness. Together: convention provides a stable, socially grounded semantic baseline; intention provides what the speaker does with that baseline on a particular occasion. A complete account of meaning needs both."
  explanation: "This two-level structure is Grice's enduring contribution. The conventional level explains how language has stable, shared meanings that can be communicated across contexts. The intentional level explains how speakers exploit, extend, and deviate from that baseline to convey richer content. Neither is reducible to the other: you cannot account for all of language with just one level, which is why philosophy of language needs both a theory of conventions (semantics) and a theory of speaker meaning (pragmatics)."
```

## Explainer

From your study of Grice and speaker meaning, you know that when someone communicates, what they mean — **speaker meaning** — often diverges from what their words literally say. Grice showed that interpretation is an inferential process: listeners use the Cooperative Principle and its maxims to figure out what a speaker intends to convey beyond the literal content. Now the deeper question emerges: what is the relationship between what words mean and what speakers mean? Can meaning be reduced entirely to intention, or does language require something more — convention?

The **intentionalist** answer, associated with Grice's program, is that meaning bottoms out in intention. Sentence meaning is built up from speaker meaning: a word or sentence means what it does because speakers use it with certain intentions, and those intentions, through use and coordination, become conventionalized. On this picture, convention is derivative — it is the stabilization of successful communicative intentions across a community. Paul Grice's formal analysis of speaker meaning runs: speaker S means something by uttering X if and only if S intends the utterance to produce a belief in an audience, and intends the audience to recognize that intention as the reason for forming the belief. Meaning, on this view, is constitutively intentional.

The opposing view emphasizes that **convention** does genuine independent work. Lewis argued that linguistic conventions are coordination solutions — ways communities solve the problem of communicating by establishing shared expectations about how expressions are used. The meaning of "bank" (financial institution vs. riverbank) isn't settled by any speaker's intention on any particular occasion; it is fixed by the conventions of English. Kripke and Wittgenstein pressed this further: a speaker cannot fix meaning by private intention alone. Meaning requires a public standard, a community practice, against which individual uses are correct or incorrect. This is the **rule-following** argument: what makes it the case that by "plus" you mean addition rather than some deviant function that happens to have agreed with addition on all previously computed cases? Only community practice, not any private mental state, can answer this.

The synthesis is that a complete account needs both. **Conventional meaning** — encoded in the grammar and lexicon of a language — fixes a stable semantic baseline that speakers can manipulate, deviate from, or build on. **Speaker meaning** is what individual communicators do with that baseline on particular occasions, conveying more or less than the conventional content. Irony, implicature, and metaphor all involve a gap between the two. Understanding this gap — and what bridges it — is what makes Gricean pragmatics and philosophy of language indispensable for anyone trying to understand how communication actually works.
