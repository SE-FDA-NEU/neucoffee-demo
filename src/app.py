"""NeuCoffee Analytics — ứng dụng nhỏ đọc CSV doanh thu và tổng hợp."""

from flask import Flask, render_template_string, request

from revenue import parse_sales_csv, summarise_by_day

app = Flask(__name__)

PAGE = """
<!doctype html>
<title>NeuCoffee Analytics</title>
<h1>Tải lên file doanh thu</h1>
<form method=post enctype=multipart/form-data>
  <input type=file name=file accept=".csv">
  <button type=submit>Tổng hợp</button>
</form>
{% if error %}<p style="color:crimson">{{ error }}</p>{% endif %}
{% if rows %}
<table border=1 cellpadding=6>
  <tr><th>Ngày</th><th>Doanh thu</th></tr>
  {% for day, total in rows %}<tr><td>{{ day }}</td><td>{{ total }}</td></tr>{% endfor %}
</table>
{% endif %}
"""


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method != "POST":
        return render_template_string(PAGE, rows=None, error=None)

    uploaded = request.files.get("file")
    if uploaded is None or uploaded.filename == "":
        return render_template_string(PAGE, rows=None, error="Chưa chọn file nào.")

    try:
        sales = parse_sales_csv(uploaded.stream)
    except ValueError as exc:
        return render_template_string(PAGE, rows=None, error=str(exc))

    return render_template_string(PAGE, rows=summarise_by_day(sales), error=None)


if __name__ == "__main__":
    app.run(debug=True)
