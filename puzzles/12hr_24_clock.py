def convert_12hr_to_24hr(timestamp) :
    if timestamp[-2] == "AM" :
        if timestamp[:2] != '12' :
            print "orig time is not 12 AM something"
            print "Converted time --- {0}".format(new_time[0:len(new_time)-2])
        else :
            print "orig time is 12 AM something"
            new_time = timestamp.replace('12', '00', 1)
            print "Converted time --- {0}".format(new_time[0:len(new_time)-2])
    elif int(timestamp[:2]) < 12 :
        print "############## ", int(timestamp[:2])+12
        new_time = timestamp.replace(timestamp[:2], str(int(timestamp[:2])+12 ) )
        print "Converted time --- {0}".format(new_time[0:len(new_time)-2])

print "Enter time to be converted in AM/PM format : "
input_time = raw_input()
convert_12hr_to_24hr(input_time)
