principal = 100000
interest_rate = 0.05
print("--- รายงานการเติบโตของเงินฝากรายปี ---")
for year in range (1, 11):
	interest = principal * interest_rate
	principal = principal + interest
	print("สิ้นปีที่")
	print(year)
	print("เงินละสมรวม (บาท):")
	print(principal)