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

## Explainer

From your work on scanner generators, you know that a lexer matches input characters against patterns defined by regular expressions or finite automata. But what happens when no pattern matches? In a textbook scanner, unrecognized input simply crashes the process. A production-quality scanner needs a principled strategy for handling malformed input — not just detecting it, but recovering from it well enough to continue scanning the rest of the file and report as many genuine errors as possible in a single pass.

The simplest recovery strategy is **panic mode**: when the scanner encounters a character that doesn't begin any valid token, it skips that character (or a short run of characters), emits an error message, and resumes scanning from the next plausible token boundary. This works because most lexical errors are local — a stray `@` in C code or an unterminated string literal doesn't invalidate the rest of the file. More sophisticated approaches include inserting a missing closing delimiter (like a quote character) or treating a sequence of illegal characters as a single error token. The goal is always the same: produce enough valid tokens that later compiler phases can do useful work, even if the source is broken.

Good error messages are surprisingly hard to write. A message like "error on line 37" is nearly useless. An effective lexical error report includes the **source location** (file, line, column), a description of what was found versus what was expected, and ideally a visual snippet showing the offending character in context. Modern compilers like Rust's `rustc` set a high bar here, underlining the exact problematic span and sometimes suggesting fixes. The key insight is that error reporting is a user interface problem — the "user" is a programmer trying to understand what went wrong.

One subtle design decision is how aggressively to report errors. If the scanner encounters `"hello` without a closing quote, it could consume the rest of the line (or the rest of the file) as part of the string before reporting the error. The choice of how far to scan before giving up affects both the quality of the error message and whether subsequent tokens are scanned correctly. A common heuristic is to terminate unterminated strings at the end of the line, since multi-line strings are rare in most languages. These design choices are language-specific and often require iterating on real-world code to get right — the scanner generator gives you the mechanism, but error handling requires judgment about what programmers actually need to hear.
