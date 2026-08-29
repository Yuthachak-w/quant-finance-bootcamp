def calculate_roi(buy_price, sell_price):
	profit_loss = sell_price - buy_price
	percentage_return = (profit_loss / buy_price) * 100
	return percentage_return
kbank_return = calculate_roi(120, 150)
print("ผลตอบแทนของหุ้น KBANK (%):")
print(kbank_return)
bbla_return = calculate_roi(50, 45)
print("ผลตอบแทนของหุ้น BBLA (%):")
print(bbla_return)