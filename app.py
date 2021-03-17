from loader import app, db, logger
import random
import time
from datetime import datetime
import schedule


def start():
    with app:
        for channel_info in db.get_channel_list():
            try:
                channel_name, channel_category = channel_info
                phrases_list = db.phrases_get(channel_category)
                channel = app.get_chat(channel_name)
                chat = channel.linked_chat
                for message in app.get_history(chat.id, limit=100):
                    if message.from_user is None and message.forward_from_chat.id == channel.id and not db.message_exists(message.message_id) and phrases_list:
                        print(f'{channel_name} - {message.message_id}')
                        text = random.choice(phrases_list)
                        app.send_message(chat.id, text, reply_to_message_id=message.message_id)
                        db.message_add(message_id=message.message_id, processed_status=1)
                        logger.info('Channel: {} / Message: {} / time: {}'.format(channel_name, text[:-10] + '...',datetime.now()))
                        time.sleep(60 * 10)
            except Exception as e:
                logger.debug(f'Error: {e} / time: {datetime.now()} ')


if __name__ == '__main__':
    start()
    schedule.every(10).minutes.do(start)
    while True:
        schedule.run_pending()
        time.sleep(1)
