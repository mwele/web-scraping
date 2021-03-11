from xtend_built_in import Contact

class MailSender:
	def send_mail(self, message):
		print(message + '  ' + self.email)
	# Add e-mail logic he
class EmailableContact(Contact,MailSender):
	pass

e=EmailableContact("john ","john@gmail.com")
print(e.send_mail("sending"))