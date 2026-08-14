import matplotlib.pyplot as plt

def plot_dimuon_mass(masses):
    """plotting invariant mass distribution of dimuon canditates"""
    plt.hist(masses, bins=50)
    plt.xlabel("dimuon invariant mass [GeV]")
    plt.ylabel("events")
    plt.title("dimuon invariant mass")
    plt.show()