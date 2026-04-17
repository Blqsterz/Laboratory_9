from PIL import Image
from pathlib import Path

img = Image.open(Path(__file__).parent / "picture.jpg")

img.show()

height, weight = img.size

print(f"Размер = {height} x {weight}")
print(f"Цветовой режим: {img.mode}")
print(f"Формат изображения:{img.format}")

