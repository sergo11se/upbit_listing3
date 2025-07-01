# Upbit Listing Bot

Телеграм-бот для отслеживания листингов и автоматических оповещений каждые 5 часов.

## Запуск на Render
1. Создайте сервис на [render.com](https://render.com/)
2. Укажите `worker` как тип сервиса
3. Добавьте переменные окружения:
   - `YOUR_TELEGRAM_BOT_TOKEN`
   - `YOUR_CHAT_ID`
4. Укажите команду запуска:
```bash
bash start.sh
```

## Локальный запуск
```bash
pip install -r requirements.txt
python bot.py
```