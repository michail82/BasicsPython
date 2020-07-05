# put your python code here
h, m, s    = map(int, input().split(':'))
h1, m1, s1 = map(int, input().split(':'))
# Часы в секунды 
sec1_h1 = h*3600 + m*60 + s #41327
sec2_h2 = h1*3600 + m1*60 + s1 #79922      #38595
h = ((sec2_h2 - sec1_h1) // 3600)
m = (((sec2_h2 - sec1_h1)  % 3600 )// 60)
s = ((sec2_h2 - sec1_h1) % 60)
print (h,m,s)



