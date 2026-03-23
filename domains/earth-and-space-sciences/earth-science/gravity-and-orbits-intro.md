---
id: gravity-and-orbits-intro
title: Introduction to Gravity and Orbits
domain: earth-and-space-sciences
course: earth-science
prerequisites:
- id: planets-in-our-solar-system
  type: hard
- id: inner-vs-outer-planets
  type: soft
builds-toward:
- kepler-laws-planetary-orbits
- two-body-orbital-problem
tags:
- gravity
- orbits
- solar-system
- newton
- falling
stage: abstract-reasoning
status: validated
---

# Introduction to Gravity and Orbits

## Core Idea
Gravity is the force of attraction between any two objects with mass. The more massive the objects and the closer they are, the stronger the gravitational pull. Earth's gravity keeps us on the ground, keeps the Moon in orbit, and keeps the atmosphere from drifting away. The Sun's gravity holds the entire solar system together. An orbit happens when an object moves fast enough sideways that it keeps falling toward the central body but keeps missing it — essentially, it is falling around it. The Moon is constantly falling toward Earth, but its sideways speed means it curves around instead of crashing in. This balance between forward motion and gravitational pull is what makes orbits possible.

## How It's Best Learned
Use a ball on a string (whirl it in a circle) to demonstrate how the inward pull (string tension, representing gravity) and the ball's sideways motion combine to create an orbit — release the string and the ball flies off in a straight line, showing that without gravity the object would not curve. Drop a ball to show gravity pulling straight down, then throw it sideways to show it follows a curved path — an orbit is just that curve continued all the way around. Newton's famous thought experiment of a cannon on a mountaintop is an excellent mental model: fire it slowly and it falls to the ground nearby; fire it faster and it lands farther away; fire it fast enough and it curves all the way around the Earth.

## Common Misconceptions
- There is no gravity in space. Gravity exists everywhere — it just gets weaker with distance. Astronauts on the space station are in free fall (orbiting), not in zero gravity. They experience weightlessness because they and the station are falling together.
- The Moon stays in orbit because it is "balanced" between Earth's and Sun's gravity. The Moon orbits Earth because of Earth's gravity alone (the Sun's gravity affects the Moon too, but Earth's dominates its orbital behavior). There is no balancing act.
- Heavier objects fall faster than lighter objects. In a vacuum, all objects fall at the same rate regardless of mass. A feather and a bowling ball dropped on the Moon (no air resistance) hit the ground at the same time.

## Questions

```yaml
- question: "What keeps the Moon in orbit around Earth instead of flying off into space or crashing into Earth?"
  type: multiple-choice
  options:
    - "There is no gravity in space, so the Moon just floats in place"
    - "The Moon is balanced between the pull of Earth and the push of the Sun"
    - "The Moon is moving sideways fast enough that as gravity pulls it toward Earth, it curves around rather than hitting it — it is continuously falling and missing"
    - "Earth's magnetic field holds the Moon in place"
  answer: 2
  explanation: "An orbit is a continuous free fall. The Moon has sideways velocity that would carry it in a straight line into space if there were no gravity. Earth's gravity constantly pulls the Moon toward it. The combination of sideways motion and inward pull produces a curved path — the Moon keeps falling toward Earth but keeps missing because of its sideways speed. This is the fundamental mechanism of all orbits."

- question: "Astronauts on the International Space Station float because there is no gravity in space."
  type: true-false
  answer: false
  explanation: "At the altitude of the ISS (about 400 km), Earth's gravity is still about 90% as strong as at the surface. The astronauts float because they and the station are in free fall — orbiting Earth together, falling toward it at the same rate. They experience weightlessness for the same reason you feel weightless at the top of a roller coaster drop — you are in free fall, and your body and your surroundings are falling together."

- question: "Why do planets farther from the Sun orbit more slowly?"
  type: short-answer
  answer: "Gravity gets weaker with distance, so the Sun pulls less strongly on distant planets. A weaker pull means the planet needs less sideways speed to maintain its orbit. Additionally, distant planets have longer orbital paths (larger circumferences) to travel. The combination of lower speed and longer path means distant planets take much longer to complete one orbit — Neptune takes 165 Earth years while Mercury takes only 88 days."
  explanation: "This relationship was first described mathematically by Johannes Kepler: the square of a planet's orbital period is proportional to the cube of its distance from the Sun. It follows directly from Newton's law of gravity and explains the precise pattern of planetary orbital periods in our solar system."
```

## Explainer
**Gravity** is perhaps the most familiar force in the universe — you experience it every second of every day — yet it is also one of the most commonly misunderstood. Let us clear up what gravity really is and how it creates orbits.

Every object with mass attracts every other object with mass. You are gravitationally attracted to your desk, your phone, and the person sitting next to you. The reason you do not notice these attractions is that the force depends on mass: gravity between everyday objects is unmeasurably tiny. It takes something as massive as Earth (6 trillion trillion kilograms) to produce a gravitational pull you can feel. This is the force that holds you on the ground, keeps the atmosphere from dispersing into space, and makes dropped objects fall.

Gravity also gets weaker with distance — specifically, it decreases with the square of the distance. Double the distance, and the force drops to one-quarter. This is why the Sun's gravitational pull on distant Neptune is much weaker than on nearby Mercury. But gravity never drops to zero. Even in deep space, far from any star, there is always some gravitational pull from something.

Now, **orbits**. An orbit seems magical — something moving around and around without ever stopping or falling. But an orbit is actually just a special case of falling. Imagine you are on a tall mountain and throw a ball horizontally. Gravity pulls it down, and it hits the ground some distance away. Throw it faster, and it goes farther before landing — the ground curves away beneath it as it flies. Throw it fast enough, and something remarkable happens: **the ground curves away as fast as the ball falls**. The ball keeps falling toward Earth but keeps missing because Earth's surface curves away beneath it. It falls forever in a circle. That is an orbit.

This is exactly what the Moon is doing. It has enormous sideways velocity (about 1 km per second) that would carry it in a straight line off into space if Earth's gravity were not pulling it inward. Earth's gravity constantly curves the Moon's path, bending it into a nearly circular orbit. The Moon is falling toward Earth every single moment — but its sideways speed means it curves around rather than crashing in.

The same principle explains every orbit in the solar system. Earth orbits the Sun because it is falling toward the Sun but moving sideways fast enough to keep missing. Satellites orbit Earth for the same reason. Astronauts on the space station are not in "zero gravity" — gravity there is almost as strong as on the surface. They float because they and the station are **in free fall together**, falling around Earth at the same rate. Weightlessness is the feeling of free fall, not the absence of gravity.
