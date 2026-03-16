---
id: relative-motion-and-reference-frames
title: Relative Motion and Reference Frames
domain: physics
course: classical-mechanics
prerequisites:
- id: kinematics-2d
  type: hard
builds-toward:
- non-inertial-frames-and-pseudo-forces
- reduced-mass-problem
tags:
- kinematics
- reference-frames
- relative-motion
- vectors
stage: formal-systems
status: draft
---

# Relative Motion and Reference Frames

## Core Idea
Velocity and position are frame-dependent. If object A has velocity v_A in frame F, and frame F moves at v_F relative to frame G, then A's velocity in G is v_A + v_F (Galilean velocity addition). The same trajectory looks different to different observers, but physics laws are identical in all inertial frames, reflecting Galilean relativity.

## Explainer

From your work on 2D kinematics, you know how to describe position, velocity, and acceleration with vectors. The key new idea in reference frames is that those vectors are not absolute — they are *relative to the coordinate system of the observer*. A reference frame is simply a coordinate system attached to a particular observer or object, within which positions and velocities are measured. Different observers, moving relative to each other, assign different numbers to the same physical event.

The concrete tool for translating between frames is **Galilean velocity addition**. Suppose you are sitting on a train moving east at 30 m/s relative to the ground. You throw a ball forward at 20 m/s relative to you. From the ground, the ball moves at 30 + 20 = 50 m/s east. This additive rule — v_ground = v_train + v_ball_in_train — is what you already know intuitively, and it is correct for all speeds much less than the speed of light. The general vector form is: v_AG = v_AF + v_FG, where v_AG is the velocity of object A in frame G, v_AF is A's velocity in frame F, and v_FG is frame F's velocity relative to G. The subscripts chain: the middle letter (F) cancels, giving the outer letters (A and G) as the meaningful pair. This chaining rule is enormously useful in problems with multiple moving bodies.

Position transforms similarly. If frame F is displaced from frame G by position r_FG, then the position of A in G is r_AG = r_AF + r_FG. Differentiating twice: acceleration transforms too, but crucially, if F moves at *constant* velocity relative to G (i.e., no acceleration between frames), then a_AF = a_AG — **acceleration is the same in both frames**. This is the physical content of **Galilean relativity**: the laws of mechanics (F = ma) take the same form in all *inertial* frames (frames not accelerating relative to each other). There is no mechanical experiment that can tell you whether you are at rest or moving at constant velocity — only your velocity *relative to something else* is physically meaningful. This invariance principle is one of the most profound symmetries in physics, and it forms the conceptual foundation for Einstein's special relativity (which refines it by making the speed of light the invariant quantity rather than time and length).

The practical skill is recognizing when a change of reference frame simplifies a problem. A boat crossing a river, a plane flying in wind, a ball thrown from a moving vehicle — all these are most naturally analyzed by choosing one frame for each component of motion, computing in that frame, then transforming back. The common error is mixing frames: treating part of the velocity as if it belongs to one frame and part to another. The fix is always to be explicit about *which frame* each velocity vector is measured in before applying the addition rule. As you build toward non-inertial frames, you will see what happens when the frame itself accelerates — that is when the equivalence between frames breaks down and fictitious forces like the Coriolis effect and centrifugal force appear.

