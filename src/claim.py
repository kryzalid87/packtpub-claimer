import scrapy

import os
import smtplib
from loginform import fill_login_form


class PaktPubClaimer(scrapy.Spider):
    name = 'packtpub-claimer'

    url = 'https://www.packtpub.com/packt/offers/free-learning'

    login_email = os.environ['PP_USER']
    login_password = os.environ['PP_PASS']

    def start_requests(self):
        yield scrapy.Request(self.url, self.parse_login, dont_filter=True)

    def parse_login(self, response):
        data, url, method = fill_login_form(response.url, response.body,
                                            self.login_email, self.login_password)

        return scrapy.FormRequest(url, formdata=dict(data),
                           method=method, callback=self.start_crawl, dont_filter=True)

    def start_crawl(self, response):
            yield scrapy.Request(self.url)
    
    def unwanted_book(self, book_title):
        with open("filter.txt", "r") as file:
            for line in file:
                 if(line.replace('\n', ' ').replace('\r', '') in book_title):
                    print "\nOMMITED BOOK: " + line + "\n"
                    return True
        return False
	
	
    def parse(self, response):
        TITLE_DIV_SELECTOR = '.dotd-title'

        for brickset in response.css(TITLE_DIV_SELECTOR):
            TITLE_SELECTOR = 'h2 ::text'
            yield {
                'name': brickset.css(TITLE_SELECTOR).extract_first().replace("\t", "").replace("\n", ""),
            }
            book_title = brickset.css(TITLE_SELECTOR).extract_first().replace("\t", "").replace("\n", "")
            if(not self.unwanted_book(book_title)):
                with open("claimed.txt", "a") as claim_file:
                        claim_file.write(book_title + "\n");
                BOOK_CLAIM_SELECTOR = '.free-ebook a ::attr(href)'
                next_page = response.css(BOOK_CLAIM_SELECTOR).extract_first()
                if next_page:
                    yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                    )
