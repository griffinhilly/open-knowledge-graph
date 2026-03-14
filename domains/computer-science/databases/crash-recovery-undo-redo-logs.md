---
id: crash-recovery-undo-redo-logs
title: 'Crash Recovery: Undo and Redo Logging'
domain: computer-science
course: databases
prerequisites:
- id: write-ahead-logging-protocol-durability
  type: hard
- id: transaction-properties-acid
  type: hard
builds-toward:
- checkpoint-fuzzy-recovery
tags:
- recovery
- undo
- redo
- ARIES
- crash
stage: formal-systems
status: draft
---

# Crash Recovery: Undo and Redo Logging

## Core Idea
Recovery algorithms use undo and redo logs to restore consistency after crashes. Undo logging records old values for backwards roll of uncommitted transactions; redo logging records new values for forwards replay of committed transactions. ARIES (Algorithm for Recovery and Isolation Exploiting Semantics) combines both: it redoes committed work, then undoes incomplete transactions. This approach minimizes recovery time and avoids re-executing long transactions.
