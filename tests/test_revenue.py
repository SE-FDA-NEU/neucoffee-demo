import io
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from revenue import parse_sales_csv, summarise_by_day  # noqa: E402


def as_stream(text):
    return io.StringIO(text)


def test_parse_valid_csv():
    rows = parse_sales_csv(as_stream("date,product,amount\n2026-03-02,tra,45000\n"))
    assert len(rows) == 1
    assert rows[0]["amount"] == 45000.0


def test_missing_column_is_rejected():
    with pytest.raises(ValueError, match="amount"):
        parse_sales_csv(as_stream("date,product\n2026-03-02,tra\n"))


def test_empty_file_is_rejected():
    with pytest.raises(ValueError, match="rỗng"):
        parse_sales_csv(as_stream(""))


def test_no_data_rows_is_rejected():
    with pytest.raises(ValueError, match="không có dòng"):
        parse_sales_csv(as_stream("date,product,amount\n"))


def test_summarise_groups_by_day():
    sales = [
        {"date": "2026-03-02", "product": "a", "amount": 10.0},
        {"date": "2026-03-02", "product": "b", "amount": 5.0},
        {"date": "2026-03-03", "product": "a", "amount": 7.0},
    ]
    assert summarise_by_day(sales) == [("2026-03-02", 15.0), ("2026-03-03", 7.0)]


def test_non_numeric_amount_reports_line_number():
    with pytest.raises(ValueError, match="Dòng 2"):
        parse_sales_csv(as_stream("date,product,amount\n2026-03-02,tra,nhieu\n"))

# Rà soát: 5 test cho các trường hợp file sai.
