from PIL import Image, ImageFilter 
from pathlib import Path

direct = Path(__file__).parent

out_dir = direct / "filtered"
out_dir.mkdir(exist_ok=True) 


files = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]

for file in files:
    source = direct / file
    if source.exists():
        img = Image.open(source).convert("RGB") 
        img = img.filter(ImageFilter.EDGE_ENHANCE)      
        img.save(out_dir / f"filtered_new_{file}")

  