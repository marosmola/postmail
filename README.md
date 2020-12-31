# Postmail

Server application that handle sending emails from postmark for client side js applications.
Main usage for web formulars.

`POST https://postmail.bluelemons.sk/api/sendmail/`
```
{
	"token": "3d835b8f-716b-4b27-9ed0-3335fe8a5e5f",
	"subject": "subject",
	"message": "this is the message!"
}
```


Use django-cors-headers signals:

https://github.com/adamchainz/django-cors-headers#signals