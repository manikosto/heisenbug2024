##### 1 - Запуск теста (нужен новый токен из https://qa-playground.com/)
`STAGE=release pytest -sv --alluredir=allure-results`

##### 2 - Если ошибка "No module named found"
- MacOS / Linux: `export PYTHONPATH="${PYTHONPATH}:ABSOLUT_PATH_TO_YOUR_PROJECT"`
- Windows: `$env:PYTHONPATH = "$env:PYTHONPATH;ABSOLUT_PATH_TO_YOUR_PROJECT"`
