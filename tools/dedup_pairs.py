#!/usr/bin/env python3
"""Merge duplicate topic pairs: delete the weaker file, redirect references.

Usage:
    python tools/dedup_pairs.py --dry-run
    python tools/dedup_pairs.py --apply
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required.")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "domains"

# (delete_id, keep_id) — from duplicate analysis
# Round 4: Math dedup sweep (Mar 26, 2026)
# 87 pairs across all math courses — naming variants of same concepts
DEDUP_PAIRS = [
    # --- Linear Algebra (26 pairs) ---
    ("change-of-basis-matrices", "change-of-basis"),
    ("cross-product-3d", "cross-product"),
    ("dot-product-definition", "dot-product"),
    ("gaussian-elimination-method", "gaussian-elimination"),
    ("linear-transformation-definition", "linear-transformations"),
    ("linear-transformations-definition", "linear-transformations"),
    ("lu-decomposition-numerical", "lu-decomposition"),
    ("matrices-intro-linear-algebra", "matrices-definition"),
    ("matrix-addition-multiplication", "matrix-multiplication"),
    ("matrix-inverses-computation", "matrix-inverses"),
    ("matrix-representation-linear-map", "linear-transformation-matrix-representation"),
    ("matrix-representation-linear-transformations", "linear-transformation-matrix-representation"),
    ("matrix-transpose-properties", "matrix-transpose"),
    ("orthogonality-and-orthonormal-sets", "orthogonal-vectors-orthonormal-bases"),
    ("rank-and-nullity-theorem", "rank-nullity-theorem"),
    ("row-echelon-form-rref", "row-echelon-form"),
    ("scalar-multiplication-vectors", "scalar-multiplication"),
    ("span-of-vectors", "span-and-basis"),
    ("span-spanning-set", "span-and-basis"),
    ("symmetric-matrices-properties", "symmetric-matrices"),
    ("vector-magnitude-norm", "vector-norms"),
    ("vector-norms-magnitude", "vector-norms"),
    ("vector-spaces-definition", "vector-spaces"),
    ("vector-subspaces", "subspaces"),
    ("vectors-in-rn-definition", "vectors-in-rn"),
    ("kernel-image-rank", "kernel-and-image"),
    # --- Differential Equations (15 pairs) ---
    ("autonomous-equations-phase-lines", "autonomous-equations"),
    ("bifurcation-analysis-ode", "bifurcation-in-odes"),
    ("damping-and-resonance", "resonance-and-damping"),
    ("eulers-method-ode", "eulers-method"),
    ("existence-and-uniqueness-theorems", "existence-uniqueness-ode"),
    ("laplace-transform-definition-and-properties", "laplace-transform-definition"),
    ("laplace-transform-derivatives", "laplace-transform-of-derivatives"),
    ("legendre-polynomials-and-equations", "legendre-equations"),
    ("linearization-nonlinear-systems", "linearization-of-nonlinear-systems"),
    ("phase-portraits-for-linear-systems", "phase-portraits-linear-systems"),
    ("power-series-solutions-to-odes", "power-series-solutions"),
    ("rlc-circuit-applications", "rlc-circuits"),
    ("solving-ivps-laplace-transform", "solving-ivps-with-laplace-transforms"),
    ("spring-mass-systems-and-vibrations", "spring-mass-systems"),
    ("systems-first-order-linear-odes", "systems-of-first-order-linear-odes"),
    # --- Numerical Analysis (18 pairs) ---
    ("chebyshev-nodes-optimal-interpolation", "chebyshev-nodes"),
    ("composite-quadrature-rules", "composite-quadrature"),
    ("condition-number-of-a-problem", "condition-number"),
    ("condition-number-of-matrix", "condition-number-of-a-matrix"),
    ("convergence-iterative-linear-solvers", "convergence-iterative-methods"),
    ("eulers-method-convergence", "euler-method-error-analysis"),
    ("gauss-seidel-iterative-method", "gauss-seidel-method"),
    ("machine-epsilon-and-rounding-errors", "machine-epsilon"),
    ("multistep-methods-adams-methods", "multistep-methods-adams"),
    ("newton-cotes-quadrature", "newton-cotes-formulas"),
    ("newtons-divided-differences", "newton-divided-differences"),
    ("newtons-method-convergence-analysis", "newton-method-convergence"),
    ("numerical-stability-and-conditioning", "numerical-stability"),
    ("qr-algorithm-eigenvalues", "qr-algorithm"),
    ("richardsons-extrapolation", "richardson-extrapolation"),
    ("runge-kutta-methods-for-odes", "runge-kutta-methods"),
    ("secant-method-root-finding", "secant-method"),
    ("stiff-equations", "stiff-differential-equations"),
    ("successive-over-relaxation-sor", "successive-over-relaxation"),
    # --- Methods of Proof (5 pairs) ---
    ("direct-proof-methods", "direct-proof"),
    ("logical-equivalences-intro", "logical-equivalences"),
    ("mathematical-induction-intro", "mathematical-induction"),
    ("predicates-and-quantifiers-intro", "predicates-and-quantifiers"),
    ("truth-tables-intro", "truth-tables"),
    # --- Multivariable Calculus (8 pairs) ---
    ("directional-derivatives-definition", "directional-derivatives"),
    ("gradient-vector-definition", "gradient-vector"),
    ("gradient-vector-properties", "gradient-vector"),
    ("line-integrals-definition-properties", "line-integrals"),
    ("multivariable-limits-definition", "multivariable-limits"),
    ("partial-derivatives-definition", "partial-derivatives"),
    ("vector-valued-functions-intro", "vector-valued-functions"),
    ("martingales-intro", "martingales-introduction"),
    # --- Measure Theory & Functional Analysis (7 pairs) ---
    ("banach-spaces-definition", "banach-spaces"),
    ("hilbert-spaces-definition", "hilbert-spaces"),
    ("lebesgue-integral-properties", "lebesgue-integral"),
    ("lp-spaces-definition", "lp-spaces"),
    ("measurable-functions-definition", "measurable-functions"),
    ("measure-spaces-definition", "measure-spaces"),
    ("outer-measure-definition", "outer-measure"),
    # --- Topology (5 pairs) ---
    ("completeness-metric-spaces-definition", "completeness-metric-spaces"),
    ("connected-spaces-definition", "connected-spaces"),
    ("subspace-topology-definition", "subspace-topology"),
    ("topological-invariants-intro", "topological-invariants"),
    ("topological-manifolds-intro", "topological-manifolds-introduction"),
    # --- Other Math (5 pairs) ---
    ("binomial-distribution-properties", "binomial-distribution"),
    ("geometric-distribution-properties", "geometric-distribution"),
    ("graph-representation-methods", "graph-representation"),
    ("poisson-distribution-properties", "poisson-distribution"),
    ("recurrence-relations-definition", "recurrence-relations"),
    ("stars-and-bars-method", "stars-and-bars"),
]


def find_topic_file(topic_id):
    """Find the .md file for a topic ID."""
    for f in DOMAINS_DIR.rglob(f"{topic_id}.md"):
        return f
    return None


def find_references(topic_id):
    """Find all files that reference a topic ID in their frontmatter."""
    refs = []
    for f in DOMAINS_DIR.rglob("*.md"):
        text = f.read_text(encoding="utf-8")
        # Check prerequisites and builds-toward for the ID
        if topic_id in text:
            refs.append(f)
    return refs


def redirect_references(delete_id, keep_id, dry_run=True):
    """Replace all references to delete_id with keep_id in other files."""
    refs = find_references(delete_id)
    modified = 0
    for f in refs:
        # Skip the file being deleted
        if f.stem == delete_id:
            continue
        text = f.read_text(encoding="utf-8")
        # Replace in prerequisite id fields: `- id: delete_id`
        new_text = re.sub(
            r'(?<=\bid: )' + re.escape(delete_id) + r'(?=\s|$)',
            keep_id, text)
        # Replace in builds-toward bare list items: `- delete_id`
        new_text = re.sub(
            r'(?<=- )' + re.escape(delete_id) + r'(?=\s|$)',
            keep_id, new_text)
        if new_text != text:
            if not dry_run:
                f.write_text(new_text, encoding="utf-8")
            modified += 1
            print(f"    {'Would update' if dry_run else 'Updated'}: {f.relative_to(ROOT)}")
    return modified


def main():
    parser = argparse.ArgumentParser(description="Deduplicate topic pairs")
    parser.add_argument("--apply", action="store_true", help="Apply changes (default: dry-run)")
    args = parser.parse_args()
    dry_run = not args.apply

    print(f"Deduplicating {len(DEDUP_PAIRS)} pairs ({'DRY RUN' if dry_run else 'APPLYING'})\n")

    total_deleted = 0
    total_redirected = 0

    for delete_id, keep_id in DEDUP_PAIRS:
        delete_file = find_topic_file(delete_id)
        keep_file = find_topic_file(keep_id)

        if not delete_file:
            print(f"  SKIP {delete_id}: file not found")
            continue
        if not keep_file:
            print(f"  SKIP {delete_id}: keeper {keep_id} not found")
            continue

        print(f"  {delete_id} -> {keep_id}")

        # Redirect references
        redirected = redirect_references(delete_id, keep_id, dry_run)
        total_redirected += redirected

        # Delete the file
        if not dry_run:
            delete_file.unlink()
        total_deleted += 1
        print(f"    {'Would delete' if dry_run else 'Deleted'}: {delete_file.relative_to(ROOT)}")

    print(f"\nSummary: {total_deleted} files {'to delete' if dry_run else 'deleted'}, "
          f"{total_redirected} files {'to update' if dry_run else 'updated'}")

    if dry_run:
        print("\nUse --apply to execute.")


if __name__ == "__main__":
    main()
