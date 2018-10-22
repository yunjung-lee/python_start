#####문자######

#문자 표현
print("%c" % "a")
print("%c" % 'b')
print("%s" % "abc")

# \t : tap 기능
# \n : 줄바꿈 기능
# \' :  ' 넣기 기능
#'""' : "" 넣기, ''넣기는 반대로 써주면 됨
print("\t연습 \n123")
print("It\'s")
msg="""
Life is \ntoo short
You need Python
"""
#\t : tap, \n : 줄바꾸기
print(msg)

#format function 인자는  , 로 구분 : 1,0의 숫자는 위치를 바꿔도 된다.
print("I eat {0} apples. so I was sick for {1} days". format(3,5))


#문자 열 입력 : """ 문자열 """ or  '''문자열 '''
a="""파이썬
만세"""
print(a)

a="""파이썬 만세"""
print(a)

#문자열 자르기
a="Life"
print(a[-2])
print(a[1:3])
#[시작: 끝+1]

# 공백문자를 기준으로 자르기 => list 형태로 나타남
print(msg.split()) # 공백문자를 기준으로 자르기 => list 형태로 나타남
msg2 = "life : is :too : short"
print(msg2.split(":"))

#a[-1]을 하나의 변수로 보고 다시 위치[0]를 넣으면 된다
a = [1,2,3,['a','b','c']]
print(a[-1][0])

#del : 값들을 버리는 기능
a=[4,5,6]
# a[1:3]=[]   : del과 같은 기능
del a[1:3]
print(a)


#join : join 앞의 기호를 삽입하여 합친다.
# a를(=",") join하는 변수에 집어 넣어라
a=","
print(a.join('abcd'))

#a[-1]=['a','b','c']을 하나의 변수로 보고 다시 위치[0]를 넣으면 된다. ==>2배열
a = [1,2,3,['a','b','c']]
print(a[-1][0])

#3배열 위치 지정
a = [1,2,3,['a','b',['c','d']]]
print(a[3][2][0])

#위치에 다른 값 대체 : a[2]=7==>a[2]인 6대신 7을 대신 위치시킨다.
a=[4,5,6]
a[2]=7
print(a)
print(a[1:2])


#len(a) : a의 개수를 출력한다.
a[1:2]=['a','b','c']
#  a = [4,a,b,c,7] ==>len(a) = 5,
# a = [4,[a,b,c],7] ==> len(a) = 3
print(a)
print(len(a))


