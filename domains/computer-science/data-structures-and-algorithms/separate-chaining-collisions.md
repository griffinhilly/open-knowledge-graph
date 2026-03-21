---
id: separate-chaining-collisions
title: Separate Chaining for Hash Table Collisions
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: hash-function-design
  type: hard
- id: hash-tables
  type: hard
- id: linked-lists
  type: soft
tags:
- hash-tables
- chaining
- collision-resolution
- linked-lists
stage: formal-systems
status: draft
---

# Separate Chaining for Hash Table Collisions

## Core Idea
Separate chaining resolves collisions by storing colliding keys in a linked list (or other structure) at each table bucket. With n keys in m buckets, expected chain length is n/m, yielding O(1 + n/m) average lookup. Chaining simplifies deletion compared to open addressing and handles high load factors gracefully.

## How It's Best Learned
Implement a chained hash table and trace insertions with collisions. Measure average chain length and lookup time as load factor increases. Compare to open addressing: chaining is simpler and more flexible, but uses extra memory for pointers.

## Common Misconceptions
- Chaining always suffers from many collisions (performance degrades gracefully with good hash functions). - Chains must be balanced (simple chaining works; advanced structures like self-balancing trees are overkill for most uses).

## Questions

```yaml
- question: "A hash table uses separate chaining with m = 100 buckets and currently holds n = 300 keys. A lookup is performed for a key that exists in the table. What is the expected number of comparisons needed to find it?"
  type: multiple-choice
  options:
    - "O(1), because hash tables always provide constant-time lookup"
    - "O(n) = O(300), because all keys might be in one chain"
    - "O(1 + n/m) = O(1 + 3) = O(4), reflecting the hash step plus average chain traversal"
    - "O(log n), because chains self-balance over time"
  answer: 2
  explanation: "With a load factor α = n/m = 300/100 = 3, the expected chain length is 3. Lookup requires O(1) to compute the hash and jump to the correct bucket, then O(α) = O(3) to traverse the chain — giving O(1 + α) total. Option A confuses 'expected O(1)' with O(1) in all cases: constant-time average performance only holds when α is bounded by a constant. Option D is wrong; separate chaining uses simple linked lists, not self-balancing structures (unless Java's HashMap threshold is crossed, and even then it's a refinement, not the default)."

- question: "Why is deletion simpler in a separate chaining hash table than in an open-addressing hash table?"
  type: multiple-choice
  options:
    - "Separate chaining never needs to resize, so there are no rehashing complications"
    - "In chaining, you simply remove the node from the linked list; in open addressing, deleting a key can break the probe sequence that subsequent lookups depend on"
    - "Open addressing uses more memory, making deletion slower"
    - "Separate chaining stores keys in sorted order, making deletion O(log n) rather than O(n)"
  answer: 1
  explanation: "In open addressing, keys are stored directly in the array, and lookup works by following a probe sequence until the key is found or an empty slot is reached. If you simply delete a key by marking its slot empty, subsequent lookups for keys that were inserted after this key (and that passed through this slot during probing) will incorrectly stop at the now-empty slot and miss their target. The standard fix — tombstone markers or full rehashing — adds complexity. In separate chaining, each chain is an independent linked list; deleting a node has no effect on any other bucket or chain."

- question: "A chained hash table can have a load factor greater than 1.0 and still function correctly — it just has longer average chains."
  type: true-false
  answer: true
  explanation: "Load factor α = n/m is the ratio of keys to buckets, and there is no structural requirement that α ≤ 1 in separate chaining. Each bucket holds an unbounded linked list, so inserting more keys than there are buckets simply lengthens some chains. Performance degrades gracefully: average lookup time grows as O(1 + α), which is linear in α. This is one of the practical advantages of chaining over open addressing, which breaks entirely when the array is full (and degrades badly as it approaches capacity)."

- question: "Separate chaining has better cache performance than open addressing because linked list nodes are stored close together in memory."
  type: true-false
  answer: false
  explanation: "This is the opposite of the truth. Open addressing stores all keys in a contiguous array, so a probe sequence accesses nearby memory locations — which the CPU cache handles efficiently. Separate chaining allocates linked list nodes dynamically, and those nodes can be scattered anywhere in the heap. Following a pointer to the next node in a chain likely causes a cache miss. This is a genuine practical disadvantage of chaining compared to open addressing: better theoretical simplicity for deletion comes at the cost of worse cache locality."

- question: "Why does the load factor α = n/m represent the expected chain length in a separate chaining hash table, and what does this imply about how to maintain O(1) average performance?"
  type: short-answer
  answer: "With n keys distributed uniformly across m buckets, by linearity of expectation each bucket receives on average n/m keys — which is exactly α. If the hash function distributes keys uniformly at random, the expected number of keys in any particular bucket is α. Since lookup traverses the chain at the target bucket, expected lookup time is O(1 + α): O(1) for hashing to the bucket plus O(α) for chain traversal. To maintain O(1) average performance, α must be bounded by a constant — which requires resizing (rehashing) the table when n grows too large relative to m, typically when α exceeds a fixed threshold like 1 or 2."
  explanation: "The key insight is that 'expected O(1)' is conditional on α being treated as a constant. If you allow α to grow without bound, lookup degrades to O(α) = O(n/m), which is O(n) in the worst case when m is fixed. Dynamic resizing — doubling m and rehashing all keys when α exceeds the threshold — ensures α stays bounded and performance stays O(1) amortized."
```

## Explainer

You know from studying hash tables that a hash function maps keys to array indices, and from linked lists that nodes can be chained together via pointers. **Separate chaining** combines these two ideas to handle the inevitable problem of collisions — when two different keys hash to the same index. Instead of each array slot holding a single key-value pair, each slot holds the head of a linked list. When a new key hashes to an already-occupied slot, it simply gets appended (or prepended) to that slot's list. To look up a key, you hash it to find the correct slot, then walk the linked list comparing keys until you find a match or reach the end.

The performance of separate chaining depends on how evenly the hash function distributes keys across buckets. The **load factor** α = n/m (number of keys divided by number of buckets) represents the average chain length. With a good hash function that distributes keys uniformly, most chains stay close to this average, so lookups take O(1 + α) time — the O(1) to compute the hash and jump to the bucket, plus O(α) to scan the chain. As long as you keep α reasonable (say, below 1 or 2) by resizing the table when it gets too full, average-case operations remain effectively O(1). This is the fundamental bargain of hashing: you trade a small amount of extra space for constant-time access.

Compared to **open addressing** (the other major collision strategy, where colliding keys probe for the next empty slot), separate chaining has several practical advantages. Deletion is straightforward — just remove the node from the linked list — whereas open addressing requires tombstone markers or complex rehashing after deletions. Chaining also tolerates load factors above 1.0 gracefully: performance degrades linearly as chains grow, rather than catastrophically as open-addressed tables approach full capacity. On the other hand, chaining uses extra memory for the linked list pointers and has worse cache locality than open addressing, since following pointers can jump around in memory rather than scanning contiguous array slots.

In practice, many real-world hash table implementations use separate chaining as their default strategy. Java's `HashMap`, for instance, uses chaining and even upgrades long chains from linked lists to balanced trees (red-black trees) when a single chain exceeds a threshold — a refinement that prevents worst-case O(n) lookups if a bad hash function or adversarial input concentrates many keys in one bucket. For most applications, though, a well-chosen hash function keeps chains short enough that a simple linked list per bucket is all you need. The key insight is that separate chaining turns the collision problem into a manageable linked-list traversal problem, and the expected length of that traversal is controlled entirely by the load factor and the quality of your hash function.
