from openpyxl.styles import NamedStyle, Font, Alignment, Border, Side, PatternFill


header = NamedStyle(name="header")
header.font = Font(bold=True)
header.border = Border(bottom=Side(border_style="thin"),
                       top=Side(border_style="thin"),
                       left=Side(border_style="thin"),
                       right=Side(border_style="thin"))
header.alignment = Alignment(horizontal="center", vertical="center")
header.fill = PatternFill(start_color='52cc00',
                   end_color='52cc00',
                   fill_type='solid')

def set_style(sheet):
    '''Форматирует таблицу'''
    for cell in sheet[1]:
        cell.style = header
    col = sheet.column_dimensions['C']
    col.alignment = Alignment(horizontal='fill')
    sheet.column_dimensions['A'].width = 18
    sheet.column_dimensions['B'].width = 18
    sheet.column_dimensions['C'].width = 18
    sheet.column_dimensions['D'].width = 25
    sheet.auto_filter.ref = "A1:B1"
    # sheet["G1"] = "=SUBTOTAL(9,D2:D700)"
    return sheet
