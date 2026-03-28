# Telegram Time Profile

Telegram profilida real vaqtni ko'rsatuvchi userbot.

## Fayllar

- `main.py` — asosiy kod (Render'da ishlaydi)
- `get_session.py` — session string olish (local, bir marta)
- `requirements.txt` — kutubxonalar

## Ishga tushirish

### 1. Session string olish (local kompyuterda)
`get_session.py` ga yangi api_hash ni yozing, keyin:
```bash
pip install telethon
python get_session.py
```
Chiqgan stringni saqlang.

### 2. Render sozlash
Environment Variables:
- `API_ID` → 30661678
- `API_HASH` → yangi hash
- `SESSION_STRING` → get_session.py dan olgan string

Start Command: `python main.py`
