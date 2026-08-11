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

    mask = (
        (df["Q1"] * df["Q2"] < 0)
        & (df["Type1"] == "G")
        & (df["Type2"] == "G")
    )

    return df[mask]