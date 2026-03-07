# Open Knowledge Graph Memory

## Status
- Created Mar 7, 2026
- 372 math topics across 9 courses, 732 prerequisite edges
- All tooling (validate, visualize, stats) working
- Zero validation errors, 357 warnings (expected — dangling forward refs)

## Known Issues
- 16 dangling prerequisite references: IDs used by one agent don't match IDs created by another (e.g., `solving-linear-equations` vs `solving-multi-step-equations`). Need a normalization pass.
- 5 upper math courses empty: linear-algebra, multivariable-calculus, methods-of-proof, probability-and-statistics, discrete-math
- builds-toward consistency warnings: many topics reference forward targets that don't list them as prerequisites. Informational, not blocking.
- All 372 topics at status: draft. Need human review to move to validated.

## Decisions
- **Format**: Markdown + YAML frontmatter (one file per topic). Human-readable AND machine-parseable.
- **Granularity**: Math Academy-level (fine-grained, one topic per distinct concept/skill)
- **ID uniqueness**: Global across all domains. Disambiguate with prefixes if needed (e.g., `arc-length-circles` vs `arc-length` in calculus).
- **License**: CC BY-SA 4.0 for content, MIT for tools
- **No Agencyism content**: Removed to keep project domain-neutral and maximize contributor appeal
- **Course organization**: Traditional US math track (not integrated). Integrated pathway is a different traversal of the same graph.
