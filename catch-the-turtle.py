import turtle
import random
import time 

def geri_sayim(saniye):
    while saniye:
        turtle.clear()
        turtle.penup()
        turtle.goto(0, 230)
        turtle.write("Geri Sayım: {}".format(saniye), align="center", font=("Arial", 14, "normal"))
        print(saniye)
        time.sleep(1)
        saniye -= 1
    turtle.clear()
    turtle.write("Geri Sayım Bitti! " ,align="center", font=("Arial", 14, "normal"))

def skor_yaz(skor):
    skor_turtle.clear()
    skor_turtle.penup()
    skor_turtle.goto(0, 260)
    skor_turtle.write("Skor: {}".format(skor), align="center", font=("Courier", 24, "normal"))

# Skoru ekrana yazdırmak için bir fonksiyon
def skor_artir(x, y):
    global skor
    skor += 1
    skor_yaz(skor)
    tonton.goto(random.randint(-200, 200), random.randint(-200, 200))  # Kaplumbağayı farklı bir konuma taşı

# Ekran tıklamalarını dinlemek için fonksiyonu bağlama
tonton = turtle.Turtle()
tonton.color("green")
tonton.shape("turtle")
tonton.penup()
tonton.goto(random.randint(-200, 200), random.randint(-200, 200))  # Başlangıçta kaplumbağayı rastgele bir konuma yerleştir
tonton.onclick(skor_artir)

# Skoru tutmak için bir değişken tanımlama
skor = 0

# Skor turtle'ını oluşturma
skor_turtle = turtle.Turtle()
skor_turtle.color("white")
skor_turtle.penup()
skor_turtle.hideturtle()

# ekran olusturma
turtle_screen = turtle.Screen()
turtle_screen.title("Kaplumbağa Yakalama Oyunu")
turtle_screen.bgcolor("light sky blue")

saniye = 15
geri_sayim(saniye)

turtle.done()
