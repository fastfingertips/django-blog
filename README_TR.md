# Modern Django Blog Uygulaması

---
[English](README.md) | **Türkçe**
---


Django 5.1 ile modernize edilmiş; `uv` paket yöneticisi, Class-Based Views ve minimalist editoryal tasarımı içeren kurumsal standartlarda blog uygulaması.

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

