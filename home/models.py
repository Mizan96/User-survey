from django.db import models

# Create your models here.

class Question(models.Model):
    QUSTION_CHOICE = (
        ('Text','Text'),
        ('BigText', 'BigText'),
        ('Radio', 'Radio'),
        ('Checkbox', 'Checkbox')
    )
    question = models.CharField(max_length=100)
    question_type = models.CharField(choices=QUSTION_CHOICE, max_length=100)

    def __str__(self) -> str:
        return f'{self.question} {self.question_type}'
    
class Options(models.Model):
    question = models.ForeignKey(Question, verbose_name="Question Name", on_delete=models.CASCADE)
    Options = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.question.question} {self.Options}'
    

class CustomerFeedback(models.Model):
    question = models.ManyToManyField(Question)


class CustomerResponse(models.Model):
    feedback = models.ForeignKey(CustomerFeedback, on_delete=models.CASCADE)
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response_text = models.TextField(null=True, blank=True)
    selected_options = models.ManyToManyField(Options, blank=True)