from signal import pthread_kill
from browser import document, console, alert

input = document['suhu']
button = document['btn']
output = document['output']
select = document['jenis']

def getNum(x):
    temp = x
    try:
        temp = int(x)
    except ValueError:
        temp = float(x)
    finally:
        if temp != '' and type(temp) is str:
            alert('Harap masukkan angka')
            temp = ''
            input.value = temp
            return temp
        else:
            return temp

def formula(x, y):
    match x:
        case 'celcius':
            fahrenheit = y * 1.8 + 32
            kelvin = y + 273
            reamur = 0.8 * y
            return
        case 'fahrenheit':
            celcius = 5/9 * (y - 32)
            kelvin = 5/9 * (y - 32) + 273
            reamur = 4/9 * (y - 32)
            print("Fahrenheit = ", celcius)
            print("Kelvin = ", kelvin)
            print("Reamur = ", reamur)
        case _:        
            return 0


def main(ev):
    num = getNum(input.value)
    result = formula(select.value, num)
    output.textContent = str(result)

def keyEnter(ev):
    console.log(f"{ev.code}")
    traceKey = f"{ev.code}"
    if traceKey == 'Enter':
        main(0)

button.bind('click', main)
input.bind("keypress", keyEnter)
