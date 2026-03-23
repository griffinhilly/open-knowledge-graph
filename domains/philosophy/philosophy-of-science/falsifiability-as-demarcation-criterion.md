---
id: falsifiability-as-demarcation-criterion
title: Falsifiability as the Criterion of Demarcation
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: karl-popper-falsificationism
  type: hard
builds-toward:
- normal-science-versus-crisis
tags:
- falsifiability
- demarcation
- testability
stage: expert
status: validated
---

# Falsifiability as the Criterion of Demarcation

## Core Idea
For Popper, a theory is falsifiable if there exist possible observations that would disprove it; falsifiability is the mark of science. This criterion elegantly separates science from pseudoscience and unfalsifiable metaphysics. However, it faces counterexamples where unfalsifiable statements seem scientific, and auxiliary hypotheses complicate the picture.

## Questions

```yaml
- question: "A new theory of personality psychology has been confirmed by thousands of case studies, but it is formulated so that it can explain any personality trait or behavioral pattern after the fact. Under Popper's demarcation criterion, how should this theory be classified?"
  type: multiple-choice
  options:
    - "Scientific, because it has been confirmed by a large and diverse body of evidence"
    - "Scientific, because it makes accurate predictions about human behavior"
    - "Non-scientific or pseudoscientific, because it cannot specify which observations would refute it — a theory that explains everything predicts nothing"
    - "Non-scientific only if it has been explicitly used to make false predictions"
  answer: 2
  explanation: "Popper's criterion does not reward confirmation — it demands falsifiability. A theory that can accommodate any possible observation makes no genuine claim about what we will observe. Popper pointed to Freudian psychoanalysis as an example: whatever a patient did, the analyst could explain it as confirming the theory. The number of confirmations is irrelevant; what matters is whether the theory could in principle be refuted by an observation it did not predict."

- question: "When early astronomers found that Newtonian mechanics failed to fully account for Uranus's orbit, they postulated a new planet (eventually confirmed as Neptune) rather than abandoning Newton's laws. What does this illustrate about falsification in practice?"
  type: multiple-choice
  options:
    - "It shows that Newtonian mechanics was not falsifiable and therefore not scientific"
    - "It illustrates the Duhem-Quine problem: when a prediction fails, you can save the core theory by modifying an auxiliary hypothesis rather than rejecting the theory itself"
    - "It proves that scientific theories are never actually falsified — scientists always preserve them"
    - "It shows that confirmation (discovering Neptune) is what really drives science, not falsification"
  answer: 1
  explanation: "The Duhem-Quine problem shows that no single theory is tested in isolation. When a prediction fails, the blame could fall on any auxiliary assumption rather than the core theory. Saving Newton's laws by adjusting the auxiliary (that all relevant bodies had been accounted for) was scientifically productive here because it led to a novel prediction — Neptune's existence — that was confirmed. Lakatos distinguished progressive research programmes (generating new successful predictions) from degenerative ones (only accommodating old failures) to capture why this move was legitimate in Newton's case."

- question: "According to Popper, a theory that makes specific, risky predictions — ones that could easily be shown false — is more scientific than a theory that only predicts what is already likely."
  type: true-false
  answer: true
  explanation: "This is the core of Popper's asymmetry between confirmation and falsification. A 'risky' prediction — unlikely if the theory were false — is precisely what distinguishes bold scientific theories from vague ones. Einstein's prediction that light bends around the sun by a specific, quantified amount was risky: it was an unusual claim that could easily have been refuted by measurement. Theories that only predict what is likely regardless of their truth have no real empirical content. The more a theory rules out, the more scientific it is."

- question: "The Duhem-Quine problem shows that any theory can be protected from refutation by adjusting auxiliary hypotheses, proving that falsifiability cannot usefully distinguish science from non-science."
  type: true-false
  answer: false
  explanation: "The Duhem-Quine problem complicates falsifiability as a sharp criterion, but it does not eliminate its usefulness. Lakatos's response — distinguishing progressive research programmes (which use auxiliary adjustments to generate novel successful predictions) from degenerative ones (which only patch up past failures) — preserves the spirit of Popper's demarcation. Falsifiability becomes less a binary criterion and more a measure of methodological integrity: are auxiliary adjustments made in advance with testable consequences, or only post-hoc to avoid refutation?"

- question: "Why does Popper's criterion classify Freudian psychoanalysis as pseudoscience, even though it provides rich explanations for a wide range of human behaviors?"
  type: short-answer
  answer: "Popper's objection is that psychoanalytic theory is formulated so it can explain any behavior after the fact — but this explanatory power is precisely what disqualifies it. If a patient is aggressive, the analyst explains it as expression of repressed impulses; if passive, as suppression of those same impulses. No patient behavior could count as evidence against the theory. A theory compatible with every possible observation has no empirical content — it tells us nothing about what we will actually observe. Popper contrasted this with Einstein's general relativity, which made specific, risky predictions that could have been refuted."
  explanation: "Any sufficiently flexible framework can explain past events. Scientific theories earn their status by making specific claims that constrain what we will observe, thereby risking refutation. Psychoanalysis's ability to explain everything is its weakness, not its strength. The key asymmetry: a million confirmations can't prove a universal claim, but one genuine counterexample disproves it — so the scientific attitude is 'what would prove this wrong?' not 'how can I confirm this?'"
```

## Explainer

From your prerequisite on Popper, you know that he proposed falsificationism as an alternative to inductivism: rather than confirming theories with positive evidence, science advances by subjecting theories to severe tests and surviving attempted refutations. The demarcation criterion — falsifiability as the *line* between science and non-science — is both the sharpest application of that logic and its most controversial extension.

The criterion is elegant in its simplicity. A theory is **falsifiable** if there exist possible observations that would contradict it. Einstein's general relativity predicted that light bends around massive objects by a specific amount; that was a risky, testable prediction that could have been refuted when Eddington measured starlight deflection in 1919. Contrast this with the claim that "everything happens for a reason" — no possible observation could contradict it. It says nothing about what we will observe, so it tells us nothing about the world. For Popper, the asymmetry between confirmation and falsification is decisive: a million white swans can't prove all swans are white, but one black swan disproves it. So the scientific attitude is not "how can I confirm this?" but "what would prove this wrong, and does it?"

This criterion does powerful work against what Popper called pseudoscience — theories that accommodate any evidence. Freudian psychoanalysis and Adlerian psychology both struck Popper as examples: whatever a patient did, the analyst could explain it as confirmation of the theory. A theory that predicts everything predicts nothing. By contrast, Marx's historical materialism made specific predictions about the development of capitalism that failed — but Marxists kept revising auxiliary hypotheses to protect the core. Here the complication arises: the **Duhem-Quine problem** shows that no single hypothesis is ever tested in isolation. When an observation fails to match a prediction, you can always blame an **auxiliary hypothesis** rather than the core theory. Neptune was predicted before it was observed precisely by modifying an auxiliary assumption (that Newtonian mechanics had been applied to all the relevant bodies) rather than abandoning Newton's laws.

This creates a puzzle for the demarcation criterion. If scientists can always protect a core theory by adjusting auxiliaries, what makes science different from pseudoscience after all? Popper's answer invokes scientific **method and attitude**: science requires specifying in advance which observations would count as refutations, and it is intellectually dishonest to make that specification after the fact. Imre Lakatos later refined this into the idea of **research programmes** with a hard core and a protective belt of auxiliaries; a programme is progressive if it generates novel successful predictions, degenerative if it only accommodates old ones. The demarcation criterion, on this view, is less a sharp line than a spectrum of methodological integrity. Falsifiability remains the dominant intuition in scientific practice, even if its philosophical foundations require these qualifications.
