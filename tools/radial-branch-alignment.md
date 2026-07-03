# Radial Branch Alignment

For radial integration, each domain's left-right branch axis must be oriented
so the "left" side faces the more-related angular neighbor.

Radial order (clockwise): Math → Formal Sciences → Philosophy → CS → Engineering →
Physics → Earth & Space → Chemistry → Biology → Health → Psychology →
Social Sciences → Economics → Practical Life → History → Language →
Literature → Arts → Music → (back to Math)

## Per-Domain Alignment

| Domain | Branch Axis (left→right) | CCW Neighbor | CW Neighbor | Left faces | Flip? |
|--------|--------------------------|-------------|-------------|------------|-------|
| Mathematics | discrete/structure → analysis/continuous | Music | Formal Sci | Formal Sci (discrete/logic) → CW | No |
| Formal Sciences | foundational → abstract | Math | Philosophy | Math (foundational) → CCW | Yes |
| Philosophy | formal/logical → applied/practical | Formal Sci | CS | Formal Sci (logical) → CCW | Yes |
| CS | theoretical → systems | Philosophy | Engineering | Philosophy (theoretical) → CCW | Yes |
| Engineering | theoretical → applied | CS | Physics | CS (theoretical) → CCW | Yes |
| Physics | theoretical → applied/phenom | Engineering | Earth & Space | Engineering (applied) → CCW | No? |
| Earth & Space | surface → deep space | Physics | Chemistry | Physics → CCW | No |
| Chemistry | physical/theoretical → analytical | Earth & Space | Biology | Biology (analytical/organic) → CW | No |
| Biology | molecular → ecological | Chemistry | Health | Chemistry (molecular) → CCW | Yes |
| Health | individual body → population | Biology | Psychology | Biology (body) → CCW | Yes |
| Psychology | biological → social | Health | Social Sci | Health (biological) → CCW, Social Sci (social) → CW | No |
| Social Sciences | individual → structural | Psychology | Economics | Psychology (individual) → CCW | Yes |
| Economics | micro → macro | Social Sci | Practical Life | Practical Life (personal finance) → CW | No |
| Practical Life | financial → digital | Economics | History | Economics (financial) → CCW | Yes |
| History | methods/ancient → modern | Practical Life | Language | Language (structure) → CW | No |
| Language | structure → performance | History | Literature | Literature (analysis) → CW | No |
| Literature | analysis → creative genres | Language | Arts | Arts (creative) → CW | No |
| Arts | foundations → applied | Literature | Music | Literature (analysis/foundations) → CCW, Music (creative) → CW | No |
| Music | theory/math → creative/performance | Arts | Math | Arts (creative) → CCW, Math (theory) → CW | Yes |

## Implementation

For each domain, store a `flip_x` boolean. When mapping norm_x to angular position:
- If flip_x=False: x=0 maps to CCW edge, x=1 maps to CW edge (default)
- If flip_x=True: x=0 maps to CW edge, x=1 maps to CCW edge (reversed)

```python
BRANCH_FLIP = {
    "mathematics": False,
    "formal-sciences-and-logic": True,
    "philosophy": True,
    "computer-science": True,
    "engineering": True,
    "physics": False,
    "earth-and-space-sciences": False,
    "chemistry": False,
    "biology": True,
    "health-and-human-development": True,
    "psychology": False,
    "social-sciences": True,
    "economics": False,
    "practical-life-skills": True,
    "history": False,
    "language-and-communication": False,
    "literature": False,
    "arts-and-aesthetics": False,
    "music": True,
}
```

NOTE: These are best guesses based on branch axis semantics and neighbor
relationships. Should be verified visually after initial radial integration.
