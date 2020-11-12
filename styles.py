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

def set_style_cards(sheet):
    '''Форматирует таблицу'''
    for cell in sheet[1]:
        cell.style = header
    col = sheet.column_dimensions['C']
    col.alignment = Alignment(horizontal='fill')
    sheet['B1'] = "Сотрудник"
    sheet['C1'] = "Проект"
    sheet['D1'] = "Описание"
    sheet['E1'] = "Часы"
    sheet.delete_cols(1)
    for i in 'ABCD':
        sheet.column_dimensions[i].width = 18
    sheet.auto_filter.ref = "A1:B1"
    for i in 'ABCD':
        for cell in sheet[i]:
            cell.border = Border(bottom=Side(border_style="thin"),
                                   top=Side(border_style="thin"),
                                   left=Side(border_style="thin"),
                                   right=Side(border_style="thin"))
    return sheet


def set_style_creators(sheet, employee=False):
    '''Форматирует таблицу'''
    sheet.column_dimensions['A'].width = 18
    sheet.column_dimensions['B'].width = 18
    if employee:
        sheet['A1'] = 'Сотрудник'
    else:
        sheet['A1'] = 'Проект'
    sheet['B1'] = 'Часы'
    for cell in sheet[1]:
        cell.style = header
    for i in 'AB':
        for cell in sheet[i]:
            cell.border = Border(bottom=Side(border_style="thin"),
                                   top=Side(border_style="thin"),
                                   left=Side(border_style="thin"),
                                   right=Side(border_style="thin"))

    return sheet
