import openpyxl
import qrcode
from PIL import Image

filename = 'src/sites.xlsx'


def xlsx_to_qr(file):
    file = openpyxl.load_workbook(file)
    sheet = file.active

    for row in sheet.values:
        site = row[0]
        name = 'qrs/' + str(site).split('/')[2] + '.png'
        img = qrcode.make(site)
        img.save(name)

        img = Image.open(name)
        img = img.resize(size=(900, 900))
        img.save(name)


if __name__ == '__main__':
    xlsx_to_qr(filename)
