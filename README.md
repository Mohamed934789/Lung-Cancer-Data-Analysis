# Lung Cancer Dataset — exploratory learning project

This repository contains EDA, diagnostic ML baselines and an experimental aggregate-explanation UI.
It is not a clinical predictor. Original source/provenance of the large processed dataset needs owner confirmation.

Python 3.12: install `requirements.txt`; run the notebooks from here. `load_data.py` uses the raw
CSV if supplied, otherwise the retained processed ZIP. `Model.ipynb` evaluates a reproducible sample
of at most 20,000 rows against a majority baseline with minority-class metrics. Post-treatment
features and handwritten risk scores are excluded. No performance number is advertised as a validated result.

The original handwritten risk score in EDA is an unvalidated heuristic, not a medical score.
Run `python -m streamlit run chatbot5.py` only after setting your own `GEMINI_API_KEY` environment
variable. It sends deterministic full-dataset aggregates, not the first 500 patient rows, to the provider.
Provider calls may incur costs. Unsupported questions must remain unsupported by the aggregate evidence.

The previously committed Google key must be revoked by its owner if genuine; editing source does not
revoke it or erase history. No discovered credential was tested. The notebook's earlier sk-* matches
were sklearn HTML, not API keys. `pytest` tests cover aggregate correctness without provider calls.
