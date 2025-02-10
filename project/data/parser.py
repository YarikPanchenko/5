from telethon import TelegramClient, events
import asyncio

# Замените на свои данные
api_id = '21327193'  # Ваш API ID
api_hash = '550c29c62e5409f95a8877bd8d386466'  # Ваш API HASH
user_username = 'evrechonok'  # Юзернейм вашего бота (без @)

# Создаём клиент
client = TelegramClient('session_name', api_id, api_hash)

# Функция для отправки команды /start
async def send_start_command():
    # Получаем объект пользователя
    user = await client.get_entity(user_username)
    # Отправляем команду /start
    await client.send_message(user, '/start')

# Функция для сохранения сообщений в файл
def save_message_to_file(message):
    with open("info.txt", "a", encoding="utf-8") as file:
        file.write(f"{message}\n")  # Сохраняем каждое сообщение на новой строке

# Функция для очистки файла
async def clear_file():
    while True:
        await asyncio.sleep(100)  # 5 минут в секундах
        with open("info.txt", "w", encoding="utf-8") as file:
            file.truncate(0)  # Очищаем файл

# Обработчик сообщений
@client.on(events.NewMessage)
async def handler(event):
    # Если сообщение от бота
    if event.is_private:  # Проверка на приватный чат
        print(f'Ответ пользователя: {event.text}')
        save_message_to_file(event.text)  # Сохраняем ответ в файл

# Запуск клиента
async def main():
    # Подключаемся и отправляем команду /start
    await client.start()
    await send_start_command()

    # Запуск задачи по очистке файла
    asyncio.create_task(clear_file())

    # Ожидаем события (получаем ответ от пользователя)
    await client.run_until_disconnected()

# Запускаем основной асинхронный цикл
asyncio.run(main())
