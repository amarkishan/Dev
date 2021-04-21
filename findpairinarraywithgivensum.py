mathod1:
  twopointer technique 
  timecomlexity is O(nlogn) if it is unosrted
method 2:
  using hashing
  def findPair(A, sum):
 
    # create an empty dictionary
    dict = {}
 
    # do for each element
    for i, e in enumerate(A):
 
        # check if pair `(e, sum - e)` exists
 
        # if the difference is seen before, print the pair
        if sum - e in dict:
            print("Pair found", (A[dict.get(sum - e)], A[i]))
            return
 
        # store index of the current element in the dictionary
        dict[e] = i
 
    # No pair with the given sum exists in the list
    print("Pair not found")
 
 
if __name__ == '__main__':
 
    A = [8, 7, 2, 5, 3, 1]
    sum = 10
 
    findPair(A, sum)
 #timecomplexity:O(n)
method 3:
  Sliding window technique
  # Returns true if the
# there is a subarray
# of arr[] with sum
# equal to 'sum'
# otherwise returns
# false. Also, prints
# the result.
def subArraySum(arr, n, sum_):
     
    # Initialize curr_sum as
    # value of first element
    # and starting point as 0
    curr_sum = arr[0]
    start = 0
 
    # Add elements one by
    # one to curr_sum and
    # if the curr_sum exceeds
    # the sum, then remove
    # starting element
    i = 1
    while i <= n:
         
        # If curr_sum exceeds
        # the sum, then remove
        # the starting elements
        while curr_sum > sum_ and start < i-1:
         
            curr_sum = curr_sum - arr[start]
            start += 1
             
        # If curr_sum becomes
        # equal to sum, then
        # return true
        if curr_sum == sum_:
            print ("Sum found between indexes")
            print ("% d and % d"%(start, i-1))
            return 1
 
        # Add this element
        # to curr_sum
        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1
 
    # If we reach here,
    # then no subarray
    print ("No subarray found")
    return 0
 
# Driver program
arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum_ = 23
 
subArraySum(arr, n, sum_)
 

