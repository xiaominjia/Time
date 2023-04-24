import time

start_time = time.time()

Interval = input('please input Interval for measurement: ')
a = 1

#f = open('/Users/XieHong/Google Drive/Python/%stest.txt' % Interval, 'w+')
#f = open(str(a)+'%stest.txt' % Interval, 'w+')
f = open(str(a)+str(Interval)+".txt", 'w+')
f.close()

f = open(str(a)+str(Interval)+".txt", 'a')
t = 0
while t <= 10:
    time.sleep(0.1)

    print("%.3f" % (time.time() - start_time))

    f.write("%.3f"%(time.time() - start_time))
    f.write('\n')
    t += 1
f.close()

