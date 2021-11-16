from blog2_project.celery import app

from django.core.mail import send_mail


@app.task
def send_email_task(blog_creator_id):
    from users.models import CustomUser

    blog_creator = CustomUser.objects.get(id=blog_creator_id)

    subject = f'Hi author  {blog_creator}  have posted a blog go check it out'
    message = 'This is a test email sent asynchronously with Celery.'
    # users = CustomUSer.objects.filter(is_active=True, email_opt_in=True)
    # reciepient = followers.follower.all

    return send_mail(
        subject,
        message,
        'talha.yousuf@patsysjournal.com',
        ['kiceso8903@hypteo.com'],
        fail_silently=False
    )
