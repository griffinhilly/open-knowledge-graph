---
id: three-phase-commit-protocol
title: Three-Phase Commit Protocol
domain: computer-science
course: distributed-systems
prerequisites:
- id: two-phase-commit-protocol
  type: hard
builds-toward:
- saga-pattern-distributed-transactions
tags:
- transactions
- commit
- protocol
- fault-tolerant
stage: advanced
status: draft
---

# Three-Phase Commit Protocol

## Core Idea
Three-phase commit (3PC) adds a pre-commit phase between prepare and commit: if all participants can commit, the coordinator tells them to pre-commit (releasing read locks but keeping write locks), then commit. If the coordinator fails after pre-commit, participants can safely commit themselves, avoiding indefinite blocking.

## Explainer

To understand three-phase commit, you need to recall the fundamental weakness of two-phase commit (2PC). In 2PC, once participants vote "yes" in the prepare phase, they are stuck waiting for the coordinator's commit or abort decision. If the coordinator crashes after collecting votes but before sending the decision, participants are **blocked** — they cannot safely commit (because the coordinator might have decided to abort) and they cannot safely abort (because the coordinator might have decided to commit and another participant already applied the change). Resources stay locked, and the system stalls until the coordinator recovers.

**Three-phase commit (3PC)** addresses this blocking problem by splitting the commit decision into two steps, creating three phases total: **canCommit**, **preCommit**, and **doCommit**. In the first phase, the coordinator asks each participant whether it *can* commit. If all say yes, the coordinator enters the second phase and sends a preCommit message, which tells participants "everyone agreed — prepare to commit, but don't finalize yet." Only after all participants acknowledge preCommit does the coordinator send the final doCommit in the third phase. The key insight is that preCommit creates a shared state: if a participant has received preCommit, it knows that *all* participants voted yes. This knowledge is what makes the protocol non-blocking.

Here is why the extra phase helps. If the coordinator crashes after sending preCommit, the surviving participants can elect a new coordinator. The new coordinator queries the participants and finds that everyone is in the preCommit state — meaning everyone voted yes — so it can safely issue doCommit. If the coordinator crashes *before* sending preCommit (during or after canCommit), no participant has committed to anything, so the new coordinator can safely abort. The blocking window from 2PC is eliminated because there is no longer a state where some participants might have committed while others have not heard the decision.

However, 3PC comes with significant caveats that explain why it is rarely used in practice. It assumes a **fail-stop** model — nodes either work correctly or crash cleanly. If the network can partition (messages are lost or delayed rather than nodes crashing), 3PC can still produce inconsistencies: participants on one side of a partition might time out and abort while those on the other side commit. Real-world distributed systems almost always face network partitions, which is why most production systems use 2PC with logging and recovery (or avoid distributed transactions entirely using patterns like sagas) rather than adopting 3PC. The protocol is important primarily as a theoretical demonstration that non-blocking atomic commitment is possible under the right failure model.
