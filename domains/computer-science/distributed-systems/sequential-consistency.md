---
id: sequential-consistency
title: Sequential Consistency
domain: computer-science
course: distributed-systems
prerequisites:
- id: consistency-models
  type: hard
builds-toward:
- read-after-write-consistency
- strong-eventual-consistency
tags:
- consistency
- ordering
- formal-semantics
stage: advanced
status: draft
---

# Sequential Consistency

## Core Idea
Sequential consistency guarantees that there exists a total order on all operations that respects the program order of each individual process. Unlike linearizability, this total order does not have to correspond to real time—operations can appear to execute in any order as long as each process's sequence is preserved. This weaker model can be more efficient to implement.

## Explainer

From your study of consistency models, you know that distributed systems offer different guarantees about the order in which operations appear to execute. **Sequential consistency**, defined by Leslie Lamport in 1979, occupies an important middle ground: stronger than eventual consistency, weaker than linearizability, and often the best tradeoff between correctness and performance.

The guarantee is best understood through an analogy. Imagine three people — Alice, Bob, and Carol — each writing statements on separate notepads, then handing all three notepads to a judge. The judge must shuffle the statements into a single sequence (a **total order**) that could explain every observation, with one constraint: the statements from each person's notepad must appear in the same relative order they were written. The judge is free to interleave statements from different people however she likes — she just cannot reorder any individual person's statements. If such an interleaving exists and is consistent with what everyone observed, the execution is sequentially consistent.

What sequential consistency does *not* guarantee is real-time ordering. If Alice finishes writing a value at 3:00 PM and Bob starts reading at 3:01 PM, sequential consistency does not promise Bob sees Alice's write — the total order might place Bob's read before Alice's write, as long as no single process's operations are reordered. This is the key difference from linearizability, which would require Bob to see the write because Alice's operation completed before Bob's began in wall-clock time. The practical consequence is that sequentially consistent systems can batch, buffer, and reorder operations across nodes for better performance, as long as each node's own operations stay in order.

Sequential consistency appears naturally in hardware memory models. Many multiprocessor architectures guarantee something close to sequential consistency for shared memory access (though modern CPUs often relax even this for performance, requiring memory barriers). In distributed databases, sequential consistency means clients always see a progression of states — they never see writes appear and then disappear — but two clients might disagree about the order of concurrent writes from different sources. For applications like social media feeds or collaborative documents where strict real-time ordering is less critical than a coherent narrative, sequential consistency often provides enough correctness at significantly lower latency and higher availability than linearizability.
