---
id: karl-popper-falsificationism
title: Karl Popper and Falsificationism
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: problem-of-induction
  type: hard
- id: problem-of-demarcation
  type: soft
builds-toward:
- falsifiability-as-demarcation-criterion
- imre-lakatos-research-programs
tags:
- popper
- falsification
- demarcation
stage: expert
status: validated
---

# Karl Popper and Falsificationism

## Core Idea
Popper argued that science advances not by confirming theories through induction but by attempting to falsify them. A theory is scientific if it makes falsifiable predictions—if there exist possible observations that would prove it wrong. This approach sidesteps both the problem of induction and verification's self-refutation.

## Questions

```yaml
- question: "A theory of personality claims it can explain any human behavior as either the expression of an unconscious drive or its repression. According to Popper's demarcation criterion, what is the fundamental problem with this theory?"
  type: multiple-choice
  options:
    - "The theory is false — unconscious drives do not exist"
    - "The theory has too few confirming observations to be accepted"
    - "The theory is unfalsifiable — no possible observation could refute it, so it fails to make risky scientific claims"
    - "The theory is too complex to test with current experimental methods"
  answer: 2
  explanation: "This is Popper's actual example of a pseudoscientific theory (Freudian psychoanalysis). The problem is not that it's false — Popper's criterion doesn't call it false. The problem is that it's unfalsifiable: because any behavior can be accommodated as either expression or repression, no possible observation would count as evidence against it. A theory that cannot be wrong in principle is not making risky predictions and is therefore, for Popper, not science. The demarcation is about the structure of the theory's claims, not their truth."

- question: "A scientist observes that every time the full moon occurs, crime rates rise slightly in her city. After 200 observations, she concludes that the moon causes crime. According to Popper, what is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "200 observations is not enough — she needs thousands"
    - "Correlation cannot establish causation, so the inference is incorrect"
    - "Confirming observations cannot logically establish a universal theory — the 201st case could always falsify it; induction is not valid justification"
    - "The theory is unfalsifiable because you cannot control the moon"
  answer: 2
  explanation: "Popper's core point is the logical asymmetry between verification and falsification. No matter how many confirming instances accumulate, they cannot logically entail the truth of a universal generalization — this is the problem of induction. The scientist's 200 observations confirm the pattern, but confirmation is not Popperian justification for accepting the theory. Scientific theories are accepted provisionally because they have survived attempts at falsification — not because they have accumulated confirmation. Option B (correlation ≠ causation) is also true but is a different objection; Popper's critique is about inductive logic, not causal inference."

- question: "According to Popper, a theory that has been confirmed by thousands of successful predictions is more likely to be true than a theory that has only survived a few tests."
  type: true-false
  answer: false
  explanation: "Popper explicitly rejects confirmation as a measure of theoretical merit or truth-likelihood. His concept of 'corroboration' is not a probability of truth — it is a historical record of having survived severe tests. A theory with thousands of confirming observations that were never risky (easy to pass tests) is less well-corroborated than a theory that made a single bold, specific prediction that could easily have been falsified but wasn't. Scientific knowledge is always conjectural on Popper's view — corroboration never converts conjecture into certainty."

- question: "Corroboration in Popper's framework means a theory has survived genuine attempts to falsify it — not that it has accumulated confirming evidence."
  type: true-false
  answer: true
  explanation: "Popper's technical term 'corroboration' is specifically defined to contrast with 'confirmation.' A well-corroborated theory is one that has been subjected to the most severe tests — tests that genuinely risked refutation, where a different outcome would have falsified the theory — and survived. The severity of the test matters: a bold, specific, risky prediction that holds up is more corroborating than a thousand low-risk observations consistent with the theory. Corroboration is a backward-looking record, not a forward-looking probability."

- question: "Explain the logical asymmetry between verification and falsification that forms the foundation of Popper's falsificationism. Why can a single counterexample falsify a universal theory while a million confirming observations cannot prove it?"
  type: short-answer
  answer: "The asymmetry is a matter of deductive logic. A universal theory (e.g., 'all swans are white') combined with an observation (e.g., 'this bird is a black swan') produces a valid deductive argument (modus tollens) that refutes the theory. But a confirming observation ('this swan is white') does not entail the universal claim — no finite number of confirming instances does. Verification requires induction, which is logically invalid; falsification requires only deduction, which is valid."
  explanation: "This logical asymmetry is what allows Popper to sidestep the problem of induction entirely. He does not solve induction; he abandons the goal of verification as the standard of scientific knowledge. If science advances only by surviving falsification attempts, then it never claims to have inductively proved anything — it only claims to have the best current conjecture that has survived the most severe tests so far. This makes science rational (disciplined by logic and evidence) without requiring the logically impossible move of inferring from finite observations to universal truths."
```

## Explainer

Your prerequisite — the problem of induction — established that no finite set of confirming observations can logically prove a universal generalization. You can observe a million white swans and still not prove "all swans are white," because the million-and-first might be black. Popper's response is radical: instead of solving the problem of induction, he abandons the goal of verification entirely. Science doesn't confirm; it *falsifies*.

The logical asymmetry Popper exploits is this: while confirming instances never entail a universal theory, a single disconfirming instance *does* entail its falsity. If the theory says "all swans are white" and you observe one black swan, the theory is refuted — by the deductively valid argument called **modus tollens**: if T is true then observation O would hold; O does not hold; therefore T is not true. This inference requires no induction. It is pure deductive logic. Popper calls the resulting method **hypothetico-deductivism**: scientists propose bold conjectures, derive specific observable predictions from them, and submit those predictions to test. Science advances not by accumulating verification but by surviving attempts at falsification — and by clearly failing when the predictions don't hold.

From this follows the **demarcation criterion**: a theory is *scientific* if and only if it is falsifiable — if it makes predictions that could in principle be shown false by observation. This criterion does the work of distinguishing science from pseudoscience, not by calling pseudoscience false, but by noting that it makes no risky claims. Popper's examples: Freudian psychoanalysis can explain any human behavior as consistent with the theory (repression if you're inhibited, reaction formation if you're not), and Marxist historical theory absorbed every failed prediction as a "temporary setback." Because these frameworks cannot be falsified by any possible evidence, they are, for Popper, not science — regardless of whether their claims happen to be true or false.

Notice that this framework completely reframes what scientific progress is. **Corroboration** — surviving rigorous tests — is not the same as confirmation. A well-corroborated theory is one that has survived the most severe tests: tests that genuinely risked refuting it. "The planet will appear at position X at time T" is highly falsifiable and therefore scientific. "Things tend toward equilibrium in the long run" is nearly unfalsifiable and therefore less scientific. The best theories are not those with the most confirming evidence but those that make the most specific predictions and have repeatedly survived tests designed to destroy them. Scientific knowledge, on Popper's picture, is always **conjectural** — our best current guess, never proved, always provisional — but it is not arbitrary, because the guesses are disciplined by exposure to potential refutation.
