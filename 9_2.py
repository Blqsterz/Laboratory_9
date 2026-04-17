from PIL import Image
from pathlib import Path

DIR = Path(__file__).parent
img = Image.open(DIR / "picture.jpg")

reimg = img.reduce(3)
reimg.save(DIR / "reduced_picture.jpg")
print(f"Новый размер картинки: {reimg.height} x {reimg.width}")

mirror_horizontal = img.transpose(Image.FLIP_LEFT_RIGHT)
mirror_horizontal.save(DIR / "mirror_horizontal_picture.jpg")

mirror_vertical = img.transpose(Image.FLIP_TOP_BOTTOM)
mirror_vertical.save(DIR / "mirror_vertical_picture.jpg")

