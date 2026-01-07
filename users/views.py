from django.http import HttpRequest, HttpResponse


def login_view(request: HttpRequest) -> HttpResponse:
    print(request.path)
    print(request.method)

    if request.method == 'GET':
        pass

    return HttpResponse('login page')


def orders_view(request: HttpRequest) -> HttpResponse:
    query_params = request.GET

    min_value = query_params.get('min')
    max_value = query_params.get('max')
    
    return HttpResponse(f'orders page: [{min_value}, {max_value}]')


def calculators_view(request: HttpRequest) -> HttpResponse:

    # ?num1=3&num2=7&op=+

    query_params = request.GET

    num1_value = query_params.get('num1')
    num2_value = query_params.get('num2')
    op_value = query_params.get('op')
    
    num1 = float(num1)
    num2 = float(num2)

    if op == "add":
        result = num1 + num2
    elif op == "sub":
        result = num1 - num2
    elif op == "mul":
        result = num1 * num2
    elif op == "div":
        if num2 == 0:
            return HttpResponse("0 ga bo'lish mumkin emas!")
        result = num1 / num2
    else: 
        return HttpResponse("No'to'g'ri amal")


    return HttpResponse(f'result: [{result}]') # 'result: 3+7=10

