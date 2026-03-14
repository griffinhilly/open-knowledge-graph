---
id: method-development-lifecycle
title: Method Development Lifecycle
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: method-validation
  type: hard
- id: quality-assurance-analytical
  type: hard
tags:
- method development
- optimization
- robustness
- method transfer
- revalidation
- regulatory
- DOE
- design of experiments
stage: formal-systems
status: draft
---

# Method Development Lifecycle

## Core Idea
Developing an analytical method is an iterative lifecycle that extends well beyond initial optimization: it begins with defining the analytical target profile (what needs to be measured, in what matrix, at what concentration, with what precision), proceeds through screening and optimizing conditions (often using design of experiments to explore multiple variables efficiently), and culminates in formal validation. But the lifecycle does not end at validation. Method transfer to another laboratory or instrument requires demonstrating equivalent performance at the receiving site. Changes in reagents, columns, instruments, or sample types trigger partial or full revalidation. Regulatory frameworks (ICH, FDA, USP) prescribe when revalidation is mandatory and what documentation is required, embedding the method in a quality system that ensures it remains fit for purpose throughout its operational life.

## How It's Best Learned
Take a validated HPLC method and deliberately transfer it to a second instrument or column: adjust conditions to restore system suitability, run transfer validation experiments, and document equivalence. This exercise reveals that method development is never truly 'done' and builds appreciation for the regulatory and practical realities of maintaining a method.

## Common Misconceptions
- Method development is not a one-time activity that ends with validation; methods require ongoing monitoring, periodic revalidation, and adaptation as instruments, reagents, and regulatory expectations evolve.
- Optimizing one parameter at a time (OFAT) is inefficient and can miss interactions between variables; design of experiments (DOE) approaches are standard practice in modern method development because they reveal interactions and find true optima with fewer experiments.
