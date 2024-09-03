## EFK Stack and Gunicorn app

### Описание
Есть абстрактное flask приложение, которое отправляет логи во fluentd.

**app** - папка с кодом на python
**fluentd** - папка с Dockerfile и конфигом для fluentd

### Запуск

```
docker-compose up
```
