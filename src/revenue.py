"""Đọc và tổng hợp dữ liệu doanh thu.

Tách khỏi app.py để test được mà không cần dựng server.
"""

import csv
import io
from collections import defaultdict

REQUIRED_COLUMNS = {"date", "product", "amount"}


def _as_text(stream):
    """Flask đưa vào stream nhị phân, test đưa vào StringIO. Nhận cả hai."""
    if isinstance(stream, io.TextIOBase):
        return stream
    return io.TextIOWrapper(stream, encoding="utf-8-sig")


def parse_sales_csv(stream):
    """Đọc CSV doanh thu, trả về list dict. Ném ValueError nếu file sai."""
    reader = csv.DictReader(_as_text(stream))

    if reader.fieldnames is None:
        raise ValueError("File rỗng.")

    missing = REQUIRED_COLUMNS - set(reader.fieldnames)
    if missing:
        raise ValueError(f"Thiếu cột bắt buộc: {', '.join(sorted(missing))}")

    rows = []
    for line_no, row in enumerate(reader, start=2):
        try:
            amount = float(row["amount"])
        except (TypeError, ValueError):
            raise ValueError("Cột amount phải là số.") from None
        rows.append({"date": row["date"], "product": row["product"], "amount": amount})

    if not rows:
        raise ValueError("File không có dòng dữ liệu nào.")
    return rows


def summarise_by_day(sales):
    """Gộp doanh thu theo ngày, trả về list (ngày, tổng) đã sắp xếp."""
    totals = defaultdict(float)
    for row in sales:
        totals[row["date"]] += row["amount"]
    return sorted(totals.items())
