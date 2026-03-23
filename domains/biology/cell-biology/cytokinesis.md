---
id: cytokinesis
title: Cytokinesis
domain: biology
course: cell-biology
prerequisites:
- id: mitosis
  type: hard
- id: cell-membrane-structure
  type: soft
builds-toward:
- meiosis
tags:
- cytokinesis
- cleavage-furrow
- cell-plate
- division
- animal-plant
stage: formal-systems
status: validated
---

# Cytokinesis

## Core Idea
Cytokinesis is the physical division of the cytoplasm that follows mitosis (or meiosis), producing two separate daughter cells. In animal cells, a contractile ring of actin filaments forms a cleavage furrow that pinches the cell in two. In plant cells, a cell plate forms between the daughter nuclei and expands outward to form new cell walls, because the rigid cell wall prevents pinching. Cytokinesis is distinct from mitosis: nuclear division (mitosis) can occur without cytokinesis, producing multinucleate cells (syncytia).

## How It's Best Learned
Compare animal vs. plant cytokinesis side-by-side: mechanism, direction of division (inward furrow vs. outward plate), and structural materials used. Consider why plants cannot use a cleavage furrow (cell wall rigidity).

## Common Misconceptions
- Cytokinesis is not part of mitosis; it is a separate subsequent process. Mitosis ends at telophase.
- Failure of cytokinesis (but not mitosis) results in multinucleate cells, not polyploidy — the latter requires failure of spindle assembly.

## Questions

```yaml
- question: "Why can't plant cells complete cytokinesis using the same cleavage furrow mechanism that animal cells use?"
  type: multiple-choice
  options:
    - "Plant cells lack actin and myosin filaments needed to form a contractile ring"
    - "The rigid cell wall surrounding the plant cell prevents inward pinching of the membrane"
    - "Plant cells complete nuclear division differently, so a different cytoplasmic division mechanism is also required"
    - "The plant plasma membrane is too thick to deform under contractile ring tension"
  answer: 1
  explanation: "The cleavage furrow works by constricting the flexible plasma membrane inward. A rigid cell wall cannot deform this way — it would be like trying to pinch a wooden box closed. Instead, plant cells build a new wall from the center outward (the cell plate) using Golgi-derived vesicles guided along microtubules. Plant cells do have actin, but the structural constraint of the cell wall — not the absence of contractile machinery — is the reason for the different mechanism."

- question: "A researcher treats dividing animal cells with a drug that specifically inhibits formation of the contractile actin ring while leaving the mitotic spindle intact. What is the most likely outcome after the drug is applied?"
  type: multiple-choice
  options:
    - "Cells arrest in metaphase because the spindle cannot function without an intact actin ring"
    - "Cells produce daughter cells that each contain only half the normal chromosome number"
    - "Cells complete mitosis but fail to divide, producing binucleate cells with two complete chromosome sets"
    - "Cells undergo apoptosis immediately because cytokinesis failure is lethal"
  answer: 2
  explanation: "The actin contractile ring drives the cleavage furrow in animal cytokinesis. Without it, the mitotic spindle can still segregate chromosomes normally (completing mitosis through telophase), but the cell body cannot divide. The result is a binucleate cell — one cell with two nuclei, each containing a complete chromosome set. This is not the same as polyploidy, which would require failure at a different step (spindle assembly)."

- question: "Cytokinesis is the final phase of mitosis."
  type: true-false
  answer: false
  explanation: "Cytokinesis is a separate process that follows mitosis — it is not part of mitosis. Mitosis ends at telophase, when the two daughter nuclei have reformed and the chromosomes have decondensed. Cytokinesis, which divides the cytoplasm and cell body, typically begins during anaphase or telophase but is mechanistically independent. The distinction matters because nuclear division and cytoplasmic division can be uncoupled: mitosis without cytokinesis produces multinucleate cells."

- question: "In plant cytokinesis, the cell plate grows outward from the center of the cell toward the existing cell walls, eventually fusing with them to create two separate cells."
  type: true-false
  answer: true
  explanation: "This centrifugal (inside-out) mechanism is the defining feature of plant cytokinesis. Golgi-derived vesicles carrying cell wall materials and new membrane are transported along remnant spindle microtubules to the cell's equator, where they fuse and expand outward. This is the opposite of animal cytokinesis, which works centripetally (outside-in) via cleavage furrow constriction. Both strategies achieve the same result — two cells with complete membranes and genetic content — but through structurally opposite routes."

- question: "Explain why plant and animal cells use fundamentally different mechanisms for cytokinesis, and describe what structural property of each cell type determines which mechanism is used."
  type: short-answer
  answer: "Animal cells have flexible plasma membranes that can be constricted inward by an actin-myosin contractile ring — the cleavage furrow pinches the cell like a drawstring closing a bag. Plant cells are surrounded by a rigid cell wall that cannot be deformed this way. Instead, plant cells build new membrane and cell wall material from the inside out, using Golgi-derived vesicles transported to the center of the cell where they fuse to form the cell plate, which then expands outward to the existing walls."
  explanation: "This is a case where one structural feature (cell wall rigidity) dictates an entirely different molecular strategy. The plant cell plate and animal cleavage furrow are not homologous mechanisms that evolved separately — they reflect genuinely different engineering solutions to the same problem imposed by different cellular architectures. Both mechanisms ultimately rely on directed membrane trafficking and cytoskeletal organization, but the directionality (inside-out vs. outside-in) is opposite."
```

## Explainer

You have just studied mitosis — the process by which the cell divides its duplicated chromosomes into two identical sets, each enclosed in its own nuclear envelope by the end of telophase. But at the end of mitosis, you still have one cell with two nuclei. **Cytokinesis** is the physical act of splitting that single cell into two separate daughter cells, each with its own nucleus, cytoplasm, and organelles. It typically begins during anaphase or telophase and completes shortly after mitosis ends.

In **animal cells**, cytokinesis works by constriction from the outside in. A ring of **actin** and **myosin II** filaments assembles just beneath the plasma membrane at the cell's equator, positioned by signals from the mitotic spindle (specifically, the central spindle and astral microtubules, which define the division plane). This **contractile ring** functions like a drawstring on a bag: myosin II motor proteins slide along the actin filaments, generating force that progressively pinches the membrane inward, creating a visible indentation called the **cleavage furrow**. The furrow deepens until the cell is connected by only a thin bridge (the midbody), which is then severed in a final step called **abscission**. The entire process depends on the cell membrane being flexible enough to deform — a property that comes from its fluid phospholipid bilayer structure, which you studied as a prerequisite.

**Plant cells** face a fundamentally different engineering problem: they are surrounded by a rigid cell wall that cannot be pinched inward. Instead of constricting from the outside, plant cytokinesis builds a new wall from the inside out. Vesicles derived from the Golgi apparatus, carrying cell wall materials (pectins, hemicelluloses) and new membrane, are transported along remnant spindle microtubules to the center of the cell, where they fuse to form the **cell plate**. The cell plate expands outward toward the existing cell walls, eventually fusing with them to create a complete septum that divides the cell in two. Each side of the cell plate becomes the new plasma membrane for its respective daughter cell, and the material between them matures into the new cell wall.

An important conceptual point is that cytokinesis and mitosis are mechanistically independent. Mitosis divides the genome; cytokinesis divides the cell body. If cytokinesis fails while mitosis succeeds, the result is a single cell with two (or more) nuclei — a **syncytium** or multinucleate cell. This is not always pathological: skeletal muscle fibers are multinucleate syncytia formed by the intentional fusion (not failed division) of myoblasts, and some fungi grow as coenocytic hyphae with many nuclei sharing one continuous cytoplasm. Understanding that nuclear division and cytoplasmic division are separable processes clarifies many phenomena in both normal development and disease.
