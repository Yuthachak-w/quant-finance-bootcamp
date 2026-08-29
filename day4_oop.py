class InsurancePolicy:
	def __init__(self, name, account_number, balance):
		self.owner = name
		self.acc_num = account_number
		self.money = balance
	def deposit(self, amount):
		self.money = self.money+amount
		print("ฝากเงินสำเร็จ")
	def display_info(self):
		print("--- กรมธรรม์ประกันภัย ---")
		print("ชื่อบัญชี: " + self.owner)
		print("เลขบัญชี: " + self.acc_num)
		print("ยอดเงินคงเหลือ (บาท):")
		print(self.money)
my_account = InsurancePolicy("Yuthachak", "123-456-789", 7500)
my_account.display_info()
my_account.deposit(2500)
my_account.display_info()