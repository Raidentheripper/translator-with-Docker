# Лабораторна робота — Перекладач на базі Docker + googletrans

## Структура проєкту
```
translator/
├── translator.py      # Основна програма (пункти 2–2.4)
├── requirements.txt   # Залежності
├── Dockerfile         # Конфігурація Docker-контейнера
├── .gitignore         # Ігноровані файли для Git
└── README.md          # Ця інструкція
```

---

## Пункт 1 — Віртуальне оточення з Python 3.11

```bash
# 1. Завантажити Python 3.11 з https://www.python.org/downloads/
#    При встановленні поставити галочку "Add to PATH"

# 2. Створити оточення з Python 3.11 через launcher (Windows):
py -3.11 -m venv Прізвище

# macOS / Linux:
python3.11 -m venv Прізвище

# 3. Активувати оточення:
# Windows:
Прізвище\Scripts\activate
# macOS/Linux:
source Прізвище/bin/activate

# 4. Встановити залежності:
pip install -r requirements.txt
```

---

## Пункт 2 — Запуск програми локально

```bash
python translator.py
```

---

## Пункт 3–6 — Docker

### Збірка образу
```bash
# ЗАМІНІТЬ "Прізвищеіі" на прізвище та ініціали (наприклад: KovalenkoAV)
docker build -t прізвищеіі .
```

### Запуск контейнера в інтерактивному режимі
```bash
docker run -it прізвищеіі
```

### Перевірити що папка створена всередині контейнера
```bash
docker run -it прізвищеіі ls /
# Повинна бути папка з прізвищем
```

---

## Пункт 7 — GitHub

```bash
git init
git add .
git commit -m "Initial commit: translator lab work"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

---

## Приклад роботи програми

```
Оригінал : Доброго дня. Як справи?
Визначення мови : Detected(lang=uk, confidence=1)
Переклад на 'en' : Good day. How are you?
CodeLang('En')      : English
CodeLang('English') : en
```
