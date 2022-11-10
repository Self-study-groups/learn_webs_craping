import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://ltmpt.ac.id/?mid=22',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
       for i in range (1, 175):
       # for sekolah in response.css('.table > tbody:nth-child(2)'):
            yield {
                'Nomer' : response.css('.col-md-10 > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child('+ str(i) +') > td:nth-child(1)::text').extract(),
                'Kode' : response.css('.col-md-10 > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child('+ str(i) +') > td:nth-child(2)::text').extract(),
                'Nama' : response.css('.col-md-10 > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child('+ str(i) +') > td:nth-child(3)::text').extract(),
                'Alamat' : response.css('.col-md-10 > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child('+ str(i) +') > td:nth-child(4)::text').extract(),
                'Kode Pos' : response.css('.col-md-10 > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child('+ str(i) +') > td:nth-child(5)::text').extract(),
                'No Telpon' : response.css('.col-md-10 > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child('+ str(i) +') > td:nth-child(6)::text').extract(),
                'Email' : response.css('.col-md-10 > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child('+ str(i) +') > td:nth-child(7)::text').extract(),

            }
# Nomer
# .col-md-10 > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1)
# Kode
# .col-md-10 > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2)
# .col-md-10 > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(3)