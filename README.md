# 🧠 SAB TRADING PLAZA

Неофициальная торговая площадка для игры **Steal a Brainrot** (Roblox).

## Функции
- 🔄 **Трейд** — обменяй брейнрота
- 💰 **Продаю** — продай брейнрота
- 🎁 **Раздача** — отдай бесплатно
- 💬 Комментарии с пометкой "предложение о трейде"
- 🗑️ Удаление с выбором причины
- 👤 Профиль: ник, фото, телефон, Roblox username
- 🧠 60+ брейнротов от Common до OG

## Деплой на Render

### 1. Загрузи на GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/ТВОЙ_НИК/sab-trading-plaza.git
git push -u origin main
```

### 2. На render.com
1. New → Web Service
2. Connect GitHub repo
3. Build Command:
```
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate && python manage.py seed_brainrots
```
4. Start Command: `gunicorn sab_trading.wsgi:application`
5. Environment Variables:
   - `SECRET_KEY` = любой длинный случайный ключ
   - `DEBUG` = `False`
   - `ALLOWED_HOSTS` = `.onrender.com`

### 3. База данных PostgreSQL (бесплатно)
- New → PostgreSQL → создай базу
- Скопируй `Internal Database URL`
- Добавь как переменную `DATABASE_URL`

### Локальный запуск
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_brainrots
python manage.py createsuperuser
python manage.py runserver
```

## Стек
- Django 5.0
- WhiteNoise (статика)
- PostgreSQL / SQLite
- Gunicorn
- Шрифт: Orbitron + Rajdhani
