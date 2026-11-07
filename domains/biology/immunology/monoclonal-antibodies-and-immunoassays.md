---
id: monoclonal-antibodies-and-immunoassays
title: Monoclonal Antibodies and Immunoassays
domain: biology
course: immunology
prerequisites:
- id: adaptive-immunity-overview
  type: hard
- id: antibody-structure-and-function
  type: soft
- id: plasma-cells-and-antibody-secretion
  type: soft
builds-toward:
- cancer-immunotherapy-approaches
tags:
- monoclonal-antibodies
- hybridoma
- ELISA
- flow-cytometry
- immunoassays
- therapeutic-antibodies
stage: advanced
status: validated
---

# Monoclonal Antibodies and Immunoassays

## Core Idea
A monoclonal antibody is a single kind of antibody, made by one clone of B-cell-derived cells, that binds one epitope on one antigen. Georges Köhler and César Milstein made the first monoclonal antibodies in 1975 by fusing antibody-producing B cells with immortal myeloma cells to create hybridomas. Because they are uniform and highly specific, monoclonal antibodies are used as detection tools in immunoassays such as ELISA, flow cytometry and rapid tests, and as drugs for cancer, autoimmune disease and infection. Engineering mouse antibodies into chimeric, humanized or fully human forms reduces immune reactions against the drug itself.

## How It's Best Learned
Walk through hybridoma production as a flowchart and ask at each step why the cells that are not wanted die. Then draw a sandwich ELISA layer by layer, from the plate to the colored product, and run the same logic on a home pregnancy test strip. Finish by decoding a few drug names ending in -mab.

## Common Misconceptions
- A monoclonal antibody binds several different parts of an antigen. (It binds a single epitope; a polyclonal antibody mixture from an immunized animal contains antibodies to many epitopes.)
- Mouse antibodies work equally well as drugs in people. (The human immune system recognizes mouse antibody regions as foreign and can make antibodies against them, which reduces effectiveness and can cause reactions.)
- An ELISA measures the antigen directly by its color. (The color comes from an enzyme linked to a detection antibody; the amount of color reflects how much antibody, and therefore antigen, was bound.)

## Questions

```yaml
- question: "In hybridoma production, B cells are fused with myeloma cells that lack the enzyme HGPRT, and the mixture is grown in HAT medium. Why do only hybrid cells survive?"
  type: multiple-choice
  options: ["HAT medium kills all B cells immediately", "Unfused myeloma cells cannot make nucleotides when aminopterin blocks the main pathway because they lack HGPRT, and unfused B cells die naturally in culture; hybrids get HGPRT from the B cell and immortality from the myeloma", "Hybrids are larger and are separated by filtering", "Myeloma cells produce the desired antibody on their own"]
  answer: 1
  explanation: "Aminopterin blocks de novo nucleotide synthesis. Cells can survive only by the salvage pathway, which needs HGPRT. Myeloma cells lack it and die. Normal B cells have it but stop dividing and die within days. Only fused cells have both the enzyme and the ability to divide indefinitely."
- question: "A monoclonal antibody preparation contains antibodies that recognize many different epitopes on the same protein."
  type: true-false
  answer: false
  explanation: "All antibodies in a monoclonal preparation come from one clone and have the same antigen-binding site, so they bind one epitope. Mixtures that recognize many epitopes are polyclonal."
- question: "Why are therapeutic antibodies such as trastuzumab humanized rather than given as pure mouse antibodies?"
  type: short-answer
  answer: "Patients' immune systems recognize mouse antibody regions as foreign and make anti-mouse antibodies, which clear the drug faster and can cause allergic reactions. Humanizing replaces most mouse sequence with human sequence while keeping the parts that bind the target, so the drug is less immunogenic."
  explanation: "Under the naming convention used for most approved antibodies, -ximab marked chimeric antibodies (mouse variable regions, human constant regions), -zumab humanized antibodies and -umab fully human ones. Rituximab, trastuzumab and adalimumab are examples of each."
- question: "In a sandwich ELISA, what is the role of the second (detection) antibody?"
  type: multiple-choice
  options: ["It coats the plate and captures the antigen", "It binds a different epitope on the captured antigen and carries an enzyme that produces a measurable color", "It destroys unbound antigen", "It blocks the enzyme reaction"]
  answer: 1
  explanation: "The capture antibody on the plate binds the antigen. The detection antibody, linked to an enzyme, binds a second epitope. After washing, a substrate is added, and the enzyme converts it into a colored product. More antigen means more bound detection antibody and more color."
```

## Explainer
When an animal is immunized, many B-cell clones respond, each making antibodies against a different part of the antigen. The resulting serum is polyclonal, a mixture that varies from animal to animal. A single, defined antibody is often more useful, but a B cell making one antibody dies after a short time in culture.

In 1975 Georges Köhler and César Milstein solved this. They immunized a mouse, collected B cells from its spleen, and fused them with myeloma cells, cancerous plasma cells that divide indefinitely. The myeloma cells lacked the enzyme HGPRT. Later work used myeloma lines that also make no antibody of their own, so each hybrid secretes only the B cell's antibody. The cells were then grown in HAT medium, which contains hypoxanthine, aminopterin and thymidine. Aminopterin blocks the cell's main route to making nucleotides, leaving only a salvage route that needs HGPRT. Unfused myeloma cells die. Unfused B cells die on their own. Only hybrid cells, called hybridomas, survive, with HGPRT from the B cell and immortality from the myeloma. Researchers then screen the hybridomas, pick one that makes the desired antibody, and grow it as a clone. Köhler and Milstein shared the 1984 Nobel Prize in Physiology or Medicine with Niels Jerne.

Monoclonal antibodies became standard laboratory tools. In an ELISA (enzyme-linked immunosorbent assay), an antibody or antigen is attached to a plastic plate. In a sandwich ELISA, a capture antibody holds the antigen, and an enzyme-linked detection antibody binds a second site. A substrate turns colored where the enzyme is present, and the color intensity measures the antigen. Lateral-flow strips, used in home pregnancy tests and rapid antigen tests, apply the same sandwich idea along a paper strip, with colored particles in place of an enzyme. In flow cytometry, cells tagged with fluorescent antibodies stream past a laser one at a time, so researchers can count, for example, the CD4 T cells in a blood sample.

Monoclonal antibodies are also drugs. Mouse antibodies, however, provoke an immune response in people. Genetic engineering produced chimeric antibodies, with mouse variable regions and human constant regions, then humanized antibodies, in which only the antigen-binding loops are from the mouse, and finally fully human antibodies. Rituximab, a chimeric antibody against CD20 on B cells, treats some lymphomas. Trastuzumab, a humanized antibody against HER2, treats HER2-positive breast cancer. Adalimumab, a fully human antibody against the cytokine TNF, treats rheumatoid arthritis and other inflammatory diseases.
