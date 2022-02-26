import datetime 



def log_cal(val_a,ch,val_b,res):
    with open('log.csv','a') as data:
        data.write(f'{datetime.datetime.now()},value_a = {val_a},choice {ch},value_b = {val_b},result =  {res}\n')

