# PgApp

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://mit-license.org/)
![Version: 0.0.1](https://img.shields.io/badge/Version-0.0.1-orange.svg)

---

**Bạn mới bắt đầu xây dựng một chương trình cần giao diện đồ họa mà chưa biết bắt đầu từ đâu hay quản lý cửa sổ, sự kiện như thế nào, PgApp sẽ giúp bạn.**

**PgApp là thư viện hỗ trợ xây dựng và phát triển phần mềm cần giao diện đồ họa một cách nhanh chóng nhờ các tính năng quản lý và xây dựng dễ tiếp cận.**

## Cách tải

```bash
# Install latest stable version from PyPI
pip install pgapp
```

## Phụ thuộc

PgApp phụ thuộc vào các thư viện:

| **Tên** | **Phiên bản** |
| --- | --- |
| pygame-ce | == 2.5.8 |
| argparse | == 1.4.0 |

## CLI

Cách dùng:

```bash
python -m pgapp <command> ...
```

Các lệnh:

| **<lệnh>** | **Mô tả** |
| --- | --- |
| version | Hiển thị phiên bản của PgApp. |
| start | Khởi tạo một dự án mới với PyApp. |
| config | Mở trình chỉnh sửa cấu hình (config.toml). |
| scene | Mở trình chỉnh sửa cảnh. |
| inputs | Mở trình chỉnh sửa bản đồ đầu vào. |
| theme | Mở trình chỉnh sửa chủ đề. |
| setting | Mở trình chỉnh sửa cài đặt. |
| help | Hiển thị cách dùng CLI và lệnh. |
