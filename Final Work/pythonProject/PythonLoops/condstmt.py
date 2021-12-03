#Example file for working with conditional statement
def main():
	x,y =2,8
	if(x < y):
		st= "x is less than y"
	print(st)
if __name__ == "__main__":
	main()
def main():
	x,y =8,4
	if(x < y):
		st="x is less than y"
	else:
		st="x is greater than y"
	print(st)
if __name__ == "__main__":
	main()
#Example file for working with conditional statement with elseif
def main():
	x,y =8,8
	if(x < y):
		st= "x is less than y"
	elif (x == y):
		st= "x is same as y"
	else:
		st="x is greater than y"
	print(st)
if __name__ == "__main__":
	main()
# minium code execution
def main():
	x, y = 10, 8
	if (x < y):
		st = "x is less than y"
	else:
		st="x is greater than or equal to y"
	print(st)
if __name__ == "__main__":
	main()