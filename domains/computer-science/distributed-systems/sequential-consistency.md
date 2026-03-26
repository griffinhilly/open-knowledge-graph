---
id: sequential-consistency
title: Sequential Consistency
domain: computer-science
course: distributed-systems
prerequisites:
- id: consistency-models
  type: hard
- id: read-after-write-consistency
  type: soft
- id: total-order-broadcast
  type: soft
builds-toward:
- read-after-write-consistency
- strong-eventual-consistency
tags:
- consistency
- ordering
- formal-semantics
stage: advanced
status: validated
---
# Sequential Consistency

## Core Idea
Sequential consistency guarantees that there exists a total order on all operations that respects the program order of each individual process. Unlike linearizability, this total order does not have to correspond to real time—operations can appear to execute in any order as long as each process's sequence is preserved. This weaker model can be more efficient to implement.

## Questions

```yaml
- question: "Process A writes X=1 at time 3:00 PM. Process B begins reading X at 3:01 PM (after A's write completed) and reads X=0 (the initial value). Is this execution sequentially consistent?"
  type: multiple-choice
  options:
    - "Yes — a total order exists where B's read is placed before A's write, and neither process's program order is violated"
    - "No — B started after A finished, so B must see A's write under any reasonable consistency model"
    - "No — sequential consistency requires all reads to return the most recently written value globally"
    - "Yes — but only if A and B are on the same machine sharing memory"
  answer: 0
  explanation: "Sequential consistency does not respect real-time ordering between processes. It only requires that some valid total order of all operations exists such that each process's own operations appear in the same order they were issued. Here, a total order of [B reads X=0, A writes X=1] is valid: it preserves B's program order (trivially, one operation) and A's program order (trivially, one operation), and B reads X=0 which is consistent with X=0 being the value when B's read appears in the total order. Linearizability would reject this because A's write completed before B's read began in real time."

- question: "How does sequential consistency differ from linearizability?"
  type: multiple-choice
  options:
    - "Sequential consistency is stronger — it requires all processes to agree on a single global ordering of all operations"
    - "Linearizability additionally requires the total order to respect real-time (wall-clock) ordering: if one operation completes before another begins, it must appear first"
    - "Sequential consistency requires operations to be atomic; linearizability allows operations to take time"
    - "Linearizability is weaker — it does not require each individual process's operations to appear in program order"
  answer: 1
  explanation: "Sequential consistency only requires a total order that is consistent with each process's program order — the order operations appeared from each process's perspective. Linearizability adds a stricter constraint: the total order must also be consistent with real-time. If operation A completed before operation B began (in wall-clock time), then A must appear before B in the total order. This additional constraint makes linearizability stronger and more expensive to implement but provides the intuitive guarantee that completed operations are visible to later operations."

- question: "Under sequential consistency, if process A's write completes before process B's read begins (measured in real time), process B is expected to see the value written by A."
  type: true-false
  answer: false
  explanation: "This guarantee is provided by linearizability, not sequential consistency. Sequential consistency only requires that a valid total ordering of all operations exists — one that preserves each process's program order. That total order can place B's read before A's write even if A's write completed first in real time. This is precisely the relaxation that makes sequential consistency weaker than linearizability and easier to implement: distributed systems can buffer, batch, and reorder operations across nodes without violating sequential consistency, as long as each individual node's operations stay in order."

- question: "Sequential consistency guarantees that operations from a single process always appear in the global total ordering in the same sequence they were issued by that process."
  type: true-false
  answer: true
  explanation: "This is the defining constraint of sequential consistency: per-process program order is preserved in the global total order. You cannot construct a sequentially consistent execution where a process's second operation appears before its first. What sequential consistency does NOT preserve is the relative ordering of operations from different processes — the system is free to interleave their operations in any order, as long as each process's own subsequence stays intact. This is both the key guarantee and the key limitation."

- question: "Explain why sequential consistency is weaker than linearizability, and why this relaxation makes it easier to implement efficiently in distributed systems."
  type: short-answer
  answer: "Linearizability requires the total order of operations to respect real-time: if one operation's effect is visible (it 'completed') before another begins, the first must appear earlier in the total order. Sequential consistency drops this requirement — the total order only needs to preserve each process's own program order, with no constraints on cross-process real-time ordering. In a distributed system, enforcing real-time ordering requires tight coordination: nodes must communicate to agree on whether one operation 'completed' before another 'began,' typically requiring synchronization protocols with communication overhead proportional to latency. Sequential consistency allows nodes to operate independently, batching and reordering across nodes freely, as long as they report a consistent program-order-preserving sequence to each client — achievable with cheaper coordination mechanisms like causal ordering or vector clocks."
  explanation: "The real-time constraint in linearizability is what makes it expensive: to guarantee that a completed write is visible to subsequent reads from any process, the system must synchronize across all replicas before acknowledging the write. Sequential consistency allows writes to propagate asynchronously as long as the ordering seen by each individual client is consistent with program order. For many applications (feeds, timelines, document viewing) this weaker guarantee is sufficient and comes at significantly lower latency cost."
```

## Explainer

From your study of consistency models, you know that distributed systems offer different guarantees about the order in which operations appear to execute. **Sequential consistency**, defined by Leslie Lamport in 1979, occupies an important middle ground: stronger than eventual consistency, weaker than linearizability, and often the best tradeoff between correctness and performance.

The guarantee is best understood through an analogy. Imagine three people — Alice, Bob, and Carol — each writing statements on separate notepads, then handing all three notepads to a judge. The judge must shuffle the statements into a single sequence (a **total order**) that could explain every observation, with one constraint: the statements from each person's notepad must appear in the same relative order they were written. The judge is free to interleave statements from different people however she likes — she just cannot reorder any individual person's statements. If such an interleaving exists and is consistent with what everyone observed, the execution is sequentially consistent.

What sequential consistency does *not* guarantee is real-time ordering. If Alice finishes writing a value at 3:00 PM and Bob starts reading at 3:01 PM, sequential consistency does not promise Bob sees Alice's write — the total order might place Bob's read before Alice's write, as long as no single process's operations are reordered. This is the key difference from linearizability, which would require Bob to see the write because Alice's operation completed before Bob's began in wall-clock time. The practical consequence is that sequentially consistent systems can batch, buffer, and reorder operations across nodes for better performance, as long as each node's own operations stay in order.

Sequential consistency appears naturally in hardware memory models. Many multiprocessor architectures guarantee something close to sequential consistency for shared memory access (though modern CPUs often relax even this for performance, requiring memory barriers). In distributed databases, sequential consistency means clients always see a progression of states — they never see writes appear and then disappear — but two clients might disagree about the order of concurrent writes from different sources. For applications like social media feeds or collaborative documents where strict real-time ordering is less critical than a coherent narrative, sequential consistency often provides enough correctness at significantly lower latency and higher availability than linearizability.
