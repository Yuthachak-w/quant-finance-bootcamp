price_list = [120.0, 122.5, 121.0, 125.0, 124.5, 130.0]
day1_price = price_list[0]
day6_price = price_list[5]
print("ราคาวันแรก:")
print(day1_price)
print("ราคาวันสุดท้าย:")
print(day6_price)
total_sum = 0
for price in price_list:
	total_sum = total_sum + price
average_price = total_sum / len(price_list)
print("ราคารวม 6 วัน:")
print(total_sum)
print("ราคาเฉลี่ยย้อนหลัง 6 วัน:")
print(average_price)