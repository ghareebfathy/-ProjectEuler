
# Problem 74
import time
t0 = time.time()
'هذا الجزء الخاص بي 👇 '
def factorial(n):
    res = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}
    r = str(n)
    result = 0
    for i in r:
        result+=res[int(i)% 10]
    return  result


"""
حل محدود الذاكرة
الحل الأخير الذي سأقدمه هنا أبطأ من الحل الثاني. ومع ذلك ، فإن ميزة أنه لا يستخدم الكثير من الذاكرة. لا يستخدم أي نوع من المصفوفات وبالتالي أنا أحب ذلك. من خلال معرفتنا ، نعلم أن معايير إيقاف التسلسل هي واحدة من الأرقام السبعة المذكورة أعلاه أو الرقم الذي يرسم نفسه. لذلك يمكننا جعل بعض الكود يبدو هكذا

"""
limit = 10 ** 6
result = 0
for i in range(1,limit):
    n = i
    last = 0
    count = 0
    while (n != last and
               n != 169 and n != 363601 and n != 1454 and
               n != 871 and n != 45361 and
               n != 872 and n != 45362) :
        last = n
        n = factorial(n)
        count += 1
    if count == 57 and (n == 169 or n == 363601 or n == 1454) :
        result+=1
print(result)
t1 = time.time()
print(t0- t1)
# -41.28450798988342