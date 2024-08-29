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
    question = models.ForeignKey(Question, related_name="options", on_delete=models.CASCADE)
    option_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.question}-{self.option_name}'
    

class CustomerFeedback(models.Model):
    question = models.ManyToManyField(Question)



class CustomerResponse(models.Model):
    feedback = models.ForeignKey(CustomerFeedback, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response_text = models.TextField(null=True, blank=True)
    selected_options = models.ManyToManyField(Options, blank=True)

