'''This is the main program'''
import sys
import mysql.connector as mc
from datetime import *
mydb=mc.connect(host='localhost',user='root',passwd='KaKali@1971',database='lib')
mycur=mydb.cursor()
pas='123'
sql='create table book_rec (book_id integer primary key,title varchar(75) not null unique,author varchar(50) not null,description varchar(1000),stock integer not null,no_bor integer not null)'
#mycur.execute(sql)
sql='create table mem_rec (mem_id varchar(5) primary key,name varchar(30) not null,password varchar(20) not null,doj date)'
#mycur.execute(sql)
sql='create table bor_rec(bor_id varchar(5) primary key,book_id int not null,bor_date date,mem_id varchar(5) not null,status varchar(13) not null, foreign key(book_id) references book_rec(book_id) on update cascade on delete cascade, foreign key(mem_id) references mem_rec(mem_id) on update cascade on delete cascade)'
#mycur.execute(sql)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
def add():
    '''Adds a book from the book table'''
    print('/'*100,'\n')
    mycur.execute('select max(book_id) from book_rec')
    k=mycur.fetchone()
    t=input('Enter Title of the Book:')
    print()
    a=input('Enter Author Name:')
    print()
    d=input('Enter Description:')
    print()
    s=int(input('Enter Stock:'))
    if not(k[0]):
        sql="insert into book_rec values(1001,%s,%s,%s,%s,0)"
        mycur.execute(sql,(t.upper().strip(),a.upper().strip(),d,s))
        print('\nRecord added')
    else:
        i=k[0]+1
        sql="insert into book_rec values(%s,%s,%s,%s,%s,0)"
        mycur.execute(sql,(i,t.upper().strip(),a.upper().strip(),d,s))
        print('\nRecord added\n')
    mydb.commit()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
def remove():
    '''Removes a book from the book table'''
    print('/'*100,'\n')
    i=int(input('Enter book id:'))
    sql=' select * from book_rec where book_id=%s'
    mycur.execute(sql,(i,))
    k=mycur.fetchone()
    if not(k):
        print('\nid does not exist\n')
    else:
        sql='delete from book_rec where book_id=%s'
        mycur.execute(sql,(i,))
        print('\nRecord deleted\n')
    mydb.commit()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def checkbook():
    '''Checks status of the book table'''
    while True:
        print('/'*100,'\n')
        print('''\tChoose how to find the book and its status:\n\n
        1.check status by book id\n
        2.By Title\n
        3.By Author\n
        4.Id,title and author of all books\n
        5.show status of all books\n
        6.Go back\n ''')
        c3=int(input('Enter choice:'))
        if c3==1:
            print()
            i=int(input('Enter book_id:'))
            print()
            sql=' select * from book_rec where book_id=%s'
            mycur.execute(sql,(i,))
            k=mycur.fetchone()
            if not(k):
                print('\nid does not exist\n')
            else:
                sql='select book_id,title,author,stock,no_bor from book_rec where book_id=%s'
                mycur.execute(sql,(i,))
                k=mycur.fetchone()
                print('book_id:',k[0],'\nTitle:',k[1],'\nAuthor:',k[2],'\nStock:',k[3],'\nno. bor. :',k[4],'\n')
                print('*'*50)

        elif c3==2:
            print()
            t=input('Enter Title:')
            print()
            t=t.upper().strip()
            sql=' select * from book_rec where title=%s'
            mycur.execute(sql,(t,))
            k=mycur.fetchone()
            if not(k):
                print('Title does not exist','\n')
            else:
                sql='select book_id,title,author,stock,no_bor from book_rec where title=%s'
                mycur.execute(sql,(t,))
                k=mycur.fetchone()
                print('book_id:',k[0],'\nTitle:',k[1],'\nAuthor:',k[2],'\nStock:',k[3],'\nno. bor. :',k[4],'\n')
                print('*'*50)

        elif c3==3:
            print()
            a=input('Enter author:')
            print()
            a=a.upper().strip()
            sql=' select * from book_rec where author=%s'
            mycur.execute(sql,(a,))
            k=mycur.fetchall()
            if not(k):
                print('author does not exist','\n')
            else:
                sql='select book_id,title,author,stock,no_bor from book_rec where author=%s'
                mycur.execute(sql,(a,))
                i=mycur.fetchall()
                for k in i:
                    print('book_id:',k[0],'\nTitle:',k[1],'\nAuthor:',k[2],'\nStock:',k[3],'\nno. bor. :',k[4],'\n')
                    print('*'*50)

        elif c3==4:
            sql=' select * from book_rec'
            mycur.execute(sql)
            k=mycur.fetchall()
            print()
            if not(k):
                print('Table empty add records\n')
            else:
                sql='select book_id,title,author from book_rec'
                mycur.execute(sql)
                i=mycur.fetchall()
                for k in i:
                    print('book_id: ',k[0],'\nTitle :',k[1],'\nAuthor: ',k[2],'\n')
                    print('*'*50)

        elif c3==5:
            sql=' select * from book_rec'
            mycur.execute(sql)
            k=mycur.fetchall()
            print()
            if not(k):
                print('Table empty add records\n')
            else:
                sql='select book_id,title,author,stock,no_bor from book_rec '
                mycur.execute(sql)
                i=mycur.fetchall()
                for k in i:
                    print('book_id:',k[0],'\nTitle:',k[1],'\nAuthor:',k[2],'\nStock:',k[3],'\nno. bor. :',k[4],'\n')
                    print('*'*50)
            
        elif c3==6:
            print('\nGoing back to Admin menu\n')
            break
        else:
            print('\nInvalid choice\n')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def checkborrow():
    '''Checks status of the borrow table'''
    print()
    sql='select bor_id,a.mem_id,name,book_id,bor_date from bor_rec a,mem_rec c where a.mem_id=c.mem_id and status="NOT RETURNED"'
    mycur.execute(sql)
    k=mycur.fetchall()
    for i in k:
        print('Bor_id :',i[0],'\nMem_id :',i[1],'\nNAME :',i[2],'\nBook_id :',i[3],'\nBor_Date :',i[4])
        print('*'*50)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def checkfine():
    '''Displays the details the the books and the member which have gone past due date'''
    print()
    sql='select bor_id,a.mem_id,name,book_id from bor_rec a,mem_rec c where a.mem_id=c.mem_id and status="NOT RETURNED" '
    mycur.execute(sql)
    k=mycur.fetchall()
    for i in k:
        sql='select bor_date from bor_rec where bor_id=%s'
        mycur.execute(sql,(i[0],))
        j=mycur.fetchone()
        no_days=date.today()-j[0]
        no_days=no_days.days
        if no_days>7:
            a=no_days-7
            f=a*10
            print('Bor_id :',i[0],'\nMem_id :',i[1],'\nNAME :',i[2],'\nBook_id :',i[3],'\nBor_Date :',j[0],'\nNo. Days past Due Date :',a,'\nFINE :',f)
            print('*'*50)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def addstock():
    '''Adds stock to the books'''
    print('/'*100,'\n')
    i=int(input('Enter book id for whick you want to add stock:'))
    print()
    sql=' select * from book_rec where book_id=%s'
    mycur.execute(sql,(i,))
    k=mycur.fetchone()
    if not(k):
        print('id does not exist','\n')
    else:
        s=int(input('Enter no. of copies to be added to stock:'))
        sql='update book_rec set stock=stock+%s where book_id=%s'
        mycur.execute(sql,(s,i))
        mydb.commit()
        print('\nStock updated\n')
        print('New status:\n')
        sql='select book_id,title,author,stock,no_bor from book_rec where book_id=%s'
        mycur.execute(sql,(i,))
        k=mycur.fetchone()
        print('book_id :',k[0],'\nTitle :',k[1],'\nAuthor :',k[2],'\nStock :',k[3],'\nno. bor. :',k[4],'\n')
        print('*'*50)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def readdesc():
    '''Allows admin to get the deacription of a book'''
    while True:
        print('/'*100,'\n')
        print('''\tChoose how to find the book and get it's descprintion:\n\n
        1.By book id\n
        2.By Title\n
        3.By Author\n
        4show description of all books\n
        5.Go back\n ''')
        c3=int(input('Enter choice:'))
        if c3==1:
            print()
            i=int(input('Enter book_id:'))
            print()
            sql=' select * from book_rec where book_id=%s'
            mycur.execute(sql,(i,))
            k=mycur.fetchone()
            if not(k):
                print('\nid does not exist\n')
            else:
                sql='select book_id,title,author,description from book_rec where book_id=%s'
                mycur.execute(sql,(i,))
                k=mycur.fetchone()
                print('\nBook_id:  ',k[0],'\nTitle:  ',k[1],'\nAuthor:  ',k[2],'\n\nDescription:\n\n\t',k[3],'\n')

        elif c3==2:
            print()
            t=input('Enter Title:')
            print()
            t=t.upper().strip()
            sql=' select * from book_rec where title=%s'
            mycur.execute(sql,(t,))
            k=mycur.fetchone()
            if not(k):
                print('Title does not exist','\n')
            else:
                sql='select book_id,title,author,description from book_rec where title=%s'
                mycur.execute(sql,(t,))
                k=mycur.fetchone()
                print('\nBook_id:  ',k[0],'\nTitle:  ',k[1],'\nAuthor:  ',k[2],'\n\nDescription:\n\n\t',k[3],'\n')

        elif c3==3:
            print()
            a=input('Enter author:')
            print()
            a=a.upper().strip()
            sql=' select * from book_rec where author=%s'
            mycur.execute(sql,(a,))
            k=mycur.fetchall()
            if not(k):
                print('author does not exist','\n')
            else:
                sql='select book_id,title,author,description from book_rec where author=%s'
                mycur.execute(sql,(a,))
                i=mycur.fetchall()
                for k in i:
                    print('\nBook_id:  ',k[0],'\nTitle:  ',k[1],'\nAuthor:  ',k[2],'\n\nDescription:\n\n\t',k[3],'\n')
                    print('*'*50)
        elif c3==4:
            sql=' select * from book_rec'
            mycur.execute(sql)
            k=mycur.fetchall()
            print()
            if not(k):
                print('Table empty add records\n')
            else:
                sql='select book_id,title,author,description from book_rec '
                mycur.execute(sql)
                i=mycur.fetchall()
                for k in i:
                    print('\nBook_id:  ',k[0],'\nTitle:  ',k[1],'\nAuthor:  ',k[2],'\n\nDescription:\n\n\t',k[3],'\n')
                    print('*'*50)
        elif c3==5:
            print('\nGoing back to Admin menu\n')
            break
        else:
            print('\nInvalid choice\n')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Admin():
    while True:
        print('-'*80,'\n')
        print('\tChoose from the following Actions\n\n')
        print('''1.Add a new book\n
2.Remove a existing book (using id ,to find id use option3)\n
3.Check status\n
4.Check books borrowed\n
5.Check fine status\n
6.Add Stock (using id ,to find id use option3)\n
7.Read decription\n
8.Go back to main page\n''')
        c2=int(input('Enter chioce of action:'))
        print()
        if c2==1:
            add()
        elif c2==2:
            remove()
        elif c2==3:
            checkbook()
        elif c2==4:
            checkborrow()
        elif c2==5:
            checkfine()
        elif c2==6:
            addstock()
        elif c2==7:
            readdesc()
        elif c2==8:
            print('\nGoing back to main page\n')
            break
        else:
            print('\nInvalid choice\n')
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def addmem():
    '''Add membe to mem_rec'''
    print('/'*100,'\n')
    mycur.execute('select max(mem_id) from mem_rec')
    k=mycur.fetchone()
    n=input('Enter name:')
    print()
    p=input('set password:')
    print()
    p1=input('Re-enter password:')
    print()
    while p!=p1:
        print('Password does not match enter password again,you can also set a different password\n')
        p=input('Enter password:')
        p1=input('Re-enter password:')
    if not(k[0]):
        sql="insert into mem_rec values('M101',%s,%s,curdate())"
        mycur.execute(sql,(n.upper(),p))
        print('\nAccount created,\n YOUR MEM_ID IS :  M101\nIMPORTANT:Remember your id for future use of your Account')
        mydb.commit()
        return 'M101'
    else:
        i='M'+str(int(k[0][1:])+1)
        sql="insert into mem_rec values(%s,%s,%s,curdate())"
        mycur.execute(sql,(i,n.upper(),p))
        print('\nAccount created,\n YOUR MEM_ID IS :   ',i,'\nIMPORTANT:Remember your id for future use of your Account') 
        mydb.commit()
        return i
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def search():
    '''Find books'''
    while True:
        print('\n','/'*100,'\n')
        print('''\tActions:\n\n
        1.Display list of all Book Titles, Authors (Available for borrowing)\n
        2.Search by Title\n
        3.Search by Author\n
        4.Search by Book id\n
        5.Go back\n''')
        c=int(input('Enter option number:'))
        print()
        if c==1:
            print('1.Book Titles\n2.Authors\n3.Go back\n')
            ch=int(input('Enter choice:'))
            print()
            if ch==1:
                sql='select book_id,title from book_rec where (stock-no_bor)>0'
                mycur.execute(sql)
                k=mycur.fetchall()
                n=1
                for i in k:
                    print(n,'.','Book Title:  ',i[1],'\t|Book id:',i[0])
                    n+=1
            elif ch==2:
                sql='select distinct author from book_rec where (stock-no_bor)>0'
                mycur.execute(sql)
                k=mycur.fetchall()
                n=1
                for i in k:
                    print(n,'.','Author:  ',i[0])
                    n+=1
            elif ch==3:
                print('Going back . . .')
                break
            else:
                print('invalid choice\nGoing back')
                break
        elif c==2:
            t=input('Enter Title:')
            print()
            t=t.upper().strip()
            sql=' select book_id,author,description,stock-no_bor from book_rec where title=%s'
            mycur.execute(sql,(t,))
            k=mycur.fetchone()
            if k:
                if k[3]>0:
                    print('The title is available for borrowing, written by',k[1],'\nBook id :',k[0])
                    ch=input('Do you want to read Description?(yes/no)')
                    if ch.lower()=='yes':
                        print('Description:\n\t',k[2])
                    print('\nTo borrow the book choose option 2 in previous menu, please note the book id to borrow the book\n')
                    print('Going back . . .\n')
                else:
                    print('The title exist in the library but not available for borrowing.')
            else:
                print('The title does not exist in the library.')
        elif c==3:
            a=input('Enter author:')
            print()
            a=a.upper().strip()
            sql=' select book_id,title,stock-no_bor from book_rec where author=%s'
            mycur.execute(sql,(a,))
            k=mycur.fetchall()
            if not(k):
                print('author does not exist in library','\n')
            else:
                n=1
                for i in k:
                    print(n,'. Book id :',i[0],'\tTitle : ',i[1])
                    n+=1
                    if i[2]>0:
                        print('The book is available for borrowing, to borrow use option 2 in previous menu, please note the book id')
                    else:
                        print('The book is not available for borrowing')
                    print()
                print('\nTo read Description of the any of the books available for borrowing ,search the title or book id.')
        elif c==4:
            id=int(input('Enter id:'))
            print()
            sql=' select title,author,description,stock-no_bor from book_rec where book_id=%s'
            mycur.execute(sql,(id,))
            k=mycur.fetchone()
            if k:
                if k[3]>0:
                    print('The book is available for borrowing.\nBook Title:',k[0],'\t Auhtor : ',k[1])
                    ch=input('Do you want to read Description?(yes/no)')
                    if ch.lower()=='yes':
                        print('Description:\n\t',k[2])
                        print('Going Back')
                    elif ch.lower()=='no':
                        print('Going Back')
                    else:
                        print('Invalid choice, Going back . . .')
                    print('To borrow the book choose option 2 in previous menu, please note the book id to borrow the book')
                else:
                    print('The title exist in the library but not available for borrowing.')
            else:
                print('The title does not exist in the library.')
        elif c==5:
            print('Going back . . .')
            break
        else:
            print('Invaid choice')
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def subMem(id):
    '''Member functions'''
    while True:
        print('-'*80,'\n')
        print('''\tMember Functions:\n\n
1.Search for a book\n
2.Read Description\n
3.Borrow a book (get book id from the above option)\n
4.Return borrowed book\n
5.Check Account status\n
6.Go back\n''')
        c=int(input('Enter choice:'))
        print()
        if c==1:
            search()
        elif c==2:
            readdesc()
        elif c==3:
            print('At max only two books can be borrowed.\n')
            sql='select count(*) from bor_rec where status="NOT RETURNED" and mem_id=%s'
            mycur.execute(sql,(id,))
            k=mycur.fetchone()
            if k[0]>=2:
                print('You have exceeded the 2 book limit , if you wish to borrow please return the previously borrowed book.')
                continue
            bid=int(input('Enter book_id to borrow:'))
            print()
            sql='select stock-no_bor from book_rec where book_id=%s'
            mycur.execute(sql,(bid,))
            k=mycur.fetchone()
            if not(k):
                print('Invalid book_id')
            else :
                if k[0]>0:
                    mycur.execute('select max(bor_id) from bor_rec')
                    j=mycur.fetchone()
                    if not(j[0]):
                        sql="insert into bor_rec values('B101',%s,curdate(),%s,'NOT RETURNED')"
                        mycur.execute(sql,(bid,id))
                        mydb.commit()
                        print('Book borrowed , bor_id : B101')
                    else:
                        i='B'+str(int(j[0][1:])+1)
                        sql="insert into bor_rec values(%s,%s,curdate(),%s,'NOT RETURNED')"
                        mycur.execute(sql,(i,bid,id))
                        print('Book borrowed , bor_id :',i)
                        mydb.commit()
                    print()
                    sql=' select title,author from book_rec where book_id=%s'
                    mycur.execute(sql,(bid,))
                    p=mycur.fetchone()
                    print('Book details:\n\tTitle : {}\n\tAuthor : {}'.format(p[0],p[1]))
                    sql='update book_rec set no_bor=1+no_bor where book_id=%s'
                    mycur.execute(sql,(bid,))
                    mydb.commit()
                else:
                    print("There aren't enough copies for this book to be borrowed.")  
        elif c==4:
            sql='select bor_id,bor_date,a.book_id,title,author from bor_rec A,book_rec b where a.book_id=b.book_id and mem_id=%s and status="NOT RETURNED"'
            mycur.execute(sql,(id,))
            k=mycur.fetchall()
            if k:
                print('Number of books currently borrowed',len(k))
                print('Details of the books borrowed:')
                for i in k:
                    print('Bor_id : {}\nBorrow Date : {}\nBook_id: {}\nTitle : {}\nAuthor : {} \n'.format(i[0],i[1],i[2],i[3],i[4]))
            else:
                print('Currently no books Borrowed')
                continue
            bid=input('Enter bor_id of the book you are returning:')
            bid=bid.upper()
            for i in k :
                if i[0]==bid:
                    sql='select bor_date from bor_rec where bor_id=%s'
                    mycur.execute(sql,(bid,))
                    j=mycur.fetchone()
                    no_days=date.today()-j[0]
                    no_days=no_days.days
                    if no_days>7:
                        a=no_days-7
                        print('You have exceeded the 7-Day Return Period by',a,'days fine for each day is Rs. 10')
                        print('Your fine amount is : Rs. ',a*10)
                    sql='Update bor_rec set status="RETURNED" where bor_id=%s'
                    mycur.execute(sql,(bid,))
                    mydb.commit()
                    print('Book successfully returned.')
                    sql='update book_rec set no_bor=no_bor-1 where book_id=%s'
                    mycur.execute(sql,(i[2],))
                    mydb.commit()
                    break
            else:
                print('Invalid bor_id !!!')      
        elif c==5:
            sql='select bor_id,bor_date,a.book_id,title,author from bor_rec A,book_rec b where a.book_id=b.book_id and mem_id=%s and status="NOT RETURNED"'
            mycur.execute(sql,(id,))
            k=mycur.fetchall()
            if k:
                print('Number of books currently borrowed',len(k))
                print('Details of the books borrowed:')
                for i in k:
                    print('Bor_id : {}\nBorrow Date : {}\nBook_id: {}\nTitle : {}\nAuthor : {} \n'.format(i[0],i[1],i[2],i[3],i[4]))
            else:
                print('Currently no books Borrowed')
        elif c==6:
            print('Going back . . . ')
            break
        else:
            print('Invalid Choice!')
        
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def Member():
    '''Main member module'''
    while True:
        print('-'*80,'\n')
        print('''1.Member Already?\n
2.New? Create account!\n
3.Go back to main page\n''')
        c=int(input('Enter choice:'))
        print()
        if c==1:
            i=input('Enter mem_id:')
            sql='select * from mem_rec where mem_id=%s'
            mycur.execute(sql,(i.upper(),))
            k=mycur.fetchone()
            if not k:
                print('Mem_id does not exist try again,going back . . .')
                continue
            else:
                p=input('Enter password:')
                if p==k[2]:
                    print('Successful login!')
                    subMem(i)
                else:
                    print('Incorrect password, try again, going back . . .')
                    continue
        elif c==2:
            i=addmem()
            print('Successful Sign in !')
            subMem(i)
        elif c==3:
            print('Going Back to main page. . .')
            break
        else:
            print('Invalid Choice')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    while True:
        '''first step menu'''
        print('~'*60)
        print('\n\tWelcome to the National Library Management System\n\n')
        print('''1.Admin\n
2.Member\n
3.Exit\n''')
        try:
            c1=int(input('Choose your role:'))
            if c1==1:
                '''Admin Access'''
                print()
                p=input('Enter Admin password:')
                if p==pas:
                    print('correct password')
                    Admin()
                else:
                    print('Wrong Password')
                    continue
            elif c1==2:
                '''Member Access'''
                Member()
            elif c1==3:
                print('Good bye ! have a great day')
                break
            else:
                print('Invalid choice')
        except ValueError:
            print('Please Enter an Integer as Choice!')
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
print('\t\t         COMPUTER  SCIENCE  PROJECT\n\t\t         ========== ======== ========\n\n\n\t\t\tLIBRARY MANAGEMENT\n\t\t\t=======  ============\n\n\n\t\t\t\t\t\t--By :NANDITA GUPTA\n\t\t\t\t\t\t      ------------------- ------------\n\t\t\t\t\t\t       12 A\n\t\t\t\t\t\t       --------\n\t\t\t\t\t\t      12117\n\t\t\t\t\t\t      -------------\n\n\t')
p=input('Press Enter to continue . . . .')
main()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
mydb.close()

'''
[\
(1001, "HARRY POTTER AND THE PHILOSOPHER'S STONE", 'J. K. ROWLING', "The first novel in the Harry Potter series and Rowling's debut novel, it follows Harry Potter, a young wizard who discovers his magical heritage on his eleventh birthday, when he receives a letter of acceptance to Hogwarts School of Witchcraft and Wizardry. Harry makes close friends and a few enemies during his first year at the school, and with the help of his friends, Harry faces an attempted comeback by the dark wizard Lord Voldemort, who killed Harry's parents, but failed to kill Harry when he was just 15 months old.", 10), \
(1002, 'HARRY POTTER AND THE CHAMBER OF SECRETS', 'J. K. ROWLING', "The second novel in the Harry Potter series. The plot follows Harry's second year at Hogwarts School of Witchcraft and Wizardry, during which a series of messages on the walls of the school's corridors warn that the 'Chamber of Secrets' has been opened and that the 'heir of Slytherin' would kill all pupils who do not come from all-magical families. These threats are found after attacks that leave residents of the school petrified. Throughout the year, Harry and his friends Ron and Hermione investigate the attacks.", 12),\
(1003, 'THE FAULT IN OUR STARS', 'JOHN GREEN', 'The story is narrated by Hazel Grace Lancaster, a 16-year-old girl with thyroid cancer that has affected her lungs. Hazel is forced by her parents to attend a support group where she subsequently meets and falls in love with 17-year-old Augustus Waters, an ex-basketball player and amputee. ', 8),\
(1004, "ALICE'S ADVENTURES IN WONDERLAND", 'LEWIS CARROLL', ' It tells of a young girl named Alice, who falls through a rabbit hole into a subterranean fantasy world populated by peculiar, anthropomorphic creatures. It is considered to be one of the best examples of the literary nonsense genre. The tale plays with logic, giving the story lasting popularity with adults as well as with children.', 12), \
(1005, 'THE JUNGLE BOOK', 'RUDYARD KIPLING', "The Jungle Book (1894) is a collection of stories by the English author Rudyard Kipling. Most of the characters are animals such as Shere Khan the tiger and Baloo the bear, though a principal character is the boy or 'man-cub' Mowgli, who is raised in the jungle by wolves. The stories are set in a forest in India; one place mentioned repeatedly is 'Seonee' (Seoni), in the central state of Madhya Pradesh.", 4)\
]
'''
        
