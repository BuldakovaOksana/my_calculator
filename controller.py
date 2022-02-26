import view 
import modul.modul_div as div
import modul.modul_mult as mult
import modul.modul_sub as sub
import modul.modul_sum as sum
import modul_choice as mod
import log_cala as log

def button_click(): 
    value_a=view.get_value()
    ch=view.get_choice()
    value_b=view.get_value()
    div.init(value_a,value_b)
    mult.init(value_a,value_b)
    sub.init(value_a,value_b)
    sum.init(value_a,value_b)
    result=mod.choice(ch)
    view.view_data('result',result)
    log.log_cal(value_a,ch,value_b,result)








