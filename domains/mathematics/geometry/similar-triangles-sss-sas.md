---
id: similar-triangles-sss-sas
title: "Similar Triangles: SSS and SAS Similarity"
domain: mathematics
course: geometry
prerequisites:
  - id: similar-triangles-aa
    type: hard
  - id: proportions
    type: hard
builds-toward:
  - proportions-in-similar-triangles
tags: [similarity, triangles, SSS, SAS, proportionality]
stage: abstract-reasoning
status: validated
---

# Similar Triangles: SSS and SAS Similarity

## Core Idea
Beyond AA, there are two other criteria for triangle similarity. SSS Similarity: if all three pairs of corresponding sides are proportional (same ratio), the triangles are similar. SAS Similarity: if two pairs of corresponding sides are proportional and the included angles are congruent, the triangles are similar. These parallel the congruence criteria but use proportionality instead of equality for sides.

## How It's Best Learned
Compare with the congruence versions (SSS, SAS) and emphasize the shift from "equal" to "proportional." Practice computing side ratios and checking whether they are all equal. For SAS, stress that the angle must be the included angle. Give problems that require choosing the correct similarity criterion.

## Common Misconceptions
- Confusing similarity SSS (proportional sides) with congruence SSS (equal sides).
- For SAS similarity, using a non-included angle.
- Setting up ratios inconsistently (mixing which triangle's sides go in the numerator vs. denominator).

## Questions

```yaml
- question: "Triangle ABC has sides 6, 9, and 12. Triangle DEF has sides 4, 6, and 8. Which statement best describes the relationship between these triangles?"
  type: multiple-choice
  options:
    - "They are congruent by SSS because all three side pairs are given"
    - "They are similar by SSS because all three side ratios are equal (3/2)"
    - "They cannot be compared without knowing the angles"
    - "They are similar, but the criterion is AA, not SSS"
  answer: 1
  explanation: "All three side ratios are equal: 6/4 = 9/6 = 12/8 = 3/2. This satisfies SSS Similarity. Note that option A confuses similarity with congruence — congruence requires equal sides, not proportional ones. Since the sides are proportional but not equal, the triangles are similar (same shape, different size), not congruent. No angle information is needed when all three side ratios are confirmed equal."

- question: "Triangle PQR has PQ = 5, PR = 10, and angle P = 40°. Triangle XYZ has XY = 3, XZ = 6, and angle Y = 40°. Are these triangles similar by SAS?"
  type: multiple-choice
  options:
    - "Yes — the side ratios are equal and a congruent angle exists in each triangle, which is sufficient for SAS similarity"
    - "No — the 40° angle in triangle XYZ is angle Y, not the included angle between XY and XZ (which would be angle X)"
    - "Yes — two side ratios are equal (5/3 = 10/6) and a 40° angle appears in each triangle"
    - "No — SAS similarity requires all three side ratios to be equal, not just two"
  answer: 1
  explanation: "The side ratios are equal (5/3 = 10/6), but SAS similarity requires the congruent angle to be the INCLUDED angle — sandwiched between the two proportional sides. In triangle PQR, angle P is between PQ and PR: it is the included angle. In triangle XYZ, the included angle between XY and XZ would be angle X, not angle Y. Since the 40° angle in XYZ is at vertex Y, not vertex X, the SAS criterion is not satisfied. This is the most common SAS error."

- question: "If all three pairs of corresponding sides of two triangles are in the same ratio, the triangles must be similar even if no angle measures are given."
  type: true-false
  answer: true
  explanation: "This is exactly what SSS Similarity states: proportional corresponding sides alone are sufficient to establish similarity — no angle information is needed. Compare this with SSS Congruence, which requires equal (not merely proportional) corresponding sides. SSS Similarity is a complete, self-sufficient criterion."

- question: "In SAS Similarity, any pair of congruent angles combined with two proportional side pairs is sufficient, regardless of which angle it is."
  type: true-false
  answer: false
  explanation: "SAS Similarity specifically requires the congruent angle to be the INCLUDED angle — the one formed between the two proportional sides. If the congruent angle is not included (not between those two sides), the triangles may not be similar. This mirrors how SSA fails as a congruence criterion: the position of the angle relative to the sides determines whether the criterion holds. Always verify that the congruent angle is sandwiched between the two proportional side pairs."

- question: "Explain the key difference between SSS Congruence and SSS Similarity, and describe how you would set up the check for SSS Similarity given two triangles."
  type: short-answer
  answer: "SSS Congruence requires all three pairs of corresponding sides to be equal in length; SSS Similarity requires all three pairs to be in the same ratio. To check SSS Similarity, pair corresponding sides (smallest-to-smallest, largest-to-largest, or by vertex labeling), compute the three ratios, and verify they are all equal. If they are, the triangles are similar with that ratio as the scale factor."
  explanation: "The shift from 'equal' to 'proportional' is the heart of similarity. Congruence is similarity with scale factor 1. Students who confuse the two often try to use equal side lengths to establish similarity, or mistakenly test for congruence when similarity is called for. Setting up ratios consistently — always putting the same triangle's sides in the numerator — prevents the arithmetic errors that come from mixing the orientation."
```

## Explainer

From AA similarity, you know that two triangles with two pairs of equal angles must be similar — the angles force the shape to be the same even if the sizes differ. But what if you're given side lengths rather than angle measures? That's where **SSS similarity** and **SAS similarity** come in, and your work with proportions is the key tool.

**SSS Similarity** says: if all three pairs of corresponding sides are in the same ratio, the triangles are similar. Suppose triangle ABC has sides 6, 8, 10, and triangle DEF has sides 9, 12, 15. Check the ratios: 6/9 = 2/3, 8/12 = 2/3, 10/15 = 2/3. All three ratios are equal, so the triangles are similar with scale factor 2/3. Crucially, you must pair the sides correctly — smallest to smallest, largest to largest, or use the ordering of corresponding vertices. This is where proportions from your prerequisite work come in: equal ratios, cross-multiplication, consistent labeling.

**SAS Similarity** requires only two sides and the angle *between* them. If two pairs of corresponding sides are proportional *and* the **included angle** (the one sandwiched between those two sides) is congruent, the triangles are similar. For example, if triangle PQR has PQ = 4, PR = 6, and angle P = 50°, and triangle XYZ has XY = 6, XZ = 9, and angle X = 50°, then PQ/XY = 4/6 = 2/3, PR/XZ = 6/9 = 2/3, and the included angles match — so the triangles are similar by SAS. The included angle requirement is non-negotiable: if you use a non-included angle, the criterion fails (just as SSA fails for congruence).

The connection to congruence criteria sharpens your understanding: SSS and SAS congruence check that corresponding sides are *equal*; SSS and SAS similarity check that corresponding sides are *proportional*. Similarity is congruence "up to scale." Any congruent pair is also similar (with ratio 1), but not vice versa. This framework gives you two complete toolkits — AA, SSS, SAS — for determining triangle similarity from different types of given information, and sets up proportionality theorems about the side lengths of similar triangles.
