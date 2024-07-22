#### Features:
- **Automatic Message Deletion**: Scans and deletes messages containing offensive words in private Telegram chats.
- **Case-Insensitive Filtering**: Detects offensive words regardless of case.
- **User-Friendly Output**: Provides console output for each message deleted and any errors encountered.
- **Customizable Word List**: Easily update the list of offensive words to fit your needs.

#### Requirements:
- Python 3.6+
- Telethon library

#### Installation:
1. Clone the repository:
   ```sh
   git clone https://github.com/Inerger/python-telegram-cleaner.git
   ```
2. Navigate to the project directory:
   ```sh
   cd python-telegram-cleaner
   ```
3. Install the required dependencies:
   ```sh
   pip3 install Telethon
   ```

#### Usage:
1. Update your API credentials and list of offensive words in the `delete_offensive_messages.py` script.
2. Run the script:
   ```sh
   python3 python-telegram-cleaner.py
   ```


