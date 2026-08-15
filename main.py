

import  streamlit as st
import string
import random






isim= st.text_input("isim giriniz")
soyisim= st.text_input("soyisim giriniz")
domain= st.selectbox("domain seçiniz",["finiscode.com.tr","finis.code","finisfile.com.tr"])

basharf=isim[0]
email=basharf+"."+soyisim+"@"+domain

email=email.lower()

email=email.replace("ç","c")
email=email.replace("ü","u")
email=email.replace("ö","o")
email=email.replace("ş","s")
email=email.replace("ı","i")
email=email.replace("ğ","g")
email=email.replace(" ","")


bhsec=random.choices(string.ascii_uppercase,k=2)
khsec=random.choices(string.ascii_lowercase,k=2)
dgsec=random.choices(string.digits,k=2)
sysec=random.choices(string.punctuation,k=2)

sifre=bhsec+khsec+dgsec+sysec
random.shuffle(sifre)

sifre="".join(sifre)

st.write(email)
st.write(sifre)
st.button("Yenile")



#pip install streamlit
#streamlit run main.py

















