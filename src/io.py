import uproot

def load_events(path, entry_start=None, entry_stop=None):
    """loading the data from the root file"""

    branches = [
        "Muon_pt",
        "Muon_eta",
        "Muon_phi",
        "Muon_mass",
        "Muon_charge",
        "Muon_isGlobal",
        "Muon_isTracker",
    ]

    tree = uproot.open(path)["Events"]

    return tree.arrays(
        branches,
        entry_start=entry_start,
        entry_stop=entry_stop,
        library="ak",
    )