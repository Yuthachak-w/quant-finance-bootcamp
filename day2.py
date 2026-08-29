income = 60000
has_bad_credit = False
age = 65
if income >= 30000 and not has_bad_credit:
	if age > 60:
		result = "อนุมัต แต่อยู่ในกลุ่มเบี้ยประกันความเสี่ยงสูง"
	elif age > 18: 
		result = "อนุมัติ ผ่านเกณฑ์ความเสี่ยงปกติ"
	else:
		result = "ปฏิเสธ เนื่องจากอายุไม่บรรลุนิติภาวะ"
else:
	result = "ปฏิเสธ เนื่องจากรายได้ไม่ถึงเกณฑ์ หรือมีประวัติเครดิตบูโร"
print("ผลการตรวจสอบระบบ:")
print(result)