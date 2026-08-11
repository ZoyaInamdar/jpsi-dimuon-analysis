import pandas as pd

from src.selection import select_opposite_sign_global_muons


def test_selects_opposite_sign_global_muons():
    df = pd.DataFrame({
        "Q1": [1, 1, -1, -1],
        "Q2": [-1, 1, 1, 1],
        "Type1": ["G", "G", "T", "G"],
        "Type2": ["G", "G", "G", "G"],
    })

    selected = select_opposite_sign_global_muons(df)

    assert len(selected) == 2
    assert list(selected.index) == [0, 3]


def test_rejects_same_sign_muons():
    df = pd.DataFrame({
        "Q1": [1, -1],
        "Q2": [1, -1],
        "Type1": ["G", "G"],
        "Type2": ["G", "G"],
    })

    selected = select_opposite_sign_global_muons(df)

    assert len(selected) == 0


def test_rejects_non_global_muons():
    df = pd.DataFrame({
        "Q1": [1, -1],
        "Q2": [-1, 1],
        "Type1": ["T", "G"],
        "Type2": ["G", "T"],
    })

    selected = select_opposite_sign_global_muons(df)

    assert len(selected) == 0