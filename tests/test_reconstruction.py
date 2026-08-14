import numpy as np
from src.reconstruction import build_muon_vectors, reconstruct_dimuon

def test_build_muon_vectors():
    row = {
        "Pt1":5.0,
        "Eta1":0.3,
        "Phi1":0.1,
        "Pt2":4.2,
        "Eta2":-0.2,
        "Phi2":2.9,
    }

    mu1, mu2 = build_muon_vectors(row)

    assert np.isclose(mu1.pt, 5.0)
    assert np.isclose(mu1.eta, 0.3)
    assert np.isclose(mu1.phi, 0.1)

    assert np.isclose(mu2.pt, 4.2)
    assert np.isclose(mu2.eta, -0.2)
    assert np.isclose(mu2.phi, 2.9)


def reconstruct_dimuon(row):
    """reconstruct combined 4 vector of 2 muons"""
    mu1, mu2 = build_muon_vectors(row)
    return mu1+mu2

def test_reconstruct_dimuon():
    row = {
        "Pt1": 5.0,
        "Eta1": 0.3,
        "Phi1": 0.1,
        "Pt2": 4.2,
        "Eta2": -0.2,
        "Phi2": 2.9,
    }

    dimuon = reconstruct_dimuon(row)

    assert dimuon.px != 0
    assert dimuon.py != 0
    assert dimuon.E > 0
    assert dimuon.mass > 0

def test_reconstruct_dimuon_mass():
    row = {
        "Pt1": 5.0,
        "Eta1": 0.3,
        "Phi1": 0.1,
        "Pt2": 4.2,
        "Eta2": -0.2,
        "Phi2": 2.9,
    }

    dimuon = reconstruct_dimuon(row)

    mu1, mu2 = build_muon_vectors(row)

    expected_mass = np.sqrt(
        (mu1.E + mu2.E)**2
        -(mu1.px+mu2.px)**2
        -(mu1.py+mu2.py)**2
        -(mu1.pz+mu2.pz)**2
    )

    assert np.isclose(dimuon.mass, expected_mass)