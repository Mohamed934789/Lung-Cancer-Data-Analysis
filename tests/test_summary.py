import pandas as pd
from data_summary import summarize
def test_summary_uses_all_rows_without_patient_identifiers():
    frame=pd.DataFrame({"patient_name":["fictional"]*501,"gender":["A"]*500+["B"],"survived":[0]*500+[1]})
    result=summarize(frame)
    assert result["rows"]==501 and result["gender_counts"]["B"]==1
    assert "patient_name" not in str({k:v for k,v in result.items() if k!="missing_values"})
