import xlwt

# create an object of workbook

wk = xlwt.Workbook()
ws = wk.add_sheet("Testing")
ws.write(0,0,"Testing WOrld")
ws.write(0,1,"www.theTestingWorld.com")

wk.save("TestingWorld1.xlsx")
