# the minimal blog

---
[English](README.md) | **Türkçe**
---

![the minimal blog](https://github.com/user-attachments/assets/96a953c6-6b86-45f1-8c08-9c20d4b063ba)

django 5.1 ile inşa edilmiş; `uv` paket yöneticisi ve sınıf tabanlı görünümler (cbv) kullanan, radikal şekilde minimalist ve editoryal odaklı bir blog uygulaması. "highlighter" estetiği ile sadece içeriğe ve sadeliğe odaklanır.

## Hızlı Başlangıç

### 1. Ön Gereksinimler
- Python 3.11+
- [uv](https://docs.astral.sh/uv/) (Hızlı Python paket yöneticisi)
  ```bash
  pip install uv
  ```

### 2. Kurulum
```bash
uv sync
```

### 3. Veritabanı ve Admin
```bash
uv run python manage.py migrate
uv run python manage.py createsuperuser
```

### 4. Çalıştırma
```bash
uv run python manage.py runserver
```

---

## Betikler (Scripts)

Hızlı kurulum ve çalıştırma için aşağıdaki betikleri kullanabilirsiniz:

### Windows
- `setup.bat`: `uv` kurumunu kontrol eder, bağımlıkları yükler, varsayılan `.env` dosyasını oluşturur ve migration'ları çalıştırır.
- `run.bat`: Geliştirme sunucusunu başlatır.

### Unix/macOS
- `setup.sh`: Otomatik kurulum betiği.
- `run.sh`: Hızlı çalıştırma betiği.

---

## Teknik Özellikler
- Django 5.1: En güncel kararlı sürüm.
- Class-Based Views: Sürdürülebilir ve modüler yapı.
- Hot Reload: Kod değişiminde otomatik tarayıcı yenileme.
- Kalite: Ruff formatlama ve kapsamlı Python tip belirteçleri.
- Minimalist UI: Okunaklılık odaklı, keskin hatlara sahip editoryal ve metin tabanlı tasarım.

