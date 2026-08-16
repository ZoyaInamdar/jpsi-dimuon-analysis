from src.vectors import LorentzVector

MUON_MASS = 0.10566

def build_muon_vectors(row):
    """build two muon four vectors from one dataframe row"""

    mu1 = LorentzVector.from_ptetaphim(
        pt=row["Pt1"],
        eta=row["Eta1"],
        phi=row["Phi1"],
        m=MUON_MASS,
    )

    mu2 = LorentzVector.from_ptetaphim(
        pt=row["Pt2"],
        eta=row["Eta2"],
        phi=row["Phi2"],
        m=MUON_MASS,
    )
    return mu1, mu2

def reconstruct_dimuon(row):
    """Reconstruct the combined four-vector of the two muon"""

    mu1, mu2 = build_muon_vectors(row)

    return mu1 + mu2

def calculate_dimuon_mass(row):
    """calculating invariant mass of 2 muon system"""

    dimuon = reconstruct_dimuon(row)
    return dimuon.mass

def calculate_dimuon_masses(df):
    """calculate dimuon invariant mass for every event"""
    return df.apply(calculate_dimuon_mass, axis=1)

def reconstruct_selected_events(df):
    """calculating dimuon masses for already selected events"""
    masses = calculate_dimuon_masses(df)
    return masses

def reconstruct_cms_dimuon(event, pair):
    """reconstructinh dimuon 4 vector from CMS event and selected muon pair"""

    _,i,j=pair

    mu1 = LorentzVector.from_ptetaphim(
        pt=event["Muon_pt"][i],
        eta=event["Muon_eta"][i],
        phi=event["Muon_phi"][i],
        m=event["Muon_mass"][i],
    )

    mu2 = LorentzVector.from_ptetaphim(
        pt=event["Muon_pt"][j],
        eta=event["Muon_eta"][j],
        phi=event["Muon_phi"][j],
        m=event["Muon_mass"][j],
    )

    return mu1+mu2