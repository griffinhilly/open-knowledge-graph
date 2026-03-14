---
id: volumes-by-shell-method
title: Volumes by Shell Method
domain: mathematics
course: calculus-2
prerequisites:
  - id: volumes-by-washer-method
    type: soft
  - id: fundamental-theorem-of-calculus-part-2
    type: hard
builds-toward: []
tags: [integration, applications, volumes, revolution, shells]
stage: formal-systems
status: validated
---

# Volumes by Shell Method

## Core Idea
The shell method computes volumes of revolution by integrating cylindrical shells instead of disks or washers. For a region revolved about the y-axis, V = integral from a to b of 2*pi*x*f(x) dx. Each shell has radius x (distance from the axis), height f(x), and thickness dx. The shell method is often easier than the washer method when revolving about the y-axis while the function is given in terms of x, because it avoids solving for x in terms of y.

## How It's Best Learned
Derive the shell volume element 2*pi * radius * height * thickness. Compare the same problem done with shells vs. washers to see when each is more convenient. Practice identifying the radius and height for different axes of revolution.

## Common Misconceptions
- Confusing when to use shells vs. washers (shells are parallel to the axis, washers perpendicular).
- Using the wrong expression for the radius of the shell.
- Forgetting the 2*pi factor or confusing it with the pi in the disk/washer method.
