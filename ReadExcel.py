import xlrd
# we neeed to create an object of workbook
wk = xlrd.open_workbook("XLRD.xls")

print(wk.nsheets)

# we need to create sheet object
ws = wk.sheet_by_name("Sheet1")
# print(ws.nrows)
# print(ws.ncols)
# Pick a data
# wc = ws.cell(2,1)
# print(wc.value)

n = ws.nrows
c = ws.ncols

for i in range(0,n):
    for j in range(0,c):
        wc = ws.cell(i,j)
        print(wc.value)




