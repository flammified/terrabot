from PIL import Image, ImageDraw

def draw_world(world):
    image = Image.new("RGB", (world.maxX, world.maxY), "white")
    imgdraw = ImageDraw.Draw(image)

    print(len(world.tiles))
    print(len(world.tiles[0]))
    x = 0
    y = 0
    for j in world.tiles:
        for i in j:
            try:
                if i is None:
                    continue
                else:
                    color = "rgb(" + str(i.type) + "," + str(i.type) + "," + str(i.type) + ")"
                imgdraw.point((x, y), fill=color)
            except Exception as e:
                print(str(e))
                print(str(x) + " " + str(y))
            x += 1
        x = 0
        y += 1

    image.show()
