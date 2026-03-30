---
id: cache-oblivious-algorithms
title: Cache-Oblivious Algorithms
domain: computer-science
course: advanced-algorithms
prerequisites:
- id: external-memory-algorithms
  type: hard
- id: divide-and-conquer-strategy
  type: hard
- id: b-trees
  type: soft
tags:
- cache-oblivious
- memory-hierarchy
- van-emde-boas-layout
- funnel-sort
stage: expert
status: validated
---

# Cache-Oblivious Algorithms

## Core Idea
Cache-oblivious algorithms achieve optimal I/O complexity without knowing the memory parameters M (cache size) and B (block size). They work by being simultaneously efficient for all values of M and B, relying on an ideal cache replacement policy (like LRU) to manage block transfers. The van Emde Boas layout stores a static search tree in memory so that searching costs O(log_B N) I/Os — matching B-trees — without knowing B. Funnelsort achieves the optimal sorting bound O((N/B) * log_{M/B}(N/B)) without knowing M or B. The key design principle is recursive decomposition at all scales: problems are divided into subproblems that fit in cache at some level of the recursion, regardless of the actual cache size. This yields algorithms that are portable across memory hierarchies and simultaneously optimal at every cache level.

## Questions

```yaml
- question: "The van Emde Boas (vEB) layout stores a complete binary tree so that a root-to-leaf search touches O(log_B N) cache blocks, matching B-trees. How does it achieve this without knowing B?"
  type: multiple-choice
  options:
    - "It stores the tree in BFS order, which naturally groups nearby levels into blocks"
    - "It recursively splits the tree at height h/2: the top subtree of height h/2 and all bottom subtrees of height h/2 are each stored contiguously. At the recursion level where subtree size ≈ B, each subtree fits in one block, and a root-to-leaf path crosses O(log N / log B) = O(log_B N) such subtrees"
    - "It randomizes the tree layout so that on average each block contains useful nodes"
    - "It stores the tree in DFS order, which optimizes for sequential access"
  answer: 1
  explanation: "The vEB layout is recursive: split a tree of height h into a top tree of height h/2 and sqrt(N) bottom trees of height h/2. Store the top tree contiguously, followed by each bottom tree contiguously. At the recursion depth where subtree size equals B, each subtree fits in a single cache block. A root-to-leaf path traverses h = log N levels, grouped into subtrees of size ~B, crossing at most log(N)/log(B) = log_B(N) subtrees = cache blocks. This works for ANY B because the recursive structure adapts to all block sizes simultaneously."

- question: "Cache-oblivious algorithms assume an ideal (optimal offline) cache replacement policy. In practice, LRU provides a constant-factor simulation of the optimal policy."
  type: true-false
  answer: true
  explanation: "Sleator and Tarjan showed that LRU with cache size 2M has at most twice the cache misses of the optimal offline policy (Bélády's MIN) with cache size M. Since cache-oblivious analysis uses the optimal policy, an LRU cache of size 2M achieves the same asymptotic I/O bounds. This constant-factor slack in cache size is why cache-oblivious algorithms work in practice with standard hardware caches that use LRU or LRU-approximation replacement policies. The assumption of an ideal replacement policy is not a weakness — it is validated by this simulation result."

- question: "Explain why standard (RAM-model) mergesort is NOT cache-oblivious optimal, and how funnelsort achieves cache-oblivious optimality."
  type: short-answer
  answer: "Standard 2-way mergesort performs O(N/B * log_2(N/B)) I/Os because it merges only 2 runs at a time, regardless of how much memory is available. Cache-oblivious optimal is O(N/B * log_{M/B}(N/B)), requiring M/B-way merging — but a cache-oblivious algorithm cannot know M. Funnelsort solves this with a recursive 'funnel' data structure: a k-funnel merges k sorted streams using a binary tree of mergers, where each merger recursively uses sub-funnels. The recursive structure ensures that when a sub-funnel fits in cache (size ~M), it merges ~sqrt(M/B) streams without cache misses. This implicitly achieves the optimal merge degree at each cache level without knowing M or B. Funnelsort's I/O complexity matches the external memory sorting bound for all M and B simultaneously."
  explanation: "The key insight is that recursive decomposition at all scales creates a structure that automatically adapts to the cache size. At the level where a sub-funnel fits in cache, it achieves the bandwidth of an M/B-way merge. This 'automatic parameter adaptation' is the hallmark of cache-oblivious algorithm design."

- question: "A cache-oblivious algorithm that is optimal for a two-level memory hierarchy (cache + main memory) is automatically optimal for all levels of a multi-level hierarchy."
  type: true-false
  answer: true
  explanation: "This is one of the most elegant properties of cache-oblivious algorithms. Since the analysis holds for ALL M and B simultaneously, it applies to every adjacent pair of levels in a multi-level hierarchy (L1-L2, L2-L3, L3-RAM, RAM-disk). An algorithm that achieves the optimal I/O bound at each level pair is automatically optimal for the entire hierarchy. Cache-aware (external memory) algorithms, by contrast, are tuned for specific M and B values and may be suboptimal at other hierarchy levels. This multi-level optimality is the primary practical advantage of the cache-oblivious approach."
```

## Explainer

External memory algorithms optimize for one level of the memory hierarchy by explicitly managing block transfers between cache and disk. But modern systems have 4-5 levels (L1, L2, L3 caches, RAM, disk), each with different M and B parameters. Tuning an algorithm for one level may make it suboptimal for others. Cache-oblivious algorithms sidestep this entirely: they achieve optimal I/O complexity at every level simultaneously, without knowing any of the parameters.

The van Emde Boas tree layout is the clearest illustration of the design principle. A complete binary search tree stored in the standard array layout (BFS or DFS order) incurs O(log_2 N) cache misses per search — because consecutive tree levels are far apart in memory. The vEB layout recursively splits the tree at the midpoint of its height: the top half-tree is stored contiguously, followed by each bottom half-tree contiguously, applied recursively. At whatever recursion depth the subtree size matches the block size B, each subtree fits in one block. A root-to-leaf path crosses O(log N / log B) = O(log_B N) such block-sized subtrees, matching the B-tree's I/O complexity — without the algorithm or data structure knowing B.

Funnelsort extends this principle to sorting. The challenge is that optimal external memory sorting requires M/B-way merging, but a cache-oblivious algorithm cannot know M. Funnelsort introduces a recursive "funnel" data structure: a k-funnel merges k^3 elements from k sorted inputs using a binary tree of sub-funnels. The recursion ensures that at some level, sub-funnels fit entirely in cache and operate without misses, implicitly achieving the optimal merge degree. The result: O((N/B) * log_{M/B}(N/B)) I/Os for all M and B, matching the external memory sorting lower bound universally.

The theoretical foundation rests on the ideal cache model: the analysis assumes an optimal replacement policy (evict the block used farthest in the future), but Sleator-Tarjan's result shows that LRU with 2M memory simulates optimal-M within a constant factor. This makes cache-oblivious results practically relevant — real hardware uses LRU-like policies. The design methodology — recursive decomposition at all scales, so that subproblems fit in cache at some recursion depth regardless of cache size — has been applied to matrix multiplication, FFT, graph algorithms, and priority queues, establishing cache-oblivious design as a general and powerful paradigm.
