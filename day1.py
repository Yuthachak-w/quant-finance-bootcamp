stock_name = "KBANK"
stock_price = 125.50
shares_owned = 200

total_value = stock_price * shares_owned

print(total_value)
customer_age = 35
base_premium = 10000
if customer_age > 60:
    final_premium = base_premium * 1.5
    print("ลูกค้ากลุ่มเสี่ยงสูง เบี้ยประกันรวม:")
else:
    final_premium = base_premium
    print("ลูกค้ากลุ่มความเสี่ยงปกติ เบี้ยประกันรวม:")
print(final_premium)