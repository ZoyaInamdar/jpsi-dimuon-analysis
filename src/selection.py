def select_opposite_sign_global_muons(df):
    """
    Select dimuon events where:
    - The two muons have opposite charge.
    - Both muons are global muons.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing Q1, Q2, Type1 and Type2.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing only events passing the selection.
    """

    opposite_sign = df["Q1"]*df["Q2"] < 0
    
    global_muons = (
        (df["Type1"] == "G")
        & (df["Type2"] == "G")
    )

    pt_cut = (
        (df["Pt1"]>3.0)
        & (df["Pt2"]>3.0)
    )

    eta_cut = (
        (df["Eta1"].abs()<2.4)
        & (df["Eta2"].abs()<2.4)
    )

    mask = (
        opposite_sign
        & global_muons
        & pt_cut
        & eta_cut
    )

    return df[mask]

def find_muon_pairs(events):
    """finding opp sign global muon pairs passing kinematic cuts"""
    pairs = []

    for event_index,event in enumerate(events):
        pt=event["Muon_pt"]
        eta=event["Muon_eta"]
        charge=event["Muon_charge"]
        is_global=event["Muon_isGlobal"]

        n_muons=len(pt)

        for i in range(n_muons):
            for j in range(i+1, n_muons):
                if charge[i]*charge[j]>=0:
                    continue
                if not is_global[i] or not is_global[j]:
                    continue
                if pt[i]<=3.0 or pt[j]<=3.0:
                    continue
                if abs(eta[i])>=2.4 or abs(eta[j])>=2.4:
                    continue
                pairs.append((event_index,i,j))

    return pairs