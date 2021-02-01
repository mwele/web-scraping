import builtwith
import whois
print(builtwith.parse("https://b-ok.africa/book/3524989/5646dd?dsource=recommend"))
domain=whois.query("https://pypi.org/project/whois/")
print(domain.name)