# 🧠 Machine Learning & Deep Learning Specialization

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge)](https://matplotlib.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

Comprehensive collection of labs, coursework, practice assignments, and custom implementations for the **Machine Learning & Deep Learning Specialization** offered by **Stanford Online** and **DeepLearning.AI**, instructed by **Andrew Ng**.

---

## 📌 Table of Contents
- [About The Specialization](#-about-the-specialization)
- [Repository Structure](#-repository-structure)
- [Course Roadmap](#-course-roadmap)
  - [Course 1: Supervised Machine Learning (Regression & Classification)](#course-1-supervised-machine-learning---regression--classification)
- [Getting Started & Installation](#-getting-started--installation)
- [Credits & Attributions](#-credits--attributions)
- [Author](#-author)

---

## 📖 About The Specialization

This repository tracks my journey through the Machine Learning Specialization. It covers fundamental and advanced machine learning concepts, including:
- **Supervised Learning**: Linear Regression, Logistic Regression, Feature Engineering, Regularization, and Gradient Descent.
- **Unsupervised Learning**: Clustering, Anomaly Detection, Recommender Systems, and Reinforcement Learning.
- **Deep Learning**: Neural Networks, Activation Functions, Model Evaluation, Decision Trees, and Hyperparameter Tuning.

All notebooks contain complete implementations, math visualizations, vectorization techniques, and bug-fixes for seamless interactive execution.

---

## 📁 Repository Structure

```text
ML-DL-Specalization/
├── Machine Learning/
│   └── Course 1/
│       ├── Week 1/                          # Linear Regression with One Variable
│       │   ├── deeplearning.mplstyle         # Custom Matplotlib stylesheet
│       │   ├── lab_utils_common.py          # Common plotting utilities
│       │   ├── lab_utils_uni.py             # Univariate plotting helpers
│       │   ├── LAB 1.ipynb                  # Model Representation
│       │   ├── LAB 2.ipynb                  # Cost Function Intuition
│       │   └── LAB 3.ipynb                  # Gradient Descent Implementation
│       │
│       ├── Week 2/                          # Multiple Linear Regression & Feature Engineering
│       │   ├── data/                        # Datasets (houses.txt, ex1data1.txt, ex1data2.txt)
│       │   ├── deeplearning.mplstyle         # Stylesheet
│       │   ├── lab_utils_common.py          # Common utilities
│       │   ├── lab_utils_multi.py           # Multivariate plotting helpers
│       │   ├── public_tests.py              # Test suite for practice lab
│       │   ├── utils.py                     # Data loading utilities
│       │   ├── LAB 1.ipynb                  # NumPy & Vectorization
│       │   ├── LAB 2.ipynb                  # Multiple Linear Regression
│       │   ├── LAB 3.ipynb                  # Feature Scaling & Normalization
│       │   ├── LAB 4.ipynb                  # Feature Engineering & Polynomial Regression
│       │   ├── LAB 5.ipynb                  # Sklearn SGDRegressor
│       │   └── Week 2 Practive Lab-Linear Regression.ipynb  # Practice Assignment
│       │
│       └── Week 3/                          # Classification & Logistic Regression
│           ├── deeplearning.mplstyle         # Stylesheet
│           ├── lab_utils_common.py          # Common utilities
│           ├── plt_logistic_loss.py         # Logistic loss plotting routines
│           ├── plt_one_addpt_onclick.py     # Interactive decision boundary plot
│           ├── plt_overfit.py               # Overfitting visualization
│           ├── plt_quad_logistic.py         # Quadratic boundary visualization
│           ├── LAB 1.ipynb                  # Classification & Decision Boundaries
│           ├── LAB 2.ipynb                  # Logistic Loss & Cost Function
│           └── LAB 3.ipynb                  # Gradient Descent for Logistic Regression
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🗺️ Course Roadmap

### Course 1: Supervised Machine Learning - Regression & Classification

* **Week 1: Introduction to Machine Learning & Univariate Linear Regression**
  * Model representation, hypothesis function $f_{w,b}(x) = wx + b$.
  * Squared error cost function $J(w,b)$.
  * Gradient descent algorithm & parameter update rules.

* **Week 2: Multiple Linear Regression, Feature Scaling & Scikit-Learn**
  * Vectorization using NumPy for fast matrix computation.
  * Gradient descent for multiple variables $f_{\mathbf{w},b}(\mathbf{x}) = \mathbf{w} \cdot \mathbf{x} + b$.
  * Feature scaling techniques (Z-score normalization & Min-Max scaling).
  * Polynomial feature engineering to fit non-linear curves.
  * Linear Regression using `scikit-learn` (`SGDRegressor` & `StandardScaler`).

* **Week 3: Classification, Logistic Regression & Overfitting**
  * Sigmoid / Logistic activation function $g(z) = \frac{1}{1 + e^{-z}}$.
  * Decision boundaries & Non-linear boundaries.
  * Logistic Loss Function & Convex Cost Function.
  * Gradient descent for Logistic Regression.

---

## ⚙️ Getting Started & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Khubaib7-del/ML-DL-Specalization.git
cd ML-DL-Specalization
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install numpy matplotlib scipy scikit-learn jupyter ipywidgets
```

### 4. Launch Jupyter Notebook
```bash
jupyter notebook
```

---

## 💳 Credits & Attributions

> **Course Attribution & License Notice**:
> All original course structure, lecture concepts, initial assignment frameworks, helper scripts (`lab_utils_*.py`, `plt_*.py`), and datasets are property of **DeepLearning.AI**, **Stanford Online**, and **Andrew Ng**.
> 
> This repository contains my personal solutions, bug fixes (e.g. Matplotlib 3.7+ compatibility, path resolution), interactive visual enhancements, and completed lab exercises published for educational purposes and personal portfolio presentation.

---

## 👤 Author

* **Khubaib Nazeer**
  * GitHub: [@Khubaib7-del](https://github.com/Khubaib7-del)
