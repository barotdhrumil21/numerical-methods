def netprob(d1,d2):
	l=[]
	i = 0
	for k in d1:
		l.append((d1[k]/sum(d1.values())))
	for k in d2:
		l[i] *= d2[k]/100
		i+=1

	return sum(l)

def bayes(dict_a,dict_b,event_a):
	return ((dict_a[event_a]/sum(dict_a.values())) * (dict_b[event_a]/100)) / netprob(dict_a,dict_b)

sup={}
sub={}
print("example :: In a bolt factory, machines A, B, C manufacture 25%, 35% and 40% respectively of the total bolts. Of their output 5%, 4% and 2% respectively are defective bolts. A bolt is drawn at random and is found to be defective. Find the probability that it is manufactured by machine B. ans = ")
print("\n")
print("enter the main class with key and value seperated with space i.e. A ,B ,C production values in above example. enter ""e"" when done entering ")
while True:
	inp = input().split(" ")
	if inp[0] == "e":
		break
	else:
		sup[inp[0]] = int(inp[1])

print("\n")
print("enter the sub class with key and value seperated with space i.e. A ,B ,C defected values in above example. enter ""e"" when done entering ")
while True:
	inp = input().split(" ")
	if inp[0] == "e":
		break
	else:
		sub[inp[0]] = int(inp[1])

print("enter ")
a=input()
print(bayes(sup,sub,a))