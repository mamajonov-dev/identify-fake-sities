import os
from aiogram.types import Message
from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv
load_dotenv()
from bs4 import BeautifulSoup
TOKEN = os.getenv('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot)
sites = ['daryo.uz', 'olx.uz', 'm.olx.uz', 'www.olx.uz',  'uzumbank.uz', 'uzcard.uz', 'myuzcard.uz', 'ofb.uz', 'asakabank.uz',
         'agrobank.uz', 'aloqabank.uz', 'banklar.uz', 'humocard.uz', 'www.sqb.uz',  'taxi.yandex.uz', 'delivery.yandex.com', 'yoshlar.gov.uz',
         'hamkorbank.uz',  'www.ipotekabank.uz', 'www.banklar.uz', '2gis.uz', 'www.kdb.uz', 'cbu.uz', 'www.turonbank.uz', 'ipb.uz', 'yoshlardaftari.uz',
         'nbu.uz', 'bank.uz', 'yandex.uz', 'yandex.com', 'go.yandex', 'trustbank.uz', 'www.infinbank.com', 'kapital24.uz', 'www.kapital24.uz', 'yoshlarportali.uz',
         'ipakyulibank.uz', 'click.uz', 'clickclub.uz', 'fargo.uz', 'www.oilakredit.uz', 'tengebank.uz', 'www.xb.uz', 'bankxizmatlari.uz', 'online-mahalla.uz',
         'talim-krediti.uz','talim-krediti.mf.uz', 'sqb.uz', 'infokredit.uz', 'depozit.uz', 'tbcbank.uz','mkbank.uz', 'parliament.gov.uz', 'kun.uz', 'tbs.uz',
         'president.uz', 'my.gov.uz', 'soliq.uz', 'soliqservis.uz','esi.uz', 'senat.uz','invest.gov.uz', 'miit.uz', 'singlewindow.uz', 'emu.uz', 'www.bts.uz', 'bts.uz',
         'tezbor.uz','university.zoodpay.com', 'www.zoodpay.com', 'tezz.uz', 'www.prizma.uz','www.dpd.uz', 'www.prom.uz', 'davrbank.uz', 'www.gov.uz','data.egov.uz',
         'beemall.uz', 'nmc.uz', 'simpleglobal.com', 'shopi.uz', 'sello.uz', 'avtoelon.uz', 'www.avtoelon.uz', 'olcha.uz', 'bmtm.uz', 'www.sos-kd.uz', 'dd.gov.uz', 'www.creditasia.uz',
         'credit.uz', 'milliykredit.uz', 'chakana.uz', 'kun.uz', 'crediton.uz', 'cyberweek.uz', 'koronapay.com', 'www.youtube.com', 'm.youtube.com']





@dp.message_handler(commands='start')
async def start(message: Message):
    chat_id = message.chat.id
    fullname = message.from_user.full_name
    await bot.send_message(chat_id, f'Xush kelibsiz {fullname}!\n'
                                    f'Xozirda Fake internet sahifalar orqali ko\'pchilik '
                                    f'<b>Fishing</b> qurboniga aylanmoqda. Shunday sahifalarning '
                                    f'xaqiqiy yoki fake ekanligini tekshirish uchun ushbu bot yaratilgan. '
                                    f'Saytni tekshirmoqchi bo\'lsangiz havolani usbu botga yuboring!', parse_mode='HTML')

@dp.message_handler(lambda message: 'http' in message.text)
async def checklink(message: Message):
    chat_id = message.chat.id
    hidden_link = message.html_text


    soup = BeautifulSoup(hidden_link, 'html.parser')
    count = 0
    try:
        link_url = soup.find('a').get('href').split('/')
        for links in link_url:
            if links in sites:
                count += 1
            else:
                pass
        if count == 0:
            await bot.send_message(chat_id, 'Diqqat Fake sayt❗ Havola ostida yashiringan havola mavjud. Bu sayt malumotlar omborida mavjud emas❗')
        else:
            await bot.send_message(chat_id, 'Sayt malumotlar omborida mavjud va tekshirilgan. Saytdan foydalanishingiz mumkin✅')
    except:
        hidden_link = hidden_link.split()
        lin = []

        for link in hidden_link:

            if link.startswith('http'):
                lin.append(link)

        if len(lin) == 0:
            await bot.send_message(chat_id, 'Iltimos havola jo\'nating!')
        elif len(lin) == 1:
            for elm in lin:
                elm = elm.split('/')
                for i in elm:
                    if i in sites:
                        count += 1
                    else:
                        pass
            if count == 0:
                await bot.send_message(chat_id, 'Diqqat tekshirilmagan sayt❗ Bizning ma\'lumotlar omborida mavjud emas❗ Fake sayt bo\'lishi mumkin❗')
            elif count == 1:
                await bot.send_message(chat_id, 'Sayt malumotlar omborida mavjud va tekshirilgan. Saytdan foydalanishingiz mumkin✅')
        elif len(lin) > 1:
            for elm in lin:
                elm = elm.split('/')
                for i in elm:
                    if i in sites:
                        count += 1
                    else:
                        pass
            if count == 0 or count == 1:
                await bot.send_message(chat_id, 'Diqqat tekshirilmagan sayt❗ Bizning ma\'lumotlar omborida mavjud emas❗ Fake sayt bo\'lishi mumkin❗')
            elif count > 1:
                await bot.send_message(chat_id, 'Sayt malumotlar omborida mavjud va tekshirilgan. Saytdan foydalanishingiz mumkin✅')


@dp.message_handler()
async def checklink(message: Message):
    a = message.text.lower()
    if a in sites:
        await bot.send_message(message.chat.id, 'Sayt malumotlar omborida mavjud va tekshirilgan. Saytdan foydalanishingiz mumkin✅')
    else:
        await bot.send_message(message.chat.id, 'Diqqat tekshirilmagan sayt❗ Bizning ma\'lumotlar omborida mavjud emas❗ Fake sayt bo\'lishi mumkin❗')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
