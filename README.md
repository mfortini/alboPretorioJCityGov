# alboPretorioJCityGov
Scraper per albi pretori creati con software J-City Gov che invia i nuovi elementi su twitter e su un canale Telegram

## Dipendenze

* scrapy http://scrapy.org/
* tweepy http://www.tweepy.org/
* python-telegram-bot https://pypi.python.org/pypi/python-telegram-bot
* 
## Come partire

* Ottenere le chiavi di twitter. Se può essere utile utilizzare il file `authuser/getaccesstoken.py` per dare l'accesso alla propria app a un terzo profilo twitter
* Nominare il bot Telegram amministratore di un canale
* Modificare `alboPretorio.cfg.sample` con le proprie impostazioni e rinominarlo in `alboPretorio.cfg`
* Verificare il funzionamento con `sh scrape.sh`
* Inserire l'invocazione dello scraper per esempio come cronjob
