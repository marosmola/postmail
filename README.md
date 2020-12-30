# Postmail

Server application that handle sending emails from postmark for client side js applications.

`POST https://bluelemons.sk/sendmail/`
```
{
	"token": "3d835b8f-716b-4b27-9ed0-3335fe8a5e5f",
	"receiver": "ssmolenm@gmail.com",
	"subject": "subject",
	"message": "this is the message!"
}
```



Use django-cors-headers signals:

https://github.com/adamchainz/django-cors-headers#signals