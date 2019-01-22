a=[[2,2,2],[2,2,2],[2,2,2]]
player1=3
player2=5
blank=2
notWinning=10
def movePlayer2(i):
	if(i==2):
		if(a[1][1] == blank):
			go(4,player2)
		else:
			go(0,player2)
	elif(i==4):
		z=poss(player1)
		if(z != notWinning):
			go(z,player2)
		else:
			z=make5()
			go(z,player2)
	elif(i==6):
		z=poss(player2)
		if(z != notWinning):
			go(z,player2)
			return
		z=poss(player1)
		if(z != notWinning):
			go(z,player2)
			return
		z=make5()
		go(z,player2)
	else:
		z=poss(player2)
		if(z != notWinning):
			go(z,player2)
			return
		z=poss(player1)
		if(z != notWinning):
			go(z,player2)
			return
		for l1 in range(0,3):
			for l2 in range(0,3):
				if(a[l1][l2] == blank):
					a[l1][l2]=player2
					return
	
def movePlayer1(i):
	if(i==1):
		go(0,player1)
	elif(i==3):
		if(a[2][2] == blank):
			go(8,player1)
		else:
			go(2,player1)
	elif(i==5):
		z=poss(player1)
		if(z != notWinning):
			go(z,player1)
			return
		z=poss(player2)
		if(z != notWinning):
			go(z,player1)
			return
		if(a[2][0] == blank):
			go(6,player1)
		else:
			go(3,player1)
	
	else:
		z=poss(player1)
		if(z != notWinning):
			go(z,player1)
			return
		z=poss(player2)
		if(z != notWinning):
			go(z,player1)
			return
		for l1 in range(0,3):
			for l2 in range(0,3):
				if(a[l1][l2] == blank):
					a[l1][l2]=player1
					return
def go(index,playerNo):
	if(index == 0):
		if(a[0][0] == blank):
			a[0][0]=playerNo
	if(index == 1):
		if(a[0][1] == blank):
			a[0][1]=playerNo
	if(index == 2):
		if(a[0][2] == blank):
			a[0][2]=playerNo
	if(index == 3):
		if(a[1][0] == blank):
			a[1][0]=playerNo
	if(index == 4):
		if(a[1][1] == blank):
			a[1][1]=playerNo
	if(index == 5):
		if(a[1][2] == blank):
			a[1][2]=playerNo
	if(index == 6):
		if(a[2][0] == blank):
			a[2][0]=playerNo
	if(index == 7):
		if(a[2][1] == blank):
			a[2][1]=playerNo
	if(index == 8):
		if(a[2][2] == blank):
			a[2][2]=playerNo
		
def make5():
	if(a[1][1] == blank):
		return 4
	if(a[0][1] == blank):
		return 1
	if(a[1][0] == blank):
		return 3
	if(a[1][2] == blank):
		return 5
	if(a[2][1] == blank):
		return 7
		
		
def poss(playerNo):
	if(a[0][0] == blank):
		if((a[0][1]==playerNo and a[0][2]==playerNo) or (a[1][0]==playerNo and a[2][0] ==playerNo) or(a[1][1]==playerNo and a[2][2]==playerNo)):
			return 0
	if(a[0][1] == blank):
		if((a[0][0]==playerNo and a[0][2]==playerNo) or (a[1][1]==playerNo and a[2][1] ==playerNo)):
			return 1 
	if(a[0][2] == blank):
		if((a[0][0]==playerNo and a[0][1]==playerNo) or (a[1][2]==playerNo and a[2][2] ==playerNo)or(a[1][1]==playerNo and a[2][0]==playerNo)):
			return 2 
	if(a[1][0] == blank):
		if((a[1][1]==playerNo and a[1][2]==playerNo) or (a[0][0]==playerNo and a[2][0]==playerNo)):
			return 3 
	if(a[1][1] == blank):
		if((a[1][0]==playerNo and a[1][2]==playerNo) or (a[0][1]==playerNo and a[2][1]==playerNo) or (a[0][0]==playerNo and a[2][2] == playerNo)or(a[0][2]==playerNo and a[2][1]==playerNo)):
			return 4
	if(a[1][2] == blank):
		if((a[1][0]==playerNo and a[1][1]==playerNo) or (a[0][2]==playerNo and a[2][2]==playerNo)):
			return 5 
	if(a[2][0] == blank):
		if((a[2][1]==playerNo and a[2][2]==playerNo) or (a[0][0]==playerNo and a[1][0] ==playerNo) or (a[1][1]==playerNo and a[0][2]==playerNo)):
			return 6
	if(a[2][1] == blank):
		if((a[2][0]==playerNo and a[2][2]==playerNo) or (a[0][1]==playerNo and a[1][1] ==playerNo)):
			return 7
	if(a[2][2] == blank):
		if((a[2][0]==playerNo and a[2][1]==playerNo) or (a[0][2]==playerNo and a[1][2] ==playerNo) or (a[0][0]==playerNo and a[1][1]==playerNo)):
			return 8 
	
	return notWinning
	

ip=input("enter X for 1st player and y for 2nd player  \n")
print("Choices that can be entered are:")
i=0
for l1 in range(0,3):
	print(i,"|",i+1,"|",i+2)
	print("----------")
	i=i+3
print()
print()
for i in range(1,10):
	if(ip == 'Y' or ip == 'y'):
		if(i%2==0):
			index=int(input("enter your choice"))
			go(index,player2)
		else:
			movePlayer1(i)
	else:
		if(i%2 == 0):
			movePlayer2(i)
		else:
			index=int(input("enter your choice"))
			go(index,player1)
		
	b=[[0,0,0],[0,0,0],[0,0,0]]
	m=-1
	for l1 in range(0,3):
		for l2 in range(0,3):
			m=m+1;
			if(a[l1][l2]==blank):
				b[l1][l2]=m;
			elif(a[l1][l2]==player1):
				b[l1][l2]='X'
			else:
				b[l1][l2]='Y'
	for l1 in range(0,3):
		print(b[l1][0],"|",b[l1][1],"|",b[l1][2])
		print("----------")

	if((a[0][0]==a[0][1]==a[0][2]!=blank)or(a[0][0]==a[1][0]==a[2][0]!=blank)or(a[0][0]==a[1][1]==a[2][2]!=blank)or(a[1][0]==a[1][1]==a[1][2]!=blank)or(a[2][0]==a[2][1]==a[2][2]!=blank)or(a[2][0]==a[1][1]==a[0][2]!=blank)or(a[0][1]==a[1][1]==a[2][1]!=blank)or(a[0][2]==a[1][2]==a[2][2]!=blank)):
		print("Game Ended")
		exit(0)
	print()
	print()
	
	
print("DRAW")
