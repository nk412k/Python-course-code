from one import func

func()
def func():
	print("this is in two.py")



if __name__ == '__main__':
	print("two.py is directly run")
else:
	print("two.py is import")
