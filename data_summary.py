"""Deterministic aggregates; no patient rows are sent to a model."""
import pandas as pd

def summarize(frame):
    result={"rows":len(frame), "missing_values":frame.isna().sum().to_dict()}
    for col in ["gender","cancer_stage","treatment_type","smoking_status"]:
        if col in frame:
            result[col+"_counts"]=frame[col].fillna("Unknown").value_counts().to_dict()
            if "survived" in frame:
                result[col+"_observed_survival"]=frame.groupby(col,dropna=False)["survived"].agg(["count","mean"]).to_dict("index")
    return result
