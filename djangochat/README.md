# Start Djangochat 
cd djangochat

# To Activate Virtual Env chatapp_env 
chatapp_env/Scripts/activate

cd djangochat

python manage.py runserver

# To Deactivate Virtual Env
deactivate


# To Create Super User
python manage.py createsuperuser 

# To Delete Super User
python manage.py shell
from django.contrib.auth.models import User
User.objects.get(username="admin", is_superuser=True).delete()

# To login as admin
Visit http://127.0.0.1:8000/admin in different browser

USERNAME: admin

Email: admin@chat.com	

Password: admin123

# To delete chat messages 
I have created delete_chat_messages.py in the directory room/management/commands

Just type below command to delete all room messages

python manage.py delete_chat_messages

# Author
This repository is created by Manan Jain.
