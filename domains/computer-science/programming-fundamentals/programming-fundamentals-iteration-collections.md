---
id: programming-fundamentals-iteration-collections
title: Iterating Over Collections
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-for-loops
  type: hard
- id: programming-fundamentals-array-indexing
  type: hard
tags:
- loops
- collections
- iteration
stage: formal-systems
status: draft
---

# Iterating Over Collections

## Core Idea
Iterating over a collection accesses each element in sequence. Index-based loops use a counter to access elements by index; for-each loops iterate directly over elements. Many languages offer both approaches.

## Questions

```yaml
- question: "You have a list of names and want to print each one. Which loop style is most appropriate?"
  type: multiple-choice
  options:
    - "An index-based loop, so you can track your position in the list"
    - "A for-each loop, since you only need each element's value and don't need the index"
    - "A while loop, because for-each loops only work with numbers"
    - "Either works identically — there is no meaningful difference between them"
  answer: 1
  explanation: "When you only need each element's value (not its position), a for-each loop is simpler and less error-prone. It expresses intent clearly: 'for every name in names, do this.' An index-based loop works but introduces extra variables and the risk of off-by-one errors for no benefit. The choice between loop styles should be driven by what information you actually need."

- question: "You need to compare each element in an array with the element immediately after it (e.g., to detect two identical consecutive values). Which approach is required?"
  type: multiple-choice
  options:
    - "A for-each loop, because it automatically provides access to neighboring elements"
    - "An index-based loop, because you need to access both items[i] and items[i+1] by their indices"
    - "Both approaches work equally well for accessing adjacent elements"
    - "Neither — arrays must be sorted before adjacent elements can be compared"
  answer: 1
  explanation: "Accessing adjacent elements (items[i] and items[i+1]) requires knowing the index. A for-each loop gives you the element's value but not its position, so you cannot reach the next element without additional machinery. This is the defining use case for index-based iteration: any time you need to compare, swap, or reference elements relative to each other, you need the index directly."

- question: "A for-each loop is just syntactic shorthand for an index-based loop and provides no practical advantage in any situation."
  type: true-false
  answer: false
  explanation: "For-each loops generalize to collection types that don't support indexing at all — dictionaries, sets, linked lists, and many others can be iterated with for-each but have no meaningful index. They also eliminate the off-by-one errors that are a constant hazard with index-based loops (starting at 1 instead of 0, using <= instead of <). And they make code more readable by expressing intent directly: 'do this for each element' rather than 'start at 0, loop while less than length, access by index.'"

- question: "If you need to modify elements in an array in place during iteration (e.g., doubling every value), an index-based loop is more appropriate than a for-each loop."
  type: true-false
  answer: true
  explanation: "In most languages, for-each iteration gives you a copy of each element's value. Modifying that copy does not change the original array. An index-based loop lets you write items[i] = items[i] * 2 directly to the array's actual storage location. Python's enumerate() provides a partial workaround (giving you both index and value), but the fundamental point stands: when you need to write back to the collection, you need the index."

- question: "Why is for-each iteration preferred in most production code, even though index-based loops are more explicit about position?"
  type: short-answer
  answer: "For-each loops are preferred when you only need element values because they are less error-prone (no off-by-one mistakes), more readable (the code clearly says 'process each element'), and more general (they work with any iterable, not just indexed structures). Off-by-one errors — the classic bug of using <= instead of < or starting at 1 instead of 0 — are a persistent hazard with index-based loops and entirely absent from for-each. As code scales and collection types diversify beyond arrays, for-each iteration also becomes necessary for types that lack meaningful indices."
  explanation: "The guiding principle is to choose the simplest tool that meets the requirement. For-each satisfies 'process every element' with the minimum machinery. Index-based iteration is the right tool when position, adjacency, or in-place modification is actually needed — not as a default."
```

## Explainer

You already know two things that combine here: for loops let you repeat a block of code a controlled number of times, and array indexing lets you access any element by its position. Iterating over a collection is what happens when you bring these together — you use a loop to visit every element in an array (or list, or other collection) one at a time.

The most explicit approach is an **index-based loop**. You set a counter variable to 0, loop while it's less than the collection's length, and use the counter as an index: `for i in range(len(items)): print(items[i])`. This gives you full control — you know exactly which position you're at, you can skip elements, go backwards, or access neighboring elements. But it's also verbose, and off-by-one errors (starting at 1 instead of 0, or using `<=` instead of `<`) are a constant hazard.

Most modern languages offer a cleaner alternative: the **for-each loop** (called `for...in` in Python, `for...of` in JavaScript, or enhanced `for` in Java). Instead of managing an index yourself, you simply say `for item in items: print(item)`. The language handles the indexing internally. The variable `item` takes on each element's value in sequence. This is less error-prone and more readable when you just need to process every element. The tradeoff is that you don't automatically know the index — if you need it, you either switch back to index-based iteration or use a construct like Python's `enumerate()`.

Choosing between these two styles is a judgment call that depends on what you need. If you only need each element's value — to sum numbers, print names, or check a condition — a for-each loop is simpler and less error-prone. If you need the index itself — to modify elements in place, compare adjacent elements, or iterate over two collections in parallel — an index-based loop gives you that control. As you encounter more collection types beyond arrays (dictionaries, sets, linked lists), you'll find that for-each iteration generalizes to all of them, while index-based access does not. This is why for-each is the default idiom in most production code.
