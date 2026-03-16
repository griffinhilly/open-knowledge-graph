---
id: bacterial-growth-and-reproduction
title: Bacterial Growth and Reproduction
domain: biology
course: microbiology
prerequisites:
  - id: bacterial-cell-structure
    type: hard
builds-toward:
  - microbial-fermentation
  - microbial-ecology-overview
tags: [binary-fission, growth-curve, lag-phase, log-phase, stationary-phase, doubling-time]
stage: abstract-reasoning
status: validated
---

# Bacterial Growth and Reproduction

## Core Idea
Bacteria reproduce asexually through binary fission — a single cell duplicates its DNA, elongates, and divides into two genetically identical daughter cells. Population growth follows a predictable four-phase curve: the lag phase (adaptation, no division), the log (exponential) phase (rapid, constant-rate division), the stationary phase (growth rate equals death rate as nutrients deplete), and the death phase (cells die faster than they divide). Doubling time — the time required for a population to double — varies enormously by species and conditions, from ~20 minutes for E. coli under ideal lab conditions to days or weeks for slow-growing species like Mycobacterium tuberculosis.

## How It's Best Learned
Plot actual growth data on both linear and semi-log graphs so students can see why the log phase appears as a straight line on a semi-log plot. Have students calculate doubling time from real datasets using the formula t_d = t × ln(2) / ln(N_t / N_0). Connect each growth phase to what's happening at the cellular level — why do cells "lag" before dividing? What resource limits trigger the stationary phase? Lab exercises growing bacteria on agar plates and counting colonies at intervals make the abstract curve tangible.

## Common Misconceptions
- Thinking binary fission is the same as mitosis — fission is simpler, with no spindle apparatus or defined chromosome condensation.
- Assuming bacteria always grow exponentially — real populations hit resource limits and enter stationary or death phases.
- Confusing generation time with the time for a single cell to divide — generation time is a population-level average.
- Believing the lag phase means nothing is happening — cells are actively synthesizing enzymes and adapting to the medium.

## Explainer

From your understanding of bacterial cell structure, you know that a bacterium is a self-contained unit with a chromosome, ribosomes, a cell membrane, and usually a cell wall. **Binary fission** is the process by which this single cell becomes two. The cell replicates its circular chromosome starting from a single origin of replication, and the two copies attach to different points on the cell membrane. As the cell elongates, the chromosomes are passively separated. A septum of new cell wall and membrane material grows inward at the cell's midpoint, eventually pinching the cell into two daughter cells. Unlike eukaryotic mitosis, there is no mitotic spindle, no nuclear envelope breakdown, and no condensed chromosomes — fission is a simpler, faster process that allows bacteria to divide with remarkable speed.

When you place bacteria into fresh growth medium and track population size over time, you observe the characteristic **bacterial growth curve** with four phases. During the **lag phase**, cells are not dividing — but they are far from idle. They are sensing their new environment, activating genes for metabolizing available nutrients, synthesizing the enzymes and ribosomes they will need, and repairing any damage accumulated during storage. The length of the lag phase depends on how different the new conditions are from the old; cells transferred to identical fresh medium may have almost no lag, while cells moved from a glucose-rich to a lactose-only medium must first induce the lac operon before growth can begin.

Once the cells are metabolically prepared, they enter the **log phase** (also called exponential phase), where each cell divides at a constant rate, and population size doubles at regular intervals. The **doubling time** (or generation time) is the key parameter: *E. coli* in rich media at 37°C doubles roughly every 20 minutes, meaning one cell becomes over a billion in about 10 hours. On a standard linear graph, exponential growth produces a steeply curving upward line that becomes nearly vertical, which is why microbiologists often plot growth on a semi-logarithmic scale — the log phase appears as a clean straight line, making doubling time easy to calculate from the slope.

Exponential growth cannot continue indefinitely. As nutrients deplete, waste products accumulate, and physical space becomes limiting, the growth rate slows until it matches the death rate — this is the **stationary phase**. The total population holds roughly constant, but it is not a static state: cells are still dividing and dying at equal rates, and many species activate stress-response genes, form biofilms, or begin sporulation during this phase. Eventually, conditions deteriorate further and cells die faster than they divide, entering the **death phase**. Understanding these phases matters practically: antibiotics like penicillin target actively dividing cells and are most effective during log phase, while stationary-phase bacteria are often more resistant to treatment, which is one reason chronic infections can be so difficult to clear.
