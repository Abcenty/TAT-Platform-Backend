## users-service

Микросервис для регистрации / авторизации пользователей.

### Инструкция по запуску:
1. cp .env.example .env
2. docker-compose up -d
3. Для продакшена дополнительно прописать:
   1. php artisan key:generate
   2. php artisan jwt:secret

#### * Документация по эндпоинтам в public/docs/index.html или http://localhost/docs
