# 🚀 ds_template_cookiecutter

Welcome to **`ds_template_cookiecutter`**, a professional and production-ready template for data science projects — built with ❤️ by **JayRD** using [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/).

This repository gives you a powerful, clean, and modular foundation to kickstart any serious data science project, whether you're building ETL pipelines, training ML models, or delivering visual reports.

---

## ✨ What You'll Find in This Template

✅ **Cookiecutter-ready** structure  
✅ **Modern environment management** with `conda`, `docker`, or `py_venv`  
✅ **Modular project layout** for scalability  
✅ **Editable install mode** for reusable packages  
✅ **Notebook-friendly tools** with autoreload and `nbdime`  
✅ **Invoke** tasks for automation  
✅ Fully customizable and easy to extend

---

## 🧪 Getting Started

### 🔧 Requirements

- Python ≥ 3.8  
- Conda or Mamba (or Docker)  
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

# If you chose conda
conda env create -f environment.yml
conda activate your_project_folder

# If you chose py_venv
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Then (in any case)
pip install --editable .
```

Then you're ready to go! 🎉

---

## 🧰 Project Structure (Generated Project)

```text
{{ cookiecutter.project_slug }}/
├── Dockerfile                # Container build instructions
├── docker-compose.yml        # Multi-container orchestration (optional)
├── environment.yml           # Conda environment specification
├── install.md                # Setup/installation notes
├── LICENSE                   # Project license
├── README.md                 # Project overview and usage instructions
├── requirements.txt          # pip-based dependency list (if not using conda)
├── scripts/                  # Utility scripts (ETL, automation, etc.)
│
├── models/                   # Trained and serialized ML models
│
├── notebooks/                # Jupyter notebooks for exploration and prototyping
│
├── outputs/                  # Generated outputs of the project
│   └── reports/              # Reports generated during experiments
│       └── visualization/    # Exported plots, charts, figures
│
├── src/                      # Source code (main package)
│   ├── app/                  # Application layer: orchestrates pipelines, CLI
│   ├── core/                 # Core domain logic
│   │   ├── contracts/        # Interfaces/ABCs/Protocols
│   │   └── implementations/  # Concrete classes implementing contracts
│   └── utils/                # Utility helpers (logging, validation, etc.)
│
├── tests/                    # Unit and integration tests
│
├── setup.py                  # Install configuration (classic setuptools)
└── tasks.py                  # Automation tasks (invoke/doit)
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
