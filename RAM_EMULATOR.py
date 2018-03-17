import sys

from icecream import ic

class Ram_Emulator:

	def __init__(self,name,argv):
		self.com=[]
		self.point=0
		self.code=self.readFile(name)
		self.add_Arg([int(x) for x in argv])

	def add_com_0(self,n):
		while len(self.com)<=n:
			self.com.append(0)

	def add_Arg(self,lista):
		self.com.append(0)
		self.com+=lista


	def fun_Z(self,arg):

		n=arg[0]
		self.add_com_0(n)

		self.com[n]=0
		self.point+=1

	def fun_S(self,arg):
		n=arg[0]
		self.add_com_0(n)
		self.com[n]+=1
		self.point+=1

	def fun_T(self,arg):

		n=arg[0]
		m=arg[1]

		self.add_com_0(n)
		self.add_com_0(m)

		self.com[n]=self.com[m]
		self.point+=1

	def fun_I(self,arg):

		n=arg[0]
		m=arg[1]
		q=arg[2]


		self.add_com_0(n)
		self.add_com_0(m)
		self.add_com_0(q)

		if self.com[n]==self.com[m]:
			self.point=q
		else:
			self.point+=1

	def readFile(self,name):
		with open(name) as file:
			return file.read().replace("\n","").replace(" ","").split(";")

	def readCode(self):

		fun_dir={"Z":self.fun_Z,"S":self.fun_S,"T":self.fun_T,"I":self.fun_I}
		while self.point<len(self.code):
			instruction=self.code[self.point]
			if len(instruction)>=4 and instruction[0] in fun_dir:
				argv=instruction[2:-1].split(",")
				argv=[int(x) for x in argv]
				fun_dir[instruction[0]](argv)
			elif instruction=="":
				break


		print(self.com[0])





def main():
	Ram_Emulator(sys.argv[1],sys.argv[2:]).readCode()

if __name__ == '__main__':
	main()