---
id: topographic-maps
title: Reading Topographic Maps
domain: earth-and-space-sciences
course: earth-science
prerequisites:
- id: mountains-valleys-and-plains
  type: soft
- id: scale-drawings-and-maps
  type: soft
- id: spatial-representation-maps
  type: soft
builds-toward: []
tags:
- maps
- contour-lines
- elevation
- gradient
- landforms
- map-skills
stage: abstract-reasoning
status: validated
---

# Reading Topographic Maps

## Core Idea
A topographic map shows the shape of the land on a flat sheet by using contour lines, which connect points of equal elevation. The contour interval is the change in elevation between neighboring lines. Lines that are close together show steep slopes, and lines that are far apart show gentle slopes. With a few rules, a reader can find hills, valleys, depressions, and the direction streams flow, and can calculate how steep the land is.

## How It's Best Learned
Build a clay hill in a clear container, add water in equal depth steps, and trace each waterline from above onto plastic; the tracings become a contour map. Then have students practice on real maps, such as U.S. Geological Survey quadrangles, by finding the highest point, the steepest slope, and which way a stream flows. Finish by drawing a profile, a side view of the land along a line across the map.

## Common Misconceptions
- Contour lines show roads or trails. (They are imaginary lines of equal elevation; roads and trails use different symbols.)
- Contour lines that are close together mean the land is high. (Close spacing means the land is steep; height is read from the labeled elevations.)
- A V-shaped bend in a contour line points downstream. (Where contours cross a stream, the V points upstream, toward higher ground.)

## Questions

```yaml
- question: "On a topographic map, where is the land steepest?"
  type: multiple-choice
  options:
    - "Where the contour lines are farthest apart"
    - "Where the contour lines are closest together"
    - "Where the contour lines form a closed circle"
    - "Where the contour lines have the highest labels"
  answer: 1
  explanation: "Each line marks the same change in elevation. When lines are packed tightly, the land rises a lot over a short horizontal distance, which means a steep slope."

- question: "A map has a contour interval of 20 m. Point A is on the 340 m contour, and point B is on the 420 m contour. The two points are 2 km apart. What is the average gradient between them?"
  type: short-answer
  answer: "The elevation difference is 420 − 340 = 80 m. Gradient = 80 m ÷ 2 km = 40 m per km."
  explanation: "Gradient is the change in elevation divided by the horizontal distance. Map units must be stated clearly; here the answer is 40 meters of rise per kilometer."

- question: "Where a contour line crosses a stream, it bends into a V that points upstream."
  type: true-false
  answer: true
  explanation: "A stream sits in a valley. Following one elevation line toward the stream, you must go up the valley to stay at the same height, so the line bends in a V that points uphill, toward where the stream comes from."

- question: "A set of closed contour loops has short tick marks (hachures) on the inside of the innermost loop. What does this show?"
  type: multiple-choice
  options:
    - "A hilltop"
    - "A depression, such as a crater or sinkhole"
    - "A lake"
    - "A cliff"
  answer: 1
  explanation: "Plain closed loops show a hill. Hachure marks pointing inward show that the land goes down inside the loop, which is a depression."
```

## Explainer
Imagine slicing a hill with a set of flat, evenly spaced cuts, like a loaf of bread laid on its side. Each cut makes an outline at one exact height. If you look down on all the outlines from above and draw them on paper, you have a **topographic map**.

Each line on the map is a **contour line**. Every point on one contour line has the same elevation, usually measured above sea level. The **contour interval** is the difference in elevation between neighboring lines, such as 10 meters or 20 feet. To make maps easier to read, every fifth line is usually darker and labeled with its elevation. These are called **index contours**.

A few rules let you read the land.

- **Spacing shows steepness.** Lines close together mean a steep slope. Lines far apart mean gentle or flat ground.
- **Closed loops show hills.** The smallest closed loop marks the top. If the loop has small tick marks, called hachures, pointing inward, it shows a depression instead.
- **Lines do not cross.** A point on the ground has only one elevation. At a vertical cliff, lines can run together, and only a rare overhanging cliff makes them cross.
- **Lines bend upstream.** Where contours cross a stream, they form a V that points uphill. This tells you which way the water flows: away from the point of the V.

You can also measure. The **map scale** relates distance on the map to distance on the ground. A scale of 1:24,000 means 1 centimeter on the map equals 24,000 centimeters, or 240 meters, on the ground. To find the **gradient**, or steepness, divide the change in elevation by the horizontal distance. If a trail climbs from 300 meters to 500 meters over 4 kilometers, the gradient is 200 m ÷ 4 km = 50 m per km.

A **profile** shows the land from the side. Draw a straight line across the map, mark where it crosses each contour, and plot those elevations on a graph. The result is a side view of the hills and valleys along that line.

Hikers, engineers, and geologists use these maps to plan routes, choose building sites, and study how water shapes the land. Today the same information is often stored as digital elevation data, but the rules for reading contours remain the same.
