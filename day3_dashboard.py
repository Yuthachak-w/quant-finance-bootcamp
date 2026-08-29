def get_average(prices):
	total = 0 
	for p in prices:
		total = total + p
	return total / len(prices)
def make_decision(current_price, avg_price):
	if current_price < avg_price:
		return "คำแนะนำ: น่าซื้อ (เนื่องจากราคาปัจจุบันต่ำกว่าค่าเฉลี่ย)"
	else:
		return "คำแนะนำ: ถือหรือรอดูสถานการณ์ (ราคาปัจจุบันสูงกว่าค่าเฉลี่ย)"
ptt_prices = [32.0, 32.5, 33.0, 31.5, 31.0]
ptt_current = 30.5
ptt_avg = get_average(ptt_prices)
ptt_signal = make_decision(ptt_current, ptt_avg)
print("--- ระบบวิเคราะห์หุ้น QUANT DASHBOARD V1.0 ---")
print ("ราคาเฉลี่ยย้อนหลัง 5 วัน:")
print(ptt_avg)
print("ราคาปัจจุบัน:")
print(ptt_current)
print(ptt_signal)