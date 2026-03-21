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

## Questions

```yaml
- question: "In 2PC, all participants have voted 'yes' in the prepare phase and the coordinator then crashes before sending any commit or abort. A new coordinator takes over. What is the fundamental problem?"
  type: multiple-choice
  options:
    - "The new coordinator must restart the entire transaction because participant votes expire after a timeout"
    - "The new coordinator cannot determine whether to commit or abort safely — it doesn't know whether the original coordinator decided to commit or abort, and participants cannot distinguish these cases either"
    - "The participants will automatically abort after a timeout, safely rolling back the transaction"
    - "The new coordinator can safely commit because all participants already voted yes and no abort was sent"
  answer: 1
  explanation: "This is the blocking problem of 2PC. After voting yes, participants hold locks and wait. The new coordinator queries participants and finds them all in the 'prepared' state — but this is consistent with both a commit decision (coordinator crashed after deciding commit) and an abort decision (coordinator crashed before sending anything). The new coordinator cannot safely choose either. Option D is tempting but wrong: a participant could have received an abort before the crash, and committing would violate atomicity."

- question: "Why does 3PC's non-blocking guarantee break down when the network can partition, even though it solves the coordinator-crash scenario?"
  type: multiple-choice
  options:
    - "Network partitions prevent the preCommit acknowledgment from reaching the coordinator, stalling the protocol indefinitely"
    - "Participants on one side of a partition may time out waiting for the coordinator and abort, while participants on the other side receive preCommit and eventually commit — violating atomicity"
    - "The 3PC protocol uses UDP, which is unreliable, making partitions catastrophic in a way that TCP-based 2PC handles gracefully"
    - "Network partitions corrupt the flow table in the coordinator's switch, causing it to route preCommit messages incorrectly"
  answer: 1
  explanation: "3PC's non-blocking property depends on participants being able to communicate with each other to determine the global state. A network partition isolates groups of participants. Those who received preCommit know everyone voted yes and will eventually commit. Those who didn't receive preCommit (because the partition occurred before it arrived) will time out and abort. Both groups are acting rationally given the 3PC rules — but the outcome violates atomicity. This failure mode doesn't exist in 2PC's original blocking scenario because 2PC doesn't allow participants to act autonomously."

- question: "In 3PC, if a participant has received a preCommit message, it knows that all other participants voted 'yes' in the canCommit phase, which enables a new coordinator to safely issue doCommit."
  type: true-false
  answer: true
  explanation: "This is the key informational property that preCommit creates. The coordinator only sends preCommit after receiving unanimous yes votes. So a participant in the preCommit state has a guarantee: the commit decision is safe because no participant voted no. If the coordinator crashes now, the new coordinator queries participants, sees they're all in preCommit state, and can safely issue doCommit. This shared knowledge — absent in 2PC — is what breaks the blocking deadlock."

- question: "Three-phase commit was designed to improve transaction throughput over 2PC by reducing the total number of messages exchanged during the commit process."
  type: true-false
  answer: false
  explanation: "3PC actually adds a phase and increases message overhead compared to 2PC — it requires more round trips, not fewer. Its purpose is to eliminate the indefinite blocking problem, not to improve throughput. In practice, 3PC is rarely used in production systems because its added complexity and message overhead are not worth the benefit when network partitions (which 3PC cannot handle anyway) are the more realistic failure mode. Systems instead use 2PC with careful logging, or avoid distributed transactions entirely."

- question: "What specific knowledge does the preCommit phase give participants that allows 3PC to avoid the indefinite blocking problem of 2PC, and what failure assumption must hold for this to work?"
  type: short-answer
  answer: "The preCommit phase gives every participant the knowledge that all other participants voted 'yes' — a fact no participant has in 2PC. In 2PC, a participant in the 'prepared' state cannot tell whether others also voted yes or whether some voted no. In 3PC, receiving preCommit is proof that the commit is globally safe. This allows any participant (or a new coordinator) to complete the commit autonomously without needing the original coordinator. The assumption that must hold is fail-stop: nodes either operate correctly or crash cleanly, and the network delivers messages reliably. If the network can partition, participants may diverge despite following the protocol correctly."
  explanation: "The blocking problem in 2PC arises from ambiguity — prepared participants cannot distinguish 'coordinator decided commit' from 'coordinator decided abort.' 3PC resolves this by creating an intermediate state (preCommit) that is only reachable if the commit is globally safe. Participants in preCommit can complete the transaction; participants not yet in preCommit can safely abort. The fail-stop assumption is critical: with partitions, this disambiguation breaks down."
```

## Explainer

To understand three-phase commit, you need to recall the fundamental weakness of two-phase commit (2PC). In 2PC, once participants vote "yes" in the prepare phase, they are stuck waiting for the coordinator's commit or abort decision. If the coordinator crashes after collecting votes but before sending the decision, participants are **blocked** — they cannot safely commit (because the coordinator might have decided to abort) and they cannot safely abort (because the coordinator might have decided to commit and another participant already applied the change). Resources stay locked, and the system stalls until the coordinator recovers.

**Three-phase commit (3PC)** addresses this blocking problem by splitting the commit decision into two steps, creating three phases total: **canCommit**, **preCommit**, and **doCommit**. In the first phase, the coordinator asks each participant whether it *can* commit. If all say yes, the coordinator enters the second phase and sends a preCommit message, which tells participants "everyone agreed — prepare to commit, but don't finalize yet." Only after all participants acknowledge preCommit does the coordinator send the final doCommit in the third phase. The key insight is that preCommit creates a shared state: if a participant has received preCommit, it knows that *all* participants voted yes. This knowledge is what makes the protocol non-blocking.

Here is why the extra phase helps. If the coordinator crashes after sending preCommit, the surviving participants can elect a new coordinator. The new coordinator queries the participants and finds that everyone is in the preCommit state — meaning everyone voted yes — so it can safely issue doCommit. If the coordinator crashes *before* sending preCommit (during or after canCommit), no participant has committed to anything, so the new coordinator can safely abort. The blocking window from 2PC is eliminated because there is no longer a state where some participants might have committed while others have not heard the decision.

However, 3PC comes with significant caveats that explain why it is rarely used in practice. It assumes a **fail-stop** model — nodes either work correctly or crash cleanly. If the network can partition (messages are lost or delayed rather than nodes crashing), 3PC can still produce inconsistencies: participants on one side of a partition might time out and abort while those on the other side commit. Real-world distributed systems almost always face network partitions, which is why most production systems use 2PC with logging and recovery (or avoid distributed transactions entirely using patterns like sagas) rather than adopting 3PC. The protocol is important primarily as a theoretical demonstration that non-blocking atomic commitment is possible under the right failure model.
