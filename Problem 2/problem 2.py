'''
Subnetting :

With Class C subnet mask
Input from user- A) Enter the any / (slash) notation (/24 to /30) of the IPv4 subnet mask
Output to be displayed on the terminal/console:
Show the output on the terminal/console for the following:
1) Subnet mask for entered / (slash) notation of the IPv4 subnet mask
2) The maximum number of subnets
3) Valid host address per subnet

Input from user-
B) Enter the valid IP address. (Input from user-User has to type on terminal/console)
Output to be displayed on the terminal/console:
Show the output on the terminal/console for the following
1) The Network Id and Broadcast address for each subnet.
2) Show the valid host address range with starting and ending addresses.

'''

def getClassSubNet(classId):
	if classId == 'A':
		return [255, 0, 0, 0]
	elif classId == 'B':
		return [255, 255, 0, 0]
	elif classId == 'C':
		return [255, 255, 255, 0]

def getClassSubNetForHost(classId):
	if classId == 'A':
		return [0, 255, 255, 255]
	elif classId == 'B':
		return [0, 0, 255, 255]
	elif classId == 'C':
		return [0, 0, 0, 255]

def doAnding(list1, list2):
	list3 = []
	for i in range(len(list1)):
		list3.append(list1[i] & list2[i])
	return list3

def getClass(data):
	if data[0] >= 0 and data[0] <= 127: #A
		return 'A'
	elif data[0] >=128 and data[0] <= 191: #B
		return 'B'
	elif data[0] >= 192 and data[0] <= 223: #C
		return 'C'
	elif data[0] >= 224 and data[0] <= 239: #D
		return 'D'
	elif data[0] >= 240 and data[0] <= 255: #E
		return 'E'
	else:
		return "DN"

def getNetworkID(data):
	className = getClass(data)
	if className in ['D', 'E']:
		return "Dont have Nework Dividation"
	elif className == 'DN':
		return "Dont Know"
	return doAnding(data, getClassSubNet(className))

def getHostID(data):
	className = getClass(data)
	if className in ['D', 'E']:
		return "Dont have Nework Dividation"
	elif className == 'DN':
		return "Dont Know"
	return doAnding(data, getClassSubNetForHost(className))

def getStringOutOf(data):
	st = ""
	for ele in data:
		st += str(ele)
		st += '.'
	return st[:-1]

def getBroadCastAddress(chunks):
	chunks = getNetworkID(chunks)
	for i in range(len(chunks)):
		if chunks[i] == 0:
			chunks[i] = 255
	return chunks

def getMaskFromSlashNotation(data):
	chunks = []
	while data > 8:
		chunks.append(int('1' * 8, 2))
		data -= 8
	if data != 0:
		a = '1' * data
		if len(a) != 8:
			a += "0" * (8 - len(a))
		chunks.append(int(a, 2))

	while len(chunks) != 4:
		chunks.append(0)
	return chunks

#For Class C
def getMaxSubnet(data):
	return pow(2, 24 - data)

#For Class C
def getMaxHost(data):
	return pow(2, 32 - data) - 2

part = input("Select The Part : ")
if part == 'A':
	print("Part - A")
	data = str(input("Enter the slash Notation Value : "))
	data = int(data.split('/')[1])
	mask = getMaskFromSlashNotation(data)
	print("Sub Net Mask : ", getStringOutOf(mask))
	print("Max SubNets : ", getMaxSubnet(data))
	print("Max Hosts : ", getMaxHost(data))
elif part == 'B':
	print("Part - B")
	data = str(input("Enter the Ip Address : "))
	chunks = [int(d) for d in data.split('.')]
	if len(chunks) != 4:
		print("Invlaid IP ..!!")
	else:
		print("Network Id Is : ", getStringOutOf(getNetworkID(chunks)))
		print("BroadCast Address Is : ", getStringOutOf(getBroadCastAddress(chunks)))
		print("Host Id Is : ", getStringOutOf(getHostID(chunks)))
		print("Host Range Is Starting From :  ", getStringOutOf(chunks), "  Upto : " , getStringOutOf(getBroadCastAddress(chunks)), " Exclude First And Last Address.")
else:
	print("Invalid Choice ..!!")

