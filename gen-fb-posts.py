#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tao anh banner 1200x630 cho cac bai dang Facebook Fanpage Cyber B."""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, 'fb-posts')
os.makedirs(OUT, exist_ok=True)

W, H = 1200, 630
BG_TOP = (11, 18, 32)
BG_BOT = (24, 32, 54)
ORANGE = (255, 122, 0)
WHITE = (255, 255, 255)
MUTED = (176, 186, 210)
GREEN = (60, 220, 140)


def font(size, bold=False):
    names = []
    if bold:
        names += ['arialbd.ttf', 'Arial Bold.ttf', 'seguisb.ttf']
    names += ['arial.ttf', 'Arial.ttf', 'segoeui.ttf', 'DejaVuSans.ttf']
    for n in names:
        try:
            return ImageFont.truetype(n, size)
        except Exception:
            pass
    for root in ['C:/Windows/Fonts', '/usr/share/fonts/truetype/dejavu']:
        if os.path.isdir(root):
            for f in os.listdir(root):
                if ('bold' in f.lower() or 'bd' in f.lower()) == bold and f.lower().endswith('.ttf'):
                    try:
                        return ImageFont.truetype(os.path.join(root, f), size)
                    except Exception:
                        pass
    return ImageFont.load_default()


def gradient():
    img = Image.new('RGB', (W, H), BG_TOP)
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / (H - 1)
        d.line([(0, y), (W, y)],
               fill=tuple(int(BG_TOP[i] + (BG_BOT[i] - BG_TOP[i]) * t) for i in range(3)))
    return img


def fit(text, f, maxw):
    """Chu dong wrap theo do rong pixel."""
    words, lines, cur = text.split(' '), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if f.getlength(t) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_lines(d, text, f, x, y, maxw, fill, lh, align='left'):
    for ln in fit(text, f, maxw):
        ox = 0
        if align == 'center':
            ox = (maxw - f.getlength(ln)) / 2
        d.text((x + ox, y), ln, font=f, fill=fill)
        y += lh
    return y


def badge(d, x, y, label, f, pad=14, fill=GREEN, fg=(10, 20, 15)):
    tw = f.getlength(label)
    h = f.size + pad
    d.rounded_rectangle([x, y, x + tw + pad * 2, y + h], radius=h / 2, fill=fill)
    d.text((x + pad, y + pad / 2 - 2), label, font=f, fill=fg)
    return x + tw + pad * 2


def make(name, kicker, title, sub, bullets, badge_text=None, img_rel=None, price=None):
    img = gradient()
    d = ImageDraw.Draw(img)

    # accent bar top
    d.rectangle([0, 0, W, 8], fill=ORANGE)

    # subtle glow circle right
    glow = Image.new('RGB', (W, H), (0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([W - 380, -180, W + 260, 460], fill=(46, 34, 20))
    img = Image.blend(img, Image.blend(img, glow, 0.0), 0.0)
    img = Image.composite(img, img, Image.new('L', (W, H), 255))

    d = ImageDraw.Draw(img)

    # brand
    d.text((70, 52), 'PD', font=font(38, True), fill=WHITE)
    w12682 = font(38, True).getlength('PD')
    d.text((70 + w12682, 52), '12682', font=font(38, True), fill=ORANGE)
    d.text((72, 98), 'C Y B E R   B   •   P H O N E   S T O R E', font=font(15, True), fill=MUTED)

    y = 150
    if kicker:
        d.text((70, y), kicker, font=font(21, True), fill=ORANGE)
        y += 42

    ft = font(52, True)
    y = draw_lines(d, title, ft, 70, y, 640, WHITE, 60)

    if sub:
        y += 6
        y = draw_lines(d, sub, font(24), 70, y, 640, MUTED, 34)

    if bullets:
        y += 20
        fb = font(20)
        for b in bullets:
            d.ellipse([72, y + 9, 84, y + 21], fill=GREEN)
            d.text((100, y), b, font=fb, fill=WHITE)
            y += 34

    if price:
        y += 14
        d.text((70, y), 'Giá:', font=font(24), fill=MUTED)
        pw = font(24).getlength('Giá: ')
        d.text((70 + pw, y - 4), price, font=font(38, True), fill=ORANGE)

    # product image right
    if img_rel and os.path.exists(os.path.join(BASE, img_rel)):
        p = Image.open(os.path.join(BASE, img_rel)).convert('RGBA')
        # Lo nen trang/sang -> trong suot
        px_ = p.load()
        for yy in range(p.height):
            for xx in range(p.width):
                r, g, b, a = px_[xx, yy]
                if r > 242 and g > 242 and b > 242:
                    px_[xx, yy] = (r, g, b, 0)
                elif r > 228 and g > 228 and b > 228:
                    px_[xx, yy] = (r, g, b, int(a * 0.45))
        scale = min(400 / p.width, 400 / p.height)
        p = p.resize((int(p.width * scale), int(p.height * scale)), Image.LANCZOS)
        # card nen toi cho san pham noi bat
        card_w, card_h = p.width + 48, p.height + 48
        card = Image.new('RGBA', (card_w, card_h), (255, 255, 255, 22))
        mask = Image.new('L', (card_w, card_h), 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, card_w - 1, card_h - 1],
                                               radius=28, fill=255)
        card.paste(p, (24, 24), p)
        card.putalpha(mask)
        px = W - card_w - 60
        py = (H - card_h) // 2
        img.paste(card, (px, py), card)
        d = ImageDraw.Draw(img)

    # badge top-right
    if badge_text:
        fb = font(20, True)
        tw = fb.getlength(badge_text)
        d.rounded_rectangle([W - tw - 54, 44, W - 34, 44 + fb.size + 22],
                            radius=(fb.size + 22) / 2, fill=ORANGE)
        d.text((W - tw - 44, 55), badge_text, font=fb, fill=(20, 14, 6))

    # footer bar
    d.rectangle([0, H - 62, W, H], fill=(8, 12, 22))
    d.text((70, H - 45), 'emtenlamua.github.io/cyberb-facebook',
           font=font(19, True), fill=WHITE)
    d.text((W - 330, H - 45), 'Bảo hành 12 tháng  •  Giao 2 giờ  •  Trả góp 0%',
           font=font(17), fill=MUTED)

    path = os.path.join(OUT, name + '.png')
    img.convert('RGB').save(path, 'PNG', optimize=True)
    print('OK', path)


if __name__ == '__main__':
    make('post-01-tong-quan', '25 MẪU ĐIỆN THOẠI CHÍNH HÃNG',
         'Giá tốt nhất tháng này', 'Apple • Samsung • Xiaomi • OPPO • vivo • realme',
         ['Bảo hành chính hãng 12 tháng', 'Giao hàng 2 giờ nội thành',
          'Trả góp 0% qua thẻ tín dụng', 'Đổi trả 1-1 trong 7 ngày'],
         'HOTLINE 079 634 6492', 'img/og-cover.png')

    make('post-02-galaxy-s25', 'SAMSUNG GALAXY S25 256GB',
         'Đẳng cấp công nghệ', 'Chip Snapdragon 8 Elite • Camera 50MP • 120Hz',
         ['Chính hãng, bảo hành 12 tháng', 'Còn 12 máy trong kho',
          'Giao 2 giờ — trả góp 0%'],
         'CÒN 12 MÁY', 'img/samsung-galaxy-s25-256gb.png', '19.990.000đ')

    make('post-03-iphone-16-pro-max', 'APPLE iPHONE 16 PRO MAX 256GB',
         'Flagship đỉnh cao', 'Màn hình LTPO 120Hz • Camera tele • IP68',
         ['Giảm 2.000.000đ so với giá gốc', 'Còn 11 máy • Đánh giá 4.7/5',
          'Bảo hành chính hãng 12 tháng'],
         'BÁN CHẠY #1', 'img/apple-iphone-16-pro-max-256gb.png', '32.990.000đ')

    make('post-04-galaxy-s25-ultra', 'SAMSUNG GALAXY S25 ULTRA 256GB',
         'Đỉnh cao thực sự', 'Camera 200MP zoom cực đỉnh • Sạc nhanh 45W',
         ['Chính hãng, bảo hành 12 tháng', 'Còn 8 máy • Đánh giá 4.8/5',
          'Giao 2 giờ — COD toàn quốc'],
         'CÒN 8 MÁY', 'img/samsung-galaxy-s25-ultra-256gb.png', '28.990.000đ')

    make('post-05-xiaomi-14t-pro', 'XIAOMI 14T PRO 256GB',
         'Cấu hình khủng, giá mềm', 'Hiệu năng mạnh • Camera 50MP • Sạc 120W',
         ['Chính hãng, bảo hành 12 tháng', 'Còn 15 máy • Đánh giá 4.8/5',
          'Trả góp 0% qua thẻ tín dụng'],
         'GIÁ TỐT', 'img/xiaomi-xiaomi-14t-pro-256gb.png', '13.990.000đ')

    make('post-06-reno13', 'OPPO RENO13 5G 256GB',
         'Camera chân dung đỉnh cao', 'Camera 50MP • AMOLED 120Hz • Sạc 80W',
         ['Chính hãng, bảo hành 12 tháng', 'Còn 20 máy • Đánh giá 4.8/5',
          'Giao 2 giờ nội thành'],
         'CÒN 20 MÁY', 'img/oppo-reno13-5g-256gb.png', '12.490.000đ')

    make('post-07-tai-nghe-sony', 'TAI NGHE SONY WH-1000XM5',
         'Chất âm đỉnh cao', 'Chống ồn chủ động • Pin 30 giờ • Bluetooth 5.2',
         ['Chính hãng, bảo hành 12 tháng', 'Còn 12 máy • Đánh giá 4.8/5',
          'Tặng tai nghe cho đơn từ 5 triệu'],
         'PHỤ KIỆN HOT', 'img/sony-sony-wh-1000xm5.png', '6.990.000đ')

    make('post-08-bao-hanh', 'PD12682 / CYBER B',
         'Bảo hành chính hãng 12 tháng', 'Mua sắm an tâm — đổi trả 1-1 trong 7 ngày',
         ['Bảo hành chính hãng 12 tháng', 'Đổi trả 1-1 trong 7 ngày',
          'Thu cũ đổi mới trợ giá 2 triệu', 'COD thanh toán khi nhận hàng'],
         'AN TÂM MUA SẮM', None)

    make('post-09-flash-sale', 'FLASH SALE CUỐI TUẦN',
         'Giảm đến 2 triệu đồng', 'Hết hạn Chủ Nhật này — số lượng có hạn',
         ['iPhone 16 Pro Max: giảm 2.000.000đ', 'Galaxy S25 256GB: 19.990.000đ',
          'Xiaomi 14T Pro: 13.990.000đ', 'Freeship toàn quốc từ 500.000đ'],
         'HẾT HẠN CHỦ NHẬT', None)

    make('post-10-chon-may', 'HƯỚNG DẪN CHUYÊN GIA',
         'Chọn điện thoại theo ngân sách', 'Gợi ý cụ thể cho từng mức giá',
         ['Cần chơi game tầm 15 triệu', 'Chụp ảnh đẹp tầm 20 triệu',
          'Dùng lâu, pin trâu', 'Tư vấn miễn phí 24/7'],
         'TƯ VẤN MIỄN PHÍ', None)

    make('post-11-kiem-tra-may', 'HƯỚNG DẪN A-Z',
         '7 bước kiểm tra máy khi nhận hàng', 'Trước khi thanh toán, bạn nên làm đúng các bước này',
         ['Kiểm tra IMEI và phụ kiện', 'Test camera, loa, cảm ứng',
          'Kiểm tra tình trạng máy', 'Báo lại ngay nếu có vấn đề'],
         'CHECKLIST NHẬN HÀNG', None)
