from django.http import HttpRequest, HttpResponse


def login_view(request: HttpRequest, pk: int) -> HttpResponse:
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
<<<<<<< HEAD

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
=======
    query_params = request.GET
>>>>>>> b68c2a648268ecfa908945752c11f94a7e145807

    # validation
    if query_params.get('num1') is None:
        return HttpResponse('num1 is required.')
    if query_params.get('num2') is None:
        return HttpResponse('num2 is required.')
    if query_params.get('op') not in ['add', 'mul', 'sub', 'div']:
        return HttpResponse("op should be ('add', 'mul', 'sub', 'div').")

    # calculate
    num1 = int(query_params.get('num1'))
    num2 = int(query_params.get('num2'))
    op = query_params.get('op')
    
    # if op == 'add':
    #     result = f'{num1}+{num2}={num1 + num2}'
    # elif op == 'sub':
    #     result = f'{num1}-{num2}={num1 - num2}'
    # elif op == 'mul':
    #     result = f'{num1}*{num2}={num1 * num2}'
    # elif op == 'div':
    #     result = f'{num1}/{num2}={num1 / num2}'
    # else:
    #     result = 'operator not found.'

    match op:
        case 'add':
            result = f'{num1}+{num2}={num1 + num2}'
        case 'sub':
            result = f'{num1}-{num2}={num1 - num2}'
        case 'mul':
            result = f'{num1}*{num2}={num1 * num2}'
        case 'div':
            result = f'{num1}/{num2}={round(num1 / num2, 2)}'
        case _:
            result = 'operator not found.'
    
    return HttpResponse(f'<h1>result: {result}<h1>') # 'result: 3+7=10
