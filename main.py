if __name__ == '__main__':
	MEMBER_NO = 0
	MEMBER_SEX = 1
	MEMBER_BIRTH = 2
	MEMBER_CONNECTION_COUNT = 3
	ORDER_NO = 4
	ORDER_STATUS = 5
	PRODUCT_NO = 6
	ORDER_PRODUCT_QUANTITY = 7
	ORDER_PRODUCT_PRICE = 8
	ORDER_DATE = 9

	f = open('order.csv', 'r', encoding='euc-kr')
	reader = csv.reader((line.replace('\0','') for line in f))
	header = next(reader)

# 	with open('features.data', 'rb') as file:
# 	   pickle_features = pickle.load(file)
# 	   pickle_cycles = pickle.load(file)
# 	   print(pickle_features)
# 	   print(pickle_cycles)

	order_list = OrderList()
	members_no = set()
	products_no = set()
	for row in tqdm(reader):	
	    order = Order(
	        row[MEMBER_NO],
	        row[MEMBER_CONNECTION_COUNT],
	        row[PRODUCT_NO],
	        row[ORDER_PRODUCT_PRICE],
	        row[ORDER_PRODUCT_QUANTITY],
	        row[ORDER_DATE]
	    )
	    order_list.add(order)
	f.close()

	with open('features.data', 'wb') as file:
	    pickle.dump(np.array([feature.as_list() for feature in features]), file)
	    pickle.dump(np.array(cycles), file)