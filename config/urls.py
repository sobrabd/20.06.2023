"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("dogs.urls")),
]

def delete_vacancy(self) -> None:
    """
    Функция для удаления вакансий
    """
    if not self.vacancies:
        raise IndexError
    
    vacancy_id = input("Введите идентификатор вакансии для удаления: ").strip()

        
    try:
        if vacancy_id.isdigit() is False:
            raise ValueError("Идентификатор вакансии должен состоять только из цифр.")
       
        deleted_vacancies = []
        filtered_vacancies = filter(lambda vacancy: int(vacancy.id) == int(vacancy_id), self.vacancies)
        for vacancy in filtered_vacancies:
            deleted_vacancies.append(vacancy)
            self.path.remove_vacancy(vacancy_id=vacancy_id)
            print(f"Вакансия успешно удалена из загруженных")

        if len(deleted_vacancies) > 0:
            self.vacancies = [v for v in self.vacancies if v not in deleted_vacancies]
        else:
            raise ValueError("Вакансия не найдена. Введите корректный идентификатор вакансии.")
        
    except ValueError as error:
        print(str(error))
    


