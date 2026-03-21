---
id: aktionsart-lexical-aspect
title: Aktionsart (Lexical Aspect)
domain: language-and-communication
course: linguistics
prerequisites:
- id: verbs-intro
  type: hard
- id: lexical-semantics
  type: hard
- id: event-semantics
  type: hard
builds-toward:
- viewpoint-aspect-perfective-imperfective
- tense-aspect-formal-semantics
tags:
- semantics
- aspect
- verb-classes
- telicity
stage: advanced
status: draft
---

# Aktionsart (Lexical Aspect)

## Core Idea
Aktionsart (lexical aspect) refers to the inherent temporal properties of verbs and predicate phrases independent of grammatical marking. Verbs fall into classes—states (know), activities (run), accomplishments (build a house), and achievements (reach)—that determine how they interact with time operators, adverbial modification, and progressive or perfect marking.

## How It's Best Learned
Begin with the classic verb-class classification and examine how each class behaves with progressive (be running), perfect (have built), and temporal adverbials (for an hour). Then compare across typologically distant languages to see universal vs. language-specific patterns.

## Common Misconceptions
Conflating aktionsart (lexical meaning) with grammatical aspect (morphosyntactic marking). Assuming all languages encode verb classes identically; many have less granular or different aspectual classification systems.

## Questions

```yaml
- question: "A student classifies 'run' as an accomplishment because running takes time and can last an hour. What error have they made?"
  type: multiple-choice
  options:
    - "'Run' is a state, not an accomplishment, because it lacks internal dynamism"
    - "'Run' is an activity — it is dynamic and durative but lacks a telic endpoint; 'run a marathon' is an accomplishment"
    - "Duration alone is sufficient to classify a predicate as an accomplishment; the student is correct"
    - "'Run' is an achievement because it describes a rapid physical transition"
  answer: 1
  explanation: "Accomplishments require both durativity AND telicity — they have a built-in natural endpoint. 'Run' alone has no inherent completion point: you can run indefinitely without reaching any goal. It passes the atelic diagnostic: 'She ran for an hour' is perfectly natural, but 'She ran in an hour' is odd or requires special context. Add a goal ('run a marathon,' 'run to the store') and the predicate becomes telic — now 'in two hours' is natural and the event can be completed or left incomplete."

- question: "Which diagnostic best distinguishes accomplishments from activities?"
  type: multiple-choice
  options:
    - "The progressive test — activities accept the progressive freely; accomplishments do not"
    - "The 'for an hour / in an hour' test — accomplishments accept 'in an hour' naturally; activities accept 'for an hour' but resist 'in an hour'"
    - "The stative test — accomplishments resist the progressive; activities are fully compatible with it"
    - "The perfect entailment test — activities entail completion in the perfect; accomplishments leave completion open"
  answer: 1
  explanation: "Telicity is what distinguishes accomplishments (telic) from activities (atelic), and the 'in an hour / for an hour' test probes exactly this. 'She built the bridge in a year' is natural; 'She built the bridge for a year' implies she didn't finish. 'She swam for an hour' is natural; 'She swam in an hour' is odd without a telic modifier. Both classes accept the progressive and do not resist it, so the progressive test (option A) doesn't help here — it distinguishes states (which resist progressive) from dynamic predicates."

- question: "Grammatical aspect (e.g., the English progressive or perfect) and lexical aspect (Aktionsart) are two names for the same phenomenon, differing only in whether they are studied by linguists or philosophers of language."
  type: true-false
  answer: false
  explanation: "They are analytically distinct. Aktionsart (lexical aspect) is an inherent property of the verb or predicate phrase — the temporal structure built into its meaning. Grammatical aspect is what the speaker imposes through morphosyntactic marking (progressive, perfect, etc.) — it reflects the speaker's perspective on how the event is viewed. A speaker can use imperfective morphology with a telic predicate ('She was building the house when it collapsed'), coercing the predicate out of its default telic reading. Conflating the two produces systematic errors in cross-linguistic analysis."

- question: "The same verb can appear in different Aktionsart classes depending on the full predicate context — for example, 'push a cart' (activity) versus 'push a cart to the door' (accomplishment)."
  type: true-false
  answer: true
  explanation: "This is crucial: Aktionsart is a property of the full predicate, not just the bare verb. Adding a goal phrase ('to the door'), a quantized object ('a house' vs. 'houses'), or a result state converts an atelic predicate into a telic one. This compositionality of aspect — called 'aspectual coercion' or 'telicity shift' — shows that Aktionsart is not a fixed lexical property of verb roots but emerges from the entire VP. The diagnostics must be applied to full predicate phrases, not bare verbs."

- question: "Why is the telicity distinction — whether a predicate has a natural endpoint — important for predicting how a verb will interact with grammar?"
  type: short-answer
  answer: "Telicity determines how a predicate interacts with time adverbials, tense-aspect morphology, and entailment patterns in principled ways. A telic predicate in the simple past entails that the endpoint was reached ('She built the house' implies completion). An atelic predicate in the simple past does not entail any completion ('She ran' makes no claim about reaching a goal). This contrast drives the 'in an hour' vs. 'for an hour' distribution, the progressive entailment test (accomplishments under progressive entail partial completion of the endpoint; achievements do not), and cross-linguistic variation in how perfectivity is encoded. Telicity is not just a classification label — it is an explanatory variable for a wide range of grammatical phenomena."
  explanation: "The practical payoff of the Aktionsart framework is precisely its predictive power. Once you know a predicate's temporal class, you can predict a cluster of grammatical behaviors, not just classify it into a box. This is why Vendler's analysis was theoretically important: it connected what seemed like unrelated grammatical facts (progressive oddness with states, 'in'/'for' distribution, perfect entailments) to a single underlying parameter — the internal event structure of the predicate."
```

## Explainer

From your study of **lexical semantics** and **event semantics**, you know that verbs do not merely name actions — they encode structured information about how events unfold in time. Aktionsart (German for "type of action," also called lexical aspect) captures this temporal structure as a property of the verb or predicate phrase itself, before any grammatical marking. The canonical classification, developed by Zeno Vendler, sorts predicates into four classes based on three binary features: **dynamism** (does the situation involve change?), **telicity** (does it have a natural endpoint?), and **durativity** (does it extend over time?).

**States** (know, believe, contain) are non-dynamic and atelic: they persist without internal change toward any goal. **Activities** (run, swim, push a cart) are dynamic and durative but atelic — running has no inherent completion point. **Accomplishments** (build a house, paint a picture) are dynamic, durative, and telic: they unfold over time toward a specific endpoint that constitutes their completion. **Achievements** (reach the summit, notice the error) are dynamic and telic but non-durative — they are instantaneous transitions. The classification is not about world facts but about the event structure lexicalized into the predicate: *push a cart* (activity) versus *push a cart to the door* (accomplishment) shows how the same verb can shift class depending on the full predicate.

The critical skill in applying this framework is the battery of diagnostics. The **"for an hour" / "in an hour"** test distinguishes atelic from telic predicates: *She swam for an hour* is natural (activity); *She swam in an hour* is odd. Conversely, *She built the bridge in a year* is natural (accomplishment); *She built the bridge for a year* implies she didn't finish. The **progressive entailment test** separates achievements from other dynamic classes: if *She is building a house* entails that she has made some progress toward a complete house, but *She is noticing the error* does not entail she has partially noticed it, then noticing is an achievement and building is an accomplishment. These tests are not just classification exercises — they reveal how the temporal structure of a predicate interacts with grammatical operators in principled ways.

Aktionsart matters for grammar because it constrains how verbs interact with morphosyntax. States resist the progressive (*I am knowing the answer* is ungrammatical in English); achievements are odd with the simple past in some languages because they are instantaneous; accomplishments in the perfect (*She has built the house*) imply completion in a way that activities (*She has been running*) do not. This is the bridge to your next topic: **viewpoint aspect** (grammatical aspect) is what the speaker chooses to impose on a situation; Aktionsart is the situation's inherent temporal shape. The two interact — grammatical aspect can coerce a verb out of its default class — but they are analytically distinct, and conflating them produces systematic errors in cross-linguistic analysis.
