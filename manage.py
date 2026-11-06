import os
from application import create_app

# Создаем экземпляр приложения
app = create_app()

if __name__ == "__main__":
    # Запускаем сервер напрямую (это полный аналог старой команды "runserver")
    # host="0.0.0.0" нужен, если вы также запускаете это в Docker
    app.run(debug=True, host="0.0.0.0", port=7345)