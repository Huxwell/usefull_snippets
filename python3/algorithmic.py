# steps=2 a=[1,2,3,4,5], n=len(a); output:[3,4,5,1,2]
def leftrotation(a,steps,n):
	steps = steps % n
	return(a[steps:]+a[:steps])
