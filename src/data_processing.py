import pandas as pd


def drop_manual(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby(["npl_prodord"]).filter(
        lambda grp: (
            (grp["manual_match"] == "YES")
            & grp["npl_prodord_desc"].notna()
            & ~(
                grp["neighbor_prodord_desc"].isna()
                & grp["predecessor_prodord_desc_ramesses"].isna()
            )
        ).any()
    )


def drop_na(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna(
        subset=["predecessor_prodord_desc_ramesses", "neighbor_prodord_desc"]
    )


def process_data(df: pd.DataFrame) -> pd.DataFrame:
    df = drop_manual(df)
    df = drop_na(df)
    return df
