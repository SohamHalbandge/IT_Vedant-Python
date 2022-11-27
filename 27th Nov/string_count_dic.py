test_str = input("Enter your string: ")
freq = {}

for i in test_str:
	if i in freq:
		freq[i] += 1
	else:
		freq[i] = 1

# printing result
print(freq)