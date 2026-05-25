import os
import re
from pathlib import Path
from datetime import datetime

try:
    from pillow_heif import register_heif_opener
    register_heif_opener()
    heif_available = True
except ImportError:
    heif_available = False

from PIL import Image

BASE = Path(r"C:\Users\muram\Dev\ak9puppies\public\assets\processed")

# Stage inference from date in Photo filenames
MONTH_MAP = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}
BIRTH = datetime(2026, 3, 30)

def date_to_stage(month_str, day):
    month = MONTH_MAP.get(month_str, 0)
    if month == 0:
        return None
    photo_date = datetime(2026, month, day)
    age_days = (photo_date - BIRTH).days
    if age_days <= 15:
        return 'newborn'
    elif age_days <= 35:
        return '3w'
    elif age_days <= 45:
        return '6w'
    else:
        return '7w'

def extract_stage(filename):
    """Extract stage from Photo date filename."""
    m = re.match(r'Photo\s+(\w+)\s+(\d+)\s+\d+', filename)
    if m:
        return date_to_stage(m.group(1), int(m.group(2)))
    return None

def to_webp(src_path, dst_path):
    """Convert any image to WebP. Returns True on success."""
    try:
        with Image.open(src_path) as img:
            # Preserve orientation from EXIF
            try:
                from PIL import ImageOps
                img = ImageOps.exif_transpose(img)
            except Exception:
                pass
            # Convert to RGB if needed (HEIC/PNG can be RGBA or other modes)
            if img.mode not in ('RGB', 'RGBA'):
                img = img.convert('RGB')
            img.save(dst_path, 'WEBP', quality=88, method=4)
        return True
    except Exception as e:
        print(f"  ERROR converting {src_path.name}: {e}")
        return False

IMAGE_EXTS = {'.jpg', '.jpeg', '.png', '.heic', '.heif', '.bmp', '.tiff', '.tif', '.jpeg'}

converted = 0
deleted = 0
skipped = 0
errors = 0

for folder in sorted(BASE.iterdir()):
    if not folder.is_dir():
        continue

    folder_name = folder.name  # e.g. 'aang', 'parents', 'gallery'
    print(f"\n{'='*50}")
    print(f"Processing: {folder_name}")

    # Collect all image files, skip .gitkeep and already-done .webp
    files = sorted([
        f for f in folder.iterdir()
        if f.is_file() and f.name != '.gitkeep'
        and not (f.suffix.lower() == '.webp' and not f.name.endswith('.webp.jpg'))
    ])

    # Separate into:
    # 1. Already-named descriptive files (e.g. aang-hero-1.webp.jpg, katara-hero.webp.jpg)
    # 2. Photo date files
    # 3. IMG_ / other generic files
    # 4. Skip pure .webp (already converted)

    # Group by stage for puppy folders
    stage_counters = {}  # stage -> counter
    generic_counter = 1

    for f in files:
        ext = f.suffix.lower()
        name = f.name

        # Skip already-correct .webp files
        if ext == '.webp':
            print(f"  SKIP (already webp): {name}")
            skipped += 1
            continue

        # Handle .webp.jpg fake files (e.g. aang-hero-1.webp.jpg)
        if name.endswith('.webp.jpg'):
            base_name = name[:-4]  # strip the .jpg → gives e.g. 'aang-hero-1.webp'
            # strip the .webp too and re-add to ensure clean naming
            clean = base_name[:-5] if base_name.endswith('.webp') else base_name
            # clean = e.g. 'aang-hero-1', 'katara-hero', 'mila-puppy-hero'
            dst = folder / f"{clean}.webp"
        elif name.startswith('Photo '):
            # Date-stamped puppy/gallery photo
            stage = extract_stage(name)
            if stage and folder_name in (
                'aang','azula','bumi','hakoda','iroh','katara',
                'kyoshi','mai','sokka','toph','ty-lee','zuko'
            ):
                key = stage
                stage_counters[key] = stage_counters.get(key, 0) + 1
                n = stage_counters[key]
                dst = folder / f"{folder_name}-{stage}-{n:03d}.webp"
            else:
                # gallery or unknown stage
                dst = folder / f"{folder_name}-{generic_counter:03d}.webp"
                generic_counter += 1
        else:
            # IMG_XXXX, 2867767E-..., etc.
            dst = folder / f"{folder_name}-{generic_counter:03d}.webp"
            generic_counter += 1

        # Skip if ext not an image we handle
        if ext not in IMAGE_EXTS and not name.endswith('.webp.jpg') and ext.upper() not in ['.JPG','.JPEG','.PNG','.HEIC','.HEIF','.BMP','.TIFF','.TIF']:
            # Check case-insensitive
            if f.suffix.upper() not in ('.JPG', '.JPEG', '.PNG', '.HEIC', '.HEIF', '.BMP', '.TIFF', '.TIF'):
                print(f"  SKIP (not image): {name}")
                skipped += 1
                continue

        print(f"  {name} -> {dst.name}")

        if to_webp(f, dst):
            converted += 1
            # Delete original
            try:
                f.unlink()
                deleted += 1
            except Exception as e:
                print(f"    WARNING: could not delete {name}: {e}")
        else:
            errors += 1

print(f"\n{'='*50}")
print(f"COMPLETE")
print(f"  Converted : {converted}")
print(f"  Deleted   : {deleted}")
print(f"  Skipped   : {skipped}")
print(f"  Errors    : {errors}")
