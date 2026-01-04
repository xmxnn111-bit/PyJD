from DrissionPage import ChromiumPage
import csv
import time

bp = ChromiumPage()

bp.get('https://item.jd.com/100054970380.html')

time.sleep(1)

bp.listen.start('client.action')

bp.ele('css:.all-btn').click()

f = open('data.csv', 'w', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['昵称', '日期', '评分', '产品', '评论'])
csv_writer.writeheader()

tanc = bp.ele('css:._rateListContainer_1ygkr_45')

for page in range(1,30):
    print(f'爬取第{page}页数据。。')
    resp = bp.listen.wait()
    json_data = resp.response.body
    data = json_data['result']['floors'][2]['data']

    for index in data:
        try:
            dit = {
                '昵称': index['commentInfo']['userNickName'],
                '日期': index['commentInfo']['commentDate'],
                '评分': index['commentInfo']['commentScore'],
                '产品': index['commentInfo']['productSpecifications'],
                '评论': index['commentInfo']['commentData']
            }
            csv_writer.writerow(dit)
            print(dit)
        except:
            pass
    tanc.scroll.to_bottom()
    tanc.scroll.to_bottom()