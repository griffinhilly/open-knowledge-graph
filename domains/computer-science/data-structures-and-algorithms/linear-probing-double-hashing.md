---
id: linear-probing-double-hashing
title: 'Open Addressing: Linear Probing and Double Hashing'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: hash-function-design
  type: hard
- id: hash-tables
  type: hard
tags:
- open-addressing
- hash-tables
- collision-resolution
- linear-probing
- double-hashing
stage: formal-systems
status: validated
---

# Open Addressing: Linear Probing and Double Hashing

## Core Idea
Open addressing resolves collisions by storing all keys in the table itself, probing for empty slots when collisions occur. Linear probing checks consecutive slots (h, h+1, h+2, ...), while double hashing uses a second hash function h(k, i) = (h1(k) + i*h2(k)) mod m to avoid clustering. Both achieve O(1) amortized lookup with load factor below 0.5–0.75.

## How It's Best Learned
Trace insertion and lookup with primary clustering visible in linear probing. Implement both methods and measure performance. Understand load factor and table resizing triggers. See how double hashing mitigates primary clustering better than linear probing.

## Common Misconceptions
- Open addressing is always faster than chaining (depends on load factor, cache locality, and implementation). - Linear probing is simpler and better than double hashing (double hashing avoids primary clustering).

## Questions

```yaml
- question: "A hash table uses linear probing. Initially, many keys hash to index 5, filling slots 5, 6, 7, 8, 9 into a long cluster. A new key hashes to index 3. How does inserting it affect the cluster?"
  type: multiple-choice
  options:
    - "It has no effect on the cluster — index 3 is separate from the cluster starting at 5"
    - "It extends the cluster leftward to index 3"
    - "It extends the cluster rightward, because probe scanning from 3 reaches and merges with the cluster"
    - "It is blocked from insertion until the cluster is resolved"
  answer: 2
  explanation: "This is primary clustering in action. The new key hashes to 3, finds slot 3 empty, and inserts there — but on a future lookup, a key hashing to 3, 4, 5, 6, 7, 8, or 9 may all end up probing into the same long run. More importantly, a key that hashes to 4 must probe past 4 and scan all the way through 5–9, extending the cluster further. Any key that hashes anywhere into or adjacent to an existing cluster makes it grow, which is why clusters grow superlinearly and performance degrades faster than the load factor alone predicts."

- question: "Why does double hashing avoid primary clustering while linear probing does not?"
  type: multiple-choice
  options:
    - "Double hashing uses a longer probe sequence, so collisions happen less often"
    - "Double hashing resizes the table more aggressively, keeping load factor lower"
    - "Double hashing makes the probe step size key-dependent, so different keys that collide initially follow diverging probe sequences"
    - "Double hashing stores keys in a separate overflow area, preventing cluster formation"
  answer: 2
  explanation: "In linear probing, every key that collides at slot h probes h+1, h+2, h+3, … — the exact same sequence. So all keys that land in an existing cluster pile into it. In double hashing, the step size is h2(k) — derived from the key itself — so two keys colliding at the same initial slot typically have different step sizes and immediately diverge to different probe sequences. There is still secondary clustering (different keys with the same h2 share a sequence), but primary clustering — long runs of consecutive occupied slots that grow by capturing nearby insertions — is eliminated."

- question: "An open-addressing table with linear probing performs best when the load factor is kept below 0.5."
  type: true-false
  answer: true
  explanation: "For linear probing, the expected number of probes for a successful lookup is approximately 1/(1 − α), where α is the load factor. As α approaches 1, this expression explodes — at α = 0.9, expected probes are around 10. In practice, linear-probing tables are resized (typically by doubling) when α exceeds 0.5 to keep performance near O(1). Double hashing tolerates slightly higher load (up to ~0.7) because its probes are more uniformly distributed, but both methods require load management that chaining-based tables do not."

- question: "Open addressing is generally faster than chaining-based hash tables because it avoids memory allocation."
  type: true-false
  answer: false
  explanation: "Open addressing has better cache locality (all keys are in a single array) and no pointer overhead, which does give it an advantage at low load factors. But at high load factors, long probe sequences more than offset this advantage. The claim 'always faster' ignores the critical role of load factor. Chaining degrades more gracefully under high load — at α = 1, chaining has expected O(1) lookup (one element per chain on average), while linear probing is already showing significant clustering. The right choice depends on expected load factor, memory constraints, and whether cache performance outweighs clustering risk."

- question: "Why must the second hash function h2(k) in double hashing never return zero, and why is it helpful for h2(k) to be coprime to the table size?"
  type: short-answer
  answer: "If h2(k) = 0, the probe sequence h1(k) + i*0 visits only the original slot repeatedly — the table search loops forever without finding an empty slot, causing an infinite loop. If h2(k) and the table size m share a common factor d > 1, the probe sequence only visits m/d distinct slots before cycling, meaning large portions of the table are never checked. Making h2(k) coprime to m guarantees the probe sequence visits every slot before repeating, ensuring any insertion can always find an empty slot as long as the table is not completely full."
  explanation: "These two constraints together ensure the probe sequence is a complete permutation of the table indices. The zero constraint prevents stalling; the coprimality constraint prevents partial cycles that leave table regions unreachable. A common implementation trick is to choose a prime table size m — then any h2(k) in the range 1 to m−1 is automatically coprime to m, satisfying both constraints."
```

## Explainer

You already know that a hash table maps keys to slots using a hash function, and that collisions are inevitable when two keys hash to the same index. Chaining solves this by hanging a linked list off each slot, but **open addressing** takes a fundamentally different approach: every key lives directly inside the table array. When a collision occurs, you probe — you check a sequence of alternative slots until you find an empty one. The entire question is how to choose that probe sequence.

**Linear probing** is the simplest strategy: if slot h is occupied, try h+1, then h+2, and so on (wrapping around at the end of the table). This has a beautiful advantage — because you are scanning consecutive memory locations, modern CPUs load these slots into cache lines together, giving you excellent cache performance. The downside is **primary clustering**: occupied slots clump together into long runs. Once a cluster forms, any new key that hashes anywhere into that cluster must scan to its end, and doing so extends the cluster further. The result is that as the table fills, clusters grow superlinearly and performance degrades much faster than you would expect from the load factor alone.

**Double hashing** eliminates primary clustering by making the probe step size itself depend on the key. Instead of always stepping by 1, you compute a second hash function h2(k) and probe at positions h1(k), h1(k) + h2(k), h1(k) + 2·h2(k), and so on. Because different keys that collide at the same initial slot will typically have different step sizes, their probe sequences diverge immediately rather than piling into the same cluster. The tradeoff is that you lose the cache-friendly sequential access pattern of linear probing, and you need a well-chosen h2 — it must never return zero, and ideally h2(k) should be coprime to the table size so the probe sequence visits every slot.

The load factor α (number of entries divided by table size) governs performance for both methods. For linear probing, the expected number of probes for a successful search is roughly 1/(1 − α), which explodes as α approaches 1. Double hashing performs better under high load because its probes are spread more uniformly, but both methods degrade as the table fills. In practice, open-addressing tables resize (typically doubling) when α exceeds a threshold — usually 0.5 for linear probing and 0.7 for double hashing. The key engineering insight is that open addressing trades the pointer overhead and allocation cost of chaining for simpler memory layout and better cache behavior, but demands careful load management to avoid the clustering pathologies that make probe sequences long.
