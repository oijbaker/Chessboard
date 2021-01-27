def helper_fib(number, counter, lists):
	if counter <= 0:
		return lists
	temps = lists[len(lists) - 1]
	lists.append(temps + number)
	return helper_fib(temps, counter - 1, lists)
