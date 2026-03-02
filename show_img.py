import cv2

def show_img(img: cv2.typing.MatLike | None, title: str = ""):
    cv2.imshow(title, img)
    cv2.waitKey(0)