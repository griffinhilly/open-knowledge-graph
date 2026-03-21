---
id: hash-function-design-universal
title: Hash Function Design and Universal Hashing
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: algorithm-design-basics
  type: hard
builds-toward:
- hash-table-collision-resolution-chaining
- hash-table-collision-resolution-open-addressing
tags:
- hash-function
- hashing
- universal
stage: formal-systems
status: draft
---

# Hash Function Design and Universal Hashing

## Core Idea
Good hash functions distribute keys uniformly to minimize collisions. Division hashing (h(k) = k mod m), multiplication hashing, and universal hashing families (randomized) are common. Bad hashing leads to clustering and O(n) performance.

## Questions

```yaml
- question: "A web server uses a fixed hash function h(k) = k mod 1009 (a prime) to route requests to backend slots. An attacker discovers which hash function is in use. What can the attacker do to degrade performance?"
  type: multiple-choice
  options:
    - "Nothing — choosing a prime modulus guarantees uniform distribution regardless of input"
    - "Craft requests whose keys all hash to the same slot, creating a collision chain and O(n) lookup time"
    - "Overflow the hash table by sending more keys than there are slots"
    - "Force the server to switch to a slower multiplication-based hash function"
  answer: 1
  explanation: "For any fixed hash function, an adversary who knows the function can construct a set of keys that all map to the same slot. For h(k) = k mod 1009, the adversary simply sends keys 0, 1009, 2018, 3027, … — all of which hash to 0. This turns the hash table's O(1) average case into O(n) per lookup. Choosing a prime modulus helps with random inputs but provides no protection against a targeted adversary. Universal hashing defeats this attack by randomly selecting the hash function at runtime, so the adversary cannot know which function is in use."

- question: "Why is choosing m as a prime number (not close to a power of 2) the standard recommendation for division hashing h(k) = k mod m?"
  type: multiple-choice
  options:
    - "Prime values of m guarantee zero collisions for any input set"
    - "When m is a power of 2, the hash depends only on the lowest-order bits of k, ignoring the rest and wasting information"
    - "Prime values of m are computationally cheaper to compute mod against"
    - "When m is even, the hash table can only store even-indexed keys"
  answer: 1
  explanation: "When m = 2^p, computing k mod m is equivalent to keeping only the lowest p bits of k. All higher-order bits are discarded, so keys that differ only in their upper bits will collide. A prime m forces all bits of k to participate in the modular arithmetic, producing more thorough mixing of the key's information into the hash value. This is why primes not close to powers of 2 are preferred — they avoid both the powers-of-2 problem and the near-power-of-2 problem."

- question: "Universal hashing guarantees that for any two distinct keys x and y, the probability that h(x) = h(y) is at most 1/m, where the probability is over the random choice of hash function."
  type: true-false
  answer: true
  explanation: "This is the defining property of a universal hash family: for any pair of distinct keys, no more than 1/m of the functions in the family cause them to collide. This bound is exactly what you would get if hash values were chosen uniformly at random. Crucially, the probability is over the random choice of function, not over the distribution of keys — so the guarantee holds for *any* input set, including adversarially chosen ones. The adversary cannot predict which function was selected and therefore cannot engineer collisions."

- question: "Using h(k) = k mod 1024 distributes integer keys uniformly across all slots for any input set."
  type: true-false
  answer: false
  explanation: "m = 1024 = 2^10 means h(k) = k mod 1024 keeps only the lowest 10 bits of k and ignores all higher bits. Keys that differ only in their upper bits will collide. For example, the keys 0, 1024, 2048, … all hash to slot 0. If the key set has any structure in its lower bits — common for sequentially allocated identifiers or byte-aligned data — severe clustering results. A prime m forces more thorough mixing of all bits of k into the hash value."

- question: "Why can't a single fixed hash function guarantee O(1) average-case performance for all possible input sets, and how does universal hashing address this limitation?"
  type: short-answer
  answer: "For any fixed hash function h, you can always construct a worst-case input: the set of all keys that map to the same slot. An adversary (or unlucky data) can trigger this, making every operation O(n). Universal hashing addresses this by randomly selecting h from a carefully designed family at runtime. No adversary can construct a bad input without knowing which function was chosen, and the guarantee that any two distinct keys collide with probability ≤ 1/m ensures that the expected number of collisions per slot is bounded regardless of the input."
  explanation: "The key insight is that universality is a property of the *family*, not any individual function. Each individual function in the family may have its own worst-case inputs, but by randomly selecting one, you make it statistically impossible for an adversary to reliably target those worst cases. This is a classic technique in algorithm design: replace a deterministic worst-case guarantee that is hard to achieve with a probabilistic guarantee that is easy to achieve."
```

## Explainer

A hash function's job is deceptively simple: map a key (which could be any data — an integer, a string, an object) to an index in a fixed-size array. The quality of this mapping determines whether your hash table runs in O(1) average time or degrades toward O(n). A good hash function distributes keys **uniformly** across the available slots, minimizing the chance that two different keys land in the same slot (a **collision**). A bad hash function clumps keys together, creating long collision chains that turn your hash table into an expensive linked list.

The simplest approach is **division hashing**: `h(k) = k mod m`, where m is the table size. If m is 10 and your key is 47, the hash is 7. This works, but the choice of m matters enormously. If m is even, all odd keys hash to odd slots and all even keys hash to even slots — you have already lost half your distribution. If m is a power of 2, the hash depends only on the lowest-order bits of k, ignoring the rest. The standard advice is to choose m as a prime number not close to a power of 2, which forces the modular arithmetic to mix more bits of the key into the result. **Multiplication hashing** (`h(k) = floor(m × (k × A mod 1))` for a carefully chosen constant A) avoids the sensitivity to m entirely and works well with power-of-2 table sizes, making it popular in practice.

The deeper problem is that for *any* fixed hash function, an adversary (or just bad luck) can construct a set of keys that all hash to the same slot, producing worst-case O(n) behavior. **Universal hashing** solves this with randomization. Instead of choosing one hash function, you define a *family* of hash functions and randomly select one at runtime. A universal hash family guarantees that for any two distinct keys, the probability of collision is at most 1/m — no worse than if the hash values were perfectly random. A classic construction for integer keys is `h(k) = ((a × k + b) mod p) mod m`, where p is a prime larger than any key and a, b are chosen randomly at initialization. The adversary cannot construct a bad input because they do not know which function was chosen.

The choice of hash function is the foundation on which all collision resolution strategies rest. Whether you use chaining (linked lists at each slot) or open addressing (probing for empty slots), the expected number of collisions — and therefore the expected time per operation — depends directly on how uniformly your hash function distributes keys. Investing in a well-designed hash function, or using a universal family, is always cheaper than dealing with the clustering and performance degradation that a poor function produces.
