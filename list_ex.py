def fun_sentence():
    words="hello world"
    k=words.split(" ")
    s=k[::-1]
    m=" ".join(s)
    print(m)

#fun_sentence()

def list_To_dict(l1,l2):

    di={}
    size=len(l1)
    for i in range(size):
        di[l1[i]]=l2[i]
    print(di)
a= [1, 2, 3, 7, 8, 9, 11, 10]
b = [4, 5, 6, 11, 2, 3, 5, 6]
list_To_dict(l2=b,l1=a)


















