---
id: moment-of-force-2d
title: Moment of a Force in 2D
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: force-systems-resultants
  type: hard
- id: torque
  type: soft
- id: cross-product
  type: soft
builds-toward:
- varignons-theorem
- couple-moment
- equilibrium-rigid-bodies
tags:
- statics
- moment
- torque
- rotation
stage: formal-systems
status: draft
---

# Moment of a Force in 2D

## Core Idea
The moment of a force about a point is the tendency of that force to cause rotation about that point, calculated as M = r × F (cross product) or equivalently M = F·d, where d is the perpendicular distance from the point to the force's line of action. In 2D, moments are scalar quantities with sign indicating direction (counterclockwise positive by convention). The moment depends on both the force magnitude and the perpendicular geometry — a force directed through the reference point produces zero moment.

## How It's Best Learned
Compute moments using both the cross product method and the perpendicular distance method and verify the answers agree. Always establish a positive direction convention before starting. Practice identifying the line of action to find the correct perpendicular distance.

## Common Misconceptions
- Using the distance to the point of force application rather than the perpendicular distance to the line of action.
- Sign errors when determining clockwise versus counterclockwise sense.
- Thinking a force that passes through the reference point has a nonzero moment.
