# J‑constant Geometric Framework for the Riemann Hypothesis (Z6)

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.19770193-blue)](https://doi.org/10.5281/zenodo.19770193)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

**A Geometric Interpretation of the Riemann Hypothesis**  
*A Unified Framework Based on the J‑Constant and Ellipse Compensation Identity*  
– Peiying Jie (2026)

This repository contains the **final version (Z6)** of the paper, the complete LaTeX source, all numerical validation data (CSV), and a standalone appendix. The work unifies non‑trivial zeros of the Riemann zeta function, high‑precision ellipse circumference computation, and a geometric inversion of $\pi$ through a single wall‑thickness constant $J_\infty = \gamma_E/(2\pi)$.

---

## 📁 Repository Structure
```

.
├── Geometric_Riemann_Z6.pdf          # Full paper
├── Geometric_Riemann_Z6.tex          # LaTeX source
├── FigA1_psi_20.png                  # Figure: Ψ(t) precision for first 20 zeros
├── zero_reproduction_100_zeros.csv   # Full data (113 zeros, backward validation)
├── zero_reproduction_validation.csv  # First 20 zeros + geometric parameters
├── README.md
├── requirements.txt                  # Python dependencies (numpy, scipy, mpmath)
└── archives/                         # Previous versions (v2, v3)
├── v2-2026-04-25/
└── v3-2026-04-28/

```

---

## 📄 Paper Summary

- **Core constant**  $J_\infty = \gamma_E/(2\pi)$ (from Euler’s constant)
- **Geometric axiom** $a-b = J_\infty$ for every non‑trivial zero
- **Compensation identity** $C + 2J = 2\pi(a-b)$ → high‑precision ellipse perimeter ($1.87\!\times\!10^{-7}\%$ error)
- **One‑to‑one correspondence** $t_k \leftrightarrow e_k$ validated for 113 zeros (forward precision $10^{-159}$, backward error $10^{-16}$)
- **Geometric inversion of $\pi$** $\pi = \gamma_E/(2J_\infty)$
- **Consequence** Under the proposed axioms, the Riemann hypothesis holds (all non‑trivial zeros have real part $1/2$)

---

## 🧪 Numerical Data

The CSV files provide:
- `zero_reproduction_100_zeros.csv` – For the first 113 non‑trivial zeros: actual $t_k$, reproduced $t_k$, error, eccentricity $e_k$.
- `zero_reproduction_validation.csv` – Detailed geometric parameters ($a$, $b$, $e_k$) for the first 20 zeros.

All data are machine‑precision and fully reproducible.

---

## 🔗 DOI & Citation

**This version (Z6) is archived on Zenodo with a permanent DOI:**  
[https://doi.org/10.5281/zenodo.19770193](https://doi.org/10.5281/zenodo.19770193)

### BibTeX
```bibtex
@article{Jie2026Geometric,
  title   = {A Geometric Interpretation of the Riemann Hypothesis: A Unified Framework Based on the J-Constant and Ellipse Compensation Identity},
  author  = {Jie, Peiying},
  journal = {Zenodo},
  year    = {2026},
  doi     = {10.5281/zenodo.19770193},
  url     = {https://github.com/J-constant-math/-J-constant-Riemann-}
}
```

---

📎 Related Preprints

· Ellipse circumference compensation (v4/v5 algorithm, polynomial correction)
    DOI: 10.5281/zenodo.19687408 – GitHub ellipse-compensation

---

📜 License

This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

---

✨ Acknowledgements

The author thanks the open‑source mathematical community (LMFDB, Odlyzko) for high‑precision zero data, and the AI assistants Doubao, Kimi, and DeepSeek for collaborative theoretical derivation, numerical validation, and logical review. Their synergistic cooperation greatly facilitated this research.

---

Maintainer: Peiying Jie – GitHub
Repository: J-constant-math/-J-constant-Riemann-

```
