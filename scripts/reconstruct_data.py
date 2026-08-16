import awkward as ak

from src.io import load_events
from src.selection import find_muon_pairs
from src.reconstruction import reconstruct_cms_dimuon

FILE="data/054FF886-5548-4434-A52A-F85C24B0F7F8.root"

print("Loading events...")
events=load_events(FILE)

print("Events loaded:", len(events))

print("Finding muon pairs...")
pairs=find_muon_pairs(events)

print("number of selected pairs: ",len(pairs))

masses = []

print("Reconstructing masses...")

for pair in pairs:
    event_idx,_,_=pair

    dimuon=reconstruct_cms_dimuon(
        events[event_idx],
        pair,
    )
    masses.append(dimuon.mass)

masses = ak.Array(masses)

print("number of reconstructed masses: ", len(masses))
print("first 10 masses: ", masses[:10])