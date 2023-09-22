from main.models import LottoDraw, Typing

def get_data_in_rows():
        draws=LottoDraw.objects.all()
        data = []
        dataplus=[]
        for draw in draws:
                row = [draw.id, draw.date]
                rowplus = [draw.id, draw.date]
                numbers = draw.typing_set.all().order_by("number")
                for number in numbers:
                        if number.is_plus==False:
                                row.append(number.number)
                        else:
                                rowplus.append(number.number)
                data.append(row)
                if len(rowplus)>2:
                        dataplus.append(rowplus)
        return data, dataplus

header = ['id', 'date', 'number1', 'number2', 'number3', 'number4', 'number5', 'number6']
data, dataplus = get_data_in_rows()