import base64


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher

def decrypt_data(encrypt_msg):
    
    private_key = RSA.importKey('''-----BEGIN RSA PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDBg/4WMCs6jSaw
fqURyX2OvzZ1O8GTMw+C24ucUoQIv7zrLthCdY0AMUD5q+QtVpMkrF/m+RXC+ZO/
RV+mzaBkbwHJoSr8lXjLSZ689J78mm3xcX/W0vpJ8Td+3/RRR9oLuR4mnkss8b2I
LsQiVGYfY3ailJUPTfK3yUIAAyhKsBGTiZ4KsJTWDJ2UJvYo0w81s9r1iQba8NAR
nEdKOhiHn/TUXMoQNS254bpHUJdJvb18l9FWWnLzbqOICjwuNvityhtQSw6ua/TV
bGTz84VMjx+c2bANECq/Tq6JeB4AHSpUy2+S0GbSCXRpNDL6M962uVuNF/+/CLOA
TLb+gXxtAgMBAAECggEAOy0q4Qwf3ArX/vbrcZIFJEbS12zLmEDwCFssyUPufmJr
2ht8JG6gDKQDM5Zd84NbAcb4mMAo6HO7u6zyQCb3Wl8b09XGOHFY/AlqUmwXxjVP
U5satc3UnhH2n4TKyKRJSHZ2gua7JGZUSDXM4paemBCpcbQwFPsIMy2HUkuk4ZmG
w1iIk7dvLlerLGzqELJluu2oSJQCZUNpyNE75iz4qBXRdG6ptaRf1gEbEPRsgqGz
BMU5rMPitHrJBKcz3WTiOHpfLlZ7oqW/UcWFD3zaoxGQ6asmoFMyKcQsgsimK3v+
oWWo0k3oHlYUWFA5qtI+HkW/+PdiRKpQn9ZY67/8IQKBgQD8T3tDJcisHOyNvXxw
niF6kXD+jhs5JVXGFKDfQNxrYppJMMQYjMy6x1MTtamQDax1Zk5mVEqhZPbN+QJA
mF9Lq6BVkdNK8d9msV4C+hAg+Kb7oeLAqLlR0DNun23FIvw+I0zFSW1dDB2MLsiP
uxIQlwuFM7y/MfLXJ9phc4UDyQKBgQDEWGnrMl28bSlKbkpHCB0kueHd3rhGdO8q
r6y5K62UJUI/8Jhy6vBOIObAMUSMipxrHp/+Q8NcfhyCAyr59JbNcwZn9l7ODlxF
SQAG7+MvmTO/vcBs7Uohl4mjLhjlp7GSY2/LLgDXKQFlkpc/ay1kTIROdv/68it+
8QEv0hLdhQKBgAumV9in2/Ymd72rrB0/D+iq4n6+bP9ce/NjbHIieoryyJDskYFY
rvNI1MsqLiQanYXmLWSIK9H76XFlN/dnka7aw9Jvo0PomxoQwnh8t1XuZTdlKCUh
JT1j0Zwf/F+H2AG+e4L4evY64vpgBp6sUo81ijCiTOq/Ealhi7HINbIRAoGAcqJI
HNiIH7YAEIO5/CTBlyqrs3UQU5p79Ikip+3XZxIlztzytM10Rbkx3+4j3oYi8uur
b7Eyg3LhxAqDcfIahZLtn48ZJOb/ejg3utUd6DFjJERt72rPCDPIWSxVvuecZiKG
J7MRLI21Ug83HQC/PLrr2D/kDiiLuo6NKdVVzF0CgYArW8AKnjnoRbSOSCLdV3jt
b9Dv58z/YOJ9i+B0aUZ93t0iU4Rio8NbWaSnHgH85SVaoG4L6r7Ly9cLEDxyBMJk
Eqtr07EHZlG9qPO3HyeBNfcOz/OWP8o635kT7l/VAxZstLArzNZtgaCxPLgLT39J
39pykAfG/WCpBPXr3+chgw==
-----END RSA PRIVATE KEY-----''')
    cipher = PKCS1_cipher.new(private_key)
    back_text = cipher.decrypt(base64.b64decode(encrypt_msg), 0)
    return back_text.decode('utf-8')
def test():
    password = decrypt_data('Ggd1Lkzt9oaqwfs9i/paL/TBF5oh33aOKlaNlunpWD2olLbUrEBljram9G0Mui5zAq2gd2SzM5xMgbi0Diq20i8LYa0RVFhHDmtwTtVvcPiLawTBIn85UxmOkKkEnnlIztDDIHJSOdccj0xyaYVqz0v3Qi1ONUQxfeo2Lt4vjRfOq0TDP2tg1nFYfDQIUYhvYTR0LGB+sW499VTC/qGc1b9hP9R8mM49HDD2pRNdhyrJ7qoVP2rwKtrojq9RRaQJb7Q6N1nJzPWMIwZ0bPHG+IBZ2+6KlC9zRdSQUHppEEswIgI6geIgCq50Y1ZekmAIU2xHUrExBqlHiQmsOHS/nA==')
    print(password)

if __name__ == '__main__':
    test()