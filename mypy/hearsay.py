from band import Band

hs = Band("Hearsay")

new = ["Suzanne", "Danny", "Kym", "Myleene", "Noel"]

for name in new:
    hs.employ(name, 10)

print(hs.write_annual_report())

hs.sack("Danny")
hs.get_members()

#hs.employ("Madonna", 10000000)
