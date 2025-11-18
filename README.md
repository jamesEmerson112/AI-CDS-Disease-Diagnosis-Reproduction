# AI-CDS-Disease-Diagnosis-Reproduction

An AI-powered clinical decision support system for disease diagnosis using sentence embeddings. This system predicts diagnoses based on symptom similarity using sent2vec embeddings and K-fold cross-validation.

## Overview

This project implements a machine learning approach to disease diagnosis by:
- Converting symptoms and diagnoses to vector embeddings using sent2vec
- Computing similarity between test symptoms and training data
- Predicting diagnoses based on highest similarity scores
- Evaluating performance using 10-fold cross-validation

## Prerequisites

- **Python**: 3.6 or higher
- **C Compiler**: Required for Cython compilation (GCC on Linux/Mac, MSVC on Windows)
- **Pre-trained Model**: sent2vec or fasttext pre-trained model (BioWordVec or similar biomedical model recommended)

### Required Python Packages
- numpy
- scipy
- scikit-learn
- gensim
- sent2vec
- Cython

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/jamesEmerson112/AI-CDS-Disease-Diagnosis-Reproduction.git
cd AI-CDS-Disease-Diagnosis-Reproduction
```

### 2. Install Python Dependencies
```bash
pip install numpy scipy scikit-learn gensim sent2vec Cython
```

Or create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install numpy scipy scikit-learn gensim sent2vec Cython
```

### 3. Compile Cython Module
The `util_cy.c` file contains Cython-optimized methods. Compile it before running:
```bash
python setup.py build_ext --inplace
```

### 4. Download Pre-trained Model
Download a pre-trained sent2vec or fasttext model (biomedical domain recommended):
- Place the model file in the project directory
- Update the model loading path in `util_cy.c` or `CS2V.py`

## Configuration

### Important: Update Working Directory
Before running the project, you **must** update the `CH_DIR` constant in `utils/Constants.py`:

```python
CH_DIR = "/path/to/your/AI-CDS-Disease-Diagnosis-Reproduction"
```

Replace with your actual project directory path.

### Configurable Parameters (utils/Constants.py)

- `K_FOLD`: Number of cross-validation folds (default: 10)
- `TOP_K_LOWER_BOUND`: Minimum Top-K value (default: 10)
- `TOP_K_UPPER_BOUND`: Maximum Top-K value (default: 60)
- `TOP_K_INCR`: Top-K increment step (default: 10)
- `PRUNING_SIMILARITY`: Similarity threshold for pruning (default: 0.5)
- `MIN_SIMILARITY`: Minimum similarity threshold (default: 0)

## How to Run

### Basic Execution
```bash
python CS2V.py
```

The script will:
1. Load the symptoms-diagnosis dataset
2. Load the pre-trained embedding model
3. Generate embeddings for symptoms and diagnoses
4. Run 10-fold cross-validation
5. Compute predictions and performance metrics
6. Generate output files with results

### Expected Output
- **Console**: Progress information for each fold
- **Files**: 
  - `Prediction Output_[timestamp]/` - Prediction results for each fold
  - `Prediction Symptom Details_[timestamp]/` - Detailed symptom-level analysis
  - `PerformanceIndex.txt` - Aggregated performance metrics

### Runtime
Processing time depends on:
- Dataset size
- Number of folds
- Model complexity
- Hardware specifications

Expect several minutes to hours for complete execution.

## Dataset Structure

### Input Format
**Symptoms-Diagnosis.txt**: Semicolon-separated file with format:
```
HADM_ID;SUBJECT_ID;ADMIT_TIME;DISCHARGE_TIME;SYMPTOMS;DIAGNOSIS
```

### Cross-Validation Folds
The `Dataset/` directory contains 10 pre-split folds (Fold0-Fold9):
- `TrainingSet.txt`: Training data for each fold
- `TestSet.txt`: Test data for each fold

Each fold represents a different train-test split for cross-validation.

## Output Description

### Prediction Output
- **Prediction files**: Individual prediction results for each test case
- **Performance metrics**: Confusion matrices, accuracy, precision, recall, F-score
- **Similarity matrices**: Computed similarities between test and training samples

### Performance Index
The system evaluates predictions using:
- **TP** (True Positives)
- **FP** (False Positives)
- **P** (Precision)
- **R** (Recall)
- **FS** (F-Score)
- **PR** (Performance Ratio)

Results are computed for:
- Maximum similarity predictions
- Top-K similarity predictions (K = 10, 20, 30, 40, 50)

## Project Structure

```
AI-CDS-Disease-Diagnosis-Reproduction/
├── CS2V.py                      # Main execution script
├── util_cy.c                    # Cython-optimized utility methods
├── Symptoms-Diagnosis.txt       # Sample input data
├── entity/                      # Data model classes
│   ├── __init__.py
│   ├── Admission.py            # Admission data model
│   ├── Drgcodes.py             # DRG codes model
│   ├── Symptom.py              # Symptom model
│   └── SymptomsDiagnosis.py    # Main symptoms-diagnosis model
├── utils/                       # Utility modules
│   ├── __init__.py
│   └── Constants.py            # Configuration constants
└── Dataset/                     # Cross-validation datasets
    ├── Fold0/
    │   ├── TrainingSet.txt
    │   └── TestSet.txt
    ├── Fold1/ ... Fold9/        # Additional folds
```

## Troubleshooting

### Common Issues

**Import Error: No module named 'util_cy'**
- Ensure Cython module is compiled: `python setup.py build_ext --inplace`

**FileNotFoundError**
- Verify `CH_DIR` in `utils/Constants.py` points to correct directory
- Ensure all dataset files exist in `Dataset/Fold*/`

**Model Loading Error**
- Confirm pre-trained model file exists
- Check model path in code
- Verify model format compatibility

**Memory Error**
- Reduce dataset size
- Reduce number of folds
- Use a machine with more RAM

## Citation

If you use this code in your research, please cite the original paper or repository.

## License

See LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contact

For questions or issues, please open an issue on GitHub.
