# HƯỚNG DẪN CÁCH LÀM WEBSITE E-COMMERCE — TỪ A ĐẾN Z
## Bài ASM WEB2053 — Cyber B Phone Store

> **Website:** https://emtenlamua.github.io/cyberb-facebook/
> **GitHub:** https://github.com/emtenlamua/cyberb-facebook
> **Fanpage:** https://www.facebook.com/profile.php?id=61595723233897
> **Blogger:** https://cyberb-phone.blogspot.com

---

## PHẦN 1: TẠO WEBSITE VÀ ĐẨY LÊN GITHUB PAGES

### Bước 1: Chuẩn bị source code
- Source code website gồm: HTML, CSS, JavaScript, JSON data, hình ảnh
- Cấu trúc thư mục:
  ```
  cyberb/
  ├── index.html          (trang chủ)
  ├── products.html       (trang sản phẩm)
  ├── blog.html           (trang bài viết)
  ├── admin.html          (quản trị cửa hàng)
  ├── admin-seo.html      (cấu hình SEO & Facebook)
  ├── login.html          (đăng nhập)
  ├── style.css           (stylesheet chính)
  ├── app.js              (JavaScript chính)
  ├── admin-seo.js        (JS cho trang SEO admin)
  ├── robots.txt          (cấu hình crawler)
  ├── sitemap.xml         (sitemap cho Google)
  ├── data/               (dữ liệu JSON)
  │   ├── products.json   (41 sản phẩm)
  │   ├── posts.json      (6 bài viết)
  │   ├── users.json      (tài khoản đăng nhập)
  │   ├── seo.json        (cấu hình SEO hệ thống)
  │   └── facebook.json   (cấu hình Facebook)
  ├── img/                (hình ảnh: og-cover, banner)
  └── sp-*.html           (41 trang sản phẩm riêng biệt)
  └── bv-*.html           (6 trang bài viết riêng biệt)
  ```

### Bước 2: Tạo repository GitHub
1. Đăng ký tài khoản GitHub tại https://github.com
2. Tạo repository mới:
   - **Tên repo:** `cyberb-facebook`
   - **Visibility:** Public
   - **Initialize:** README
3. Lấy Personal Access Token:
   - Vào Settings → Developer settings → Personal access tokens
   - Tạo token mới với scope `repo` và `read:org`

### Bước 3: Push code lên GitHub
```bash
# Khởi tạo git
git init
git config user.name "emtenlamua"
git config user.email "quanhi1805@gmail.com"

# Thêm remote và push
git remote add origin https://github.com/emtenlamua/cyberb-facebook.git
git add -A
git commit -m "Initial commit - Cyber B Phone Store"
git push -u origin master
```

### Bước 4: Bật GitHub Pages
1. Vào repository → Settings → Pages
2. Source: Deploy from branch
3. Branch: `master` / root `/`
4. Save → Chờ 1-2 phút build
5. Website live tại: `https://emtenlamua.github.io/cyberb-facebook/`

**Cách bật GitHub Pages bằng API (nếu không thấy nút Settings):**
```bash
gh api repos/emtenlamua/cyberb-facebook/pages -X POST \
  -f source[branch]=master -f source[path]=/
```

---

## PHẦN 2: TẠO FANPAGE FACEBOOK

### Bước 1: Tạo Fanpage
1. Vào https://www.facebook.com/pages/create
2. Chọn loại: **Shopping & Retail**
3. Điền thông tin:
   - **Tên page:** Cyber B
   - **Mô tả:** Cửa hàng điện thoại chính hãng, bảo hành 12 tháng, giao 2 giờ
   - **Ảnh đại diện:** Logo Cyber B
   - **Ảnh bìa:** Banner sản phẩm
4. Tạo xong → lấy Page ID từ URL

### Bước 2: Tạo bài đăng Facebook
- Thiết kế 11 banner (1200×630px) bằng Python Pillow:
  - Nền gradient cam-đen
  - Ảnh sản phẩm (đã xử lý nền trắng)
  - Logo Cyber B + giá + SĐT
- Viết 11 nội dung bài đăng kèm banner
- Lên lịch đăng: 2 tuần, cách ngày

### Bước 3: Cấu hình Facebook trên website
- Vào `admin-seo.html` → Tab 4 (Cấu hình Facebook)
- Điền:
  - **Tên page:** Cyber B Shop
  - **Page ID:** 61595723233897
  - **Đường dẫn page:** https://www.facebook.com/profile.php?id=61595723233897
- Bật:
  - ✅ Bong bóng nhắn tin (Messenger)
  - ✅ Nút chia sẻ Facebook

---

## PHẦN 3: TỐI ƯU SEO

### Bước 1: SEO cho từng sản phẩm (Tab 1)
- Vào `admin-seo.html` → Tab 1 (SEO sản phẩm)
- Mỗi sản phẩm có 5 trường SEO:
  1. **Tiêu đề SEO:** `iPhone 16 Pro Max 256GB — 32.990.000₫ | Cyber B` (30-65 ký tự)
  2. **Meta description:** Mô tả 120-160 ký tự, có giá + bảo hành + giao hàng
  3. **Keywords:** Tên sản phẩm + thương hiệu + danh mục + "chính hãng"
  4. **Slug:** `iphone-16-pro-max-256gb` (không dấu, cách bằng dấu gạch)
  5. **Ảnh OG:** URL ảnh sản phẩm
- Có nút "Tạo tự động" để sinh SEO từ dữ liệu sản phẩm
- **Kết quả: 41/41 sản phẩm đạt SEO**

### Bước 2: SEO cho từng bài viết (Tab 2)
- Vào `admin-seo.html` → Tab 2 (SEO bài viết)
- Tương tự sản phẩm, mỗi bài viết có: title, description, keywords, slug, ogImage
- **Kết quả: 6/6 bài viết đạt SEO**

### Bước 3: Tối ưu SEO hệ thống (Tab 3)
- Vào `admin-seo.html` → Tab 3 (Tối ưu SEO hệ thống)
- Cấu hình:
  - **Tên website:** Cyber B
  - **Mẫu tiêu đề:** `%s | Cyber B`
  - **Tiêu đề trang chủ:** `Cyber B — Điện thoại chính hãng, giá tốt, giao 2 giờ`
  - **Meta description:** 157 ký tự (trong khoảng 120-160)
  - **Keywords:** 15 cụm từ khoá
  - **Canonical base:** `https://emtenlamua.github.io/cyberb-facebook/`
  - **Ảnh OG mặc định:** `https://emtenlamua.github.io/cyberb-facebook/img/og-cover.png`
  - **Ngôn ngữ:** vi_VN
  - **Robots:** index,follow
  - **Twitter card:** summary_large_image
  - **Sitemap:** Bật
  - **Google Analytics:** G-QW3TSMDH34
  - **Google Search Console:** Đã xác minh
  - **JSON-LD:** Tên tổ chức + SĐT + email + địa chỉ
- **Điểm SEO hệ thống: 100/100**

### Bước 4: Sửa Canonical URL
- Vấn đề: 59 file HTML đều trỏ canonical về `/cyberb/` (sai)
- Đã sửa thành `/cyberb-facebook/` (đúng) cho toàn bộ 59 file
- 9 file thiếu canonical → đã thêm mới
- **Cách sửa:** Dùng Python script `fix-seo-canonical-ga.py`

### Bước 5: Sửa Sitemap và Robots.txt
- **sitemap.xml:** 50 URL, đã sửa từ `/cyberb/` sang `/cyberb-facebook/`
- **robots.txt:**
  ```
  User-agent: *
  Allow: /
  Disallow: /admin.html
  Disallow: /admin-seo.html
  Disallow: /login.html
  Sitemap: https://emtenlamua.github.io/cyberb-facebook/sitemap.xml
  ```

---

## PHẦN 4: GOOGLE ANALYTICS + SEARCH CONSOLE

### Bước 1: Tạo Google Analytics
1. Vào https://analytics.google.com
2. Tạo tài khoản mới:
   - **Tên tài khoản:** Cyber B Phone Store
3. Tạo property:
   - **Loại:** Web
   - **URL:** https://emtenlamua.github.io/cyberb-facebook/
   - **Múi giờ:** Việt Nam
4. Tạo luồng dữ liệu:
   - **Tên luồng:** Cyber B Web
5. Lấy Measurement ID: `G-QW3TSMDH34`

### Bước 2: Chèn mã Google Analytics vào website
- Thêm đoạn mã sau vào `<head>` của tất cả 59 file HTML:
```html
<!-- Google Analytics (GA4) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-QW3TSMDH34"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-QW3TSMDH34');
</script>
```
- Cách chèn: Dùng Python script tự động chèn vào trước `</head>` của mọi file
- Cập nhật `data/seo.json`: `"googleAnalytics": "G-QW3TSMDH34"`
- Commit + push lên GitHub

### Bước 3: Tạo Google Search Console
1. Vào https://search.google.com/search-console
2. Thêm property:
   - **Loại:** Tiền tố URL (URL prefix)
   - **URL:** https://emtenlamua.github.io/cyberb-facebook/
3. Xác minh quyền sở hữu:
   - Chọn phương thức: Google Analytics (G-tag)
   - Vì website đã có GA → bấm "Xác minh" là xong
4. Gửi sitemap:
   - Menu trái → Sitemaps
   - Nhập: `sitemap.xml`
   - Bấm "Gửi"
5. Cập nhật `data/seo.json`: `"searchConsole": "G-QW3TSMDH34"`

---

## PHẦN 5: TẠO BACKLINK (BLOGGER + WORDPRESS)

### Bước 1: Tạo blog Blogger
1. Vào https://www.blogger.com → đăng nhập bằng Gmail
2. Tạo blog mới:
   - **Tiêu đề:** Cyber B — Điện thoại chính hãng
   - **Địa chỉ:** cyberb-phone
   - **URL:** https://cyberb-phone.blogspot.com
3. Bật cài đặt SEO:
   - Settings → Meta tags → Bật "Enable search description"
   - Mô tả: `Cyber B — Cửa hàng điện thoại chính hãng, bảo hành 12 tháng, giao 2 giờ, trả góp 0%.`

### Bước 2: Đăng 3 bài trên Blogger
Mỗi bài:
1. Tạo bài mới → chuyển sang chế độ HTML
2. Dán nội dung HTML (đã viết sẵn)
3. Cấu hình SEO:
   - Tiêu đề, Labels, Permalink tùy chỉnh, Search description
4. Ấn Đăng (Publish)

**3 bài đã đăng:**

| Bài | Tiêu đề | Permalink |
|-----|---------|-----------|
| 1 | Mua iPhone chính hãng ở đâu? 5 điều phải kiểm tra trước khi trả tiền | mua-iphone-chinh-hang-o-dau |
| 2 | Điện thoại tầm trung dưới 15 triệu đáng mua nhất | dien-thoai-tam-trung-duoi-15-trieu |
| 3 | Trả góp 0% mua điện thoại: 5 điều cần hỏi trước khi ký | tra-gop-0-phan-tram-mua-dien-thoai |

Mỗi bài có 2 backlink:
- Link "Cyber B" → https://emtenlamua.github.io/cyberb-facebook/
- Link "fanpage Cyber B" → https://www.facebook.com/profile.php?id=61595723233897

**Tổng: 3 bài × 2 link = 6 backlink từ Blogger**

### Bước 3: Tạo blog WordPress (chưa làm)
1. Vào https://wordpress.com → Get Started
2. Chọn Blog → Miễn phí (Free)
3. Tên: Cyber B Shop — Điện thoại chính hãng
4. Địa chỉ: cyberbshop.wordpress.com
5. Đăng 3 bài tương tự (copy HTML từ Blogger)

**Tổng target: 6 bài × 2 link = 12 backlink từ 2 nền tảng**

---

## PHẦN 6: EMAIL MARKETING (BREVO)

### Bước 1: Thiết kế email template
- Tạo file `email-marketing/brevo-email.html`
- Nội dung: Logo Cyber B, 5 sản phẩm nổi bật, nút CTA, thông tin liên hệ
- Logo: `Cyber<span>B</span>` (hai màu: cam + trắng)

### Bước 2: Gửi email qua Brevo
1. Đăng ký https://www.brevo.com
2. Tạo campaign email
3. Dán HTML template
4. Chọn danh sách người nhận
5. Gửi

---

## TỔNG KẾT KẾT QUẢ

| Hạng mục | Trạng thái | Chi tiết |
|----------|------------|----------|
| Website | ✅ Hoàn thành | 59 file HTML, GitHub Pages |
| Sản phẩm | ✅ 41 sản phẩm | Có SEO đầy đủ |
| Bài viết | ✅ 6 bài viết | Có SEO đầy đủ |
| Admin panel | ✅ Có | Quản lý + Cấu hình SEO |
| Fanpage Facebook | ✅ Đã tạo | Page ID: 61595723233897 |
| Bài đăng FB | ✅ 11 banner sẵn sàng | + Lịch đăng 2 tuần |
| SEO sản phẩm | ✅ 41/41 | Title, desc, keywords, slug, ogImage |
| SEO bài viết | ✅ 6/6 | Title, desc, keywords, slug, ogImage |
| SEO hệ thống | ✅ 100/100 điểm | Meta, canonical, robots, sitemap, JSON-LD |
| Canonical URL | ✅ Đã sửa | 59 file đúng /cyberb-facebook/ |
| Sitemap | ✅ 50 URL | Đã gửi Search Console |
| Robots.txt | ✅ Có | Allow all + Disallow admin |
| Open Graph | ✅ Có | og:title, og:description, og:image, og:url |
| Google Analytics | ✅ Đã tích hợp | G-QW3TSMDH34 (59 file) |
| Search Console | ✅ Đã xác minh | + Đã gửi sitemap |
| Blogger backlink | ✅ 3 bài đã đăng | cyberb-phone.blogspot.com |
| WordPress backlink | ⚠️ Chưa làm | cyberbshop.wordpress.com |
| Email marketing | ⚠️ Template sẵn | Chưa gửi qua Brevo |

---

## THÔNG TIN TÀI KHOẢN

| Loại | Giá trị |
|------|---------|
| GitHub username | emtenlamua |
| GitHub email | quanhi1805@gmail.com |
| GitHub repo | emtenlamua/cyberb-facebook |
| Admin web | pd12881@gmail.com / admin123 |
| User web | user@gmail.com / 123456 |
| Hotline | 079 220 3565 |
| Email liên hệ | quanhi1805@gmail.com |
| Google Analytics | G-QW3TSMDH34 |
| Blogger URL | cyberb-phone.blogspot.com |
| Fanpage FB | facebook.com/profile.php?id=61595723233897 |
