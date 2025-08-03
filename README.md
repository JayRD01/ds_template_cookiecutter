# 🚀 ds_template_cookiecutter

Welcome to **`ds_template_cookiecutter`**, a professional and production-ready template for data science projects — built with ❤️ by **JayRD** using [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/).

This repository gives you a powerful, clean, and modular foundation to kickstart any serious data science project, whether you're building ETL pipelines, training ML models, or delivering visual reports.

---

## ✨ What You'll Find in This Template

✅ **Cookiecutter-ready** structure  
✅ **Modern environment management** with `conda`  
✅ **Modular project layout** for scalability  
✅ **Editable install mode** for reusable packages  
✅ **Notebook-friendly tools** with autoreload and `nbdime`  
✅ **Invoke** tasks for automation  
✅ Fully customizable and easy to extend

---

## 🧪 Getting Started

### 🔧 Requirements

- Python ≥ 3.8  
- Conda or Mamba  
- Cookiecutter  
- Git (recommended)

### 📦 Create a new project

```bash
pip install cookiecutter
cookiecutter https://github.com/JayRD01/ds_template_cookiecutter.git
```

---

## ⚙️ Setup Your Project

After generating the project:

```bash
cd your_project_folder
conda env create -f environment.yml
conda activate your_project_folder
pip install --editable .
```

Then you're ready to go!

---

## 🧰 Project Structure

```text
{{ cookiecutter.project_slug }}
├── data/                  # Organized data folders
│   ├── raw/               # Raw data (immutable)
│   ├── processed/         # Cleaned and engineered
│   └── external/          # 3rd-party or shared sources
│
├── models/                # Trained ML models
├── notebooks/             # Jupyter notebooks
├── outputs/               # Reports, plots, deliverables
│   └── reports/
│       └── visualization/ # Visual components
│
├── scripts/               # Modular and reusable code
├── tests/                 # Unit tests
│
├── environment.yml        # Conda environment config
├── install.md             # Full setup instructions
├── tasks.py               # Automation with Invoke
├── setup.py               # pip installable module
├── .gitignore             # Git tracking rules
├── .here                  # Project root marker
├── LICENSE                # MIT License
└── README.md              # This file 🧠
```

---

## 📌 Why Use This Template?

- 🧼 **Well-structured** and production-focused
- 🧪 **Test-ready** and automation-friendly
- 🔁 **Reusable modules** with editable installs
- 📊 **Jupyter-first** design with `autoreload` and `nbdime`
- 🚀 **Perfect for teams or solo developers**

---

## ✍️ Author

**JayRD**  
GitHub: [@JayRD01](https://github.com/JayRD01)

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for full details.
