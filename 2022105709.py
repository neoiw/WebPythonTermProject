def function1(string1,string2):
    return string1+string2 

def function2(string1,string2):
    return len(string1)+len(string2)

def function3(string1,int1):
    return(string1 * int1)

def function4(string1,chr1):
    if chr1 in string1:
        return("True")
    else:
        return("False")

def function5(int1,int2):
    output = 0
    for i in range(int2-int1+1):
        output+=i+int1
    return(output)

def function6(list1,string1):
    if string1 in list1:
        return("True")
    else:
        return("False")

def function7(list1):
    return(sum(list1))

def function8(list1):
    sum=0
    for i in list1:
        if i%2==0:
            sum+=i
    return(sum)

def function9(list1,string1):
    if string1 in list1:
        for i in list1:
            if i == string1: 
                list1.remove(i) 
        return(list1)
    else:
        return("False")


#테스트용

#print(function1("Hello,"," world!"))
#print(function2("Hello,"," world!"))
#print(function3("Hello, world!",3))
#print(function4("Hello, world!","H"))
#print(function5(1,10))
#print(function6(["Apple","Pear","Orange"],"Grape"))
#print(function7([1,2,3,5]))
#print(function8([1,2,3,4,5,6,7,8,9,10]))
#print(function9(["Apple","Orange","Pear","Apple"],"Grape"))


