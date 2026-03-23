---
id: contextualism-in-epistemology
title: Epistemic Contextualism
domain: philosophy
course: epistemology
prerequisites:
- id: responses-to-skepticism
  type: hard
- id: external-world-skepticism
  type: soft
- id: first-order-logic-syntax
  type: soft
builds-toward:
- epistemology-of-disagreement
tags:
- contextualism
- DeRose
- Cohen
- knowledge-attributions
- standards
stage: formal-systems
status: validated
---

# Epistemic Contextualism

## Core Idea
Epistemic contextualism holds that 'knows' is a context-sensitive term: the truth conditions of knowledge attributions vary with the epistemic standards salient in the context of the attributor, not the subject. In a low-stakes context ('Does Mary know her car is in the lot?'), loose standards apply and she knows. In a high-stakes or philosophically charged context ('Does Mary know she's not being deceived by an evil demon?'), stringent standards apply and she does not know. Contextualism explains why skeptical arguments seem compelling in philosophical discussion yet harmless to ordinary knowledge claims: both can be true — at different standards.

## How It's Best Learned
Evaluate contextualism against the 'bank cases' (DeRose): low-stakes and high-stakes scenarios where intuitions about knowledge attribution shift. Ask whether the shift reflects a change in the standards for 'knows' or a change in how careful the subject is being.

## Common Misconceptions
- Contextualism is about the *attributor's* context, not the *subject's* situation — the same agent can be said to know in one conversational context and not know in another.
- Contextualism is not relativism about truth; 'knows' sentences have determinate truth values relative to contexts of attribution.

## Questions

```yaml
- question: "Mary parks her car in her usual lot before going to work. A colleague asks: 'Does Mary know her car is in the lot?' The same question is asked again while they are searching the lot because her car may have been towed. According to epistemic contextualism, which of the following is correct?"
  type: multiple-choice
  options:
    - "Mary either knows or she doesn't — the question can only have one correct answer regardless of who is asking"
    - "In both contexts it is false that Mary knows, because she could always be deceived about her car's location"
    - "In the first context it is true that Mary knows; in the second it is true that she does not — with no contradiction"
    - "Whether Mary knows depends on how confident she feels, not on the conversational context"
  answer: 2
  explanation: "Contextualism holds that 'knows' tracks different epistemic standards in different conversational contexts. In the ordinary first context, low standards apply and her belief based on parking the car suffices — she knows. In the second context, where the possibility of towing is explicitly salient, standards rise and her unverified belief no longer meets them — she does not know. Both attributions are true because 'knows' means something different in each context. Option A assumes invariantism; option B is the skeptic's position; option D conflates subjective confidence with contextualism's standards."

- question: "What is the most fundamental feature that distinguishes epistemic contextualism from invariantism?"
  type: multiple-choice
  options:
    - "Contextualists deny that knowledge requires justified true belief; invariantists require all three conditions"
    - "Contextualists hold that the truth conditions of 'knows' vary with the attributor's context; invariantists hold that 'knows' has fixed truth conditions regardless of context"
    - "Contextualists think skeptical arguments are valid; invariantists think they can always be refuted"
    - "Contextualists locate knowledge in the community; invariantists locate it in the individual"
  answer: 1
  explanation: "The defining contextualist thesis is that 'knows' is a context-sensitive expression whose truth conditions shift with the context of the person making the attribution. Invariantism maintains that 'knows' has a single fixed semantic standard — the subject either meets it or doesn't, regardless of who is talking. This disagreement about the semantics of 'knows' is the core dispute. Options A and C do not accurately describe either position; option D mischaracterizes both."

- question: "On the contextualist view, whether a person knows something depends on the quality of their evidence and the reliability of their cognitive processes — not on the context of the person making the knowledge attribution."
  type: true-false
  answer: false
  explanation: "That description characterizes the subject's epistemic situation, which is what invariantist views like reliabilism focus on. Contextualism adds that even holding the subject's situation fixed, whether the knowledge attribution is true depends on the attributor's context. The same subject with the same evidence can be correctly said to know in one conversational context and correctly said not to know in another — because the standards embedded in 'knows' vary across contexts. The critical and initially counterintuitive point is that it is the attributor's context, not the subject's, that shifts the standard."

- question: "Contextualism can explain why skeptical arguments seem compelling in philosophical discussion but do not undermine our everyday knowledge claims, without concluding that either the skeptic or the ordinary knowledge-claimer is making a mistake."
  type: true-false
  answer: true
  explanation: "This is the central appeal of contextualism as a response to skepticism. In the philosophy seminar, raising an evil demon possibility raises conversational standards — at those elevated standards, it is genuinely true that you don't know you have hands. In everyday conversation, low standards apply — it is genuinely true that you know you have hands. Both are true in their respective contexts, so there is no contradiction and neither party errs. Contextualism dissolves the skeptical puzzle rather than solving it by refuting the skeptic."

- question: "In contextualism, what makes 'knows' similar to an indexical expression like 'here' or 'I,' and why does this matter for the skepticism debate?"
  type: short-answer
  answer: "Like 'here' and 'I,' the word 'knows' in contextualism picks out different things depending on who uses it and in what context. 'I am hungry' is true when said by a hungry person; 'She knows her car is parked outside' is true in a low-standards context but false in a high-standards one. What varies is not the world but the semantic standards the word invokes. For the skepticism debate, this means the skeptic and the ordinary person can both be stating truths — the skeptic operates at elevated standards where ruling out a Cartesian demon is required, while in everyday life those standards don't apply."
  explanation: "The indexical analogy is the core semantic machinery of contextualism. Understanding it reveals why contextualism is a thesis about language — specifically about how the word 'knows' works — rather than a thesis about metaphysics or psychology. It reframes skepticism from 'is knowledge really possible?' to 'what standards does "knows" invoke in this conversational context?' — a move that many find illuminating and others find evasive."
```

## Explainer

From your work on responses to skepticism and the problem of the external world, you are familiar with the pressure skeptical arguments place on ordinary knowledge claims. The skeptic says: you cannot know you have hands because you cannot rule out that you are a brain in a vat. The problem is that this argument seems valid — you really cannot rule out the possibility — yet walking away and denying that you know you have hands seems absurd. You know you have hands. So which is it? Contextualism is a proposal about how both can be true without contradiction.

The key move is to treat "knows" as a **context-sensitive expression** — like indexicals such as "here," "now," or "I," whose reference shifts with the context of utterance. When I say "I am hungry," the word "I" refers to me; when you say it, "I" refers to you. Both utterances are true, but about different people. Contextualism proposes that "knows" works analogously: the word "knows" picks out different epistemic relations in different conversational contexts because the **standards** that must be met to count as knowing vary with the context of the attributor. In a normal, low-stakes context, the standards are loose; in a philosophically charged or high-stakes context, they become stringent.

Keith DeRose's **bank cases** make this vivid. Case One: It is Friday afternoon. You and your partner drive past the bank and you say, "I'll just deposit this check Monday — I was here two weeks ago and it was open on Saturday." She says, "How do you know it's open Saturdays?" You reply, "I know it's open — I was just there." This seems fine. Case Two: Same situation, but you desperately need to deposit the check by Monday morning or a payment will bounce. Your partner asks the same question. Now your reply "I know it's open" seems insufficient — you should check again, call ahead, verify. In the high-stakes context, the standards for knowing have risen, and your belief based on a two-week-old visit no longer meets them. Contextualism says: in Case One, it is true that you know; in Case Two, it is true that you do not know. The same belief, in the same person, is correctly described by both attributions — because the word "knows" tracks different standards in the two contexts.

This explains the skeptical puzzle elegantly. In the philosophy seminar, raising the possibility of a Cartesian evil demon raises the conversational standards to include ruling out that possibility. At those elevated standards, you genuinely do not know you have hands — the knowledge-that-you-have-hands-sentence is false in that context. But when you leave the seminar and go about your day, the conversational context drops back to normal standards, and it becomes true again that you know you have hands. There is no contradiction because the word "knows" is doing different work in the two contexts. Contextualism thus reframes skepticism not as a discovery about the limits of human knowledge but as a reflection of what happens when you raise epistemic standards in conversation.

The main objection is the **subject-sensitivity worry**: contextualism locates the standard-shift in the *attributor's* context, not the *subject's* situation. This means that whether you know something is partly a function of who is talking about you and in what context, which seems strange. If a friend in a panic says "She doesn't know whether the bridge is safe," this could make it true that you don't know — even though nothing changed in your epistemic situation. Invariantists argue this gets things backwards: what matters is how well the subject is placed to track the truth, not what is being said about her. John Hawthorne's **subject-sensitive invariantism** and Jeremy Stanley's view that standards are fixed by *practical stakes of the subject* are alternative positions that try to capture the intuitions behind the bank cases while keeping the truth of "knows" fixed by the subject's situation. Contextualism remains one of the most discussed and contested proposals in contemporary epistemology precisely because it takes the variability in our knowledge-talk seriously while raising hard questions about where that variability is located.


