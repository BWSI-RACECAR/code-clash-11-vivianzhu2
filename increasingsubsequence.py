class Solution:
    def find_longest_increasing_subsequence(self, arr):
            #type arr: list of int
            #return type: int
            #arr=arr.sort()

            if(len(arr)!=0):
                count=1
                newcount=0
                for i in range(1,len(arr)):
                    if(arr[i]>arr[i-1]):
                        count+=1
                    else:
                        count=1
                        newcount+=1
                print(arr)
                print(count)
            else:
                count=0
            
            return count+newcount
            #TODO: Write code below to return an int with the solution to the prompt.

def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = int(array[x])

    tc1 = Solution()
    ans = tc1.find_longest_increasing_subsequence(array)
    print(ans)

if __name__ == "__main__":
    main()