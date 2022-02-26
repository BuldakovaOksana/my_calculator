import modul.modul_div as div
import modul.modul_mult as mult
import modul.modul_sub as sub
import modul.modul_sum as sum

def choice(ch):
    if ch=='+':
        return sum.do_it()
    if ch=='-':
        return sub.do_it()
    if ch=='*':
        return mult.do_it()        
    if ch=='/':
        return div.do_it()

