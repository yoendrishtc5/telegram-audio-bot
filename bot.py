import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import yt_dlp

# Función para descargar solo el audio
def download_audio(url: str, download_path: str):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Comando start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Envía el enlace del video del que deseas descargar el audio.')

# Manejo de mensajes con enlaces
def handle_message(update: Update, context: CallbackContext) -> None:
    video_url = update.message.text
    download_path = '/tmp'  # Carpeta temporal para descargar
    download_audio(video_url, download_path)
    audio_file = max([f for f in os.listdir(download_path)], key=lambda x: os.path.getctime(os.path.join(download_path, x)))
    update.message.reply_audio(audio=open(os.path.join(download_path, audio_file), 'rb'))

def main() -> None:
    TOKEN = os.getenv("7157522759:AAG65ZPGTGQQJXBW0UQQy-YFkv2f1EyMfeU")
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
