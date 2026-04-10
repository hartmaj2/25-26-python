from pathlib import Path
from PIL import Image, ImageDraw
import numpy as np
from scipy import ndimage


def detect_sprite_boxes(
    image: Image.Image,
    alpha_threshold: int = 10,
    min_area: int = 20,
    padding: int = 0,
):
    """
    Detect bounding boxes of separate sprites using connected components
    on the alpha channel.

    Returns:
        list[tuple[int, int, int, int]]
        Each box is (left, top, right, bottom), with right/bottom exclusive.
    """
    rgba = np.array(image.convert("RGBA"))
    alpha = rgba[:, :, 3]

    # Foreground mask
    mask = alpha > alpha_threshold

    # 8-neighborhood connectivity
    structure = np.ones((3, 3), dtype=np.uint8)
    labeled, num_labels = ndimage.label(mask, structure=structure)

    height, width = mask.shape
    boxes = []

    for label in range(1, num_labels + 1):
        ys, xs = np.where(labeled == label)

        if xs.size == 0:
            continue

        area = xs.size
        if area < min_area:
            continue

        left = max(0, xs.min() - padding)
        top = max(0, ys.min() - padding)
        right = min(width, xs.max() + 1 + padding)
        bottom = min(height, ys.max() + 1 + padding)

        boxes.append((left, top, right, bottom))

    # Sort: top-to-bottom, then left-to-right
    boxes.sort(key=lambda b: (b[1], b[0]))
    return boxes


def save_crops(
    image: Image.Image,
    boxes: list[tuple[int, int, int, int]],
    output_dir: str,
    prefix: str = "sprite",
):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for i, box in enumerate(boxes):
        cropped = image.crop(box)
        cropped.save(output_path / f"{prefix}_{i:03d}.png")


def save_preview(
    image: Image.Image,
    boxes: list[tuple[int, int, int, int]],
    preview_path: str,
    line_width: int = 2,
):
    preview = image.convert("RGBA").copy()
    draw = ImageDraw.Draw(preview)

    for i, (left, top, right, bottom) in enumerate(boxes):
        draw.rectangle((left, top, right - 1, bottom - 1), outline=(255, 0, 0, 255), width=line_width)
        draw.text((left, top), str(i), fill=(255, 0, 0, 255))

    preview.save(preview_path)


def extract_sprites(
    image_path: str,
    output_dir: str = "sprites_out",
    preview_path: str = "preview.png",
    alpha_threshold: int = 10,
    min_area: int = 20,
    padding: int = 1,
):
    image = Image.open(image_path).convert("RGBA")

    boxes = detect_sprite_boxes(
        image=image,
        alpha_threshold=alpha_threshold,
        min_area=min_area,
        padding=padding,
    )

    save_crops(image, boxes, output_dir)
    save_preview(image, boxes, preview_path)

    print(f"Detected {len(boxes)} sprites.")
    print(f"Crops saved to: {output_dir}")
    print(f"Preview saved to: {preview_path}")

    for i, box in enumerate(boxes):
        print(f"{i:03d}: {box}")


if __name__ == "__main__":
    extract_sprites(
        image_path="rpgcritters2.png",
        output_dir="sprites_out",
        preview_path="preview.png",
        alpha_threshold=10,
        min_area=20,
        padding=1,
    )