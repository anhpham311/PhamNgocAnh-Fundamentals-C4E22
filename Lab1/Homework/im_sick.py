from gmail import GMail, Message
import datetime

html_template = '''
<p>Thua boss,</p> 
<p>Em xin duoc nghi lam hom nay vi em dang bi om rat nang</p>
'''
now = datetime.datetime.now()
if now.hour == 7:
    gmail = GMail("pham.n.anh95@gmail.com","Muji95e$")
    msg = Message("Xin nghi om", to="anh.pham@cecr.vn",html=html_template)
    gmail.send(msg)

    
    