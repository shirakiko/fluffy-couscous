num=input("Please enter a Arabic numerals or Roman numerals.")
if num.isdigit():
     num=int(num)
     if num<1 or num>3999:
          print("The Number must be in 1-3999.")
     else:
        ones = ['','I','II','III','IV','V','VI','VII','VIII','IX'];
        tens = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'];
        hundreds = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'];
        thousands = ['','M','MM','MMM'];
        print(thousands[num // 1000] + hundreds[(num % 1000) // 100] + tens[(num % 100) // 10] + ones[num % 10])

     input("按任意键结束")

else:
     def RomanToInt(s):
        RomanInt = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000};
        num = RomanInt[s[0]];
        for i in range(1,len(s)):
            if RomanInt[s[i]] > RomanInt[s[i - 1]]:
                num += RomanInt[s[i]] - 2 * RomanInt[s[i - 1]];
            else:
                num += RomanInt[s[i]];
        print(num)
     RomanToInt(num)
     input("按任意键结束")     
