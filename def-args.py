def keyword_argument(**kwargs):  #1
    return kwargs['name']

def keyword_arguments(**options):  #2
    return options['names']

def keyword_argumentss(**options): #3
    return options['classes_']

def keyword_argument_(*args): #4
    for i in args:
        print(i)

    

if __name__=='__main__':
    print(keyword_arguments(name='__name__')) #print #1
    print(keyword_arguments(names='__name__')) #print #2
    print(keyword_argumentss(classes_='__name__')) #print #3

    keyword_argument_('name1','name2','name3') #4 print 'name1','name2'.....



