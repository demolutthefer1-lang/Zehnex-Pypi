# 🚀 Zehnex 1.1.0

**Next-Gen Hybrid Telegram Bot Framework** — Combines the simplicity of `telebot` with the power of `aiogram`. Ultra-fast, async, and feature-rich.

```bash
pip install zehnex
```

---

## 🌟 Nima uchun Zehnex?

- **Gibrid API:** Ham `aiogram` (Context style), ham `telebot` (Handler style) uslubida kod yozish imkoniyati.
- **Ultra-tezkor:** `httpx` va `asyncio.Semaphore` asosidagi yuqori samarali engine.
- **Barchasi ichida:** Video yuklovchi, valyuta kursi, Wikipedia va QR kod generatori tayyor modul sifatida.

---

## 🚀 Tez boshlash

### Aiogram uslubida:
```python
from zehnex import Zehnex, Filter

dp = Zehnex("YOUR_TOKEN")

@dp.message(commands=["start"])
async def start(ctx):
    await ctx.answer("Salom! Men Zehnex frameworkida ishlayapman 🚀")

dp.run()
```

### Telebot uslubida:
```python
from zehnex import Zehnex

bot = Zehnex("YOUR_TOKEN")

@bot.message_handler(commands=["start"])
async def start(message):
    await bot.send_message(message.chat_id, "Salom!")

bot.run()
```

---

## 🛠 O'rnatish

```bash
pip install zehnex
```

---

## 📦 Modullar

| Modul | Tavsif |
|-------|--------|
| `Zehnex` | Asosiy engine (Gibrid API) |
| `VideoDownloader` | YouTube va boshqa saytlardan video yuklash |
| `CurrencyConverter` | Real-vaqt valyuta kurslari |
| `WikiToPDF` | Wikipedia qidiruv va PDF yaratish |
| `QRGenerator` | QR kod yaratish |

---

## 📄 Litsenziya
MIT License. Created by Zehnex Team.
