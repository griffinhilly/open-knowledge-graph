---
id: newman-projections-eclipsing
title: Newman Projections and Eclipsing Interactions
domain: chemistry
course: organic-chemistry
prerequisites:
- id: conformational-analysis-alkanes
  type: hard
builds-toward:
- ring-strain-and-stability
tags:
- visualization
- eclipsing
- torsional-strain
- notation
stage: formal-systems
status: draft
---

# Newman Projections and Eclipsing Interactions

## Core Idea
A Newman projection is a diagram viewed along a C-C bond showing the three groups attached to the front atom and the three attached to the back atom. Eclipsing occurs when bonds on the front and back atoms align directly—these conformations are high-energy due to electron pair repulsion. Staggered conformations (bonds offset by 60°) are lower energy.

## Explainer

You already know from conformational analysis that rotation around C–C single bonds is not completely free — some rotational positions (conformations) are more stable than others. The **Newman projection** is a visualization tool that makes these energy differences immediately obvious by looking straight down the bond axis. Imagine grabbing a molecular model of ethane and staring directly into the C–C bond from one end. The front carbon appears as a dot (the intersection point) with three bonds radiating outward. The back carbon, hidden behind the front one, appears as a circle with three bonds radiating from its edge. This is a Newman projection.

The power of this notation is that the **dihedral angle** — the angle between a bond on the front carbon and a bond on the back carbon — is displayed directly. When bonds on the front and back atoms point in the same direction (dihedral angle = 0°), the conformation is **eclipsed**. You can see this instantly in the Newman projection because the front and back bonds overlap visually. When bonds are offset by 60°, the conformation is **staggered**, and all six bonds are evenly spaced around the projection. The eclipsed conformation is higher in energy than the staggered conformation by about 12 kJ/mol for ethane — this energy cost is called **torsional strain**, arising primarily from the repulsion between the electron clouds of the aligned bonds.

For ethane, all staggered conformations are equivalent and all eclipsed conformations are equivalent. But for butane (looking down the C2–C3 bond), the story becomes richer. The staggered conformation where the two methyl groups are 180° apart is called **anti** — this is the global energy minimum because the large groups are as far apart as possible. The staggered conformation where the methyls are 60° apart is called **gauche** — still a minimum, but higher in energy due to **steric strain** (the methyls are close enough that their electron clouds repel). The eclipsed conformations are energy maxima: the highest is the **syn-periplanar** eclipsed form where the two methyls are directly aligned at 0°, combining torsional strain with severe steric clash.

Learning to read Newman projections fluently is essential because they are the standard way to analyze conformational preferences, predict reaction stereochemistry (E2 eliminations require anti-periplanar geometry, which you can only see clearly in a Newman projection), and understand ring conformations when you study cyclohexane. Practice by building molecular models, rotating them into the Newman view, and drawing what you see. Once the translation between 3D structure and Newman projection becomes automatic, every conformational analysis problem becomes dramatically easier.
