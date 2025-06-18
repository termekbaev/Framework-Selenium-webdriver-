## Установка зависимостей
```bash
pip install -r requirements.txt
```

## Настройки
Выбрать браузер для запуска а также изменить конфигурацию запуска браузера можно в файле
```text
config\config.json
```

## Запуск тестов сайта Demoqa.com
```bash
pytest tests/ -v
```

## Или по одному
Тест работы алертов
```bash
pytest tests\test_demoqa_alerts.py -v
```
Тест работы фреймов
```bash
pytest tests\test_demoqa_frames.py -v
```
Тест работы таблиц
```bash
pytest tests\test_demoqa_tables.py -v
```
Тест работы вкладок
```bash
pytest tests\test_demoqa_handles.py -v
```

## Логи
Логи всех тестов выведены в файл.
```text
test.log
```
Файл перезаписывается перед каждым запуском.