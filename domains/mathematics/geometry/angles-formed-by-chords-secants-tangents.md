---
id: angles-formed-by-chords-secants-tangents
title: Angles Formed by Chords, Secants, and Tangents
domain: mathematics
course: geometry
prerequisites:
  - id: inscribed-angles
    type: hard
  - id: central-angles-and-arcs
    type: hard
  - id: exterior-angle-theorem
    type: hard
  - id: tangent-lines-to-circles
    type: soft
builds-toward: []
tags: [geometry, circles, arcs, chords, secants, tangents, angle-measure]
stage: abstract-reasoning
status: validated
---

# Angles Formed by Chords, Secants, and Tangents

## Core Idea
When two lines meet a circle, the angle between them depends on the arcs they cut off and on where the vertex sits. If the vertex is on the circle (an inscribed angle or a tangent-chord angle), the angle is half its intercepted arc. If the vertex is inside the circle (two chords crossing), the angle is half the sum of the two intercepted arcs. If the vertex is outside the circle (two secants, a secant and a tangent, or two tangents), the angle is half the difference of the far arc and the near arc.

## How It's Best Learned
Organize the rules by vertex location: on, inside, outside. Prove each case by drawing one extra chord that creates an inscribed angle and then applying the exterior angle theorem. Practice by first marking which arcs each angle intercepts, then choosing the rule, and check answers with the fact that the arcs of a circle total 360°.

## Common Misconceptions
- Every angle related to a circle equals half its intercepted arc. (That holds only when the vertex is on the circle; inside the circle you add arcs, and outside you subtract them.)
- For an angle formed by two chords, only the arc between the angle's sides matters. (The vertical angle's arc counts too; the angle is half the sum of both arcs.)
- For an angle outside the circle, subtract in either order. (Subtract the near arc from the far arc so the result is positive.)

## Questions

```yaml
- question: "Two chords intersect inside a circle. The angle and its vertical angle intercept arcs of 70° and 110°. What is the measure of the angle?"
  type: multiple-choice
  options: ["20°", "70°", "90°", "180°"]
  answer: 2
  explanation: "For two chords crossing inside a circle, the angle equals half the sum of the intercepted arcs: (70° + 110°)/2 = 90°. 20° would come from wrongly using half the difference, which is the rule for vertices outside the circle."

- question: "Two secants meet at a point outside a circle. They intercept a far arc of 130° and a near arc of 50°. Find the angle between the secants."
  type: short-answer
  answer: "40°"
  explanation: "For a vertex outside the circle, the angle is half the difference of the intercepted arcs: (130° - 50°)/2 = 40°."

- question: "An angle whose vertex is inside a circle (but not at the center) is always half of the arc between its sides."
  type: true-false
  answer: false
  explanation: "Half the arc is the rule for vertices on the circle. For a vertex inside, the angle is half the sum of the arc between its sides and the arc between the extensions of its sides. Only when the vertex is the center do both arcs equal the angle itself."

- question: "A tangent and a chord meet at the point of tangency, and the chord cuts off an arc of 140° on the side of the angle. What is the angle between the tangent and the chord?"
  type: multiple-choice
  options: ["70°", "140°", "40°", "110°"]
  answer: 0
  explanation: "A tangent-chord angle has its vertex on the circle, so it behaves like an inscribed angle: it measures half its intercepted arc, 140°/2 = 70°."
```

## Explainer

You know that an inscribed angle, whose vertex lies on the circle, measures half its intercepted arc. That single fact, plus the exterior angle theorem for triangles, explains every angle formed by lines that meet a circle. The key is where the vertex is.

Vertex on the circle. Besides inscribed angles, this case includes the angle between a tangent and a chord drawn from the point of tangency. It also measures half the arc it intercepts. If a tangent meets a chord that cuts off a 140° arc, the angle is 70°.

Vertex inside the circle. Suppose chords AC and BD cross at point P. Angle APB intercepts arc AB, and its vertical angle CPD intercepts arc CD. Draw chord BC. Then angle APB is an exterior angle of triangle BPC, so it equals the sum of the two remote interior angles, angle PBC and angle PCB. Each of those is an inscribed angle: angle DBC intercepts arc CD and angle ACB intercepts arc AB. So angle APB = (arc AB)/2 + (arc CD)/2 = (arc AB + arc CD)/2. With arcs of 70° and 110°, the angle is 90°.

Vertex outside the circle. Suppose two secants from point P meet the circle, with the far arc measuring x and the near arc measuring y. Draw a chord connecting one near intersection point to one far intersection point so that it forms a triangle with P. An inscribed angle that intercepts the far arc is an exterior angle of that triangle. It equals angle P plus a second inscribed angle that intercepts the near arc. So x/2 = angle P + y/2, which gives angle P = (x - y)/2. With arcs of 130° and 50°, the angle is 40°. The same rule covers a secant with a tangent and two tangents. For two tangents, the arcs are a minor arc m and the major arc 360° - m, so the angle is (360° - 2m)/2 = 180° - m.

A short summary helps: on the circle, half the arc; inside, half the sum; outside, half the difference. Before using a rule, mark the arcs each angle intercepts. Many errors come from picking the right rule but the wrong arcs.
