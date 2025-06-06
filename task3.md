## Запуск тестов сайта Demoqa.com
```bash
pytest tests/ -v -s
```

## Или по одному
Тест работы алертов
```bash
pytest tests\test_demoqa_alerts.py -v -s 
```
Тест работы фреймов
```bash
pytest tests\test_demoqa_frames.py -v -s 
```
Тест работы таблиц
```bash
pytest tests\test_demoqa_tables.py -v -s 
```
Тест работы вкладок
```bash
pytest tests\test_demoqa_handles.py -v -s
```