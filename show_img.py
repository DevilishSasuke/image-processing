import cv2
from matplotlib import pyplot as plt

def show_img(img: cv2.typing.MatLike | None, title: str = "", 
             transformation: int = cv2.COLOR_BGR2RGB, size: int = 10):
    plt.figure(figsize=(size, size))

    if len(img.shape) == 2:
        plt.imshow(img, cmap="gray", vmin=0, vmax=255)
    elif len(img.shape) == 3:
        img_trnsf = cv2.cvtColor(img, transformation)
        plt.imshow(img_trnsf)

    plt.title(title)
    plt.axis("off")
    #plt.tight_layout(pad=0, w_pad=0, h_pad=0)
    #plt.margins(x=0, y=0)
    plt.show()