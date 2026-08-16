import matplotlib.pyplot as plt
import numpy as np

from src.io import load_events
from src.selection import find_muon_pairs
from src.reconstruction import reconstruct_cms_dimuon

FILE="data/054FF886-5548-4434-A52A-F85C24B0F7F8.root"

print("loading events..")
events=load_events(FILE)

print("finding muon pairs..")
pairs = find_muon_pairs(events)

print("Reconstructing masses...")

masses = []

for pair in pairs:
    event_idx, _, _ = pair

    dimuon = reconstruct_cms_dimuon(
        events[event_idx],
        pair,
    )

    masses.append(dimuon.mass)

masses = np.asarray(masses)

jpsi_masses=masses[
    (masses>=2.5)&
    (masses<=3.5)
]

print("total masses:", len(masses))
print("masses in J/psi region:", len(jpsi_masses))

plt.figure(figsize=(10,6))

plt.hist(
    jpsi_masses,
    bins=100,
    range=(2.5,3.5),
)

plt.axvline(
    3.0969,
    linestyle="--",
    label=r"Known $J/\psi$ mass"
)

plt.xlabel(r"$m_{\mu\mu}$ [GeV]")
plt.ylabel("Number of candidates")
plt.title(r"$J/\psi \rightarrow \mu^+\mu^-$ invariant mass")
plt.legend()

plt.tight_layout()

plt.savefig(
    "plots/jpsi_mass.png",
    dpi=150
)


plt.show()
