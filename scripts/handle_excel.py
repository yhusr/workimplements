"""
Time:2019/12/18 0018
"""
import openpyxl

from scripts.handle_path import EXCEL_PATH

class ExcelObj:
    pass


class HandleExcel:
    def __init__(self, sheetname, filepath=None):
        if filepath:
            self.filepath = filepath
        else:
            self.filepath = EXCEL_PATH
        self.sheetname = sheetname

    def open_excel(self):
        self.workbook = openpyxl.load_workbook(self.filepath)
        self.sh = self.workbook[self.sheetname]

    def read_excel(self):
        self.open_excel()
        excel_rows = list(self.sh.rows)
        head_rows = [h.value for h in excel_rows[0]]
        list_obj = []
        for e in excel_rows[1:]:
            eo = ExcelObj()
            value_rows = [v.value for v in e]
            zip_hv = zip(head_rows, value_rows)
            for zh in zip_hv:
                setattr(eo, zh[0], zh[1])
            list_obj.append(eo)
        self.workbook.close()
        return list_obj

    def write_excel(self, row_num, col_num, value):
        self.open_excel()
        self.sh.cell(row=row_num, column=col_num, value=value)
        self.workbook.save(self.filepath)
        self.workbook.close()


if __name__ == '__main__':
    he = HandleExcel('register')
    obj_li = he.read_excel()
    print(obj_li[0].data)
