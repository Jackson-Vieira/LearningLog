from django.contrib import admin
from learning_logs.models import Topic, Entry

# Register your models here.
admin.site.register(Topic) # Registrar o modelo  Topic do banco de dados
admin.site.register(Entry) # "         "  "      Entry "   "     "  " 
