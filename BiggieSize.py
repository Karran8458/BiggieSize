def biggie_size(arr):
	for x in range(0,len(arr),1):
		if arr[x]>0:
			arr[x]= "big"
			
	return arr
