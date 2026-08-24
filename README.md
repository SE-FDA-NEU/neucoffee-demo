# NeuCoffee Analytics

> Repo mẫu của môn INT2208. Đây là thứ repo nhóm các bạn nên trông như thế nào
> vào cuối Sprint 1. Đọc `docs/sprint-log.md` và `docs/retro.md` trước.

Công cụ cho chủ quán cà phê: tải lên file CSV doanh thu hằng ngày và xem tổng
hợp theo ngày, theo sản phẩm.

**Nhóm:** NeuCoffee · **Thành viên:** @linh @tuan @huy @thao
**Product Owner (cố định cả kỳ):** @linh
**Scrum Master (luân phiên mỗi sprint):** @tuan (Sprint 1) → @thao (Sprint 2)

## Chạy thử

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python src/app.py
```

Mở http://localhost:5000/upload và thử với `data/sales-sample.csv`.

## Cách nhóm làm việc

Scrum, sprint 2 tuần. Board: (link tới GitHub Project của nhóm)

**Definition of Done** — xem `docs/definition-of-done.md`

### Bốn quy tắc được thực thi bằng máy

1. **Không có issue thì không có việc.** CI chặn PR không gắn issue nào.
2. **Không commit thẳng lên `main`.** Tạo nhánh, mở PR, nhờ người khác duyệt.
3. **Một nhánh một issue**, đặt tên `<số-issue>-mô-tả-ngắn`.
4. **Mỗi sprint review code của ít nhất một người khác.**

### Nếu một thành viên ngừng phản hồi

Sau 3 ngày không trả lời trong chat nhóm: SM nhắn riêng. Sau 5 ngày: nhóm
báo giảng viên và chia lại việc của người đó trong Sprint Planning kế tiếp.
Việc đã chia lại thì không tính cho người vắng.

## Ghi chú

Dự án này dùng làm ví dụ cho môn INT2208.
