---
id: immutability-and-mutation
title: Immutability and Mutation
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: array-indexing
  type: hard
builds-toward:
- intro-to-classes
tags:
- mutation
- immutability
- data
stage: formal-systems
status: validated
---
# Immutability and Mutation

## Core Idea
Immutable data cannot be changed after creation; mutable data can. Strings are immutable in many languages (operations return new strings). Arrays are mutable (operations modify them in place). Understanding mutability prevents unexpected side effects.

## How It's Best Learned
Attempt to modify immutable objects and observe errors; modify mutable collections and trace changes; compare performance of creating new objects vs modifying in place.

## Common Misconceptions
That all data is mutable (strings are often immutable); that immutable data is inefficient (it can enable optimizations); that immutability means the variable can't change (the variable can reference a new object).

## Questions

```yaml
- question: "In Python, the following code runs: name = 'Alice'; greeting = name; name = name.upper(). What is the value of greeting after these three lines?"
  type: multiple-choice
  options:
    - "'ALICE' — greeting follows name because they reference the same object"
    - "'Alice' — strings are immutable, so name.upper() created a new string and name was reassigned to it; greeting still points to the original"
    - "None — the original string was garbage collected when name was reassigned"
    - "'alice' — upper() modifies the string in place and greeting reflects the change"
  answer: 1
  explanation: "Strings are immutable in Python. name.upper() does not alter 'Alice' — it creates a new string 'ALICE' and name is reassigned to point to this new object. greeting was set to point to the original 'Alice' string, and since that string object was never modified (it can't be), greeting still sees 'Alice'. This demonstrates the critical distinction: variable reassignment changes what a variable points to, but the original string object remains unchanged and accessible through any other variable that still references it."

- question: "Two functions both hold a reference to the same list scores = [85, 90, 72]. Function A passes scores to function B. Function B sorts the list in place using scores.sort(). After B returns, what does function A's reference to scores contain?"
  type: multiple-choice
  options:
    - "[85, 90, 72] — function B received a copy of the list, so the original is unchanged"
    - "[72, 85, 90] — both references point to the same mutable object, so the sort is visible everywhere"
    - "An error — you cannot sort a list that was passed as a parameter"
    - "[85, 90, 72] — sort() on a function parameter creates a local sorted copy"
  answer: 1
  explanation: "Lists are mutable, and Python passes object references, not copies. When function B receives scores, it receives a reference to the *same list object*. Calling scores.sort() modifies that object in place — the same object that function A's variable also points to. Function A's reference now sees [72, 85, 90]. This is the classic mutation side effect: code far from the original definition can alter shared data in ways the caller doesn't expect. The fix is to either pass a copy (sorted(scores) returns a new list) or use immutable data structures."

- question: "When a programming language says strings are immutable, it means you can seldom reassign a variable that holds a string to a different string."
  type: true-false
  answer: false
  explanation: "Immutability applies to the *object*, not the *variable*. A variable is just a name that refers to an object; reassigning the variable (name = 'Bob') simply makes it point to a different object — neither the old string nor the variable binding is 'locked.' What immutability prevents is modifying the contents of the string object itself: there is no operation like name[0] = 'b' that changes a character inside an existing string (in Python this raises a TypeError). The distinction between the container (variable) and the contents (object) is fundamental."

- question: "If a mutable list is passed to a function and that function modifies it in place, the caller's variable reflects the change without the function needing to return anything."
  type: true-false
  answer: true
  explanation: "This is a direct consequence of mutation with shared references. The caller's variable and the function's parameter both point to the same underlying list object. Any in-place modification (append, sort, item assignment) is visible through both references. This behavior is intentional in many contexts (avoiding copies of large data), but it can surprise programmers who expect functions to be side-effect-free. Understanding this is why 'pass-by-object-reference' semantics matters for reasoning about program behavior."

- question: "What is the difference between reassigning a variable and mutating the object it points to? Why does this distinction matter for reasoning about program correctness?"
  type: short-answer
  answer: "Reassigning a variable changes which object the variable refers to — the original object is untouched and any other variables pointing to it still see the original value. Mutating an object changes the object itself — every variable that references that object now sees the new value. The distinction matters because mutation creates hidden dependencies: two parts of a program sharing a mutable object can interfere with each other, producing bugs that are hard to trace. Immutable objects eliminate this risk — since no one can change the data, a shared reference is always safe."
  explanation: "Many subtle bugs — accidental list modification through aliasing, unexpected behavior when objects are passed to functions — arise from confusing these two operations. Recognizing which operations create new objects (immutable behavior or explicit copies) versus which modify existing ones (mutation) is fundamental to reasoning about correctness and safety in programs."
```

## Explainer

Now that you understand how to access and modify elements in collections, it is time to examine a deeper question: should data be changeable at all? **Mutation** means altering data in place — changing an array element from 5 to 10, for example. The original value is gone, replaced by the new one. **Immutability** means data cannot be changed after creation. When you need a different value, you create a new piece of data rather than modifying the existing one.

The clearest example is strings in many popular languages. When you write `name = "Alice"` and then `name = name + " Smith"`, you might think you modified the original string. But you did not — the string `"Alice"` still exists unchanged somewhere in memory. The `+` operation created an entirely new string `"Alice Smith"` and the variable `name` now points to this new string. The old string becomes unreachable and will eventually be cleaned up. This is what it means for strings to be **immutable**: there is no operation that changes the characters inside an existing string object. Contrast this with arrays, which in most languages are **mutable**: `scores[2] = 95` genuinely overwrites the value at position 2 in the same array — no new array is created.

Why does this distinction matter? Because mutation introduces the possibility of **side effects**. If two parts of your program hold references to the same mutable array and one part modifies it, the other part sees the change — possibly without expecting it. Imagine passing your array of scores to a function that is supposed to compute an average. If that function also sorts the array as a side effect, your original data is now in a different order. With immutable data, this surprise is impossible: since no one can change the data, everyone who holds a reference sees the same values forever.

The subtlety that trips up many learners is the difference between a variable and the data it refers to. When we say a string is immutable, we mean the string *object* cannot change — but the *variable* holding a reference to it can be reassigned to point to a different string. You can write `name = "Bob"` after `name = "Alice"` — the variable changed, but neither string object was altered. Understanding this distinction between the container (the variable) and its contents (the data) is fundamental. It clarifies when you are making a new copy versus modifying in place, which directly affects both correctness and performance as your programs grow more complex.
