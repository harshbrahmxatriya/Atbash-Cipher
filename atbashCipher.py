class Solution:
	def atbash(self, text):
		N = ord('z') + ord('a')
		ans = ''
		return ans.join([chr(N - ord(s)) for s in text])
		return ans

ob = Solution()

print("Plain text: harshbrahmxatriya")
print("Atbash Cipher text:" +ob.atbash("harshbrahmxatriya"))


#print("Plain text"+text)
#print("Atbash Cipher text"+ans)
