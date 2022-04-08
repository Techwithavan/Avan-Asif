a=int(input("Which Century "))
d=int(input("Which year"))
b=(input("Which Month"))
c=int(input("Which Date"))
a=a%4
aa=0
aa+=a
dd=d//4
dd*=2
aa+=dd
ddb=d%4
aa+=ddb
b.lower()
cb=""
if b=="jan":
    cb=0
if b=="feb":
    cb=31
if b=="mar":
    cb=59
if b=="apr":
    cb=90
if b=="may":
    cb=120
if b=="june":
    cb=151
if b=="july":
    cb=181
if b=="aug":
    cb=212
if b=="sep":
    cb=243
if b=="oct":
    cb=273
if b=="nov":
    cb=304
if b=="dec":
    cb=334
aa+=cb
aa+=c
aa=aa%7
fn=""
if aa==1:
    fn="Monday"
if aa==2:
    fn="Tuesday"
if aa==3:
    fn="Wednesday"
if aa==4:
    fn="Thursday"
if aa==5:
    fn="Friday"
if aa==6:
    fn="Saturday"
if aa==0:
    fn="Sunday"
print(f"Your Date Day Is {fn}")