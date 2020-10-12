import openpyxl

vk = openpyxl.Workbook()
sh = vk.active
sh.title="HelloTEstingWorld"
print(sh.title)
sh['A4'].value="www.theTw.com"

#create a second sheet
vk.create_sheet(title="Test2")
#sh1.vk['Test2']
#sh1['A3'] = "324411323432"
vk.save("Pysheets.xlsx")