import os
import re
from pathlib import Path
from datetime import datetime

from pillow_heif import register_heif_opener
register_heif_opener()
from PIL import Image, ImageOps

PUPPIES_BASE = Path(r"C:\Users\muram\Dev\ak9puppies\public\assets\processed\puppies")

# Only process folders that still have originals
TARGET_FOLDERS = ['bumi', 'hakoda', 'iroh', 'katara', 'kyoshi', 'mai', 'sokka', 'toph', 'ty-lee', 'zuko']

MONTH_MAP = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}
BIRTH = datetime(2026, 3, 30)

def date_to_stage(month_str, day):
    month = MONTH_MAP.get(month_str, 0)
    if not month:
        return None
    age_days = (datetime(2026, month, day) - BIRTH).days
    if age_days <= 15:   return 'newborn'
    elif age_days <= 35: return '3w'
    elif age_days <= 45: return '6w'
    else:                return '7w'

def extract_stage(filename):
    m = re.match(r'Photo\s+(\w+)\s+(\d+)\s+\d+', filename)
    if m:
        return date_to_stage(m.group(1), int(m.group(2)))
    return None

def to_webp(src, dst):
    try:
        with Image.open(src) as img:
            try:
                img = ImageOps.exif_transpose(img)
            except Exception:
                pass
            if img.mode not in ('RGB', 'RGBA'):
                img = img.convert('RGB')
            img.save(dst, 'WEBP', quality=88, method=4)
        return True
    except Exception as e:
        print(f"  ERROR {src.name}: {e}")
        return False

converted = deleted = skipped = errors = 0

for folder_name in TARGET_FOLDERS:
    puppy_dir = PUPPIES_BASE / folder_name
    if not puppy_dir.exists():
        continue
    print(f"\n--- {folder_name} ---")

    files = sorted([
        f for f in puppy_dir.iterdir()
        if f.is_file() and f.name != '.gitkeep'
        and not (f.suffix.lower() == '.webp' and not f.name.endswith('.webp.jpg'))
    ])

    stage_counters = {}
    generic_counter = 1

    # Offset generic counter to avoid clashing with already-converted webp files
    existing_webp = [f for f in puppy_dir.iterdir() if f.suffix.lower() == '.webp']
    if existing_webp:
        # Find max generic counter already used
        for w in existing_webp:
            m = re.match(rf'{folder_name}-(\d+)\.webp', w.name)
            if m:
                generic_counter = max(generic_counter, int(m.group(1)) + 1)

    # Offset stage counters for already-converted files
    for w in existing_webp:
        for stage in ['newborn', '3w', '6w', '7w']:
            m = re.match(rf'{folder_name}-{stage}-(\d+)\.webp', w.name)
            if m:
                stage_counters[stage] = max(stage_counters.get(stage, 0), int(m.group(1)))

    for f in files:
        fname = f.name
        ext_lower = f.suffix.lower()

        if ext_lower == '.webp' and not fname.endswith('.webp.jpg'):
            skipped += 1
            continue

        if fname.endswith('.webp.jpg'):
            clean = fname[:-9]
            dst = puppy_dir / f"{clean}.webp"
        elif fname.startswith('Photo '):
            stage = extract_stage(fname) or 'unknown'
            stage_counters[stage] = stage_counters.get(stage, 0) + 1
            dst = puppy_dir / f"{folder_name}-{stage}-{stage_counters[stage]:03d}.webp"
        else:
            dst = puppy_dir / f"{folder_name}-{generic_counter:03d}.webp"
            generic_counter += 1

        print(f"  {fname} -> {dst.name}")
        if to_webp(f, dst):
            converted += 1
            f.unlink()
            deleted += 1
        else:
            errors += 1

print(f"\n=== DONE ===")
print(f"Converted: {converted}  Deleted: {deleted}  Skipped: {skipped}  Errors: {errors}")
