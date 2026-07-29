import numpy as np

class LorentzVector:
    """
    A four-momentum vector (px, py, pz, E), the fundamental object
    for combining particles and computing invariant masses.
    """
    
    def __init__(self,px,py,pz, E):
        self.px = px
        self.py = py
        self.pz = pz
        self.E = E

    @classmethod
    def from_ptetaphim(cls, pt, eta, phi, m):
        """Build a LorentzVector from detector-style (pt, eta, phi, mass)."""
        px = pt*np.cos(phi)
        py = pt*np.sin(phi)
        pz = pt*np.sinh(eta)
        p = pt*np.cosh(eta)
        E = np.sqrt(p**2 + m**2)
        return cls(px, py, pz, E)
    
    def __add__(self, other):
        return LorentzVector(
            self.px + other.px,
            self.py + other.py,
            self.pz + other.pz,
            self.E + other.E,
        )
    
    @property
    def p(self):
        """Magnitude of 3-momentum."""
        return np.sqrt(self.px**2+self.py**2+self.pz**2)
   
    @property 
    def eta(self):
        return np.sqrt(self.px**2+self.py**2)
    
    @property
    def phi(self):
        return np.arctan2(self.py, self.px)
    
    @property
    def mass2(self):
        """Invariant mass squared — can go slightly negative for numerical noise."""
        return self.E**2 - self.px**2 - self.py**2 - self.pz**2
    
    @property
    def mass(self):
        m2 = self.mass2
        return np.sqrt(m2) if m2 >= 0 else -np.sqrt(-m2)
    
    def __repr__(self):
        return f"LorentzVector(px={self.px:.3f},py = {self.py:.3f},pz={self.E:.3f})"
    
