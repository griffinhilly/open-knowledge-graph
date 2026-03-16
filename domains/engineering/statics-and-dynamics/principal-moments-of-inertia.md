---
id: principal-moments-of-inertia
title: Principal Moments of Inertia and Principal Axes
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: moment-of-inertia-about-centroid
  type: hard
- id: parallel-axis-theorem-statics
  type: hard
builds-toward:
- rotation-about-arbitrary-axis
- euler-equations-rigid-body-rotation
tags:
- inertia
- principal-axes
- rigid-bodies
stage: formal-systems
status: draft
---

# Principal Moments of Inertia and Principal Axes

## Core Idea
Every rigid body has three principal axes (orthogonal directions where the inertia tensor is diagonal). Rotation about a principal axis is dynamically uncoupled; however, rotation about arbitrary axes requires full tensor analysis. Bodies naturally rotate stably about principal axes with maximum and minimum moments of inertia, but unstably about the intermediate axis.

## Explainer

You already know how to compute the moment of inertia Ixx, Iyy, Izz of a body about each coordinate axis, and how to shift those values using the parallel-axis theorem. But for an arbitrarily oriented body, the resistance to angular acceleration is not fully captured by three diagonal values alone. When you spin an object about an axis that is not aligned with its geometric symmetry, the angular momentum vector **L** = **I** · **ω** is generally not parallel to **ω**. This misalignment creates **reaction torques** that must be supplied by bearings — and it is the origin of vibration in unbalanced rotating machinery.

The full resistance to rotation is described by the **inertia tensor**, a 3×3 symmetric matrix. The off-diagonal entries are the **products of inertia** (e.g., Ixy = −∫xy dm), which measure how mass is distributed asymmetrically about coordinate planes. When the products of inertia are zero for a given coordinate frame, the matrix is diagonal and the axes are **principal axes**. Mathematically, finding principal axes is an eigenvalue problem: the principal moments of inertia are the eigenvalues, and the principal axes are the eigenvectors. For any rigid body, at least three mutually orthogonal principal axes always exist — this follows from the spectral theorem for symmetric matrices.

The physical consequence of rotation about a principal axis is clean: **L** and **ω** are parallel, no reaction torques are needed, and the rotation proceeds without wobble. A symmetric object like a sphere or a circular disk has every axis through its center as a principal axis. An asymmetric object — a wrench, an L-shaped bracket — has a specific set of three orthogonal principal axes that must be found by solving the eigenvalue problem.

The **intermediate axis theorem** (sometimes called the tennis racket theorem) is the most striking result: rotation is dynamically stable about the axes of maximum and minimum principal moments, but **unstable** about the intermediate axis. A slightly perturbed spin about the smallest or largest axis returns to that axis; a slight perturbation about the intermediate axis grows into a tumbling, flipping motion. You can demonstrate this by tossing a book: it spins cleanly about its short or long axis but tumbles chaotically if you spin it about its intermediate (face-to-face) axis. This same instability governs the attitude dynamics of spacecraft with asymmetric mass distributions, making principal axis alignment a critical design consideration.
