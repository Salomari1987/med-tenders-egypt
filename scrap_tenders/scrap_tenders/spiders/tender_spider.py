from scrapy import Spider, Request
from scrapy.selector import Selector

from scrap_tenders.items import StackItem

class StackSpider(Spider):
    name = "tender"
    start_urls = ['http://www.medicaltenders.com/search.php?off=00&inc=y&global=1&region_name[]=EG']

    def parse(self, response):
        """
        Parse the url response and get certain data from it
        """
        # Select <div class='cent'>...<fieldset>...<div class='cent'>...<table>..<tr>..</tr>..<tr></tr>

        CENT_SELECTOR = '.cent fieldset div.cent>table>tr'
        trs = Selector(response).css(CENT_SELECTOR)

        # Iterate over trs
        for tr in trs:
            # Check if tr contains tender data
            if 'Tender Category:' in tr.xpath('.//b/text()').extract():
                item = StackItem()

                # Get all text inside the tender,
                # the field names are within ../tr/td/b
                # while field value are within ../tr/td
                xpression = './/tr/td/table/tr/td/text()'
                data = tr.xpath(xpression).extract()

                # TODO: move this to pipelines.py
                # Cleans data
                data = '   '.join(data).replace('\n', '').replace('\t', '').strip().split('   ')

                item['Tender_Notice_Type'] = data[0].strip()
                item['Country'] = data[1].strip()
                item['Category'] = data[2].strip()
                item['Description'] = data[3].strip()
                item['Deadline'] = data[4].strip()
                item['Ref'] = data[5].strip()

                yield item

        # Select next page if it exists
        NEXT_PAGE_SELECTOR = '//a[b/text()="Next Page"]/@href'
        next_page = response.xpath(NEXT_PAGE_SELECTOR).extract_first()

        if next_page:
            yield Request(
                response.urljoin(next_page),
                callback=self.parse
            )
