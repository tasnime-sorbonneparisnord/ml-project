```markdown
# ML Translation Pipeline (Helsinki-NLP OPUS-MT)

## Project Description
This project implements an end-to-end machine translation pipeline with automatic evaluation of translation quality. The system is modular, extensible, and organized around a central orchestrator that coordinates all processing steps.

The pipeline uses a pretrained HuggingFace model (Helsinki-NLP/opus-mt-fr-en) to translate French text into English and evaluates the output using the BLEU score metric.

---

## Objective
The goal of this project is to:
- Translate a dataset of French sentences into English
- Process and clean input data
- Evaluate translation quality using BLEU score
- Demonstrate a modular machine learning pipeline architecture

---

## Project Structure

```

src/
│
├── loaders/         # Load input data (CSV, JSON, etc.)
├── translators/     # HuggingFace translation models
├── processors/      # Data preprocessing and cleaning
├── evaluators/      # BLEU score evaluation
├── orchestrator/    # Main pipeline controller
├── config.py        # Configuration settings
├── main.py          # Entry point

````

---

## Pipeline Workflow

The orchestrator performs the following steps:

1. Load dataset (CSV or JSON)
2. Translate text using HuggingFace model
3. Apply optional preprocessing
4. Compute BLEU score
5. Save and display results

---

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
````

### 2. Run the pipeline

```bash
python main.py
```

---

## Example Output

```
Pipeline started...
Translations: ['bonjour -> translated', 'je suis étudiant -> translated']
BLEU score: 0.75
Pipeline finished
```

---

## Technologies Used

* Python 3
* HuggingFace Transformers
* PyTorch backend
* NLTK BLEU evaluation
* Modular OOP architecture

---

## Dataset

Input data is located in the data/ folder and can include:

* JSON files
* CSV files
* Custom text datasets

---

## Authors

Hakimi Tasnime + Aoun Myriam

---

## Status

Fully functional pipeline
Modular architecture
Translation and evaluation working

```
```
