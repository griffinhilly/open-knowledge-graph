---
id: test-security-and-item-banking
title: Test Security and Item Banking Systems
domain: psychology
course: psychometrics
prerequisites:
- id: classical-test-theory
  type: soft
- id: measurement-scales-psychology
  type: soft
tags:
- item-banking
- test-security
- item-exposure
- form-assembly
- item-metadata
stage: advanced
status: draft
---

# Test Security and Item Banking Systems

## Core Idea
Maintaining test security and developing systematic item banks are essential for test longevity and fairness. Item banking involves cataloging, storing, and managing items with their psychometric properties (difficulty, discrimination, IRT parameters) so that new test forms can be assembled quickly while balancing item exposure, maintaining measurement quality, and ensuring content coverage. Security practices protect against item exposure that compromises test validity.

## Explainer

Classical test theory gives you the tools to characterize individual items — difficulty, discrimination, reliability — and measurement scales give you frameworks for thinking about what a score represents. An **item bank** applies these tools at scale: it is a structured repository of items, each tagged with its psychometric properties, content specifications, and administrative history, maintained so that test forms can be assembled systematically rather than ad hoc. Think of it like a well-organized library where every book has a catalog record; without the catalog, you cannot efficiently find what you need or know what you already have.

The core function of an item bank is enabling **form assembly** — the process of constructing a new test form that meets specific measurement targets. When assembling a form, a test developer typically specifies constraints at multiple levels: content coverage (25% of items must address Topic A), statistical targets (mean difficulty around 0.60, mean discrimination above 0.30 in CTT terms, or items covering the ability range of interest in IRT terms), and practical constraints (no items that have appeared on the last two operational forms, no items that share stimulus material). Automated test assembly software treats this as a combinatorial optimization problem, selecting from the bank the set of items that best satisfies all constraints simultaneously. Without a well-maintained bank with accurate metadata, this process either fails or produces forms of inconsistent quality.

**Item exposure** is the central security concern. An item that has been seen by many examinees before they are tested has been compromised — examinees with access to the item have an unfair advantage, and the score is no longer a valid measure of the construct. Exposure control is therefore built into both form assembly (by tracking how often each item has been used across operational forms) and test administration (in computerized adaptive testing, algorithms deliberately limit how frequently high-value items are served). Items with high discrimination are the most valuable and therefore the most at risk: if a single highly discriminating item near the cut score is leaked, it can distort pass/fail outcomes for many candidates.

Security practices form a system that protects the bank's integrity across the full item lifecycle. During **item development**, draft items are handled under controlled conditions; access is limited to authorized personnel; review committees use secure workspaces. During **test administration**, proctoring protocols prevent item copying; test booklets are numbered and accounted for; digital tests use encrypted delivery. After administration, **incident response** procedures handle reports of item exposure — items suspected of compromise are retired from active use and flagged in the bank. **Item retirement** decisions involve trading off the cost of losing a calibrated item against the validity threat of continued use. The measurement scales framework you studied clarifies what is at stake: compromised items contaminate the construct validity of the score, which is the foundation of every interpretive use the test supports.
