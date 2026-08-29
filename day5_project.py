
	def _init_(self, customer_name, stock_prices, gold_prices):
		self.name = customer_name
		self.stocks = stock_prices
		self.gold = gold_prices
	def calculate_average(self, price_list):
		total = 0
		for price in price_list:
			total = total + price
		return total / len(price_list)
	def analyze_risk(self, stock_weight):
		print("--- ผลการวิเคราะห์พอร์ตของ:", self.name, "---")
		avg_stock = self.calculate_average(self.stocks)
		avg_gold = self.calculate_average(self.gold)
		print("ราคาเฉลี่ยหุ้นย้อนหลัง:", avg_stock)
		print("ราคาเฉลี่ยทองคำย้อนหลัง:", avg_gold)
		print("สัดส่วนการลงทุนในสินทรัพย์เสี่ยง (หุ้น):", stock_weight, "%")
		if stock_weight > 60:
			return "คำแนะนำ: ความเสี่ยงสูงเกินเกณฑ์! ควรเพิ่มสัดส่วนทองคำเพื่อกระจายความเสี่ยง"
		else:
			return "คำแนะนำ: ความเสี่ยงอยู่ในระดับปกติ โครงสร้างพอร์ตสมดุลดีแล้ว"
thai_stocks = [1350.0, 1360.0, 1345.0, 1355.0]
global_gold = [32000.0, 32100.0, 31950.0, 32050.0]
client_portfolio = PortfolioEngine("Yuthachak-W", thai_stocks, global_gold)
portfolio_report = client_portfolio.analyze_risk(75)
print(portfolio_report)
