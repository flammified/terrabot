from PIL import Image, ImageDraw
from progressbar import *

def draw_world(world):
    image = Image.new("RGB", (world.maxX, world.maxY), "white")
    imgdraw = ImageDraw.Draw(image)
    widgets = ['Percentage: ', Percentage(), ' ', Bar(marker=RotatingMarker()),
           ' ', ETA(), ' Speed: ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, maxval=len(world.tiles)).start()

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
                pbar.finish()
            x += 1
        x = 0
        y += 1
        pbar.update(y)
    pbar.finish()
    image.show()
