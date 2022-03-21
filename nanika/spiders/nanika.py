import scrapy
class NanikaSpider(scrapy.Spider):
    name = 'nanika'

    def start_requests(self):#self=このclass
        url='https://gamewith.jp/kuronekowiz/'

        yield scrapy.Request(url=url, callback=self.kansu)

    def kansu(self,response):
        res = response.xpath("/html/body/div[3]/div[2]/ul/li[4]/a").get()
        # txt = open("./test.html", "a", encoding="utf-8")
        # body = str(response.body)
        # txt.write(body)
        print(res)
