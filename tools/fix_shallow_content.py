"""
Expand 25 topics with shallow body content (under 50 words).
Adds substantive Core Idea, How It's Best Learned, and Common Misconceptions sections.
Target: 80-120 words total body content per topic.
"""

import re
from pathlib import Path

PROJECT = Path(r"C:\Users\griff\Projects\griffin\open-knowledge-graph")

# Each entry: (topic_id, domain, course, expanded_body)
# The expanded_body replaces everything after the closing --- of frontmatter.
# We preserve the title heading and rewrite the body sections.

EXPANSIONS = {
    "anova-one-way-theory": {
        "domain": "mathematics",
        "course": "probability-and-statistics",
        "body": """# One-Way ANOVA: Theory and F-Test

## Core Idea
One-way ANOVA tests the null hypothesis H₀: μ₁ = μ₂ = ... = μₖ, asking whether k group means differ more than chance predicts. The F-statistic equals MS_Between / MS_Within, with degrees of freedom (k−1, n−k). MS_Between captures variation among group means, while MS_Within estimates pooled within-group error. The test assumes equal variances across groups, approximate normality within groups, and independence of observations. A large F value indicates the group means differ more than expected from within-group variability alone.

## How It's Best Learned
Start with a concrete example—compare exam scores across three teaching methods. Compute group means, then manually calculate SS_Between and SS_Within to build intuition for what the F-ratio measures before relying on software output.

## Common Misconceptions
A significant F-test does not tell you which groups differ—post-hoc tests are needed. ANOVA is also reasonably robust to mild normality violations, so the normality assumption is not as fragile as students often fear.
"""
    },
    "cumulative-distribution-functions-theory": {
        "domain": "mathematics",
        "course": "probability-and-statistics",
        "body": """# Cumulative Distribution Functions

## Core Idea
The cumulative distribution function F(x) = P(X ≤ x) gives the probability that a random variable takes a value at or below x. Every CDF is non-decreasing, right-continuous, with F(−∞) = 0 and F(∞) = 1. For continuous random variables, the PDF is the derivative of the CDF: f(x) = F'(x). For discrete variables, the CDF is a step function with jumps at each possible value. CDFs provide a unified framework for computing tail probabilities, quantiles, and comparing distributions regardless of whether the variable is discrete, continuous, or mixed.

## How It's Best Learned
Plot CDFs for familiar distributions (uniform, normal, geometric) side by side. Practice reading probabilities as vertical differences: P(a < X ≤ b) = F(b) − F(a). This graphical approach builds stronger intuition than formulas alone.

## Common Misconceptions
Students often confuse F(x) with f(x), treating the CDF as a density. The CDF gives cumulative probability, not probability at a point. Also, P(X = x) is not always F(x) − F(x⁻) for continuous variables—it is zero.
"""
    },
    "sequences-convergence-topology": {
        "domain": "mathematics",
        "course": "topology",
        "body": """# Convergence of Sequences in Topological Spaces

## Core Idea
A sequence (xₙ) converges to x in a topological space if every open set containing x eventually contains all terms of the sequence—that is, for every open U containing x, there exists N such that xₙ ∈ U for all n ≥ N. This generalizes the ε-ball definition from metric spaces. Unlike metric spaces, limits in general topological spaces need not be unique; uniqueness requires the Hausdorff separation axiom. Furthermore, sequences alone may not suffice to characterize the topology—in non-first-countable spaces, nets or filters are needed to fully describe convergence behavior.

## How It's Best Learned
Compare convergence in a metric space with convergence in the cofinite topology on an infinite set, where sequences can converge to every point simultaneously. This dramatic contrast motivates why separation axioms matter.

## Common Misconceptions
Students often assume sequential convergence fully determines the topology. This holds in metric and first-countable spaces but fails in general. Also, a sequence can have multiple limits in non-Hausdorff spaces—this is a feature of the topology, not an error.
"""
    },
    "graphic-notation-interpretation": {
        "domain": "music",
        "course": "advanced-music-theory",
        "body": """# Graphic Notation and Experimental Score Systems

## Core Idea
Graphic notation replaces traditional staff notation with visual symbols, shapes, colors, and spatial relationships to convey musical ideas. Composers like Feldman, Cardew, and Cage developed systems where the score becomes a visual artwork that performers interpret. The degree of determinacy varies widely: some graphic scores specify pitch and rhythm loosely through spatial position, while others function as open prompts for improvisation. Analyzing graphic works demands attention to the composer's stated intentions, the visual grammar of the score, and the range of valid interpretive choices available to performers.

## How It's Best Learned
Study specific landmark works—Feldman's graph pieces, Cardew's *Treatise*, and Cage's notations—alongside recordings of different performers interpreting the same score. Comparing performances reveals how graphic notation creates a space of possibilities rather than a single fixed reading.

## Common Misconceptions
Graphic notation is not "anything goes." Most graphic scores have detailed performance instructions. The visual freedom does not mean absence of structure—it means a different kind of structure that balances composer intent with performer agency.
"""
    },
    "jazz-reharmonization-substitution": {
        "domain": "music",
        "course": "advanced-music-theory",
        "body": """# Advanced Jazz Reharmonization and Chord Substitution

## Core Idea
Advanced reharmonization goes beyond basic tritone substitution and relative minor swaps to reshape a tune's harmonic landscape. Techniques include chromatic approach chords, upper-structure triads over altered dominants, coltrane changes (major-third cycles), diminished substitution, and freely interpolated non-functional harmony. The goal is not merely to replace chords but to recast the melody's harmonic context so that familiar lines acquire new color and emotional weight. Reharmonization becomes a compositional act—the harmonic choices shape how a soloist hears and navigates the changes in real time.

## How It's Best Learned
Take a standard like "All The Things You Are" and create three different reharmonizations of the same eight bars. Record yourself playing the melody over each version to hear how the harmonic context transforms the melodic experience.

## Common Misconceptions
Reharmonization is not just about complexity. The best reharmonizations serve the melody and the musical moment. Students sometimes stack substitutions without considering whether the result supports or obscures the tune's character.
"""
    },
    "connected-components": {
        "domain": "mathematics",
        "course": "topology",
        "body": """# Connected Components

## Core Idea
The connected component of a point x is the largest connected subset containing x—formally, the union of all connected subsets that contain x. Connected components partition any topological space into maximal connected pieces, and they are always closed sets. This decomposition reveals the global structure of a space: a space is connected if and only if it has exactly one component. In totally disconnected spaces like the Cantor set, every component is a single point. The number and nature of connected components provide a coarse but powerful topological invariant.

## How It's Best Learned
Draw examples: identify the components of the real line minus a few points, then of a union of disjoint circles. Move to the topologist's sine curve to see that components can be connected but not path-connected, sharpening the distinction.

## Common Misconceptions
Students often assume connected components must be open—they are always closed but not necessarily open. Also, path-components and connected components can differ; path-connectedness is strictly stronger than connectedness.
"""
    },
    "cyclic-unity-chamber-works": {
        "domain": "music",
        "course": "advanced-music-theory",
        "body": """# Cyclic Form and Thematic Unity in Chamber Music

## Core Idea
Cyclic form creates coherence across a multi-movement chamber work by threading shared melodic, harmonic, or rhythmic material through all movements. Unlike simple quotation, advanced cyclic technique transforms the recurring material through fragmentation, augmentation, inversion, and recontextualization so that connections may be subtle or revealed only at the climax. Franck's Violin Sonata and Bartók's string quartets exemplify different approaches: Franck uses overt thematic recall, while Bartók embeds intervallic cells that unify without literal repetition. The listener's experience of unity emerges gradually as the work's architecture becomes apparent.

## How It's Best Learned
Analyze a complete cyclic work movement by movement, cataloging every appearance of the shared material and how it is transformed. Franck's Piano Quintet or Schumann's Piano Quintet are good starting points because the cyclic elements are relatively audible.

## Common Misconceptions
Cyclic form is not the same as a recurring motto or leitmotif. The cyclic principle involves structural integration across movements, not just surface-level repetition. Also, subtlety is a feature—some cyclic connections are meant to operate below conscious awareness.
"""
    },
    "arithmetic-functions-multiplicativity": {
        "domain": "mathematics",
        "course": "number-theory",
        "body": """# Arithmetic Functions and Multiplicativity

## Core Idea
An arithmetic function maps positive integers to complex numbers. A function f is multiplicative if f(mn) = f(m)f(n) whenever gcd(m, n) = 1, and completely multiplicative if this holds for all m and n regardless of their gcd. Because every positive integer factors uniquely into prime powers, a multiplicative function is entirely determined by its values on prime powers. Key examples include Euler's totient φ(n), the divisor function σ(n), and the Möbius function μ(n). Multiplicativity enables efficient computation and is the foundation for techniques like Möbius inversion and Dirichlet series manipulation.

## How It's Best Learned
Verify multiplicativity by hand for small examples: compute φ(12) via φ(4)·φ(3) and confirm it matches the direct count. Then see how knowing φ(pᵏ) = pᵏ − pᵏ⁻¹ lets you compute φ for any n from its prime factorization.

## Common Misconceptions
Multiplicative does not mean f(mn) = f(m)f(n) for all m, n—that is completely multiplicative. The coprimality condition is essential. Also, f(1) = 1 is a consequence of multiplicativity, not an extra assumption.
"""
    },
    "introduction-ideal-class-group": {
        "domain": "mathematics",
        "course": "number-theory",
        "body": """# Introduction to the Ideal Class Group

## Core Idea
The ideal class group measures how far a number ring departs from unique factorization. In rings of algebraic integers where elements may not factor uniquely, ideals always factor uniquely into prime ideals. Two ideals are equivalent if they differ by multiplication by a principal ideal. The class group is the quotient of fractional ideals by principal ideals, and its order—the class number h(K)—equals 1 precisely when the ring is a principal ideal domain with unique factorization. Computing class numbers reveals the arithmetic complexity of number fields and connects to deep results in algebraic number theory.

## How It's Best Learned
Work through ℤ[√−5], where 6 = 2 · 3 = (1+√−5)(1−√−5) shows factorization failure. Then verify that ideal factorization restores uniqueness and compute that h = 2, making the class group ℤ/2ℤ.

## Common Misconceptions
The class group is not about individual elements failing to factor—it is about the global structure of ideals. Students sometimes think unique factorization fails "everywhere" when h > 1, but many elements still factor uniquely; it is the exceptions that the class group quantifies.
"""
    },
    "contemporary-performance-practice": {
        "domain": "music",
        "course": "advanced-music-theory",
        "body": """# Performance Practice in Contemporary and New Music

## Core Idea
Performing contemporary music requires navigating interpretive territory that traditional notation leaves unspecified. Extended techniques—multiphonics, prepared instruments, unconventional bowing—demand physical mastery and an understanding of the sonic possibilities each technique offers. Performers must balance precision with flexibility, following the score's explicit instructions while making musical judgments about dynamics, timing, and timbral shading. The composer-performer relationship in new music is often collaborative: performers may consult directly with composers, and scores may include prose instructions alongside or instead of traditional notation. Understanding performance practice is essential for both performers preparing new works and analysts interpreting them.

## How It's Best Learned
Attend rehearsals of new-music ensembles and observe how performers negotiate ambiguous notation. Compare a score with multiple recordings to hear the range of valid interpretations, then attempt performing a short contemporary work yourself.

## Common Misconceptions
Contemporary performance practice is not purely about technical difficulty. The central challenge is often interpretive—deciding what the notation means in context. Also, "new music" performance practice has its own evolving traditions and is not simply the absence of convention.
"""
    },
    "potentiality-and-actuality": {
        "domain": "philosophy",
        "course": "metaphysics",
        "body": """# Potentiality and Actuality

## Core Idea
The distinction between potentiality and actuality concerns what could be versus what is. Aristotle introduced this framework to explain change: an acorn is potentially an oak tree, and the process of growth is the transition from potentiality to actuality. Not everything possible becomes actual, and not every actual state was inevitable. This distinction raises deep questions: Are potentialities real features of the world or merely descriptions of what we do not yet know? Does actuality have metaphysical priority over potentiality, or can potentials exist independently? Modern discussions connect this framework to dispositions, powers, and the interpretation of quantum mechanics.

## How It's Best Learned
Begin with Aristotle's own examples from *Metaphysics* Book IX, then trace how the distinction reappears in debates about dispositions (is glass fragile even when it is not breaking?) and in quantum mechanics (is a particle's position potential before measurement?).

## Common Misconceptions
Potentiality is not the same as logical possibility. A block of marble is potentially a statue but not potentially a sound. Potentialities are constrained by the nature of the thing. Also, actuality does not simply mean "existing now"—it refers to the realization of a specific capacity.
"""
    },
    "linear-transformations-of-random-variables": {
        "domain": "mathematics",
        "course": "probability-and-statistics",
        "body": """# Linear Transformations of Random Variables

## Core Idea
Linear transformations are the workhorses of probability. If Y = aX + b, then E[Y] = aE[X] + b and Var(Y) = a²Var(X)—expectation is linear while variance scales quadratically and is unaffected by shifts. For sums of random variables, E[X + Y] = E[X] + E[Y] always holds, but Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y), so independence simplifies the variance formula. These properties underpin standardization (converting any distribution to mean 0 and variance 1), the construction of confidence intervals, and the derivation of sampling distributions used throughout statistical inference.

## How It's Best Learned
Derive the rules algebraically from the definition of expectation, then verify them numerically with a simple example: roll a die, let X be the result, compute E[3X + 2] and Var(3X + 2) both by formula and by enumerating all outcomes.

## Common Misconceptions
Students frequently forget the squared coefficient in Var(aX) = a²Var(X) and write aVar(X) instead. Another common error is assuming Var(X + Y) = Var(X) + Var(Y) without checking independence—the covariance term is only zero when X and Y are uncorrelated.
"""
    },
    "logical-operators-arguments": {
        "domain": "philosophy",
        "course": "logic-and-critical-thinking",
        "body": """# Logical Operators in Arguments: AND, OR, NOT

## Core Idea
Logical operators combine simple propositions into compound statements with precisely defined truth conditions. Conjunction (AND) is true only when both components are true. Disjunction (OR) in formal logic is inclusive—true when at least one component is true, including when both are. Negation (NOT) flips the truth value. These operators let us build complex arguments from simpler claims and evaluate their validity systematically. Mastering their behavior is the first step toward propositional logic, truth tables, and recognizing how ambiguous natural language can lead to reasoning errors when "and," "or," and "not" are used imprecisely.

## How It's Best Learned
Construct truth tables by hand for simple compound propositions, then translate everyday sentences ("You can have cake or pie") into logical form to see where natural language diverges from formal logic—especially with inclusive versus exclusive "or."

## Common Misconceptions
In everyday speech, "or" is often exclusive (one or the other, not both), but in logic it is inclusive by default. Students also struggle with the scope of negation: "not A and B" is ambiguous between (¬A) ∧ B and ¬(A ∧ B). Parentheses resolve this, which is why formal notation matters.
"""
    },
    "extreme-value-theorem-rigorous": {
        "domain": "mathematics",
        "course": "real-analysis",
        "body": """# Extreme Value Theorem (Proof via Compactness)

## Core Idea
The Extreme Value Theorem states that a continuous function on a compact set attains its maximum and minimum values. The proof proceeds in two steps: first, the continuous image of a compact set is compact (since compactness is preserved under continuous maps); second, compact subsets of ℝ are closed and bounded by the Heine-Borel theorem, so they contain their supremum and infimum. This theorem is fundamental because it guarantees that optimization problems on closed bounded intervals have solutions. Without compactness, continuous functions may approach a supremum without attaining it, as shown by f(x) = 1/x on (0, 1].

## How It's Best Learned
First prove the supporting lemma that continuous images of compact sets are compact, then assemble the full proof. Studying counterexamples—continuous functions on open or unbounded domains that fail to attain extrema—solidifies understanding of why each hypothesis is necessary.

## Common Misconceptions
Students sometimes think continuity alone guarantees extrema, forgetting that the domain must be compact. The theorem also does not say where the extrema occur—they might be at interior points or boundary points.
"""
    },
    "extended-harmony-voice-leading-handling": {
        "domain": "music",
        "course": "harmony-and-voice-leading",
        "body": """# Extended Harmony: Voice Leading with 9ths, 11ths, and 13ths

## Core Idea
Extended chords add ninths, elevenths, and thirteenths above the seventh, creating richer sonorities that require careful voice-leading treatment. Upper extensions often behave like non-chord tones that must resolve stepwise or be smoothly prepared from the preceding chord. The natural eleventh over a major chord clashes with the third, so it is typically raised (♯11) or omitted. Voice spacing matters greatly: wide voicings in the upper register sound lush, while close voicings can become muddy. Understanding which extensions are stable versus tendency tones in each chord quality guides both composition and arranging decisions in jazz and orchestral contexts.

## How It's Best Learned
Voice-lead a ii-V-I progression in four voices, then gradually add extensions one at a time—first ninths, then thirteenths—observing how each addition creates new resolution obligations. Play the results at a keyboard to train your ear alongside the theory.

## Common Misconceptions
Not all notes of an extended chord need to sound simultaneously. Skilled arrangers omit the fifth and sometimes the root, keeping only the essential intervals. Students also mistakenly treat all extensions as equally consonant—the natural 11th over a major chord is a well-known avoid note.
"""
    },
    "metric-spaces-definition-and-examples": {
        "domain": "mathematics",
        "course": "topology",
        "body": """# Metric Spaces: Definition and Examples

## Core Idea
A metric space is a set X equipped with a distance function d: X × X → ℝ satisfying three axioms: non-negativity (d(x,y) ≥ 0 with equality iff x = y), symmetry (d(x,y) = d(y,x)), and the triangle inequality (d(x,z) ≤ d(x,y) + d(y,z)). The Euclidean metric on ℝⁿ is the most familiar example, but the discrete metric (d = 0 if equal, 1 otherwise) and the taxicab metric on ℝ² show that the same set can carry very different metrics. Every metric induces a topology via open balls B(x, r) = {y : d(x,y) < r}, making metric spaces a concrete gateway to general topology.

## How It's Best Learned
Verify the three axioms for several concrete metrics—Euclidean, taxicab, discrete, and the sup metric on function spaces. Draw open balls in each to see how different metrics produce different notions of "nearness" on the same underlying set.

## Common Misconceptions
A metric is not the same as a norm—norms require a vector space structure, while metrics apply to any set. Students also sometimes forget that the triangle inequality is doing essential work; without it, the notion of "closeness" becomes incoherent.
"""
    },
    "improper-integrals-rigorous": {
        "domain": "mathematics",
        "course": "real-analysis",
        "body": """# Improper Integrals (Rigorous)

## Core Idea
An improper integral extends the Riemann integral to unbounded intervals or unbounded integrands by taking limits. For infinite intervals, ∫ₐ^∞ f(x) dx = lim_{t→∞} ∫ₐᵗ f(x) dx; for unbounded integrands near a point c, ∫ₐᵇ f(x) dx = lim_{ε→0⁺} ∫ₐ^{c−ε} f(x) dx + lim_{ε→0⁺} ∫_{c+ε}ᵇ f(x) dx. The integral converges if these limits exist and are finite. Convergence criteria mirror those for series: comparison tests, limit comparison, and absolute convergence all apply. An integral can converge conditionally (like ∫₁^∞ sin(x)/x dx) without converging absolutely. These integrals arise naturally in probability, Fourier analysis, and Laplace transforms.

## How It's Best Learned
Work through the classic examples: ∫₁^∞ 1/xᵖ dx (converges iff p > 1), then ∫₀¹ 1/xᵖ dx (converges iff p < 1). These two cases build the intuition that convergence depends on how fast the integrand decays or blows up relative to the interval.

## Common Misconceptions
Students sometimes evaluate improper integrals by plugging in ∞ directly, skipping the limit process. This can produce correct-looking answers but obscures conditional convergence issues. Also, the two limits in a doubly improper integral must be taken independently—they cannot be combined into a single symmetric limit.
"""
    },
    "post-tonal-harmonic-analysis": {
        "domain": "music",
        "course": "advanced-music-theory",
        "body": """# Harmonic Function in Post-Tonal and Atonal Music

## Core Idea
Post-tonal music dispenses with traditional tonal hierarchies but does not abandon harmonic function entirely. Tension and resolution can arise from set-class relationships (certain pitch-class sets feel more stable or final), spectral properties (the harmonic series as a source of consonance), or textural density (thick clusters creating tension, sparse textures providing release). Analyzing harmonic function in post-tonal contexts means identifying functional analogues: which sonorities serve as points of arrival, which create forward motion, and how register, dynamics, and timbre participate in creating a sense of harmonic direction without relying on tonic-dominant polarity.

## How It's Best Learned
Analyze a movement from Webern's op. 21 Symphony or Bartók's Music for Strings, Percussion, and Celesta. Identify moments that feel like arrivals or departures, then examine what pitch, registral, or textural features create those functional impressions without traditional tonal cues.

## Common Misconceptions
"Atonal" does not mean "without harmonic logic." Post-tonal composers create sophisticated systems of tension and resolution; the analytical challenge is identifying those systems rather than assuming harmony is absent. Also, set-class labels alone do not capture harmonic function—context and voicing matter enormously.
"""
    },
    "rondo-composition-design": {
        "domain": "music",
        "course": "composition",
        "body": """# Rondo and Rounded Binary Form Design

## Core Idea
Rondo form alternates a recurring refrain (A) with contrasting episodes (B, C, etc.) in patterns like A-B-A-C-A or A-B-A-C-A-B-A. The refrain's return creates structural stability and a sense of homecoming, while episodes provide contrast in key, theme, or character. Rounded binary form (||: A :||: B-A' :||) adds a return to the opening material after the contrasting B section, bridging simple binary and ternary structures. Both forms are staples of Classical instrumental music, effective for creating clear, memorable architecture. Composing in these forms requires balancing predictability (the expected return) with surprise (varied episodes or a transformed reprise).

## How It's Best Learned
Compose a short rondo: write a 16-bar refrain, then two contrasting 8-bar episodes. Focus on how the refrain's return feels after each episode. Then try varying the refrain on its later returns to see how small changes maintain freshness within a predictable structure.

## Common Misconceptions
Rondo form is not rigidly fixed—many rondos include developmental passages, key changes in the refrain's returns, or coda sections. Students also sometimes confuse rondo with ritornello form, which is an orchestral Baroque procedure with different structural logic.
"""
    },
    "riemann-zeta-function-intro": {
        "domain": "mathematics",
        "course": "number-theory",
        "body": """# Introduction to the Riemann Zeta Function

## Core Idea
The Riemann zeta function ζ(s) = Σₙ₌₁^∞ 1/nˢ converges for Re(s) > 1 and extends via analytic continuation to the entire complex plane (with a simple pole at s = 1). Its Euler product representation ζ(s) = ∏_p (1 − p⁻ˢ)⁻¹ reveals the deep connection between the zeta function and prime numbers. The distribution of primes is governed by the location of ζ's zeros: the prime number theorem follows from the fact that ζ has no zeros on the line Re(s) = 1. The Riemann Hypothesis—asserting that all non-trivial zeros lie on Re(s) = 1/2—remains one of the greatest unsolved problems in mathematics.

## How It's Best Learned
Start by computing partial sums of ζ(2) = π²/6 to see convergence, then study the Euler product for small primes to understand why prime factorization makes the product work. The connection to primes becomes concrete before the analytic continuation adds complexity.

## Common Misconceptions
The zeta function is not defined by the series Σ 1/nˢ for all s—that series diverges for Re(s) ≤ 1. Statements like "ζ(−1) = −1/12" refer to the analytic continuation, not to summing 1 + 2 + 3 + .... Students must distinguish the series from its continuation.
"""
    },
    "tychonoff-theorem": {
        "domain": "mathematics",
        "course": "topology",
        "body": """# Tychonoff's Theorem

## Core Idea
Tychonoff's theorem states that an arbitrary product of compact topological spaces is compact in the product topology. For finite products this follows from elementary arguments, but the infinite case is a deep result equivalent to the Axiom of Choice. The proof typically uses Alexander's subbase theorem or Zorn's lemma to handle infinite open covers. Tychonoff's theorem is indispensable in functional analysis (the Banach-Alaoglu theorem depends on it), in probability (for constructing product measures), and throughout topology. It demonstrates that compactness, unlike many other properties, is perfectly preserved under arbitrary products.

## How It's Best Learned
First prove the finite product case directly, then study why the argument breaks for infinite products. Understanding where the Axiom of Choice enters—selecting finite subcovers simultaneously across infinitely many factors—clarifies both the theorem's depth and its logical status.

## Common Misconceptions
Students often assume the theorem is obvious because the finite case is straightforward. The infinite case is fundamentally different and requires a non-constructive choice principle. Also, the product topology (not the box topology) is essential—the theorem fails for the box topology on infinite products.
"""
    },
    "completeness-metric-spaces-definition": {
        "domain": "mathematics",
        "course": "topology",
        "body": """# Completeness of Metric Spaces

## Core Idea
A metric space is complete if every Cauchy sequence converges to a limit within the space. Euclidean space ℝⁿ, the p-adic numbers, and ℓᵖ spaces are complete, while the rationals ℚ and the open interval (0, 1) are not. Completeness means there are no "missing limits"—sequences that should converge have somewhere to land. Key structural results follow: every compact metric space is complete, every closed subset of a complete space is complete, and the Baire category theorem applies only in complete spaces. When a space is incomplete, it can be completed by adding limit points, analogous to how ℝ completes ℚ.

## How It's Best Learned
Construct a Cauchy sequence in ℚ converging to √2 to see incompleteness concretely. Then show the same sequence converges in ℝ. This example makes the abstract definition tangible and motivates why completion is a natural construction.

## Common Misconceptions
Completeness is a metric property, not a topological one—the same set can be complete under one metric and incomplete under another. Students also confuse completeness with compactness; ℝ is complete but not compact. Compactness implies completeness (in metric spaces), but not conversely.
"""
    },
    "connectedness-definition-examples": {
        "domain": "mathematics",
        "course": "topology",
        "body": """# Connectedness: Definition and Examples

## Core Idea
A topological space is connected if it cannot be written as a union of two disjoint nonempty open sets. Equivalently, the only subsets that are both open and closed (clopen) are the empty set and the whole space. Connectedness captures the intuitive idea that a space is "in one piece." The real line ℝ is connected, but ℝ minus a point is not—removing any point splits it into two open rays. The continuous image of a connected space is connected, which is why the intermediate value theorem holds: a continuous function on a connected domain cannot skip values. Connectedness is a topological invariant preserved under homeomorphisms.

## How It's Best Learned
Prove that ℝ is connected using the least upper bound property, then show ℚ is disconnected by exhibiting a clopen set. Working through these two cases builds a concrete understanding of the definition before moving to more exotic spaces.

## Common Misconceptions
Connected does not mean path-connected. The topologist's sine curve is connected but not path-connected. Students also sometimes think removing a point always disconnects a space—this is true for ℝ but false for ℝ² (which remains connected after removing any single point).
"""
    },
    "fundamental-group-of-circle": {
        "domain": "mathematics",
        "course": "topology",
        "body": """# Fundamental Group of the Circle

## Core Idea
The fundamental group π₁(S¹) is isomorphic to ℤ, the integers under addition. The isomorphism assigns to each loop its winding number—the net number of times it wraps around the circle, with counterclockwise positive and clockwise negative. A loop that winds twice composes with one that winds three times to give a loop winding five times, mirroring addition in ℤ. The proof uses the covering space ℝ → S¹ given by the exponential map t ↦ e^{2πit}, lifting loops to paths in ℝ and reading off the winding number as the endpoint. This computation is the foundational example in algebraic topology, demonstrating how topological features (the "hole" in S¹) are captured by algebraic invariants.

## How It's Best Learned
Draw loops on S¹ with different winding numbers and verify that composition corresponds to addition. Then study the covering space ℝ → S¹ to see how lifting makes the winding number rigorous, turning a geometric intuition into an algebraic proof.

## Common Misconceptions
The winding number is not about the shape of the loop but only about its net winding. A complicated loop that winds forward and backward may have winding number zero. Students also sometimes confuse π₁(S¹) ≅ ℤ with π₁(S²) ≅ 0—the sphere is simply connected because loops can be contracted over the surface.
"""
    },
    "separation-axioms-t0-t1-t2": {
        "domain": "mathematics",
        "course": "topology",
        "body": """# Separation Axioms: T₀, T₁, and T₂ (Hausdorff)

## Core Idea
Separation axioms form a hierarchy measuring how well a topology distinguishes points. T₀ (Kolmogorov) requires that for any two distinct points, at least one has an open neighborhood not containing the other. T₁ (Fréchet) strengthens this so that each point has a neighborhood excluding the other, which is equivalent to requiring all singletons to be closed. T₂ (Hausdorff) requires disjoint open neighborhoods for any two distinct points, guaranteeing that limits of convergent sequences are unique. Each level excludes more pathological spaces: most spaces encountered in analysis and geometry are at least Hausdorff, making T₂ the practical baseline for well-behaved topology.

## How It's Best Learned
Examine concrete examples at each level: the indiscrete topology fails even T₀, the cofinite topology on an infinite set is T₁ but not T₂, and the Euclidean topology is T₂. Seeing exactly where each axiom fails in these examples makes the hierarchy concrete.

## Common Misconceptions
T₁ does not imply Hausdorff—the cofinite topology on an infinite set separates points from each other with open sets but cannot produce disjoint neighborhoods. Students also sometimes think Hausdorff is an exotic condition, when in fact most familiar spaces (metric spaces, manifolds) are automatically Hausdorff.
"""
    },
}


def count_body_words(body_text: str) -> int:
    """Count words in body text, excluding markdown headers."""
    words = 0
    for line in body_text.strip().split('\n'):
        stripped = line.strip()
        if stripped.startswith('#'):
            continue
        words += len(stripped.split()) if stripped else 0
    return words


def process_file(topic_id: str, info: dict) -> None:
    domain = info["domain"]
    course = info["course"]
    filepath = PROJECT / "domains" / domain / course / f"{topic_id}.md"

    if not filepath.exists():
        print(f"  SKIP (not found): {filepath}")
        return

    content = filepath.read_text(encoding='utf-8')

    # Split frontmatter from body
    parts = content.split('---', 2)
    if len(parts) < 3:
        print(f"  SKIP (no frontmatter): {topic_id}")
        return

    frontmatter = parts[1]  # Between first and second ---
    old_body = parts[2]

    new_body = "\n" + info["body"].strip() + "\n"

    new_content = f"---{frontmatter}---\n{new_body}\n"

    # Count words
    old_wc = count_body_words(old_body)
    new_wc = count_body_words(new_body)

    filepath.write_text(new_content, encoding='utf-8')
    print(f"  OK: {topic_id} ({old_wc}w -> {new_wc}w)")


def main():
    print(f"Expanding {len(EXPANSIONS)} shallow topics...\n")

    for topic_id, info in EXPANSIONS.items():
        process_file(topic_id, info)

    print(f"\nDone. {len(EXPANSIONS)} topics processed.")


if __name__ == "__main__":
    main()
