import string
import random  #if list me sa kuch random element find kerna ho toh we use the random import
if __name__=="__main__":
    s1=string.ascii_lowercase
    print(s1)
    s2=string.ascii_uppercase
    print(s2)
    s3=string.digits
    print(s3)
    s4=string.punctuation
    print(s4)              #extend a=[1,2,3,4,5,6]
                            #b=[5,7]
                            #a.extend(b) iska mtlb hoga ki a jo list k andaar he b ki list
                            # nhi jaye gi it will be the simple no like
                            # [1,2,3,4,5,6,5,7]
    plen=int(input("Enter password length \n"))
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4)) # here s will be all the character that we want to make means all the list of character from s1 to s4
    random.shuffle(s)
    print("".join(s[0:plen]))
