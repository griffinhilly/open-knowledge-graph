---
id: peer-review-history
title: "Peer Review: Origins, Evolution, and Critiques"
domain: history
course: history-of-science
prerequisites:
- id: enlightenment-science
  type: soft
- id: science-funding-institutions
  type: hard

builds-toward:
- science-ethics-and-responsibility
tags:
- history
- History Of Science
stage: advanced
status: validated
---

# Peer Review: Origins, Evolution, and Critiques

## Core Idea
Peer review — evaluation of research by other scientists before publication — emerged gradually as the mechanism for quality control in science. Early scientific societies like the Royal Society relied on editors to judge papers; by the 20th century, peer review became standard. Peer review has advantages: it reduces publication of clearly erroneous work; it provides feedback for improvement; it creates community ownership of standards. Yet it has limitations: peers may reject novel ideas; slow review delays publication; anonymity can enable unfairness; reviewers often lack incentive to do thorough review. The crisis in replicability in some fields (psychology, medicine) has raised questions about whether peer review adequately filters poor science. P-hacking — manipulating statistical analyses to produce significant results — can escape peer review. Yet critics also recognize that alternative systems (publication without review, or publication with open post-hoc commentary) have their own problems. Peer review remains the foundation of scientific credibility, yet its shortcomings are increasingly recognized. Understanding the history and limits of peer review is important for understanding modern science: it reveals that gatekeeping is imperfect, that scientific consensus can incorporate errors, and that fixing problems requires structural changes, not just individual moral reform.

## Questions

```yaml

- question: "The replication crisis in psychology and medicine revealed a specific statistical manipulation that peer review failed to catch. What is 'p-hacking'?"
  type: short-answer
  answer: "P-hacking refers to manipulating the analysis of a dataset -- adding or removing variables, stopping data collection when results are significant, reporting only significant subgroup analyses -- until a p-value below 0.05 is achieved, then reporting the result as if the analysis had been pre-specified. Because peer reviewers rarely see raw data or analysis code, they cannot detect this. The result is published findings that appear statistically rigorous but are actually exploratory patterns inflated by selective reporting. Large replication studies, such as the 2015 Open Science Collaboration project that reproduced only 39% of published psychology findings, exposed how widespread this problem was."
  explanation: "P-hacking is not necessarily conscious fraud -- researchers may genuinely believe the manipulation is justified. The problem is structural: publication bias rewards positive results, peer review cannot detect exploratory data mining, and statistical thresholds (p < 0.05) create a bright line that incentivizes crossing it by any means."

- question: "When did peer review become the standard mechanism for evaluating scientific manuscripts before publication?"
  type: multiple-choice
  options:
    - "Since the founding of scientific journals in the 17th century -- the Royal Society used peer review from the start"
    - "Peer review became widespread only in the mid-20th century; earlier journals relied on editorial judgment, and some major journals adopted it only in the 1970s"
    - "Peer review was introduced by Vannevar Bush in 1945 as part of the NSF grant process"
    - "Peer review has existed as long as science itself -- Greek philosophers reviewed each other's arguments"
  answer: 1
  explanation: "The history of peer review is often misunderstood. The Royal Society's Philosophical Transactions (1665) had editorial oversight but not systematic peer review. External referee review became standard gradually: Nature adopted it only in the 1970s. The assumption that peer review is a timeless feature of science is itself a historical myth -- understanding its emergence helps evaluate its shortcomings."

- question: "What are the main arguments for and against anonymous (double-blind) peer review compared to open review?"
  type: short-answer
  answer: "Anonymous review argues that anonymity protects junior researchers and non-prestigious institutions from reviewer bias -- known authors from elite universities get easier reviews. Critics argue that anonymity enables irresponsible reviewing (reviewers have no accountability for unfair or superficial reviews), that it doesn't prevent reviewers from guessing authors' identities, and that it hides conflicts of interest. Open review (reviewers' names known to authors, or reviews published alongside papers) increases accountability and allows readers to evaluate reviewers' credibility and potential biases. Some journals and preprint servers have adopted open review, finding it reduces gatekeeping while maintaining quality."
  explanation: "The debate about peer review structure is active and unresolved. Different fields have adopted different practices, and evidence on which works best is limited -- peer review is itself insufficiently peer reviewed."

- question: "Peer review effectively prevents publication of fraudulent research."
  type: true-false
  answer: false
  explanation: "Several high-profile fraud cases -- Hwang Woo-suk's fabricated stem cell papers (2004-2005), Diederik Stapel's decade of fabricated psychology data, Jan Hendrik Schon's falsified physics -- all passed peer review. Peer reviewers assess manuscripts, not original data; they cannot detect fabrication without access to raw files. Peer review's purpose is to evaluate logical coherence, methodological soundness, and adequacy of evidence -- it is not designed to detect deliberate fraud. Fraud detection typically comes from anomalies noticed by other researchers, whistleblowers, or post-publication data analysis."

- question: "What was the 2015 Open Science Collaboration study, and what were its main findings about psychology research?"
  type: short-answer
  answer: "The 2015 Open Science Collaboration, involving over 270 researchers, attempted to replicate 100 studies published in prominent psychology journals. Only 36-39% of the replications produced statistically significant results matching the original findings, and effect sizes were on average about half those in the original papers. The study did not prove fraud; it showed that standard scientific practices (flexible analysis, publication of positive results only, small samples) produced inflated and unreliable findings at scale. It triggered a reform movement: pre-registration of hypotheses, open data sharing, registered reports (where journals commit to publish regardless of results)."
  explanation: "The OSC study was methodologically sophisticated and controversial -- some psychologists disputed its conclusions. The reform movement it triggered (open science practices, pre-registration) represents one of the most significant changes in scientific practice in recent decades."

```

## Explainer

Peer review -- the evaluation of scientific manuscripts by other researchers before publication -- is widely treated as a defining feature of science itself, a mechanism ensuring that published claims have withstood critical scrutiny. Yet peer review in its modern form is a mid-20th century innovation, and its limitations have become increasingly apparent through systematic study of scientific practice.

The earliest scientific journals -- the Royal Society's Philosophical Transactions (1665), the Journal des scavans (1665) -- relied on editorial judgment rather than external referees. Scientific societies served a gatekeeping function through membership and presentation norms, but the idea of systematically sending manuscripts to expert referees was slow to develop. Major journals adopted it at different times: Nature formalized referee review only in the 1970s. The assumption that peer review is ancient and universal is itself a myth.

The modern peer review system became established alongside the postwar expansion of scientific publishing. With thousands of journals and millions of papers annually, editors needed ways to filter submissions -- external reviewers provided that filter. Grant review at funding agencies (NSF, NIH) adopted similar procedures: panels of scientists evaluating proposals before funding decisions. Peer review thus became embedded in two of science's most important gatekeeping functions: publication and funding.

The limitations of peer review became visible through the replication crisis, which emerged most prominently in psychology and medicine in the 2000s-2010s. The 2015 Open Science Collaboration reproduced only 36-39% of 100 published psychology findings. Large-scale medicine analyses found that many standard treatments had never survived rigorous replication. The mechanism was not primarily fraud but structural: publication bias (journals prefer positive results), small sample sizes that permit chance findings, and p-hacking -- flexible analysis choices that allow researchers to cross the p < 0.05 threshold. None of these are detectable by standard peer review.

High-profile fraud cases (Hwang Woo-suk in stem cells, Diederik Stapel in psychology, Jan Hendrik Schon in physics) exposed another limitation: reviewers see manuscripts, not data, and cannot detect fabrication without access to original files.

The reform movement emerging from the replication crisis includes pre-registration (researchers publicly commit to hypotheses and analysis plans before data collection), open data requirements, registered reports (journals commit to publish regardless of results), and open peer review. These represent real structural changes to scientific practice -- acknowledgments that peer review alone is insufficient and that incentive structures rewarding novelty over replication need redesign. The history of peer review reveals not that science is broken but that its quality-control mechanisms are historically contingent and require ongoing revision.
