from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1> input, respone dari url </h1>')


def link(request, slug):
    page = f'<h1>{slug}</h1>'

    return HttpResponse(page)


def angka(request, input):
    heading = '<h1> page angka </h1>'

    return HttpResponse(f'{heading} {input}')


def tanggal(request, **input):
    print(input)
    tahun = input['tahun']
    bulan = input['tanggal']
    hari = input['hari']
    dataTanggal = f'{tahun} \{bulan}\{hari}'
    heading = '<h1> page tanggal </h1>'
    return HttpResponse(heading + dataTanggal)

# def tanggal(request, tahun, bulan, hari):
#     heading = '<h1> page tanggal </h1>'
#     tahun = 'tahun :' + tahun
#     tanggal = 'tanggal :' + bulan
#     hari = 'hari :' + hari
#     str = heading + tahun + '<br>' + tanggal + '<br>' + hari
#     return HttpResponse(str)
