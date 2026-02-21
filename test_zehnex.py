import sys
import os

# Zehnex papkasini pathga qo'shish
sys.path.append(os.path.join(os.getcwd()))

try:
    from zehnex import Zehnex, Filter, __version__
    print(f"✅ Zehnex muvaffaqiyatli import qilindi!")
    print(f"Versiya: {__version__}")
    
    # Engine test
    bot = Zehnex("TOKEN")
    print(f"Engine holati: OK")
    
    # Handlers test (Aiogram style)
    @bot.message(commands=['start'])
    async def start_handler(ctx):
        pass
    print(f"Aiogram-style handlers: OK")
    
    # Handlers test (Telebot style)
    @bot.message_handler(commands=['help'])
    async def help_handler(message):
        pass
    print(f"Telebot-style handlers: OK")
    
except Exception as e:
    print(f"❌ Xatolik yuz berdi: {e}")
    import traceback
    traceback.print_exc()
