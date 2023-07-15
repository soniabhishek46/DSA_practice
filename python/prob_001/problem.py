class Solution:
    def subArraySum(self,arr, n, s): 
        
        left_ptr = 0
        right_ptr = 0
        
        summ = arr[left_ptr]
        if summ == s:
            return [left_ptr+1, right_ptr+1]
        
        while((right_ptr < n)and(left_ptr <= right_ptr)):
            if ((summ < s or left_ptr == right_ptr)and(right_ptr < n-1)):
                right_ptr += 1
                summ += arr[right_ptr]
                if summ == s:
                    return [left_ptr+1, right_ptr+1]

            elif ((summ > s)and(left_ptr < n-1)):
                summ -= arr[left_ptr]
                left_ptr += 1
                if summ == s:
                    return [left_ptr+1, right_ptr+1]
            elif summ == s:
                return [left_ptr+1, right_ptr+1]
            else:
                break
            print(f'{summ}|{s}')
            print(f'LP: {left_ptr}')
            print(f'RP: {right_ptr}\n')
        return [-1]

    def get_params(self, filename:str):
        #import pdb; pdb.set_trace()
        with open(filename, 'r') as fp:
            i=0
            for line in fp:
                if i == 0:
                    n, s  = line.strip().split(' ')
                    n = int(n); s = int(s)
                else:
                    arr = line.strip().split(' ')
                    arr = [int(x) for x in arr]
                i+=1
            return n, s, arr

  
if __name__ == '__main__':
    #arr = [135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103, 154, 93, 183, 22, 117, 119, 96, 48, 127, 172, 139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134]
    #arr = [142, 112, 54, 69, 148, 45, 63, 158, 38, 60, 124, 142, 130, 179, 117, 36, 191, 43, 89, 107, 41, 143, 65, 49, 47, 6, 91, 130, 171, 151, 7, 102, 194, 149, 30, 24, 85, 155, 157, 41, 167, 177, 132, 109, 145, 40, 27, 124, 138, 139, 119, 83, 130, 142, 34, 116, 40, 59, 105, 131, 178, 107, 74, 187, 22, 146, 125, 73, 71, 30, 178, 174, 98, 113]
    

    sol = Solution()
    #n=42 
    #n=74

    #s=468 
    #s=665
    n=5; s=12
    arr=[1, 2, 3, 7, 5]
    #n, s, arr = sol.get_params('input_002.txt')
    #print(f'{n}/{s}/{arr}')
    rv = sol.subArraySum(arr, n, s)
    print(rv)