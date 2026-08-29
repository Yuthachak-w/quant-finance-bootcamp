net_income = 200000
if net_income <= 150000:
	tax_rate = 0.0
	tax_payable = 0
elif net_income <= 300000:
	tax_rate = 0.05
	tax_payable = (net_income - 150000) * tax_rate
else:
	tax_rate = 0.10
	tax_payable = ((300000 - 150000) * 0.05) + ((net_income - 300000) * tax_rate)
print("อัตราภาษีฐานสูงสุดของคุณคือ:", tax_rate = 100, "%")
print("ยอดภาษีรวมที่ต้องจ่าย:, tax_payable, "บาท")
