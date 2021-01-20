
from CCCD_class import CCCD

def classify(results):
    for item in results:
        if 'CĂN CƯỚC CÔNG DÂN' in item:
            return classify_cccd(results)


def classify_cccd(results):
    id = ''
    name = ''
    birth = ''
    nationality = ''
    sex = ''
    hometown = ''
    address = ''

    for i in range (len(results)):
        if results[i].isdigit():
            id = results[i]
        if 'Họ và tên:' in results[i]:
            name = results[i+1] 
        if 'Ngày, tháng, năm sinh' in results[i]:
            birth = results[i][22:]
        if 'Quốc tịch' in results[i]:
            nationality = results[i][11:]
        if 'Giới tính' in results[i] or 'GIỚI TÍNH' in results[i]:
            sex = results[i][11:]
        if 'Quê quán' in results[i]:
            hometown = results[i][10:]
            if 'Nơi thường trú:' not in results[i+1]:
                hometown += " "+ results[i+1]
        if 'Nơi thường trù' in results[i] or 'Nơi thường trú' in results[i]:
            address = results[i][16:]
            if 'Có giá trị đến' not in results[i+1]:
                address += " "+results[i+1]
    
    cccd = CCCD(id,name,birth,nationality,sex,hometown,address)
    return cccd