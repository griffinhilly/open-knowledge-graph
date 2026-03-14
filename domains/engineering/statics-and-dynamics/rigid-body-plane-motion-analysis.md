---
id: rigid-body-plane-motion-analysis
title: General Plane Motion of Rigid Bodies
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: rigid-body-kinematics-general-motion
  type: hard
- id: rotation-fixed-axis-dynamics
  type: hard
builds-toward:
- instantaneous-center-of-rotation-method
tags:
- plane-motion
- translation
- rotation
- general
stage: formal-systems
status: draft
---

# General Plane Motion of Rigid Bodies

## Core Idea
General plane motion combines translation of the center of mass and rotation about the center of mass. The velocity of any point is v = v_cm + ω × r. Kinetic energy is KE = ½m v_cm² + ½I_cm ω². The equations of motion are ΣF = m a_cm and ΣM_cm = I_cm α, which decouple translation and rotation.
