import asyncio
import logging
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
import os
from dotenv import load_dotenv
import datetime

# Configuration du logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Chargement des variables d'environnement
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def test_start_command(bot: Bot, chat_id: int):
    """Test de la commande /start"""
    await bot.send_message(chat_id=chat_id, text="/start")
    logger.info("✅ Test de la commande /start effectué")
    await asyncio.sleep(2)
    
    # Simuler l'entrée du nom du maître
    await bot.send_message(chat_id=chat_id, text="Test Master")
    logger.info("✅ Test de l'entrée du nom du maître effectué")
    await asyncio.sleep(2)

async def test_date_selection(bot: Bot, chat_id: int):
    """Test de la sélection de date"""
    keyboard = [[InlineKeyboardButton("Сегодня", callback_data='date_today')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await bot.send_message(chat_id=chat_id, text="Выберите дату:", reply_markup=reply_markup)
    logger.info("✅ Test de la sélection de date effectué")
    await asyncio.sleep(2)

async def test_shift_selection(bot: Bot, chat_id: int):
    """Test de la sélection de la shift"""
    keyboard = [
        [InlineKeyboardButton("День", callback_data='shift_day'),
         InlineKeyboardButton("Ночь", callback_data='shift_night')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await bot.send_message(chat_id=chat_id, text="Выберите смену:", reply_markup=reply_markup)
    logger.info("✅ Test de la sélection de shift effectué")
    await asyncio.sleep(2)

async def test_product_selection(bot: Bot, chat_id: int):
    """Test de la sélection du produit"""
    keyboard = [
        [InlineKeyboardButton("Круассан с ветчиной и сыром", callback_data='product_0')],
        [InlineKeyboardButton("Круассан классический", callback_data='product_1')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await bot.send_message(chat_id=chat_id, text="Выберите продукт:", reply_markup=reply_markup)
    logger.info("✅ Test de la sélection du produit effectué")
    await asyncio.sleep(2)

async def test_comment(bot: Bot, chat_id: int):
    """Test de l'ajout de commentaire"""
    await bot.send_message(chat_id=chat_id, text="Test commentaire pour le produit")
    logger.info("✅ Test de l'ajout de commentaire effectué")
    await asyncio.sleep(2)

async def test_photo(bot: Bot, chat_id: int):
    """Test de l'envoi de photo"""
    try:
        with open("test_photo.jpg", "rb") as photo:
            await bot.send_photo(chat_id=chat_id, photo=photo, caption="Test photo")
        logger.info("✅ Test de l'envoi de photo effectué")
    except Exception as e:
        logger.error(f"❌ Erreur lors de l'envoi de la photo: {e}")
    await asyncio.sleep(2)

async def main():
    """Fonction principale de test"""
    try:
        # Initialisation du bot
        bot = Bot(token=TOKEN)
        
        # Récupération des informations du bot
        bot_info = await bot.get_me()
        logger.info(f"✅ Bot connecté: {bot_info.username}")
        
        # ID du chat pour les tests (à remplacer par votre ID)
        chat_id = 123456789  # Remplacez par votre ID de chat
        
        # Exécution des tests
        await test_start_command(bot, chat_id)
        await test_date_selection(bot, chat_id)
        await test_shift_selection(bot, chat_id)
        await test_product_selection(bot, chat_id)
        await test_comment(bot, chat_id)
        await test_photo(bot, chat_id)
        
        logger.info("✅ Tous les tests ont été effectués avec succès")
        
    except Exception as e:
        logger.error(f"❌ Erreur lors des tests: {e}")

if __name__ == '__main__':
    asyncio.run(main()) 