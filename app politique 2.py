from tkinter import *
from tkinter import messagebox
from statistics import mean
from math import sqrt
import matplotlib.pyplot as plt
import pylab
listeh=[]
listeAcc=[]
listeAcm=[]
listetue=[]
listeblesse=[]
listebg=[]
listebl=[]
ix=40
iy=50
iz=60
x=10
y=20
z=30
ix2=100
iy2=110
iz2=120
ix1=70
iy1=80
iz1=90
ix3=130
iy3=140
iz3=150
ix4=160
iy4=170
iz4=180
#nombre aleatoire0
def aleatoire0(ixc,iyc,izc):
    global x
    global y
    global z
    x=ixc
    y=iyc
    z=izc
    x=171*(x%177)-2*(x//177)
    y=172*(y%176)-35*(y//176)
    z=170*(z%178)-63*(z//178)
    if(x<0):
        x=x+30269
    if(y<0):
        y=y+30307
    if(z<0):
        z=z+30323
    inter=((x/30269)+(y/30307)+(z/30323))
    return inter-int(inter)
#nombre aleatoire
def aleatoire(ixc,iyc,izc):
    global ix
    global iy
    global iz
    ix=ixc
    iy=iyc
    iz=izc
    ix=171*(ix%177)-2*(ix//177)
    iy=172*(iy%176)-35*(iy//176)
    iz=170*(iz%178)-63*(iz//178)
    if(ix<0):
        ix=ix+30269
    if(iy<0):
        iy=iy+30307
    if(iz<0):
        iz=iz+30323
    inter=((ix/30269)+(iy/30307)+(iz/30323))
    return inter-int(inter)
#nombre aleatoire 1
def aleatoire1(ixc,iyc,izc):
    global ix1
    global iy1
    global iz1
    ix1=ixc
    iy1=iyc
    iz1=izc
    ix1=171*(ix1%177)-2*(ix1//177)
    iy1=172*(iy1%176)-35*(iy1//176)
    iz1=170*(iz1%178)-63*(iz1//178)
    if(ix1<0):
        ix1=ix1+30269
    if(iy1<0):
        iy1=iy1+30307
    if(iz1<0):
        iz1=iz1+30323
    inter=((ix1/30269)+(iy1/30307)+(iz1/30323))
    return inter-int(inter)
#nombre aleatoire 2
def aleatoire2(ixc,iyc,izc):
    global ix2
    global iy2
    global iz2
    ix2=ixc
    iy2=iyc
    iz2=izc
    ix2=171*(ix2%177)-2*(ix2//177)
    iy2=172*(iy2%176)-35*(iy2//176)
    iz2=170*(iz2%178)-63*(iz2//178)
    if(ix2<0):
        ix2=ix2+30269
    if(iy2<0):
        iy2=iy2+30307
    if(iz2<0):
        iz2=iz2+30323
    inter=((ix2/30269)+(iy2/30307)+(iz2/30323))
    return inter-int(inter)
#nombre aleatoire 3
def aleatoire3(ixc,iyc,izc):
    global ix3
    global iy3
    global iz3
    ix3=ixc
    iy3=iyc
    iz3=izc
    ix3=171*(ix3%177)-2*(ix3//177)
    iy3=172*(iy3%176)-35*(iy3//176)
    iz3=170*(iz3%178)-63*(iz3//178)
    if(ix3<0):
        ix3=ix3+30269
    if(iy3<0):
        iy3=iy3+30307
    if(iz3<0):
        iz3=iz3+30323
    inter=((ix3/30269)+(iy3/30307)+(iz3/30323))
    return inter-int(inter)
#nombre aleatoire 4
def aleatoire4(ixc,iyc,izc):
    global ix4
    global iy4
    global iz4
    ix4=ixc
    iy4=iyc
    iz4=izc
    ix4=171*(ix4%177)-2*(ix4//177)
    iy4=172*(iy4%176)-35*(iy4//176)
    iz4=170*(iz4%178)-63*(iz4//178)
    if(ix4<0):
        ix4=ix4+30269
    if(iy4<0):
        iy4=iy4+30307
    if(iz4<0):
        iz4=iz4+30323
    inter=((ix4/30269)+(iy4/30307)+(iz4/30323))
    return inter-int(inter)


#-------------------------
def fb(alea):
    if alea<0.1 and alea>=0:
        r=aleatoire0(x,y,z)%1-2
        return r/100
    if alea>=0.1 and alea<=0.45:
        r=aleatoire0(x,y,z)%1.5
        return r/100
    if alea>=0.1 and alea<=0.45:
        r=aleatoire0(x,y,z)%1.5
        return r/100
    if alea>0.45 and alea<=0.55:
        r=aleatoire0(x,y,z)%1+2
        return r/100
    if alea>0.55 and alea<=0.8:
        r=aleatoire0(x,y,z)%1+3
        return r/100
    if alea>0.8 and alea<=0.9:
        r=aleatoire0(x,y,z)%1+9
        return r/100
    if alea>0.9 and alea<=1:
        r=aleatoire0(x,y,z)%1+14
        return r/100
#-----------------------
def f1b(alea):
    return (alea%1.5+4)/100

#------------------------
def f2b(alea):
    return (alea%2+4.5)/100
#----------------------------
def f3b(alea):
    return (alea%7+147)/100
def f4b(alea):
    return (alea%10+5)/100
#-------------------------
def fa(alea):
    if alea<0.1 and alea>=0:
        r=aleatoire0(x,y,z)%1.1-3.3
        return r/100
    if alea>=0.1 and alea<=0.45:
        r=aleatoire0(x,y,z)%1.5-0.15
        return r/100
    if alea>0.45 and alea<=0.55:
        r=aleatoire0(x,y,z)%0.9+1.8
        return r/100
    if alea>0.55 and alea<=0.8:
        r=aleatoire0(x,y,z)%0.9+2.7
        return r/100
    if alea>0.8 and alea<=0.9:
        r=aleatoire0(x,y,z)%0.9+8.1
        return r/100
    if alea>0.9 and alea<=1:
        r=aleatoire0(x,y,z)%0.9+12.6
        return r/100
#-----------------------
def f1a(alea):
    return (alea%1.3+3.6)/100

#------------------------
def f2a(alea):
    return (alea%1.8+4)/100
#----------------------------
def f3a(alea):
    return (alea%6+132)/100
def f4a(alea):
    return (alea%9+4.5)/100

def calcul():
    H=2007
    Acc=58924
    dep=int(depart.get())
    end=int(fin.get())
    fm=f1b(aleatoire1(ix1,iy1,iz1))
    Accm=Acc*fm
    ft=f2b(aleatoire2(ix2,iy2,iz2))
    nbre_tue=Acc*ft
    nbre_blesse=Acc*f3b(aleatoire3(ix3, iy3, iz3))
    nbre_grave=nbre_blesse*f4b(aleatoire4(ix4, iy4, iz4))
    nbre_leger=nbre_blesse-nbre_grave

    H=H+1
    while (H < dep):
        if(H<2019):
            Acc+=Acc*fb(aleatoire(ix,iy,iz))
            fm=f1b(aleatoire1(ix1,iy1,iz1))
            Accm=Acc*fm
            ft=f2b(aleatoire2(ix2,iy2,iz2))
            nbre_tue=Acc*ft
            nbre_blesse=Acc*f3b(aleatoire3(ix3, iy3, iz3))
            nbre_grave=nbre_blesse*f4b(aleatoire4(ix4, iy4, iz4))
            nbre_leger=nbre_blesse-nbre_grave
            H=H+1  
        else:
            Acc+=Acc*fa(aleatoire(ix,iy,iz))
            fm=f1a(aleatoire1(ix1,iy1,iz1))
            Accm=Acc*fm
            ft=f2a(aleatoire2(ix2,iy2,iz2))
            nbre_tue=Acc*ft
            nbre_blesse=Acc*f3a(aleatoire3(ix3, iy3, iz3))
            nbre_grave=nbre_blesse*f4a(aleatoire4(ix4, iy4, iz4))
            nbre_leger=nbre_blesse-nbre_grave
            H=H+1              


    while H<=end:
        if(H<2019):
            listeh.append(H)
            Acc+=Acc*fb(aleatoire(ix,iy,iz))
            listeAcc.append(int(Acc))
            fm=f1b(aleatoire1(ix1,iy1,iz1))
            Accm=Acc*fm
            listeAcm.append(int(Accm))
            ft=f2b(aleatoire2(ix1,iy1,iz1))
            nbre_tue=Acc*ft
            listetue.append(int(nbre_tue))
            nbre_blesse=Acc*f3b(aleatoire3(ix3, iy3, iz3))
            listeblesse.append(int(nbre_blesse))
            nbre_grave=nbre_blesse*f4b(aleatoire4(ix4, iy4, iz4))
            listebg.append(int(nbre_grave))
            nbre_leger=nbre_blesse-nbre_grave
            listebl.append(int(nbre_leger))
            H=H+1
        else:
            Acc+=Acc*fa(aleatoire(ix,iy,iz))
            listeh.append(H)
            listeAcc.append(int(Acc))
            fm=f1a(aleatoire1(ix1,iy1,iz1))
            Accm=Acc*fm
            listeAcm.append(int(Accm))
            ft=f2a(aleatoire2(ix1,iy1,iz1))
            nbre_tue=Acc*ft
            listetue.append(int(nbre_tue))
            nbre_blesse=Acc*f3a(aleatoire3(ix3, iy3, iz3))
            listeblesse.append(int(nbre_blesse))
            nbre_grave=nbre_blesse*f4a(aleatoire4(ix4, iy4, iz4))
            listebg.append(int(nbre_grave))
            nbre_leger=nbre_blesse-nbre_grave
            listebl.append(int(nbre_leger))
            H=H+1            
  
    result="nombre total accident corporels= %d \n nombre total accident mortel= %d \n nombre tue= %d \n nombre blesse= %d \n nombre blesse grave= %d \n nombre blesse leger= %d" %(int(Acc),int(Accm),int(nbre_tue),int(nbre_blesse),int(nbre_grave),int(nbre_leger))
    messagebox.showinfo("resultat", result)
    print("annee               ",listeh)
    print("Accident corporel   ",listeAcc)
    print("Accident mortel     ",listeAcm)
    print("nombre morts        ",listetue)
    print("nombre blesse       ",listeblesse)
    print("nombre blesses grave",listebg)
    print("nombre blesses leger",listebl)   
    fig=plt.figure()
    p1=plt.plot(listeh,listeAcc,label='Acc')
    p2=plt.plot(listeh,listeAcm,label='Acm')
    p2=plt.plot(listeh,listetue,label='morts')
    p2=plt.plot(listeh,listeblesse,label='blesse')
    p2=plt.plot(listeh,listebg,label='blesse grave')
    p2=plt.plot(listeh,listebl,label='blesse leger')
    pylab.legend(loc='best')
    plt.show()

#-------------------------


#-------------------------
def estimer():
    s1=0
    s2=0
    s3=0
    s4=0
    s5=0
    s6=0
    i=1
    m=int(n.get())
    listeacc=[]
    listeaccm=[]
    listetue=[]
    listeb=[]
    listebg=[]
    listebl=[]
    while i<=m:
        H=2007
        print(H)
        Acc=58924
        end=int(fin.get())
        fm=f1b(aleatoire1(ix1,iy1,iz1))
        Accm=Acc*fm
        print(Accm)
        ft=f2b(aleatoire2(ix2,iy2,iz2))
        nbre_tue=Acc*ft
        nbre_blesse=Acc*f3b(aleatoire3(ix3, iy3, iz3))
        nbre_grave=nbre_blesse*f4b(aleatoire4(ix4, iy4, iz4))
        nbre_leger=nbre_blesse-nbre_grave      
        H=H+1   
        while H<=end:
            if(H<2019):
                Acc+=Acc*fb(aleatoire(ix,iy,iz))
                fm=f1b(aleatoire1(ix1,iy1,iz1))
                Accm=Acc*fm
                ft=f2b(aleatoire2(ix1,iy1,iz1))
                nbre_tue=Acc*ft
                nbre_blesse=Acc*f3b(aleatoire3(ix3, iy3, iz3))
                nbre_grave=nbre_blesse*f4b(aleatoire4(ix4, iy4, iz4))
                nbre_leger=nbre_blesse-nbre_grave            
                H=H+1  
            else:
                Acc+=Acc*fa(aleatoire(ix,iy,iz))
                fm=f1a(aleatoire1(ix1,iy1,iz1))
                Accm=Acc*fm
                ft=f2a(aleatoire2(ix1,iy1,iz1))
                nbre_tue=Acc*ft
                nbre_blesse=Acc*f3a(aleatoire3(ix3, iy3, iz3))
                nbre_grave=nbre_blesse*f4a(aleatoire4(ix4, iy4, iz4))
                nbre_leger=nbre_blesse-nbre_grave            
                H=H+1                  

        listeacc.append(Acc)
        listeaccm.append(Accm)
        listetue.append(nbre_tue)
        listeb.append(nbre_blesse)
        listebg.append(nbre_grave)
        listebl.append(nbre_leger)
        i=i+1
    accmoy=mean(listeacc)
    accmmoy=mean(listeaccm)
    tue_moy=mean(listetue)
    bmoy=mean(listeb)
    bgmoy=mean(listebg)
    blmoy=mean(listebl)
    for x in listeacc:
        s1+=(x-accmoy)**2
    s1=sqrt(s1/(m-1))
    for x in listeaccm:
        s2+=(x-accmmoy)**2
    s2=sqrt(s2/(m-1))
    for x in listetue:
        s3+=(x-tue_moy)**2
    s3=sqrt(s3/(m-1))
    for x in listeb:
        s4+=(x-bmoy)**2
    s4=sqrt(s4/(m-1))
    for x in listebg:
        s5+=(x-bgmoy)**2
    s5=sqrt(s5/(m-1))
    for x in listebl:
        s6+=(x-blmoy)**2
    s6=sqrt(s6/(m-1))    
    result="intervalle de confiance de Acc =[ %.2f , %.2f ] \n intervalle de confiance de Accm =[ %.2f , %.2f ] \n intervalle de confiance de nbre de mort =[ %.2f , %.2f ] \n intervalle de confiance de nbre de blesse =[ %.2f , %.2f ] \n intervalle de confiance de blesses graves =[ %.2f , %.2f ] \n intervalle de confiance de blesse leger =[ %.2f , %.2f ] " %((accmoy-1.96*(s1/sqrt(m))),(accmoy+1.96*(s1/sqrt(m))),(accmmoy-1.96*(s2/sqrt(m))),(accmmoy+1.96*(s2/sqrt(m))),(tue_moy-1.96*(s3/sqrt(m))),(tue_moy+1.96*(s3/sqrt(m))),(bmoy-1.96*(s4/sqrt(m))),(bmoy+1.96*(s4/sqrt(m))),(bgmoy-1.96*(s5/sqrt(m))),(bgmoy+1.96*(s5/sqrt(m))),(blmoy-1.96*(s6/sqrt(m))),(blmoy+1.96*(s6/sqrt(m))))
    messagebox.showinfo("resultat", result)
    
    
#fonction distribution
print("yess")
fenetre = Tk()
var_texte = StringVar()
var_texte1 = StringVar()
var_texte2 = StringVar()
var_texte3 = StringVar()
lab1 = Label(fenetre, text="entrez une annee de depart")
lab1.pack()
depart = Entry(fenetre, textvariable=var_texte, width=30)
depart.pack()

lab2 = Label(fenetre, text="entrez une annee de fin")
lab2.pack()
fin = Entry(fenetre, textvariable=var_texte1, width=30)
fin.pack()

button = Button(fenetre, text='calcul', command=calcul)
button.pack()
lab3 = Label(fenetre, text="taille de l'echantillon")
lab3.pack()
n = Entry(fenetre, textvariable=var_texte2, width=30)
n.pack()
lab4 = Label(fenetre, text="niveau de confiance alpha")
lab4.pack()
alpha = Entry(fenetre, textvariable=var_texte3, width=30)
alpha.pack()
estbut = Button(fenetre, text='estimer', command=estimer)
estbut.pack()

#----------------------------------------

    
fenetre.mainloop()