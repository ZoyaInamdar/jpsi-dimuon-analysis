import matplotlib.pyplot as plt
import numpy as np

from src.io import load_events
from src.selection import find_muon_pairs
from src.reconstruction import reconstruct_cms_dimuon

FILE="data/054FF886-5548-4434-A52A-F85C24B0F7F8.root"

print("loading events..")
events=load_events(FILE)

print("finding muon pairs..")
pairs=find_muon_pairs(events)

print("reconstructing masses..")

masses = []

for pair in pairs:
    event_idx,_,_=pair

    dimuon=reconstruct_cms_dimuon(
        events[event_idx],
        pair,
    )

    masses.append(dimuon.mass)

masses=np.asarray(masses)

print("no of masses: ",len(masses))

plt.figure(figsize=(10,6))

plt.hist(
    masses,
    bins=200,
    range=(0,20),
)

plt.xlabel(r"$m_{\mu\mu}$ [GeV]")
plt.ylabel("number of candidates")
plt.title("dimuon invariant mass spectrum")

plt.axvline(
    3.097,
    linestyle="--",
    label=r"$J/\psi$ mass"
)

plt.legend()

plt.tight_layout()

plt.savefig("plots.dimuon_mass.png", dpi=160)

plt.show()