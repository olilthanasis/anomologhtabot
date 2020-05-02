import re
import email
from instabot import Bot
import imaplib
import time
import textwrap
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import random


def main():
    try:
        ###step 1 get email data###
        user = "botbot666toulil@gmail.com"
        pwd = "*******************"
        imap_url = "imap.gmail.com"
        con = imaplib.IMAP4_SSL(imap_url)
        con.login(user, pwd)
        con.select('INBOX')
        res, data = con.fetch(b'1', '(RFC822)')
        raw = email.message_from_bytes(data[0][1])

        def get_body(msg):
            if msg.is_multipart():
                return get_body(msg.get_payload(1))
            else:
                return msg.get_payload(None, True)

        def cleanhtml(raw_html):
            cleanr = re.compile('<.*?>')
            cleantext = re.sub(cleanr, '', raw_html)
            return cleantext

        text = (get_body(raw))
        text = text.decode('utf-8')
        text = cleanhtml(text)
        text = text[:-2]
        print(text)
        ###step 2 delete seen email###
        con.store(b'1', '+FLAGS', '\\Deleted')
        ###step 3 load text into image generator###
        astr = text
        para = textwrap.wrap(astr, width=15)
        print(astr)
        MAX_W, MAX_H = 400, 400
        im = Image.new('RGB', (MAX_W, MAX_H), (0, 0, 0, 0))
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype("arial.ttf", 28, encoding="utf-8")
        current_h, pad = 50, 10
        for line in para:
            w, h = draw.textsize(line, font=font)
            draw.text(((MAX_W - w) / 2, current_h), line, font=font, fill="white")
            current_h += h + pad
        source = r"C:\Users\mitth\Desktop\pics\img" + str(random.randint(0, 100000)) + ".jpg"
        im.save(source, "JPEG")
        ###step 4 image  using the API###

        bot = Bot()
        bot.login(username="3ogelanomologhtabot",
                  password="************************")
        bot.upload_photo(source,
                         caption="New Post\n github: https://github.com/olilthanasis/anomologhtabot")
        bot.send_message(astr, ["lil_thanasis"])
        # step 5 add answer to the text logs###
        now = datetime.now()
        with open(r"C:\Users\mitth\Desktop\logs.txt", "a") as myfile:
            myfile.write("\n" + astr + str(now))
        time.sleep(5)
    except TypeError:
        time.sleep(5)
        pass


while True:
    try:
        main()
    except:
        main()
