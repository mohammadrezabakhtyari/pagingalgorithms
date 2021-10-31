"""# LRU"""

def LRU(cap, req):

	# request list
	requests = req

	# Cash capacity
	capacity = cap

	# List of current pages in cash
	cash = []

	pageFaults = 0

	for i in requests:

		# If i is not present in cash
		if i not in cash:

			# Check if the list can hold equal pages
			if(len(cash) == capacity):
				cash.remove(cash[0])
				cash.append(i)
			else:
				cash.append(i)

			# Increment Page faults
			pageFaults +=1

		# If page is already there in Cash
		else:
			
			# Remove previous index of current page
			cash.remove(i)

			# Now append it, at last index
			cash.append(i)
	
	return pageFaults

"""# FIFO"""

def FIFO(cap, req):
  # request list
	requests = req

	# Cash capacity
	capacity = cap

	# List of current pages in cash
	cash = []

	pageFaults = 0

	for i in requests:
		# If i is not present in cash
		if i not in cash:
			# Check if the list can hold equal pages
			if(len(cash) == capacity):
				cash.remove(cash[0])
				cash.append(i)
			else:
				cash.append(i)

			# Increment Page faults
			pageFaults +=1
		# If page is already there in Cash

	return pageFaults

"""# FWF"""

def FWF(cap, req):

  # request list
  requests = req

  # Cash capacity
  capacity = cap

  # List of current pages in cash
  cash = []

  pageFaults = 0

  for i in requests:

    # If i is not present in cash
    if i not in cash:
      # Check if the list can hold equal pages
      if(len(cash) == capacity):
        cash = []
      else:
        cash.append(i)

      # Increment Page faults
      pageFaults +=1
    # If page is already there in Cash
    else:
      pass
    
  return pageFaults

"""# LFD"""

def LFD(cap, req):
  # request list
  requests = req
  print(requests)
  # Cash capacity
  capacity = cap


  # List of current pages in cash
  cash = []

  pageFaults = 0

  for index, i in enumerate(requests):
    # If i is not present in cash
    if i not in cash:
      # Check if the list can hold equal pages
      if(len(cash) == capacity):
        print("Cash is full for request " + str(index) + " with a value of " + str(i))
        temp = requests[index+1:]
        print("Future request: ", temp)
        x = []
        for m in cash:
          if np.where(temp==m)[0].size == 0:
            x.append(1000)
          else:
            x.append(np.where(temp==m)[0][0])
        print("Indices of cash content next request:", x)
        lfd_index = np.argmax(x)
        print("Page whose next request is farthest in the future:", cash[lfd_index])
        cash.remove(cash[lfd_index])
        cash.append(i)
      else:
        cash.append(i)

      # Increment Page faults
      pageFaults +=1
    # If page is already there in Cash
    else:
      pass
    print("Cash content after request " + str(index) + " with a value of "+ str(i))
    print(cash)
  return pageFaults


"""# Results"""

import numpy as np
requests = np.random.randint(low=1, high=6, size=20)
capacity = 4
LFD(capacity, requests)
