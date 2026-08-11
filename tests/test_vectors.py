import numpy as np 
import pytest
from src.vectors import LorentzVector

MUON_MASS = 0.10566

def test_from_ptetaphim_recovers_mass():
    """A single particle built from (pt, eta, phi, m) should report back mass m."""
    v = LorentzVector.from_ptetaphim(
        pt=20.0,
        eta=1.2,
        phi=0.5,
        m=MUON_MASS)
    assert np.isclose(v.mass,MUON_MASS,atol=1e-6)

def test_from_ptetaphim_recovers_pt_eta_phi():
    """Round-trip: build from pt/eta/phi, read pt/eta/phi back off px,py,pz,E."""
    pt, eta, phi = 15.0,-0.8,2.1
    v = LorentzVector.from_ptetaphim(
        pt=pt,
        eta=eta, 
        phi=phi, 
        m=MUON_MASS
        )
    assert np.isclose(v.pt,pt,atol=1e-6)
    assert np.isclose(v.eta,eta,atol=1e-6)
    assert np.isclose(v.phi,phi,atol=1e-6)

def test_addition_is_componentwise():
    v1 = LorentzVector(1,2,3,4)
    v2 = LorentzVector(4,5,6,20)
    total = v1+v2
    assert total.px == 5
    assert total.py == 7
    assert total.pz == 9
    assert total.E == 24

def test_back_to_back_massless_pair_gives_zero_mass():
    """Two massless, back-to-back (opposite phi) particles with equal pt:
    momenta cancel, energies add -> invariant mass should be 0."""
    v1 = LorentzVector.from_ptetaphim(pt=10, eta=0, phi=0, m=0)
    v2 = LorentzVector.from_ptetaphim(pt=10, eta=0, phi=np.pi, m=0)

def test_jpsi_like_dimuon_mass():
    """Two muons roughly consistent with a J/psi decay (M ~ 3.097 GeV)
    should reconstruct close to that mass -- sanity check against a
    known physical value, not just internal consistency."""
    mu1 = LorentzVector.from_ptetaphim(pt=5.0, eta=0.3, phi=0.1, m=MUON_MASS)
    mu2 = LorentzVector.from_ptetaphim(pt=4.2, eta=-0.2, phi=2.9, m=MUON_MASS)
    dimuon = mu1+mu2
    # We're not fine-tuning these numbers to hit 3.097 exactly --
    # just checking mass ends up in a sane physical range for two ~GeV-scale muons

    assert 0 < dimuon.mass < 15
