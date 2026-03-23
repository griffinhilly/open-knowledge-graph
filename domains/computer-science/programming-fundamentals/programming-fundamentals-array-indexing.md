---
id: programming-fundamentals-array-indexing
title: Array Indexing and Bounds
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-arrays-and-lists
  type: hard
builds-toward:
- programming-fundamentals-iteration-collections
tags:
- arrays
- indexing
- bounds
stage: formal-systems
status: draft
---

# Array Indexing and Bounds

## Core Idea
Indexing accesses array elements by position using bracket notation (e.g., arr[0]). Valid indices range from 0 to length-1. Accessing an out-of-bounds index causes an error.

## Questions

```yaml
- question: "A programmer writes a loop that runs while i <= arr.length and accesses arr[i] on each iteration. The array has 5 elements. What error will occur?"
  type: multiple-choice
  options:
    - "A syntax error because the comparison operator is wrong for array iteration"
    - "An out-of-bounds error because when i equals arr.length (5), arr[5] doesn't exist — the last valid index is 4"
    - "No error; arr.length is always a valid index in this context"
    - "A logic error because the loop runs one too few times"
  answer: 1
  explanation: "Zero-based indexing means a 5-element array has valid indices 0, 1, 2, 3, 4. When i reaches 5 (which equals arr.length), arr[5] is accessed — but no element exists there, causing an out-of-bounds error. The correct condition is i < arr.length (strictly less than), so i runs from 0 to 4. The off-by-one error of using <= instead of < is one of the most common bugs in programming, and it almost always stems from forgetting that the last valid index is length − 1."

- question: "In a zero-based indexed array nums = [10, 20, 30, 40, 50], what does nums[nums.length - 1] return?"
  type: multiple-choice
  options:
    - "40 (the second-to-last element)"
    - "50 (the last element)"
    - "An out-of-bounds error"
    - "10 (the first element)"
  answer: 1
  explanation: "nums.length is 5. nums.length - 1 is 4. nums[4] is 50 — the last element. This is the standard idiom for accessing the last element of an array without knowing its length in advance. Using nums[nums.length] would cause an out-of-bounds error because index 5 doesn't exist. The pattern length - 1 appears constantly in array iteration and is the direct consequence of zero-based indexing."

- question: "In a zero-based indexed array of length 8, the valid indices are 0 through 7."
  type: true-false
  answer: true
  explanation: "Zero-based indexing means the first element is at index 0 and the last is at index length − 1 = 8 − 1 = 7. Valid indices are 0, 1, 2, 3, 4, 5, 6, 7 — eight values total, matching the eight elements. Accessing index 8 would be out-of-bounds. Counting the valid indices by subtracting (7 − 0 + 1 = 8) confirms this matches the array length."

- question: "In most programming languages, array indices start at 1, so an array of 5 elements has valid indices 1 through 5."
  type: true-false
  answer: false
  explanation: "Most major programming languages (Python, JavaScript, Java, C, C++, Go, Rust) use zero-based indexing: indices start at 0, so a 5-element array has valid indices 0 through 4. A few languages (MATLAB, Lua, Fortran) use 1-based indexing, but they are exceptions. The off-by-one errors that result from assuming 1-based indexing in a 0-based language are extremely common bugs, which is why this distinction is fundamental to learn early."

- question: "Explain why the last valid index of an array is length − 1 rather than length. Use a concrete example."
  type: short-answer
  answer: "Because indexing starts at 0, not 1. An array of 3 elements has elements at positions 0, 1, and 2 — three positions, but the highest is 2 = 3 − 1. If you think of the index as 'how many steps from the start,' the first element is 0 steps from the start, the second is 1 step, and the third is 2 steps. The index at position 'length' (3 in this case) would be one step past the last element — there's nothing there, so accessing it causes an out-of-bounds error."
  explanation: "For example: arr = ['a', 'b', 'c']. arr[0] = 'a', arr[1] = 'b', arr[2] = 'c'. arr.length = 3. arr[3] is out-of-bounds. The last valid index is arr.length − 1 = 2. Keeping this relationship (last valid index = length − 1) in mind is the key to writing correct array iteration and avoiding the most common type of runtime error."
```

## Explainer

Now that you understand arrays as ordered collections of elements, the next question is: how do you get at a specific element? The answer is **indexing** — using a number inside bracket notation to specify which position you want. If you have an array `fruits = ["apple", "banana", "cherry"]`, then `fruits[0]` gives you `"apple"`, `fruits[1]` gives you `"banana"`, and `fruits[2]` gives you `"cherry"`. The number inside the brackets is called the **index**.

The critical detail that trips up nearly every beginner is that indexing starts at zero, not one. The first element is at position 0, the second at position 1, and so on. This is called **zero-based indexing**, and it means the last element in an array of length `n` sits at index `n - 1`. Think of the index as an offset from the beginning: the first element is zero steps from the start, the second is one step from the start. Once this clicks, zero-based indexing feels natural.

What happens when you use an index that doesn't exist? If your array has three elements (indices 0, 1, 2) and you try to access `fruits[3]` or `fruits[-1]` (in languages without negative indexing), the program raises an **out-of-bounds error**. The array simply has no element at that position, so there is nothing to return. This is one of the most common runtime errors in programming, and it almost always means your index math is off by one — often because you forgot that the last valid index is `length - 1`, not `length`.

Understanding indexing also unlocks a powerful pattern: you can use a variable as the index. Instead of writing `fruits[0]`, you can write `fruits[i]` where `i` is a variable that changes. This is the foundation of iterating through arrays — stepping through each element by incrementing the index from 0 up to `length - 1`. Getting comfortable with index arithmetic now will make loops over collections feel straightforward when you encounter them next.
