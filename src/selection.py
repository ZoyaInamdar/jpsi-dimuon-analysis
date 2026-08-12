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