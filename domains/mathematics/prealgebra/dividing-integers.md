---
id: dividing-integers
title: Dividing Integers
domain: mathematics
course: prealgebra
prerequisites:
  - id: multiplying-integers
    type: hard
builds-toward:
  - integer-order-of-operations
  - solving-proportions
tags: [integers, division, operations]
stage: abstract-reasoning
status: validated
---

# Dividing Integers

## Core Idea
Division of integers follows the same sign rules as multiplication: dividing two numbers with the same sign gives a positive quotient, and dividing two numbers with different signs gives a negative quotient. This is because division is the inverse of multiplication — if (−3) × (−4) = 12, then 12 ÷ (−4) = −3. Division by zero remains undefined. Integer division is heavily used in solving equations, working with rational expressions, and computing slopes.

## How It's Best Learned
Connect explicitly to multiplication: "dividing is asking what number times the divisor gives the dividend." Show that the sign rules must match multiplication's sign rules for consistency. Practice alongside multiplication so students see them as inverse operations. Include problems with zero as the dividend (result is 0) and as the divisor (undefined).

## Common Misconceptions
- Students sometimes apply different sign rules for division than for multiplication — emphasize they are identical.
- Confusion about 0 ÷ 5 = 0 versus 5 ÷ 0 = undefined.
- Students may write −12 ÷ −4 = −3 (wrong sign) because they see two negatives and think the result should be negative.

## Questions

```yaml
- question: "A student claims that (−18) ÷ (−3) = −6, reasoning that 'two negatives in division must give a negative, like subtracting a negative.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — two negatives in division do produce a negative result"
    - "Division sign rules are the inverse of multiplication sign rules, so two negatives give a positive"
    - "The reasoning is wrong because division sign rules are unrelated to multiplication sign rules"
    - "The sign rules for division are the same as multiplication, so (−18) ÷ (−3) = 6, because division is the inverse of multiplication and must be consistent with it"
  answer: 3
  explanation: "Division is the inverse of multiplication and must use identical sign rules for consistency. To check: what number times (−3) gives (−18)? That number is 6, because 6 × (−3) = −18. So (−18) ÷ (−3) = 6. The student's confusion likely comes from mixing up different contexts where 'two negatives' have different effects — subtracting a negative does add, but dividing two negatives gives a positive, just like multiplying two negatives."

- question: "Which of the following expressions is UNDEFINED?"
  type: multiple-choice
  options:
    - "0 ÷ (−7)"
    - "(−5) ÷ 5"
    - "(−12) ÷ (−4)"
    - "(−9) ÷ 0"
  answer: 3
  explanation: "(−9) ÷ 0 is undefined because you are asking: what number times 0 gives −9? Nothing times zero ever equals a nonzero number, so no answer exists. The other expressions all have valid answers: 0 ÷ (−7) = 0 (zero divided by anything nonzero is 0), (−5) ÷ 5 = −1, and (−12) ÷ (−4) = 3. The confusion between 0 ÷ n (= 0) and n ÷ 0 (undefined) is one of the most common errors."

- question: "The sign rules for dividing integers are the same as the sign rules for multiplying integers: same signs give a positive result, different signs give a negative result."
  type: true-false
  answer: true
  explanation: "This is precisely the key insight of the topic. Division is the inverse of multiplication, so the sign rules must be identical for the two operations to be consistent. If same-sign multiplication gives positive, then same-sign division must also give positive — otherwise the operations would contradict each other."

- question: "Dividing zero by any number is undefined, just like dividing any number by zero."
  type: true-false
  answer: false
  explanation: "These two cases are completely different. Dividing zero BY a nonzero number gives zero: 0 ÷ 5 = 0, because 0 × 5 = 0. Dividing a nonzero number BY zero is what is undefined, because no number times 0 can give a nonzero result. The inverse-of-multiplication perspective makes this clear: 0 ÷ n asks 'what times n gives 0?' — the answer is always 0. But n ÷ 0 asks 'what times 0 gives n?' — impossible."

- question: "A classmate says: 'Since (−3) × (−4) = 12, I must memorize a separate sign rule for division to figure out (−12) ÷ (−3).' Why is this reasoning wrong, and what is the correct answer?"
  type: short-answer
  answer: "(−12) ÷ (−3) = 4. No separate rule is needed — division is the inverse of multiplication, so the sign rules are forced to be the same. To compute (−12) ÷ (−3), ask: what number times (−3) gives (−12)? The answer is 4, because 4 × (−3) = −12. Since same-sign multiplication gives positive, same-sign division must also give positive. The sign rules aren't separate facts to memorize; they follow automatically from the relationship between the two operations."
  explanation: "The power of understanding division as the inverse of multiplication is that you don't need to memorize sign rules separately. Every division problem can be checked by converting it to a multiplication question. This is the conceptual core of the topic and the reason sign rules for division and multiplication are identical."
```

## Explainer

You already know how to multiply integers, including the sign rules: positive × positive = positive, negative × negative = positive, positive × negative = negative. Division inherits exactly these same rules — and the reason is simple. Division is the inverse of multiplication. If you want to know what 12 ÷ (−4) equals, you are asking: "what number, when multiplied by −4, gives 12?" The answer is −3, because (−3) × (−4) = 12. The sign rules for division are not separate facts to memorize — they are forced by consistency with multiplication.

Let's trace through each case. Dividing two **positives** gives a positive: 15 ÷ 3 = 5, because 5 × 3 = 15. Dividing a **negative by a positive** (or positive by negative) gives a negative: (−15) ÷ 3 = −5, because (−5) × 3 = −15. Dividing a **negative by a negative** gives a positive: (−15) ÷ (−3) = 5, because 5 × (−3) = −15. The shortcut: same signs → positive quotient, different signs → negative quotient. This matches multiplication exactly.

Division by zero requires special attention. You cannot divide by zero because there is no number satisfying ? × 0 = 5 — anything times zero is zero, never 5. Division *of* zero is fine: 0 ÷ 5 = 0, because 0 × 5 = 0. These two cases — zero as dividend versus zero as divisor — look superficially similar but are completely different. The inverse-of-multiplication perspective makes them easy to distinguish: ask "what times the divisor gives the dividend?" Zero times anything is zero, so 0 ÷ (any nonzero) = 0. But nothing times zero gives a nonzero number, so (nonzero) ÷ 0 is undefined.
