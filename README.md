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

Here's how you can obtain your `api_id` and `api_hash`:

---

#### Obtaining API ID and API Hash:
To use this script, you need to obtain your own Telegram API credentials (`api_id` and `api_hash`). Follow these steps:

1. **Visit Telegram's API development tools**: Go to the [Telegram API development tools](https://my.telegram.org/auth) page and log in with your Telegram account.

2. **Create a new application**:
   - After logging in, click on "API development tools".
   - Click on "Create new application".
   - Fill out the form with your application details.
   - After submitting the form, you will see your `api_id` and `api_hash`.

3. **Note down your credentials**: Save the `api_id` and `api_hash` provided, as you will need to input them into the script.


#### Usage:
1. Update your API credentials and list of offensive words in the `delete_offensive_messages.py` script.
2. Run the script:
   ```sh
   python3 python-telegram-cleaner.py
   ```


