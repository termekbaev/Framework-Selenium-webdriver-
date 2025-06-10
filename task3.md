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

## Настройки
Выбрать браузер для запуска а также изменить конфигурацию запуска браузера можно в файле
```bash
config\config.json
```

## Логи
Логи всех тестов выведены в файл.
```bash
test.log
```
Файл перезаписывается перед каждым запуском.