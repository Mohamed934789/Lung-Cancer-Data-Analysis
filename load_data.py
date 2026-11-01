from pathlib import Path
import zipfile
import pandas as pd
def load_existing():
    root=Path(__file__).resolve().parent
    raw=root/"Lung Cancer.csv"
    if raw.exists():return pd.read_csv(raw)
    with zipfile.ZipFile(root/"cancer_analysis_final.zip") as archive:
        member=next(n for n in archive.namelist() if n.endswith(".csv"))
        with archive.open(member) as source:return pd.read_csv(source)
