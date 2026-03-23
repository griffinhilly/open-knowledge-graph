---
id: problem-of-induction-hume
title: The Problem of Induction
domain: philosophy
course: philosophy-of-science
prerequisites:
- id: inductive-reasoning
  type: hard
- id: empiricism-scientific-inquiry
  type: soft
builds-toward:
- confirmation-theory-science
- popper-falsificationism
- bayesian-confirmation-science
tags:
- induction
- justification
- inference
stage: expert
status: validated
---

# The Problem of Induction

## Core Idea
David Hume identified a deep logical problem: induction (reasoning from observed cases to unobserved ones) cannot be justified by logical deduction alone. Yet science relies fundamentally on inductive inference. How can scientists justify their inductive conclusions? And is induction rationally justifiable at all? This problem drives much of modern philosophy of science.

## How It's Best Learned
Study Hume's original argument, then examine philosophical responses: Popper's falsificationism avoids induction, Bayesian approaches assign probabilities to conclusions, inference to the best explanation offers non-inductive justification.

## Common Misconceptions
- The problem of induction shows induction is irrational.
- Science can avoid induction entirely.
- Induction has been 'solved' and is no longer philosophically relevant.

## Questions

```yaml
- question: "A scientist argues: 'Induction is justified because it has worked reliably in the past — every time we've applied inductive reasoning, our conclusions have been borne out.' What is Hume's response to this justification?"
  type: multiple-choice
  options:
    - "Hume accepts this as a valid justification — past success is exactly the kind of empirical evidence that justifies scientific methods"
    - "This justification is itself an inductive inference (past success → future reliability), making it circular — using induction to justify induction"
    - "Hume rejects this because the scientist has confused induction with deduction"
    - "Hume accepts empirical justifications but not logical ones, so this works as a practical defense even if not a logical one"
  answer: 1
  explanation: "This is precisely the circularity Hume identifies. The claim 'induction has worked in the past, therefore it will work in the future' is itself an inductive inference — it assumes the principle of uniformity of nature (past patterns continue) to justify the principle of uniformity of nature. You cannot justify induction by pointing to its track record without already assuming that past track records are a reliable guide to future performance — which is exactly what the justification is trying to establish. Hume's point is not that induction doesn't work but that any attempt to rationally justify it runs in circles."

- question: "Popper proposed that science proceeds through falsification rather than confirmation — we test theories by trying to refute them, not confirm them. Does this dissolve Hume's problem of induction?"
  type: multiple-choice
  options:
    - "Yes — falsificationism eliminates inductive inference entirely; science only needs deductive logic to refute theories"
    - "Mostly yes — falsificationism shows that science can proceed without induction in the context of discovery, though not in the context of justification"
    - "No — falsificationism faces its own induction problem: we inductively prefer theories that have survived tests over untested ones, which requires inductive reasoning"
    - "No — Popper's view is internally inconsistent because falsification is itself an inductive process"
  answer: 2
  explanation: "Falsificationism avoids inductively confirming theories but does not fully escape induction. If we never inductively support theories and only eliminate refuted ones, we face the question: why should we trust a theory that has survived tests more than an untested one? The answer — 'because it has proven robust to refutation' — is itself an inductive inference about future performance from past test results. Popper acknowledged this problem in different forms. Falsificationism shifts where induction enters the picture but does not eliminate the underlying logical gap Hume identified."

- question: "Hume's problem of induction demonstrates that induction is irrational and scientists should stop relying on it."
  type: true-false
  answer: false
  explanation: "This is the most common misreading of Hume. The problem of induction shows that induction cannot be justified by purely non-circular logical argument — the justification is either circular (appealing to induction to justify induction) or involves premises that themselves require inductive support. This is a problem of *justification*, not *rationality in practice*. Most philosophers and scientists hold that induction is in some sense rational and practically indispensable; the problem is giving a philosophically satisfying account of *why* it is rational. Hume himself described induction as a psychological habit ('custom') — he explained it, he didn't condemn it."

- question: "Any attempt to justify induction by appealing to its past reliability is itself an inductive inference."
  type: true-false
  answer: true
  explanation: "The argument 'induction has worked reliably in the past, therefore it will work in the future' has exactly the same logical structure as any inductive inference: it moves from observed instances (past successes) to a conclusion about unobserved cases (future reliability). To assume this argument is valid, you must already accept that past patterns predict future ones — which is the principle of uniformity of nature that induction is supposed to justify. The circularity is not subtle: the conclusion contains the premise needed to validate the inference."

- question: "Explain why attempts to justify induction by appealing to its past reliability are circular, and why this circularity is philosophically significant."
  type: short-answer
  answer: "To justify induction by its past track record ('induction has worked before, so it will work again') is to make an inductive inference — reasoning from past instances to a future conclusion. But this is exactly the type of reasoning whose justification is in question. You cannot validate the inference form 'observed patterns continue' by using an inference of that same form; doing so assumes the conclusion. The circularity is philosophically significant because it means there is no purely logical, non-circular foundation for one of science's most fundamental reasoning patterns. Hume's insight is that the confidence we place in induction rests on a psychological disposition — what he called 'custom' — rather than a logical proof. This forces philosophers to either accept that some important epistemic practices lack circular-free justification, or to redefine what rational justification requires."
  explanation: "The responses to this problem reveal fundamentally different views of rationality: Popper avoids induction (but at significant cost to how science works), Bayesians embrace probabilistic updating while accepting arbitrary priors, and pragmatists argue that 'it works' is a legitimate credential even without a foundational proof. None has fully closed the gap Hume opened."
```

## Explainer

You already know from your study of inductive reasoning that induction means inferring general conclusions from specific observations: every swan I've observed is white, therefore all swans are white. Science is built on this kind of inference — every law of physics, every clinical finding, every engineering specification rests on the assumption that patterns observed in the past will continue into the future. Hume's problem is a devastating attack on the rational foundations of this assumption.

Hume's argument is surprisingly simple and surprisingly hard to answer. Suppose you observe the sun rise every morning for your entire life and want to conclude it will rise tomorrow. What justifies that conclusion? You might say: *nature is uniform* — the future resembles the past, so past patterns are a reliable guide. But where does this principle of **uniformity of nature** come from? You haven't deduced it from pure logic — it's not a logical truth that the future resembles the past. You believe it because the future has resembled the past *in your experience so far*. But that is itself an inductive inference. You are justifying induction by appealing to induction — a **circular argument**. Hume concluded that induction cannot be rationally justified: it is a psychological habit (a "custom") rather than a logical principle.

What makes this more than an academic puzzle is that it strikes at the foundations of empirical science itself. Science doesn't just collect observations; it extrapolates from them to laws, predicts the future, and generalizes to unobserved cases. If those extrapolations have no rational foundation — if we're running on psychological habit rather than logic — then the authority of scientific knowledge is in doubt. The problem of induction is what makes confirmation theory (how evidence supports hypotheses) a serious philosophical discipline, not just a housekeeping problem.

The major responses to Hume reveal a lot about how different philosophical traditions understand rationality. **Popper's falsificationism** tries to avoid induction entirely: science doesn't confirm theories, it eliminates refuted ones. We never establish that a theory is true, only that it has survived attempts to falsify it. This is bold but generates its own problems — if we can't inductively support a theory, why prefer one that has survived tests over an untested one? **Bayesian approaches** assign probabilities to hypotheses and update them using Bayes's theorem; this doesn't justify the starting prior probabilities but offers a formally rigorous framework for updating beliefs as evidence arrives. **Pragmatist and naturalist responses** question whether rational justification of the kind Hume demands is even the right goal — we use induction because it works, and "works" is a legitimate epistemic credential.

The misconceptions matter here. The problem of induction doesn't prove that induction is *irrational* — it shows that the *justification* of induction can't be purely logical or non-circular. In practice, induction is indispensable, and most scientists and philosophers believe it is in some sense rational. The problem is explaining *why* it is rational in a way that doesn't smuggle in circular reasoning. That this question remains open after 300 years is part of what makes it one of the most important problems in philosophy.

