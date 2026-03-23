---
id: carroll-diagrams
title: Carroll Diagrams
domain: formal-sciences-and-logic
course: patterns-and-logic
prerequisites:
- id: sorting-by-attributes-logic
  type: hard
- id: venn-diagrams-logic
  type: soft
builds-toward:
- classifying-multiple-attributes
tags:
- classification
- tables
- logic
- sorting
stage: concrete-operations
status: draft
---

# Carroll Diagrams

## Core Idea
A Carroll diagram (named after Lewis Carroll, author of Alice in Wonderland and a mathematician) is a grid that sorts objects by two yes/no attributes. One attribute defines the rows (e.g., "red" vs. "not red") and the other defines the columns (e.g., "circle" vs. "not circle"), creating four cells. Each object goes in exactly one cell based on whether it has or lacks each attribute. Carroll diagrams make the "not" concept explicit: instead of just grouping things that share an attribute, you also classify things that lack it. This is a concrete introduction to negation and binary classification.

## How It's Best Learned
Draw a 2x2 grid on paper or the board. Label the rows with one attribute and its opposite (e.g., "Even" / "Not Even") and the columns with another attribute and its opposite (e.g., "Greater than 10" / "Not Greater than 10"). Give students a set of numbers to place in the correct cells. Compare with a Venn diagram of the same data to see that both show the same information differently. Include examples with physical objects: sort buttons by "has 2 holes vs. does not have 2 holes" and "is round vs. is not round."

## Common Misconceptions
- Confusing the Carroll diagram with a regular table or chart — a Carroll diagram specifically uses an attribute and its negation (yes/no for each property).
- Placing objects in the wrong cell by forgetting to check both attributes.
- Thinking the "not" categories are less important — in logic, knowing what something is NOT is just as informative as knowing what it IS.

## Questions

```yaml
- question: "In a Carroll diagram sorting numbers by 'Even / Not Even' and 'Less than 20 / Not Less than 20,' where does the number 15 go?"
  type: multiple-choice
  options:
    - "Even, Less than 20"
    - "Not Even, Less than 20"
    - "Even, Not Less than 20"
    - "Not Even, Not Less than 20"
  answer: 1
  explanation: "15 is odd (Not Even) and 15 < 20 (Less than 20), so it goes in the 'Not Even, Less than 20' cell. You must check both attributes independently — being not even and being less than 20 are separate properties that together determine the correct cell."

- question: "A Carroll diagram always has exactly how many cells?"
  type: multiple-choice
  options:
    - "Two cells — one for each attribute"
    - "Three cells — yes, no, and maybe"
    - "Four cells — each attribute has two options (yes/no), and 2 x 2 = 4"
    - "It depends on how many objects you are sorting"
  answer: 2
  explanation: "A standard Carroll diagram uses two yes/no attributes, creating a 2x2 grid with exactly four cells. Each cell represents one combination: yes-yes, yes-no, no-yes, no-no. The number of objects does not change the number of cells — cells can have many objects, one object, or be empty."

- question: "A Carroll diagram and a two-circle Venn diagram can display the same information."
  type: true-false
  answer: true
  explanation: "Both organize objects by two attributes. The four regions of a Venn diagram (left only, right only, overlap, outside) correspond to the four cells of a Carroll diagram. The formats are different — circles vs. grid — but the logical structure is identical. Some people find Carroll diagrams easier because the cells are clearly separated and labeled, while Venn diagrams better show the overlap visually."

- question: "Why does a Carroll diagram label rows with both an attribute and its opposite (e.g., 'Red' and 'Not Red') instead of just listing 'Red'?"
  type: short-answer
  answer: "Including the opposite makes the classification exhaustive — every object has a place. If you only listed 'Red,' you would have no designated place for non-red objects, and your sort would be incomplete. By explicitly including 'Not Red,' the Carroll diagram forces you to account for everything, including objects that lack the attribute. This is also an introduction to negation in logic: 'not red' is a meaningful category, not just the absence of a category."
  explanation: "The explicit negation is what makes Carroll diagrams a logic tool rather than just a sorting tool. In formal logic, negation (NOT) is a fundamental operation. Carroll diagrams train students to think in terms of 'has property X' and 'does not have property X' — which is exactly how propositions and their negations work."
```

## Explainer

You have used Venn diagrams to sort objects by two attributes, with overlapping circles showing what belongs to both groups, one group, or neither. A **Carroll diagram** does the same job with a different format: a 2x2 grid. Each attribute gets a row pair (yes and no) and a column pair (yes and no), creating four cells.

Here is an example. Suppose you are sorting numbers by two questions: "Is it even?" and "Is it greater than 10?" Your Carroll diagram looks like this: the rows are "Even" and "Not Even," the columns are "Greater than 10" and "Not Greater than 10." The number 14 is even AND greater than 10, so it goes in the top-left cell. The number 7 is not even AND not greater than 10, so it goes in the bottom-right cell. Every number has exactly one correct cell.

What makes Carroll diagrams special is that they force you to think about **negation** — the "not" version of every attribute. In a Venn diagram, the space outside both circles is easy to overlook. In a Carroll diagram, the "not" rows and columns are just as prominent as the "yes" rows and columns. This trains an important logical habit: when you classify something, you should be equally clear about what it IS and what it IS NOT.

Carroll diagrams and Venn diagrams display the same information in different formats. The four cells of a Carroll diagram correspond to the four regions of a two-circle Venn diagram. Some people find the grid format clearer because there is no ambiguity about where the boundaries are — each cell is a separate box. Others prefer the visual overlap of Venn diagrams. Being able to use both formats and translate between them is a sign of flexible logical thinking.

The Carroll diagram is named after Lewis Carroll — the pen name of Charles Dodgson, who wrote *Alice in Wonderland* and was also a mathematics lecturer at Oxford. He invented this diagram as a tool for teaching logic, believing that clear visual organization helps people reason more carefully. He was right.
