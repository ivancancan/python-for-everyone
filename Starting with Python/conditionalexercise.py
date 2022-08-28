hrs = input("Enter Hours: ")
h = float(hrs)

rate = input("Enter Rate: ")
r = float(rate)

erate = r * 1.5


epay = h - 40
npay = h - epay


if epay > 0:
    repay = epay * erate
    rnpay = npay * r
    print(repay + rnpay)
else:
   print("no extra time")
