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

## Explainer

You have seen how to build volumes of revolution by slicing a solid into thin disks or washers perpendicular to the axis of revolution and integrating their areas. The **shell method** offers an alternative decomposition: instead of slices perpendicular to the axis, you wrap the solid into thin cylindrical **shells** parallel to the axis — like a stack of nested tin cans, each one a bit larger than the last. Integrating the volume of each shell gives the total volume. Both methods give the same answer; the choice is about which is easier for a given problem.

The volume of a single thin shell comes from unwrapping it into a flat slab. A cylindrical shell with **radius** r, **height** h, and thickness dr has volume approximately equal to its circumference times height times thickness: 2πr · h · dr. When you revolve the region under y = f(x) from x = a to x = b about the y-axis, each vertical strip at position x becomes a shell. The strip's distance from the y-axis is its radius x, its height is f(x), and its thickness is dx. The total volume is therefore V = ∫_a^b 2π · x · f(x) dx. The factor of 2π is the key distinction from the washer method, which uses π.

The practical question is when to prefer shells over washers. The guiding principle: **use the method that avoids solving for the inverse function**. If the region is described by y = f(x) and you revolve about a *vertical* axis (the y-axis or x = k), shells integrate in x naturally — you never need to write x as a function of y. The washer method for the same revolution would require you to find x = f⁻¹(y) and integrate in y, which is often harder. Conversely, for revolution about a *horizontal* axis (the x-axis or y = k), washers integrate in x naturally, while shells would require rewriting everything in terms of y.

For axes that are not at the origin, the **radius** of each shell changes. For revolution about x = k, the shell radius is |x − k|, not just x. For revolution about a horizontal axis, the method rotates: shells become horizontal rings, the radius is the y-value, the height is measured horizontally as a function of y, and you integrate in y. In all cases, the formula remains 2π · (radius) · (height) · d(variable). Identifying the three quantities — radius, height, and integration variable — correctly for any given setup is the central skill.
