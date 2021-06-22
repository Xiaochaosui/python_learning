# 把内容写进Excel
import  xlwt
def write_old_xls(worksheet: xlwt.Worksheet, data, offset=0, ):
    style = xlwt.Style.easyxf(
        f"font: height 200, name 宋体; align: vert centre, horiz center, wrap 1; borders: left {xlwt.Borders.THIN},"
        f" right {xlwt.Borders.THIN}, top {xlwt.Borders.THIN}, bottom {xlwt.Borders.THIN}")
    for k, v in enumerate(data):
        k = k + offset
        height = 50
        for key, value in enumerate(v):
            width = worksheet.col(key).width
            if str(value).split(".")[-1].upper() in ["JPG", "JPEG", "PNG"]:
                value = value.replace(config["FILE"]["PATH"], config["FILE"]["IP"])
            if len(str(value)) * 200 > worksheet.col(key).width:
                width = len(value) * 200
            worksheet.col(key).width = width
            if "http" in str(value):
                value = xlwt.Formula(f'Hyperlink("{value}";"{value}")')
            worksheet.write(k, key, value, style=style)
        worksheet.row(k).height_mismatch = True
        worksheet.row(k).height = int(20 * height)

