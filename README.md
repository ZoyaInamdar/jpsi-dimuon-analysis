# J/ψ Dimuon Invariant Mass Analysis

## Overview

This project reconstructs the J/ψ meson from real proton-proton collision data collected by the CMS detector at CERN's Large Hadron Collider.

The analysis will:

- Read CMS Open Data ROOT files using Uproot
- Reconstruct muon four-vectors
- Compute dimuon invariant masses
- Identify the J/ψ resonance
- Fit the signal using Gaussian and Crystal Ball models
- Estimate the statistical significance of the signal

## Tech Stack

- Python
- Uproot
- Awkward Array
- NumPy
- SciPy
- Matplotlib
- ROOT
- LaTeX