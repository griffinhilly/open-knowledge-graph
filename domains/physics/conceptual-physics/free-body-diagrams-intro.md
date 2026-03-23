---
id: free-body-diagrams-intro
title: Introduction to Free-Body Diagrams
domain: physics
course: conceptual-physics
prerequisites:
- id: newtons-second-law-conceptual
  type: hard
- id: newtons-third-law-conceptual
  type: soft
- id: balanced-and-unbalanced-forces
  type: hard
builds-toward:
- free-body-diagrams
tags:
- free-body-diagram
- forces
- analysis
stage: abstract-reasoning
status: validated
---
# Introduction to Free-Body Diagrams

## Core Idea
A free-body diagram (FBD) is a simple sketch that shows a single object and all the forces acting on it, drawn as arrows. Each arrow points in the direction of the force, and its length represents the force's strength. Free-body diagrams help you organize force information so you can apply Newton's laws to predict whether an object will accelerate and in which direction.

## How It's Best Learned
Start by drawing FBDs for simple situations: a book on a table, a ball in free fall, a box being pushed across the floor. Label every force (gravity, normal, friction, applied). Practice identifying which forces are balanced and which are not, then connect your diagram to Newton's Second Law.

## Common Misconceptions
- You should include forces that the object exerts on other things. (A free-body diagram only shows forces acting ON the object, not forces the object exerts on others.)
- There must always be a force in the direction of motion. (An object can move in a direction even if no force points that way — think of a ball continuing to roll after the push stops.)
- The normal force is always equal to the weight. (This is only true on flat, horizontal surfaces with no extra vertical forces. On a ramp, the normal force is less than the weight.)
- Heavier objects always have more forces drawn on them. (The number of forces depends on the situation, not the object's weight. A falling ball has just one force — gravity.)

## Questions

```yaml
- question: "A box sits on a flat table with no one touching it. How many forces should appear on its free-body diagram?"
  type: multiple-choice
  options: ["One — gravity only", "Two — gravity pulling down and the normal force pushing up", "Three — gravity, normal force, and friction", "Zero — it is not moving"]
  answer: 1
  explanation: "Gravity pulls the box downward and the table's normal force pushes it upward. Since the box is not being pushed sideways and is not moving, there is no friction force. Two forces, balanced."

- question: "In a free-body diagram, the arrow for a stronger force should be drawn longer than the arrow for a weaker force."
  type: true-false
  answer: true
  explanation: "Arrow length in a free-body diagram represents the magnitude (strength) of the force. A longer arrow indicates a greater force."

- question: "Why should a free-body diagram only include forces acting on the object, not forces the object exerts?"
  type: short-answer
  answer: "Because Newton's Second Law (F = ma) uses the net force on the object to determine its acceleration. Forces the object exerts on other things affect those other objects, not this one."
  explanation: "A free-body diagram isolates one object so you can sum the forces on it and apply Newton's Second Law. Including forces it exerts on others would mix up the analysis."
```

## Explainer
Physics problems often involve multiple forces pulling and pushing an object in different directions. Trying to keep track of all of them in your head is like trying to track every player on a basketball court without watching the screen — you need a visual tool. That tool is the **free-body diagram**, or FBD.

To draw one, you start by representing the object as a simple dot or box. Then you draw an arrow for every force acting ON that object. Each arrow starts at the object, points in the direction the force pushes or pulls, and has a length proportional to the force's strength. You label each arrow with the type of force: **gravity** (Fg, pointing down), **normal force** (FN, perpendicular to the surface), **friction** (Ff, opposing the direction of sliding), **applied force** (Fa, in whatever direction you are pushing), **tension** (FT, along a rope or string), and so on.

The key rule is that you only draw forces acting on the chosen object. If you are analyzing a box on a table, you draw the table's normal force pushing up on the box, but you do not draw the box's weight pushing down on the table — that force acts on the table, not on the box. Mixing up which forces belong to which object is the most common mistake in force analysis.

Once your diagram is complete, you look at whether the forces are **balanced** (equal in all directions, meaning no acceleration) or **unbalanced** (a net force exists, meaning the object accelerates in the direction of the net force). You can add up all the forces pointing in each direction: if the upward forces equal the downward forces and the leftward forces equal the rightward forces, the object is in equilibrium. If not, the difference tells you the net force, and Newton's Second Law tells you the resulting acceleration.

Free-body diagrams are the single most useful problem-solving tool in mechanics. Professional engineers use them to design bridges, roller coasters, and spacecraft. Getting comfortable drawing and reading them now will make every force problem you encounter easier to solve.
