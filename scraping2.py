from bs4 import BeautifulSoup
with open('home.html','r') as html_file:
    content =html_file.read()
    #print(content)
    #creating an instance 
    soup=BeautifulSoup(content,'lxml') #parsing method to be used here is the lxml method
    #print(soup.prettify())
    #tags=soup.find_all('h5')
    #print(tags)
    #for tag in tags:
       # print(tag.text)
    course_cards=soup.find_all('div',class_="card")
    for course in course_cards:
        #print(course.h5)
        course_name =course.h5.text 
        course_price =course.a.text.split( )[-1] 
        #print(course_name)
        #print(course_price)
        print(f'{course_name} costs {course_price}')