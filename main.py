from PIL import Image, ImageDraw, ImageFont

FONT_COLOR = "#763626"
FONT_TEXT = ImageFont.truetype(r'font/Allura-Regular.ttf', size=140)
MASTER = Image.open(r'master.png')
WIDTH, HEIGHT = MASTER.size

with open('name-list.txt') as f:
    names = f.readlines()
    for name in names:
        name = name.replace("\n", '')

        image = Image.open(r'master.png')
        draw = ImageDraw.Draw(image)

        name_width, name_height = draw.textsize(name, font=FONT_TEXT)

        draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2 - 30), name, fill=FONT_COLOR, font=FONT_TEXT)

        image.save("./export/" + name +".png")
        print('Saving Certificate of:', name)        
