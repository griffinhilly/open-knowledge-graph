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
status: validated
---

# Relative Motion and Reference Frames

## Core Idea
Velocity and position are frame-dependent. If object A has velocity v_A in frame F, and frame F moves at v_F relative to frame G, then A's velocity in G is v_A + v_F (Galilean velocity addition). The same trajectory looks different to different observers, but physics laws are identical in all inertial frames, reflecting Galilean relativity.

## Questions

```yaml
- question: "A train moves east at 30 m/s relative to the ground. A passenger walks west (backward) at 2 m/s relative to the train. What is the passenger's velocity relative to the ground?"
  type: multiple-choice
  options:
    - "32 m/s east — the two velocities add because both are in the east direction"
    - "28 m/s east — the train's velocity minus the walking velocity relative to the train"
    - "2 m/s west — only the passenger's motion relative to the train matters"
    - "30 m/s east — the walking velocity is too small to matter"
  answer: 1
  explanation: "Using Galilean velocity addition: v_passenger/ground = v_passenger/train + v_train/ground. The passenger walks west at 2 m/s relative to the train (−2 m/s east), and the train moves east at +30 m/s relative to the ground. So v_passenger/ground = −2 + 30 = +28 m/s east. The subscripts chain: v_person/ground = v_person/train + v_train/ground. The middle label (train) cancels, leaving person relative to ground. This chaining structure is the key to solving multi-body frame problems correctly."

- question: "Two inertial frames F and G are moving at constant velocity relative to each other. An object accelerates at 5 m/s² in frame F. What is its acceleration in frame G?"
  type: multiple-choice
  options:
    - "5 m/s² minus the relative velocity between the frames"
    - "5 m/s² — acceleration is the same in all inertial frames"
    - "It depends on how fast F moves relative to G"
    - "We cannot determine the acceleration in G without knowing the object's mass"
  answer: 1
  explanation: "When two frames move at constant relative velocity (neither accelerating), acceleration is the same in both frames. Differentiating the velocity addition rule v_AG = v_AF + v_FG with respect to time: if v_FG is constant, its derivative is zero, so a_AG = a_AF. This is the key physical content of Galilean relativity: because F = ma and acceleration is frame-independent (for inertial frames), Newton's second law takes the same form in every inertial frame. Only velocity is frame-dependent, not acceleration."

- question: "The velocity of an object is only meaningful when specified relative to a particular reference frame."
  type: true-false
  answer: true
  explanation: "Velocity is inherently relational — it describes motion relative to some observer or coordinate system. The statement 'the car moves at 60 km/h' is incomplete without specifying 'relative to the ground' or 'relative to another car.' This is not a pedantic distinction: in problems with multiple moving bodies, failing to track which frame a velocity belongs to is the most common source of errors. There is no 'absolute' velocity in classical mechanics — only velocity relative to something."

- question: "In an inertial reference frame, forces acting on an object have different magnitudes than in another inertial frame moving at constant velocity."
  type: true-false
  answer: false
  explanation: "Forces and accelerations are identical in all inertial frames. Only velocities differ between inertial frames — and forces (F = ma) depend on acceleration, not velocity. This is precisely why Galilean relativity holds for mechanics: no mechanical measurement of force or acceleration can distinguish one inertial frame from another. The frame-dependence of velocity is observable (the Doppler effect, for example), but force measurements give the same result in every inertial frame."

- question: "Why is it essential to be explicit about which reference frame each velocity is measured in before applying the Galilean velocity addition rule?"
  type: short-answer
  answer: "The addition rule v_AG = v_AF + v_FG only works correctly when all velocities are expressed in the right frames. Mixing frames — treating part of a velocity as if it were in one frame and part in another — gives wrong answers. For example, treating a ball's speed relative to a thrower as if it were already relative to the ground, then adding the thrower's ground velocity, double-counts. Explicit frame labels (subscripts) ensure the middle frame cancels correctly, producing the velocity of one object relative to the intended frame."
  explanation: "Frame mixing is the most common error in relative-motion problems. The fix is always to write out the subscripts: what is the velocity of (A) relative to (B)? Then identify which pieces of information you have and check that the subscripts chain correctly. Once the labeling is right, the arithmetic is straightforward. The conceptual discipline of always asking 'relative to what?' carries forward into all of physics, including special relativity."
```

## Explainer

From your work on 2D kinematics, you know how to describe position, velocity, and acceleration with vectors. The key new idea in reference frames is that those vectors are not absolute — they are *relative to the coordinate system of the observer*. A reference frame is simply a coordinate system attached to a particular observer or object, within which positions and velocities are measured. Different observers, moving relative to each other, assign different numbers to the same physical event.

The concrete tool for translating between frames is **Galilean velocity addition**. Suppose you are sitting on a train moving east at 30 m/s relative to the ground. You throw a ball forward at 20 m/s relative to you. From the ground, the ball moves at 30 + 20 = 50 m/s east. This additive rule — v_ground = v_train + v_ball_in_train — is what you already know intuitively, and it is correct for all speeds much less than the speed of light. The general vector form is: v_AG = v_AF + v_FG, where v_AG is the velocity of object A in frame G, v_AF is A's velocity in frame F, and v_FG is frame F's velocity relative to G. The subscripts chain: the middle letter (F) cancels, giving the outer letters (A and G) as the meaningful pair. This chaining rule is enormously useful in problems with multiple moving bodies.

Position transforms similarly. If frame F is displaced from frame G by position r_FG, then the position of A in G is r_AG = r_AF + r_FG. Differentiating twice: acceleration transforms too, but crucially, if F moves at *constant* velocity relative to G (i.e., no acceleration between frames), then a_AF = a_AG — **acceleration is the same in both frames**. This is the physical content of **Galilean relativity**: the laws of mechanics (F = ma) take the same form in all *inertial* frames (frames not accelerating relative to each other). There is no mechanical experiment that can tell you whether you are at rest or moving at constant velocity — only your velocity *relative to something else* is physically meaningful. This invariance principle is one of the most profound symmetries in physics, and it forms the conceptual foundation for Einstein's special relativity (which refines it by making the speed of light the invariant quantity rather than time and length).

The practical skill is recognizing when a change of reference frame simplifies a problem. A boat crossing a river, a plane flying in wind, a ball thrown from a moving vehicle — all these are most naturally analyzed by choosing one frame for each component of motion, computing in that frame, then transforming back. The common error is mixing frames: treating part of the velocity as if it belongs to one frame and part to another. The fix is always to be explicit about *which frame* each velocity vector is measured in before applying the addition rule. As you build toward non-inertial frames, you will see what happens when the frame itself accelerates — that is when the equivalence between frames breaks down and fictitious forces like the Coriolis effect and centrifugal force appear.

