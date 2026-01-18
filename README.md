# Modern Django Blog App

---
**English** | [Türkçe](README_TR.md)
---

https://github.com/fastfingertips/django-blog/assets/46646991/aa5d7f9a-635e-4afa-9a1a-4248a716edd8

A modernized, enterprise-grade blog application built with Django 5.1, featuring `uv` package manager, Class-Based Views, and a premium frontend.

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

## Technical Features
- Django 5.1: Latest stable core.
- Class-Based Views: Maintainable and modular structure.
- Hot Reload: Automated browser refresh on code changes.
- Quality: Ruff formatting and comprehensive Python type hints.
- Modern UI: Bootstrap 5 with custom glassmorphism and micro-interactions.

