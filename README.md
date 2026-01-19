# the minimal blog

---
**English** | [Türkçe](README_TR.md)
---

<img src="https://github.com/user-attachments/assets/96a953c6-6b86-45f1-8c08-9c20d4b063ba" width="800" alt="the minimal blog">

a strictly minimalist, editorial-grade blog application built with django 5.1. it features the `uv` package manager, class-based views, and a unique "highlighter" design aesthetic focused on silence and content.

## Quick Start

### 1. Prerequisites
- Python 3.11+
- [uv](https://docs.astral.sh/uv/) (Fast Python package manager)
  ```bash
  pip install uv
  ```

### 2. Setup
```bash
uv sync
```

### 3. Database & Admin
```bash
uv run python manage.py migrate
uv run python manage.py createsuperuser
```

### 4. Run
```bash
uv run python manage.py runserver
```

---

## Scripts

You can use the following scripts for quick setup and execution:

### Windows
- `setup.bat`: Installs `uv`, syncs dependencies, creates default `.env`, and runs migrations.
- `run.bat`: Starts the development server.

### Unix/macOS
- `setup.sh`: Automated setup script.
- `run.sh`: Rapid execution script.

---

## Technical Features
- Django 5.1: Latest stable core.
- Class-Based Views: Maintainable and modular structure.
- Hot Reload: Automated browser refresh on code changes.
- Quality: Ruff formatting and comprehensive Python type hints.
- Minimalist UI: Text-focused, editorial design with sharp edges and high readability.

