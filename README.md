# Бот для журнала выпечки

Telegram бот для ведения журнала выпечки.

## Требования

- Python 3.11
- Переменные окружения:
  - `TELEGRAM_TOKEN` : Токен Telegram бота
  - `GOOGLE_SHEET_ID` : ID таблицы Google Sheets
  - `GOOGLE_DRIVE_FOLDER_ID` : ID папки Google Drive
  - `GOOGLE_CREDS_JSON` : Учетные данные Google в формате JSON
  - `PORT` : Порт для веб-сервера (устанавливается автоматически Railway)

## Установка

1. Клонировать репозиторий
2. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Настроить переменные окружения
4. Запустить бота:
   ```bash
   python journal_bot.py
   ```

## Развертывание на Railway

Бот настроен для развертывания на Railway.app. Необходимые файлы конфигурации уже присутствуют:
- `railway.toml`
- `Procfile`
- `requirements.txt`
- `runtime.txt`

## Функциональность

- Запись продукции выпечки
- Управление фотографиями
- Интеграция с Google Sheets и Drive
- Интерфейс на русском языке

## Структура проекта

```
journal-boulangerie-bot/
├── journal_bot.py      # Основной код бота
├── requirements.txt    # Python зависимости
├── .gitignore         # Игнорируемые файлы
└── README.md          # Документация
```

## Безопасность

- Никогда не делитесь файлами конфигурации
- Храните токены в секрете
- Не публикуйте конфиденциальные данные

## Лицензия

MIT License 