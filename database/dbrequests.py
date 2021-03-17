import sqlite3


class DbRequests:
    def __init__(self, database_file):
        """connecting to BD"""
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    """MESSAGE"""

    def message_add(self, message_id, processed_status):
        with self.connection:
            self.cursor.execute("INSERT INTO `messages` (`message_id`, `processed_status`) VALUES (?,?)", (message_id, processed_status))


    def message_exists(self, carnumber):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM messages WHERE message_id = ? ", (carnumber,)).fetchall()
            return bool(len(result))

    def message_update_status(self, message_id):
        with self.connection:
            self.cursor.execute("UPDATE messages SET processed_status = 1 WHERE message_id = ?", (message_id,))

    """CHANNELS"""

    def get_channel_list(self):
        with self.connection:
            result = self.cursor.execute("SELECT channel_name, channel_category FROM `channels` ").fetchall()
            return result

    """PHRASES"""

    def phrase_add(self, phrase, category):
        with self.connection:
            self.cursor.execute("INSERT INTO `phrases` (`phrase`, 'category') VALUES (?, ?)", (phrase, category))

    def phrases_get(self, phrase_category):
        with self.connection:
            phlist = []
            for cortej in self.cursor.execute("SELECT phrase_text FROM phrases WHERE phrase_category = ?", (phrase_category,)).fetchall():
                for phrase in cortej:
                    phlist.append(phrase.replace('\r\n', ''))
            return phlist