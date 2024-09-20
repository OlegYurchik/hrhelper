from django.http import HttpResponse
from django.shortcuts import redirect


from .models import Vacancy


def vacancies_router(request):
    if request.method == "POST":
        return create_vacancy(request=request)
    if request.method == "GET":
        return get_vacancies(request=request)


def get_vacancies(request):
    vacancies = Vacancy.objects.all()

    response_text = "\n\n".join(
        (
            f"Company: {vacancy.company}\n"
            f"Name: {vacancy.name}\n"
            f"Description: {vacancy.description}\n"
        )
        for vacancy in vacancies
    )

    return HttpResponse(response_text)


def create_vacancy(request):
    Vacancy.objects.create(
        company=request.POST["company"],
        name=request.POST["name"],
        description=request.POST["description"],
    )
    return redirect("/hrhelper/vacancies")
