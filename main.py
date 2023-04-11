from PIL import Image, ImageFilter,ImageDraw,ImageFont

f = '5.jpg'
image = Image.open(f)

def z1():
    image.show(f)
    print(image.size)
    print(image.mode)
    print(image.format)

z1()
def z2():
    z = '5.jpg'
    image = Image.open(z)
    x, y = image.size # ()
    x //= 3
    y //= 3
    print(image.size)
    out = image.resize((x, y))
    out.show()
    print(out.size)
    c = image.transpose(Image.FLIP_TOP_BOTTOM)
    c.show()
    g = image.rotate(90)
    g.show()
    out.save("piddddd.jpg")
    c.save("ttt.jpg")
    g.save("rrr.jpg")
z2()

def z3():
    a = "1.jpg"
    b = "2.jpg"
    c = "3.jpg"
    d = "4.jpg"
    f = "5.jpg"
    h=[a,b,c,d,f]
    for file in h:
        with Image.open(file) as img:
            new_img = img.filter(ImageFilter.EMBOSS)
            new_img.show()
            new_img.save("new"+file)
z3()

def z4():
    s = "1.jpg"
    v = "2.jpg"
    image1 = Image.open(s)
    image2 = Image.open(v)
    image1.paste(image2)
    image1.show()
z4()
