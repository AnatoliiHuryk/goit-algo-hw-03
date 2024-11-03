import turtle

def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)

def koch_snowflake(t, length, level):
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)

def main():
    level = int(input("Введіть рівень рекурсії для сніжинки Коха (рекомендовано 3-5): "))

    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    length = 400

    koch_snowflake(t, length, level)

    turtle.done()

if __name__ == "__main__":
    main()
