---
id: fft-polynomial-multiplication
title: Fast Fourier Transform and Polynomial Multiplication
domain: computer-science
course: advanced-algorithms
prerequisites:
- id: divide-and-conquer-strategy
  type: hard
- id: complex-numbers-intro
  type: hard
- id: recurrence-relations-analysis-techniques
  type: soft
- id: polynomial-rings
  type: soft
tags:
- fast-fourier-transform
- fft
- discrete-fourier-transform
- polynomial-multiplication
- convolution
- schonhage-strassen
stage: expert
status: validated
---

# Fast Fourier Transform and Polynomial Multiplication

## Core Idea
The Fast Fourier Transform (FFT) computes the Discrete Fourier Transform (DFT) of a sequence of n values in O(n log n) time, down from the naive O(n^2). Its primary algorithmic application is O(n log n) polynomial multiplication: evaluate two degree-n polynomials at the n-th roots of unity (via FFT), multiply the values pointwise in O(n), then interpolate back (via inverse FFT). The Cooley-Tukey algorithm achieves this through a divide-and-conquer decomposition that splits even- and odd-indexed coefficients, exploiting the symmetry properties of roots of unity (the "butterfly" structure). The FFT is the foundation for Schonhage-Strassen integer multiplication (O(n log n log log n)) and has applications throughout signal processing, string matching, and computational algebra. It is frequently cited as one of the ten most important algorithms of the 20th century.

## Questions

```yaml
- question: "The naive algorithm for multiplying two degree-n polynomials takes O(n^2) time. Why does the FFT-based approach achieve O(n log n)?"
  type: multiple-choice
  options:
    - "The FFT compresses the polynomial coefficients, reducing the problem size"
    - "The FFT converts polynomial multiplication from coefficient representation (where multiplication requires convolution, O(n^2)) to point-value representation (where multiplication is pointwise, O(n)); the conversions (FFT and inverse FFT) each take O(n log n), giving O(n log n) total"
    - "The FFT uses matrix multiplication, which is faster than O(n^2)"
    - "The FFT avoids multiplications entirely by using only additions"
  answer: 1
  explanation: "Polynomial multiplication in coefficient form requires computing the convolution of the two coefficient vectors, which is inherently O(n^2) for the naive approach. The key insight is that in point-value form (polynomial evaluated at 2n points), multiplication is just pointwise multiplication of the values, O(n). The FFT converts between coefficient form and point-value form in O(n log n) by evaluating the polynomial at the 2n-th roots of unity. The full pipeline: (1) FFT on coefficients of A and B to get point values (two O(n log n) transforms), (2) pointwise multiply to get point values of AB (O(n)), (3) inverse FFT to recover coefficients of AB (O(n log n)). Total: O(n log n)."

- question: "The Cooley-Tukey FFT algorithm splits a polynomial A(x) = A_even(x^2) + x * A_odd(x^2) and recursively evaluates at the n-th roots of unity. What property of roots of unity makes this work?"
  type: short-answer
  answer: "The critical property is that squaring the n-th roots of unity gives the (n/2)-th roots of unity: if omega = e^(2*pi*i/n) is a primitive n-th root, then {omega^0, omega^1, ..., omega^(n-1)} squared gives {omega^0, omega^2, ..., omega^(2n-2)} = {(omega^2)^0, (omega^2)^1, ..., (omega^2)^(n/2-1)} repeated twice, and omega^2 is a primitive (n/2)-th root of unity. This means evaluating A_even and A_odd at the (n/2)-th roots of unity (a problem of half the size) gives us exactly the values we need to combine into A's values at the n-th roots of unity. The recurrence T(n) = 2T(n/2) + O(n) solves to T(n) = O(n log n)."
  explanation: "This 'halving' property is unique to roots of unity and is why the FFT uses these specific evaluation points. If you evaluated at arbitrary points, the recursive decomposition would not produce subproblems of half the size. The collapsing property — n evaluation points become n/2 after squaring — is the algebraic miracle that enables the divide-and-conquer structure."

- question: "The inverse FFT recovers polynomial coefficients from point values. It is computed by running the FFT with omega^(-1) instead of omega, then dividing by n."
  type: true-false
  answer: true
  explanation: "The DFT can be expressed as a matrix-vector product: y = F_n * a, where F_n is the n x n DFT matrix with entries F_n[j,k] = omega^(jk). The inverse DFT is a^hat = F_n^(-1) * y. The crucial fact is that F_n^(-1) = (1/n) * conjugate(F_n) = (1/n) * F_n(omega^(-1)): the inverse DFT matrix has entries (1/n) * omega^(-jk). This means the inverse FFT is the same algorithm as the forward FFT, with omega replaced by omega^(-1) = e^(-2*pi*i/n) and a final division by n. This symmetry between forward and inverse transforms is both elegant and practical — a single FFT implementation handles both directions."

- question: "The FFT requires the input length to be a power of 2."
  type: true-false
  answer: false
  explanation: "The Cooley-Tukey radix-2 FFT requires n to be a power of 2, but this is not a fundamental limitation. For arbitrary n, three approaches work: (1) zero-pad the input to the next power of 2 (simple, at most doubles the input size), (2) use the mixed-radix FFT (Cooley-Tukey generalizes to any factorization n = n_1 * n_2, recursing into FFTs of sizes n_1 and n_2), (3) use Bluestein's algorithm, which reduces an FFT of any size n to a convolution of size 2n, which can be computed via a power-of-2 FFT of size >= 2n. Rader's algorithm handles the special case of prime n by reducing the DFT to a cyclic convolution of size n-1. In practice, zero-padding to a power of 2 is by far the most common approach."

- question: "Explain how the FFT connects to integer multiplication via the Schonhage-Strassen algorithm."
  type: short-answer
  answer: "Two n-bit integers can be viewed as polynomials: write a = sum a_i * B^i and b = sum b_i * B^i where B is a base (e.g., 2^16) and the a_i, b_i are 'digits' in base B. The product ab = convolution of the digit sequences, followed by carry propagation. The convolution step is exactly polynomial multiplication, computable in O(n log n) via FFT. Schonhage-Strassen (1971) refined this by working modulo (2^m + 1) for appropriate m (a Fermat number ring), where 2 is a root of unity, eliminating the need for floating-point arithmetic and complex numbers. This gives O(n log n log log n) integer multiplication, which was the asymptotic record for 36 years until Furer (2007). Harvey and van der Hoeven (2021) achieved the conjectured optimal O(n log n), settling a major open problem."
  explanation: "The connection between polynomial multiplication and integer multiplication is that integer multiplication IS polynomial multiplication followed by carries. The FFT handles the polynomial part; carries are a linear-time postprocessing step. Schonhage-Strassen's innovation was doing the FFT over rings where exact arithmetic is possible (no floating-point issues), using the number-theoretic transform (NTT) with modular arithmetic instead of complex roots of unity."
```

## Explainer

The Fast Fourier Transform is one of the most consequential algorithms in all of computer science and applied mathematics. Its core contribution is reducing the Discrete Fourier Transform (DFT) — a linear transformation that converts between the coefficient representation and the frequency representation of a sequence — from O(n^2) to O(n log n). This speedup has had immense practical impact in signal processing, image compression, telecommunications, and scientific computing, but its role in algorithm design centers on polynomial multiplication: the FFT makes it possible to multiply two polynomials of degree n in O(n log n) time, a fundamental operation with consequences throughout theoretical computer science.

The algorithm exploits the algebraic structure of roots of unity. Let omega = e^(2*pi*i/n) be a primitive n-th root of unity. The DFT evaluates a polynomial A(x) = a_0 + a_1*x + ... + a_{n-1}*x^{n-1} at the points 1, omega, omega^2, ..., omega^{n-1}. The Cooley-Tukey FFT splits A into even-indexed and odd-indexed coefficients: A(x) = A_even(x^2) + x*A_odd(x^2). The magic is that evaluating A_even and A_odd at the squares of the n-th roots of unity is exactly evaluating them at the (n/2)-th roots of unity — because squaring the n-th roots collapses them to the (n/2)-th roots. This gives a perfect divide-and-conquer: two recursive FFTs of size n/2, plus O(n) "butterfly" operations to combine. The recurrence T(n) = 2T(n/2) + O(n) gives T(n) = O(n log n).

Polynomial multiplication follows a three-step pipeline. To multiply A(x) and B(x), both of degree n: (1) evaluate A and B at 2n roots of unity using two FFTs (O(n log n) each), (2) multiply the values pointwise to get the values of C = AB at the 2n roots of unity (O(n)), (3) apply the inverse FFT to recover the coefficients of C (O(n log n)). The correctness relies on the fundamental fact that a polynomial of degree d is uniquely determined by its values at d+1 points, and that pointwise multiplication of values corresponds to polynomial multiplication. The total cost is O(n log n), an exponential improvement over the O(n^2) of naive coefficient-by-coefficient convolution.

The connection to integer multiplication runs through the observation that multiplying two n-bit integers is essentially multiplying two polynomials (with base-B "coefficients") followed by carry propagation. The Schonhage-Strassen algorithm (1971) made this practical by performing the FFT over the ring Z/(2^m + 1)Z rather than over the complex numbers. In this ring, 2 is a root of unity of order 2m, so all arithmetic is exact (no floating-point roundoff) and each operation takes O(m) bit operations. The recursive structure (use the FFT to multiply large integers, but the FFT itself requires integer multiplications for the butterfly operations) is handled by recursing until the integers are small enough for schoolbook multiplication. The resulting O(n log n log log n) complexity was the best known for 36 years, until Furer improved the log log n factor in 2007, and Harvey and van der Hoeven achieved the conjectured optimal O(n log n) in 2021.

Beyond multiplication, the FFT appears throughout algorithm design. Fast string matching can be reduced to polynomial multiplication (represent text and pattern as polynomials, compute their convolution). The FFT is essential for fast algorithms in computational geometry (polygon area, point-set diameter), coding theory (Reed-Solomon encoding/decoding), and combinatorics (computing convolutions that arise in counting problems). The Number Theoretic Transform (NTT) — the FFT over finite fields — is the basis for fast modular arithmetic in cryptography and for efficient implementations of operations in lattice-based cryptographic schemes. The FFT's combination of theoretical elegance (a single divide-and-conquer idea, enabled by the algebraic structure of roots of unity) and extraordinary practical impact places it among the greatest algorithmic achievements of the 20th century.
