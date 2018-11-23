from band import Band

ws = Band("The White Stripes")

ws.employ("Meg", 100)
ws.employ("Jack", 100)
ws.employ("Mary", 100)
ws.write_annual_report()

ws.get_members()


ws.sack("Mary")
ws.get_members()

ws.promote("Meg", 120)
ws.write_annual_report()

