st = '...ant...ant..nat.ant.t..ant...ant..ant..ant.anant..t'
def count_dead_ants(st):
    print st
    count = 0
    st.replace('.', ' ')
    for i in st.split(' ') :
        if (i != 'ant' and i != '' ) :
            count += 1
        elif i + st
    print count

count_dead_ants("ant ant ant ant")
count_dead_ants("ant anantt aantnt")
count_dead_ants("ant ant .... a nt")

