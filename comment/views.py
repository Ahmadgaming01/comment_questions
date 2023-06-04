from django.shortcuts import render ,redirect
from .models import Question,Answer
from .forms import QuestionsForm
# Create your views here.

def Questions_list(request):
    questions = Question.objects.all()
    return render(request , 'comment/questions.html' , {'fragen':questions})

def Questions_details(request,question_id):
    data = Question.objects.get(id=question_id)
    return render(request , 'comment/details.html' , {'info':data})

def Questions_edit(request , question_id):
    data = Question.objects.get(id=question_id)
    if request.method == 'POST':
        form = QuestionsForm(request.POST , instance=data)
        if form.is_valid():
            form.save()
            return redirect('/blog/')
    else:
        form = QuestionsForm(instance=data)
        return render(request , 'comment/edit.html' , {'form':form})
    
def delete_question(request , question_id):
    data = Question.objects.get(id=question_id)
    data.delete()
    return redirect('/blog/')

