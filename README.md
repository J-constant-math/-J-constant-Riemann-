# J-Constant Wall-Thickness Framework for the Riemann Zeros

**Author:** Peiying Jie (揭培英)  
**Date:** April 25, 2026  
**License:** CC BY 4.0  
**Repository:** https://github.com/J-constant-math/J-constant-Riemann

---

## Overview

This repository contains the complete LaTeX source, numerical data, and code for the paper:

> **"From Geometric Analogy to the Riemann Zeros: The J-Constant Wall-Thickness Framework with Numerical Evidence"**

The work introduces a geometric framework for the non‑trivial zeros of the Riemann zeta function, based on a **constant wall thickness** derived from the Euler–Mascheroni constant \(\gamma\).

---

## Key Contributions

- **Geometric Heuristic:** A circle–ellipse analogy linking harmonic numbers \(H_n\) and \(\ln n\) to the critical line \(\operatorname{Re}(s)=1/2\).
- **Elliptic Model:** Dynamic wall thickness \(J(t)=a(t)-b(t)\) with semi‑axes \(a(t), b(t)\).
- **Discriminant Function:**  
  \[
  \Psi(t)=|\zeta(1/2+it)|^2 + \left(\frac{J(t)-J_\infty}{2\pi}\right)^2
  \]
- **Integral Equation:** Hilbert transform coupling \(J(t)\) to the Riemann–Siegel function \(Z(t)\).
- **Numerical Validation:** First 100 zeros show \(\Psi(t_n)\sim10^{-31}\); non‑zeros give \(\Psi(t)\sim10^{-1}\)–\(10^1\); separation ratio \(>10^{26}\).

**Note:** This work does not claim a full analytic proof of the Riemann hypothesis. It provides a geometric interpretation, a partial equivalence (necessity direction), and strong numerical evidence.

---

## Repository Contents (V3)

| File | Description |
|------|-------------|
| `JConstant_WallThickness_RiemannZeros.tex` | LaTeX source of the paper |
| `JConstant_WallThickness_RiemannZeros.pdf` | Final compiled PDF |
| `figure1.png` | Discriminant \(\Psi(t_n)\) at the first 100 zeros |
| `figure2.png` | Separation between zeros and non‑zeros |
| `figure3.png` | Four‑panel comprehensive analysis |
| `j_constant_v3_100zeros_final.csv` | Data for zeros 1–100 (V3) |
| `j_constant_v3_nonzeros_final.csv` | Data for 10 non‑zero points (V3) |
| `j_constant_algorithm.py` | Numerical verification code (elliptic integrals, discriminant) |
| `integral_equation_verification.py` | Verification of the integral equation (constructive definition at zeros) |
| `requirements.txt` | Python dependencies (`numpy`, `scipy`, `mpmath`) |

> **Note:** Earlier versions (V1, V2) are archived in the `archive/` folder.

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/J-constant-math/J-constant-Riemann.git
cd J-constant-Riemann
