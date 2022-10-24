"""Решила объединить 2 задачи - использовать Pillow и выводить график. В файле image.png вырисовывается график гиперболы"""
from PIL import Image, ImageColor
from PIL import ImageDraw


width = 400
height = 300

image = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, width-1, height-1), fill=ImageColor.getrgb("white"), outline=ImageColor.getrgb("grey"))


def function1(x):
    return 1/x


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


start_x = -4
end_x = 4
start_y = -15
end_y = 15

points = []

x = start_x
step_x = 0.1

while x <= end_x:
    y = function1(x)
    points.append(Point(x, y))
    x += step_x


def convert(point):
    scale_x = width / (end_x - start_x)
    scale_y = height / (end_y - start_y)

    local_x = point.x * scale_x
    local_y = point.y * scale_y

    local_x = (-start_x * scale_x) + local_x
    local_y = (-start_y * scale_y) + local_y

    return Point(local_x, height - local_y)


start_hor = convert(Point(start_x, 0))
end_hor = convert(Point(end_x, 0))
draw.line((start_hor.x, start_hor.y, end_hor.x, end_hor.y), fill=ImageColor.getrgb("grey"))

start_ver = convert(Point(0, start_y))
end_ver = convert(Point(0, end_y))
draw.line((start_ver.x, start_ver.y, end_ver.x, end_ver.y), fill=ImageColor.getrgb("grey"))



last_point = convert(points[0])
for point in points:
    current_point = convert(point)
    draw.line((last_point.x, last_point.y, current_point.x, current_point.y), fill=ImageColor.getrgb("red"))
    last_point = current_point

image.save("image.png", "PNG")