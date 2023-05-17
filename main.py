import  requests
from bs4 import BeautifulSoup
# baseUrl = requests.get('https://jobtest.vn/hrblog/tin-tuc')
#
# blogLinks = [];
#
#
# # DEMO CRAWL JOBTEST BLOG
# for i in range(14):
#     if i > 1:
#         res = requests.get(baseUrl)
#         soup = BeautifulSoup(res.content, "html.parser")
#         links = soup.select('.td-main-content>.td-ss-main-content >.td-block-row >.td-block-span6 > .td_module_wrap > h3>a ')
#         for link in links:
#             print('page_' + str(i + 1) + ' ' + link['href'])
#     res = requests.get(baseUrl + 'page/' + str(i))
#     soup = BeautifulSoup(res.content, "html.parser")
#     links = soup.select('.td-main-content>.td-ss-main-content >.td-block-row >.td-block-span6 > .td_module_wrap > h3>a ')
#     for link in links:
#         print('page_' + str(i + 1) + ' ' + link['href'])


# name_test = soup.select('list-service > .service-item > .bottom-content > a')




#CRAWL IMAGES LOL
baseUrl = 'https://www.leagueoflegends.com/vi-vn/champions/?_gl=1*1d017vv*_ga*NDkyMzE0MzI2LjE2ODQzMTMwNjE.*_ga_FXBJE5DEDD*MTY4NDMxMzA2MS4xLjAuMTY4NDMxMzA2MS42MC4wLjA.&_ga=2.115065028.212337929.1684313062-492314326.1684313061'
res = requests.get(baseUrl)
soup = BeautifulSoup(res.content, "html.parser")
img_champions = soup.select('.style__Body-sc-138hc9a-2 > .style__Wrapper-sc-13btjky-0 > .style__List-sc-13btjky-2 > a > .style__ImageContainer-n3ovyt-1 > img')
index = 0
for img_champ in img_champions:
    index += 1
    print({
            '_id': str(index),
            'img':  img_champ['src']
        })



