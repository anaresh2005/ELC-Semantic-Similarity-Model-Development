import pandas as pd


def eval_fuzzy(df: pd.DataFrame) -> pd.DataFrame:
    manual = df[df["manual_match"] == "YES"]
    match_count = (manual["row_number"] == 1).sum()
    fuzzy_pct = match_count / len(manual) * 100
    print(f"Fuzzy percentage: {fuzzy_pct:.2f}%")


def eval_trans(df: pd.DataFrame) -> pd.DataFrame:
    manual = df[df["manual_match"] == "YES"]
    df["max_sim"] = df.groupby("npl_prodord")["similarity_score"].transform("max")
    df["trans_manual_match"] = (df["similarity_score"] == df["max_sim"]) & (
        df["manual_match"] == "YES"
    )
    trans_pct = df["trans_manual_match"].sum() / len(manual) * 100
    print(f"Sentence Transformer percentage: {trans_pct:.2f}%")
