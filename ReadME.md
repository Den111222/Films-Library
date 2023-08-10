Запуск:
1. Скачать с репозитария

   ```git clone https://github.com/Den111222/Films-Library.git```
2. Для того чтобы проверить работы почты,
необходимо в файле

"core/settings.py"
добавить свой email и password

EMAIL_HOST_USER = 'test@gmail.com'

EMAIL_HOST_PASSWORD = 'pass'

3. Запустить docker:

    ```docker-compose up```
4. Открыть сайт по:

   ```http://127.0.0.1:8000```