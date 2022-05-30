
t="txti"
is_a_palin=True
check_palindrome=True
count=0
a=[]

def print_once(message):
    global count
    if(count==1):
        print("The string is not a palindrome")
    count=count+1

def check_if_palin(i):
    if(t[i]==t[len(t)-i-1]):
        return True


for i in range(len(t)-1,-1,-1):
    print(t[i])
    if(check_palindrome):
        if(not check_if_palin(i)):
            is_a_palin=False
            print_once("The string is not a paliindrome")

if(is_a_palin):
    print("The string is pallindrome")



# def using_recursion(string):
#     for i in range(len(string),-1,-1):
#         a.append(string[i])
#         using_recursion(string[::i])
#
#
#
# using_recursion("txt")