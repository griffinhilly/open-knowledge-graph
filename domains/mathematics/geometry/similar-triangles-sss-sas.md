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

## Explainer

From AA similarity, you know that two triangles with two pairs of equal angles must be similar — the angles force the shape to be the same even if the sizes differ. But what if you're given side lengths rather than angle measures? That's where **SSS similarity** and **SAS similarity** come in, and your work with proportions is the key tool.

**SSS Similarity** says: if all three pairs of corresponding sides are in the same ratio, the triangles are similar. Suppose triangle ABC has sides 6, 8, 10, and triangle DEF has sides 9, 12, 15. Check the ratios: 6/9 = 2/3, 8/12 = 2/3, 10/15 = 2/3. All three ratios are equal, so the triangles are similar with scale factor 2/3. Crucially, you must pair the sides correctly — smallest to smallest, largest to largest, or use the ordering of corresponding vertices. This is where proportions from your prerequisite work come in: equal ratios, cross-multiplication, consistent labeling.

**SAS Similarity** requires only two sides and the angle *between* them. If two pairs of corresponding sides are proportional *and* the **included angle** (the one sandwiched between those two sides) is congruent, the triangles are similar. For example, if triangle PQR has PQ = 4, PR = 6, and angle P = 50°, and triangle XYZ has XY = 6, XZ = 9, and angle X = 50°, then PQ/XY = 4/6 = 2/3, PR/XZ = 6/9 = 2/3, and the included angles match — so the triangles are similar by SAS. The included angle requirement is non-negotiable: if you use a non-included angle, the criterion fails (just as SSA fails for congruence).

The connection to congruence criteria sharpens your understanding: SSS and SAS congruence check that corresponding sides are *equal*; SSS and SAS similarity check that corresponding sides are *proportional*. Similarity is congruence "up to scale." Any congruent pair is also similar (with ratio 1), but not vice versa. This framework gives you two complete toolkits — AA, SSS, SAS — for determining triangle similarity from different types of given information, and sets up proportionality theorems about the side lengths of similar triangles.
