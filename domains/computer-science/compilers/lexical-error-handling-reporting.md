---
id: lexical-error-handling-reporting
title: Lexical Error Handling and Reporting
domain: computer-science
course: compilers
prerequisites:
- id: scanner-generator-implementation
  type: hard
builds-toward:
- syntax-error-recovery-techniques
tags:
- error-handling
- diagnostics
- robustness
stage: advanced
status: draft
---

# Lexical Error Handling and Reporting

## Core Idea
Real lexical analysis must handle invalid input gracefully—unknown characters, unterminated strings, malformed numeric literals. Error recovery strategies range from character skipping to fix suggestions, and messages must precisely identify problems.

## How It's Best Learned
Implement scanners handling various malformed inputs. Practice writing error messages that clearly identify the problem and source location.

## Common Misconceptions
Lexical errors mean the entire file is unusable (often you can skip characters and continue). Error messages should list all possible errors at once (better to focus on one clear error).
