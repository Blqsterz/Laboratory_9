from PIL import Image, ImageFilter, ImageFont, ImageDraw
from pathlib import Path

script_dir = Path(__file__).parent
out_dir = script_dir / "watermark"
out_dir.mkdir(exist_ok=True) 

files = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]

TEXT = "WATERMARK"
COLOR = (255, 255, 255, 100) 
POS = (100, 100)  

for file in files:
    src_path = script_dir / file

    if src_path.exists():
        img = Image.open(src_path).convert("RGBA")

        txt = Image.new("RGBA", img.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(txt)
        font = ImageFont.truetype("arial.ttf", 60)
        draw.text(POS, TEXT, fill=COLOR, font=font)


        result = Image.alpha_composite(img, txt)
        result.convert("RGB").save(out_dir / f"wm_{file}", quality=90)
   





