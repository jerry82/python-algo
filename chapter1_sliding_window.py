#1. Maximum Sum Subarray of Size K (easy)
#sliding windows section
def max_sub_array_of_size_k(k, arr):
    if k > len(arr):
        return -1
    tmp = sum(arr[0:k])
    result = tmp

    for i in range(k, len(arr)):
        next = tmp - arr[i - k] + arr[i]
        result = max(result, next)
        tmp = next

    return result

#2. Smallest Subarray with a given sum (easy)
#O(N + N) ~ O(N)
def smallest_subarray_with_given_sum(s, arr):
    left = 0
    sum = 0
    result = len(arr) + 1

    for i in range(len(arr)):
        sum += arr[i]
        while sum >= s and left <= i:
            result = min(result, i - left + 1)
            sum -= arr[left]
            left += 1

    return (result if result < len(arr) + 1 else 0)

#3. Longest Substring with no more than K Distinct Characters (medium)
def longest_substring_with_k_distinct(str, k):
    
    left = 0
    i = 0
    freq = {}
    length = 0
    
    for i in range(len(str)):      
        char = str[i]
        
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
            
        while left <= i and len(freq) > k:
            removeChar = str[left]
            
            freq[removeChar] -= 1
            if freq[removeChar] == 0:
                del freq[removeChar]
            
            left += 1
        
        length = max(length, i - left + 1)
                              
    return length

#4. Fruits into Baskets (medium)
def fruits_into_baskets(fruits):
    
    left = 0
    i = 0
    basket = {}
    length = 0
    
    for i in range(len(fruits)):
        char = fruits[i]
        
        if char not in basket:
            basket[char] = 1
        else:
            basket[char] += 1
                       
        while len(basket) > 2 and left <= i:
            removeChar = fruits[left]
            
            basket[removeChar] -= 1
            if basket[removeChar] == 0:
                del basket[removeChar]
                
            left += 1
            
        length = max(length, sum(basket.values()))
    
    return length

#5. Given a string, find the length of the longest substring which has no repeating characters.
def non_repeat_substring(str):
    left = 0
    i = 0
    freq = {}
    length = 0
    
    for i in range(len(str)):
        char = str[i]
        
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
            
        while max(freq.values()) > 1 and left <= i:
            removeChar = str[left]
            freq[removeChar] -= 1
            if freq[removeChar] == 0:
                del freq[removeChar]
            left += 1
            
        length = max(length, i - left + 1)
      
    return length

def find_permutation(str, pattern):
    
    pl = len(pattern)
    for i in range(0, len(str) - pl + 1):
        tmp = str[i: i + pl]
        if compare(tmp, pattern):
            return True
    
    return False

def compare(str1, str2):
    set1 = {}
    set2 = {}
    
    print(str1, ' ', str2)
    
    if len(str1) != len(str2): return False
    
    for ch in str1:
        if ch in set1: set1[ch] += 1
        else: set1[ch] = 1
        
    for ch in str2: 
        if ch in set2: set2[ch] += 1
        else: set2[ch] = 1
        
    for key in set1:
        if key not in set2:
            return False
        elif set2[key] != set1[key]:
            return False
        
    return True


def find_string_anagrams(str, pattern):
    result = []
    pl = len(pattern)
    for i in range(0, len(str) - pl + 1):
        tmp = str[i: i + pl]
        if compare(tmp, pattern):
            result.append(i)
    
    return result



def find_substring(str, pattern):
    res = ""
    
    left = 0
    dict = {}
    i = 0
    l = len(str) + 1
    
    for i in range(len(str)):
        ch = str[i]
        
        if ch in dict: dict[ch] += 1
        else: dict[ch] = 1
               
        while contains(dict, pattern) == True and left <= i:
            
            tmp = str[left: i + 1]
            if (l > len(tmp)):
                l = len(tmp)
                res = tmp
                
            
            removeChar = str[left]
            dict[removeChar] -= 1
            if dict[removeChar] == 0:
                del dict[removeChar]
            left += 1
     
    return res

def contains(dict, pattern):
    for ch in pattern:
        if ch not in dict:
            return False
       
    return True


def find_word_concatenation(str, words):
    res = []
    
    l = len(words) * len(words[0])
    
    for i in range(len(str) - l + 1):
        tmp = str[i: i + l]
        if (has(tmp, words)):
            res.append(i)
    
    return res

def has(str, words):
    l = len(words[0])
    tmpWords = words.copy()
    for i in range(len(str) - l + 1):
        tmp = str[i: i + l]
        if tmp in tmpWords:
            tmpWords.remove(tmp)

    return len(tmpWords) == 0

'''
Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
'''
def length_of_longest_substring(str, k):
    
    left = 0
    l = 0
    dict = {}
    
    for i in range(len(str)):
        ch = str[i] 
        
        if ch in dict: dict[ch] += 1
        else: dict[ch] = 1
        
        while valid(dict, k) == False and left <= i:
            removeChar = str[left]
            left += 1
            
            dict[removeChar] -= 1
            if dict[removeChar] == 0:
                del dict[removeChar]
        
        l = max(l, i - left + 1)
    
    return l

'''
sorted dictionary
'''
def valid(dict, k):
    if len(dict) > 0:
        vals = [v for (k,v) in dict.items()]
        vals.pop(0)
        if sum(vals) > k:
            return False
        
    return True

'''
Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
'''
def length_of_longest_substring(arr, k):
    
    left = 0
    l = 0
    zeros = 0
    
    for i in range(len(arr)):
        num = arr[i]
        
        if num == 0: zeros += 1
        
        while zeros > k and left <= i:
            removeNum = arr[left]
            left += 1
            
            if removeNum == 0: zeros -= 1
            
        l = max(l, i - left + 1)
    
    return l

arr=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
k=2

print(length_of_longest_substring(arr,k))
