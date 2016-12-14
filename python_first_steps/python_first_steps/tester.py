from first_mod import *

#list = ([1,2,3,4,7,2,6,8,2,1])
#print(rRev(list))

#print(fac(6))

print(fib(1,1,8))

print(fib1(1,1,8))

print('Fib sequence tests -----')
print(fib(1,2,6))
print(fib(5,9,5))
print(dFib(1,2,100)) 
print('Cart sequence tests--------')
print(cart_prod([1,2,3],[4,5,6]))
print(cart_prod([1,2],[3,4],[5,6],[7,8]))

print('all perms tests-------------')
print(all_perms([1,2,3]))
print(all_perms([1,2,3,4]))

print('towers of hanoi test------------------')
print(hannoi("A", "B", "C", 2))

print('anagrams test --------------------')
words = read_words('words-1000.txt')
#print(find_anagrams(
