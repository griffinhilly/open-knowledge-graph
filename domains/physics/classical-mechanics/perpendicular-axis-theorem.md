---
id: perpendicular-axis-theorem
title: Perpendicular Axis Theorem
domain: physics
course: classical-mechanics
prerequisites:
- id: moment-of-inertia
  type: hard
builds-toward:
- rotational-kinetic-energy
tags:
- moment-of-inertia
- rotation
- 2d-shapes
stage: formal-systems
status: validated
---

# Perpendicular Axis Theorem

## Core Idea
For any planar (2D) object, the moment of inertia about an axis perpendicular to the plane equals the sum of moments about two perpendicular axes in the plane: I_z = I_x + I_y. This gives a quick way to find the out-of-plane moment from in-plane measurements, especially useful for thin disks and plates.

## Questions

```yaml
- question: "A student applies the perpendicular axis theorem to a solid cylinder of radius R and height h. They note I_z = ½MR² and use symmetry (I_x = I_y) to conclude I_x = ¼MR². Is this correct?"
  type: multiple-choice
  options:
    - "Yes — the perpendicular axis theorem applies to any axially symmetric object"
    - "No — the theorem requires the object to be planar (all mass in a single plane), and a cylinder with height h has mass distributed at nonzero z-values, violating this requirement"
    - "The result ¼MR² is approximately correct for thin cylinders where h << R"
    - "No — the symmetry argument I_x = I_y fails for cylinders; symmetry only applies to disks"
  answer: 1
  explanation: "The perpendicular axis theorem applies ONLY to planar objects — those with all mass in the z = 0 plane. The proof uses the fact that for a mass element at (x, y, 0), r_z² = x²+y² = r_y²+r_x² exactly. For a cylinder with height h, mass elements at (x, y, z) with z ≠ 0 have r_x = √(y²+z²) ≠ y, so I_x + I_y ≠ I_z. The correct moment for a cylinder about a diameter includes an h² term and exceeds ¼MR²."

- question: "For a uniform thin disk of mass M and radius R, what is the moment of inertia about a diameter, and how does the perpendicular axis theorem derive it efficiently?"
  type: multiple-choice
  options:
    - "I = ½MR², derived by direct integration of r² dm over the disk"
    - "I = ¼MR², derived by noting I_z = ½MR² and using I_z = I_x + I_y with I_x = I_y by rotational symmetry, giving I_x = ¼MR²"
    - "I = MR², derived using the parallel axis theorem to shift from center of mass to the rim"
    - "I = ⅓MR², derived from the general formula for a planar object rotating about an in-plane axis"
  answer: 1
  explanation: "The perpendicular axis theorem at its most elegant: I_z = ½MR² for the symmetry axis (from direct integration). The disk has rotational symmetry, so any two perpendicular diameters are equivalent: I_x = I_y. The theorem gives I_z = I_x + I_y = 2I_x, so I_x = ¼MR². This avoids integrating over a tilted axis — much harder. Symmetry plus the theorem converts a difficult integral into simple algebra."

- question: "The perpendicular axis theorem states I_z = I_x + I_y and applies to any object as long as the z-axis is perpendicular to the plane containing x and y."
  type: true-false
  answer: false
  explanation: "The theorem applies only to planar objects — those with all mass at z = 0. For a 3D object, a mass element at (x, y, z) has r_x = √(y²+z²) and r_y = √(x²+z²), so I_x + I_y = Σm(y²+z²) + Σm(x²+z²) = Σm(x²+y²) + 2Σmz² = I_z + 2Σmz². The sum equals I_z only when z = 0 for all mass elements. Applying the theorem to solid 3D objects (cylinders, spheres) produces wrong answers."

- question: "For a uniform thin disk, the moment of inertia is the same about any diameter, equal to ¼MR²."
  type: true-false
  answer: true
  explanation: "By the rotational symmetry of the disk, all diameters are geometrically equivalent — the disk looks the same from every direction in its plane. So I_x = I_y for any pair of perpendicular diameters. The perpendicular axis theorem gives I_z = I_x + I_y = 2I_x, so I_x = ¼MR². This value is the same for any diameter, because the disk's circular symmetry ensures all diameters are equivalent axes."

- question: "Why does the perpendicular axis theorem require the object to be planar, and what goes wrong when you try to apply it to a three-dimensional object?"
  type: short-answer
  answer: "The proof rests on r_z² = r_x² + r_y², which holds only when z = 0 for every mass element. For a planar object: r_z = √(x²+y²), r_x = y (since z=0), r_y = x, so r_z² = x²+y² = r_y²+r_x². For a 3D object with a mass element at (x, y, z): r_x = √(y²+z²) and r_y = √(x²+z²), so I_x + I_y = Σm(x²+y²) + 2Σmz² = I_z + 2Σmz² ≠ I_z unless z = 0 everywhere."
  explanation: "This is the most common error with this theorem. The planarity condition is not a technicality — it is what makes the 2D Pythagorean theorem applicable to distances from axes. A cylinder, sphere, or any solid 3D object fails this condition. Always verify that the object is a flat plate, disk, ring, or thin shell in a single plane before applying the theorem. The parallel axis theorem, which shifts rather than rotates the axis, has no such planarity restriction."
```

## Explainer

From moment of inertia theory you know that I = Σmᵢrᵢ² (or ∫r² dm for continuous objects), where r is measured from the axis of rotation. The value of I depends crucially on which axis you choose — the same object can have very different moments about different axes. The **perpendicular axis theorem** is a relationship that connects three different moments of a single planar object, letting you find one if you know the other two.

The proof follows directly from the definition of r. Set up a coordinate system with x and y axes in the plane of the object and z perpendicular to it. For any mass element at position (x, y) in the plane: the distance from the z-axis is r_z = √(x² + y²), the distance from the x-axis is r_x = y (since the object is flat, z = 0), and the distance from the y-axis is r_y = x. Therefore I_z = Σmᵢ(xᵢ² + yᵢ²) = Σmᵢxᵢ² + Σmᵢyᵢ² = I_y + I_x. The theorem is essentially the 2D Pythagorean theorem applied to distances from axes. Note that the object *must be planar* — if it has any thickness in the z-direction, the distances r_x and r_y pick up a z² contribution and the sum no longer equals I_z.

The theorem is most useful when a shape has symmetry that makes I_x = I_y. For a uniform disk, symmetry about the center means any two perpendicular diameters are equivalent axes, so I_x = I_y = I_disk. The perpendicular theorem then gives I_z = I_x + I_y = 2I_x, so I_x = I_z/2. Since the moment of a disk about its symmetry axis (z) is ½MR², the moment about a diameter is ¼MR². This result would be more painful to derive by direct integration over the tilted axis, so the perpendicular theorem is a real shortcut.

A related theorem — the **parallel axis theorem** (which you may also encounter) — shifts an axis away from the center of mass rather than rotating it. The two theorems together form a toolkit for building up moments for composite objects or for axes that are not through the center of mass. When a problem asks for the moment about a strange axis for a planar object, your first question should be: can I find two in-plane moments that sum to this one? If the geometry cooperates, the perpendicular axis theorem turns a complicated integral into a lookup plus addition.
