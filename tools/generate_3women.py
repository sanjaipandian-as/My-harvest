from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT_PATH = ROOT / "assets" / "3women.png"


def _load_font(name: str, size: int) -> ImageFont.FreeTypeFont:
    # Prefer Windows Segoe UI (matches the rest of the system UI).
    win_fonts = Path(r"C:\Windows\Fonts")
    candidate = win_fonts / name
    return ImageFont.truetype(str(candidate), size=size)


def _draw_check(draw: ImageDraw.ImageDraw, x: int, y: int, color: tuple[int, int, int]) -> None:
    # Draw a crisp checkmark similar to the reference.
    draw.line((x, y + 6, x + 6, y + 12), fill=color, width=3, joint="curve")
    draw.line((x + 6, y + 12, x + 18, y - 2), fill=color, width=3, joint="curve")


def main() -> None:
    w, h = 592, 332
    bg = (255, 255, 255)
    dark = (6, 42, 34)  # deep green
    gray = (88, 94, 99)
    light_gray = (236, 239, 241)

    img = Image.new("RGB", (w, h), bg)
    draw = ImageDraw.Draw(img)

    # Left stick figure + halo
    halo_center = (120, 135)
    halo_r = 48
    draw.pieslice(
        (
            halo_center[0] - halo_r,
            halo_center[1] - halo_r,
            halo_center[0] + halo_r,
            halo_center[1] + halo_r,
        ),
        start=200,
        end=340,
        fill=light_gray,
    )

    # Head
    head_center = (120, 112)
    head_r = 14
    draw.ellipse(
        (
            head_center[0] - head_r,
            head_center[1] - head_r,
            head_center[0] + head_r,
            head_center[1] + head_r,
        ),
        outline=dark,
        width=4,
    )

    # Body
    draw.line((120, 126, 120, 172), fill=dark, width=4)
    # Arms (slightly angled)
    draw.line((120, 146, 92, 154), fill=dark, width=4)
    draw.line((120, 146, 155, 146), fill=dark, width=4)
    # Legs
    draw.line((120, 172, 104, 200), fill=dark, width=4)
    draw.line((120, 172, 136, 200), fill=dark, width=4)

    # Text block
    heading_font = _load_font("segoeuib.ttf", 30)
    body_font = _load_font("segoeui.ttf", 20)

    heading = "When this is fixed..."
    heading_bbox = draw.textbbox((0, 0), heading, font=heading_font)
    heading_w = heading_bbox[2] - heading_bbox[0]
    draw.text(((w - heading_w) // 2, 28), heading, font=heading_font, fill=dark)

    items = [
        "Your energy improves",
        "Your health stabilizes",
        "Your stress reduces",
        "Your daily life becomes easier",
    ]

    start_y = 92
    line_gap = 50
    check_x = 250
    text_x = 282

    for i, text in enumerate(items):
        y = start_y + i * line_gap
        _draw_check(draw, check_x, y + 6, dark)
        draw.text((text_x, y), text, font=body_font, fill=gray)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH, format="PNG", optimize=True)


if __name__ == "__main__":
    main()

