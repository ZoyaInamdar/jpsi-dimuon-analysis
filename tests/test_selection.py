import pandas as pd

from src.selection import select_opposite_sign_global_muons


def test_selects_opposite_sign_global_muons():
    df = pd.DataFrame({
        "Q1": [1, 1, -1, -1],
        "Q2": [-1, 1, 1, 1],
        "Type1": ["G", "G", "T", "G"],
        "Type2": ["G", "G", "G", "G"],
        "Pt1": [5,5,5,5],
        "Pt2": [5,5,5,5],
        "Eta1": [1.0,1.0,1.0,1.0],
        "Eta2": [1.0,1.0,1.0,1.0],
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
        "Pt1": [5,5],
        "Pt2": [5,5],
        "Eta1": [1.0,1.0],
        "Eta2": [1.0,1.0],
    })

    selected = select_opposite_sign_global_muons(df)

    assert len(selected) == 0


def test_rejects_non_global_muons():
    df = pd.DataFrame({
        "Q1": [1, -1],
        "Q2": [-1, 1],
        "Type1": ["T", "G"],
        "Type2": ["G", "T"],
        "Pt1": [5,5],
        "Pt2": [5,5],
        "Eta1": [1.0,1.0],
        "Eta2": [1.0,1.0],
    })

    selected = select_opposite_sign_global_muons(df)

    assert len(selected) == 0

def test_rejects_low_pt_muons():
    df = pd.DataFrame({
        "Q1": [1],
        "Q2": [-1],
        "Type1": ["G"],
        "Type2": ["G"],
        "Pt1": [2.9],
        "Pt2": [5.0],
        "Eta1": [1.0],
        "Eta2": [1.0],
    })

def test_rejects_muons_outside_eta_acceptance():
    df = pd.DataFrame({
        "Q1": [1],
        "Q2": [-1],
        "Type1": ["G"],
        "Type2": ["G"],
        "Pt1": [5.0],
        "Pt2": [5.0],
        "Eta1": [2.5],
        "Eta2": [1.0],
    })

    selected = select_opposite_sign_global_muons(df)

    assert len(selected) == 0