from telethon.sync import TelegramClient
from secrets_1 import secrets
import os

# Set up the Telegram client with your own account credentials
api_id = secrets.api_id
api_hash = secrets.api_hash
phone_number = secrets.phonenumber

client = TelegramClient('send things', api_id, api_hash)

async def main():
    # Log in to your Telegram account
    await client.start(phone_number)

    # Replace 'group_username' with the username of your group
    group_id = -4119703192
    group_entity = await client.get_entity(group_id)

    # Path to the folder containing images
    folder_path = 'C:\\Users\\Achak\\Pictures\\Screenshots'

    # Iterate through the images in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(folder_path, filename)

            # Send the image to the group
            await client.send_file(group_entity, file=image_path)

    print("All images sent to the group.")

# Run the main function
with client:
    client.loop.run_until_complete(main())
