import requests
from scrapy.selector import Selector
import pymysql

conn = pymysql.Connect(host='127.0.0.1', user='root', passwd='password', db='51auto', port=3306)
cursor = conn.cursor()


def crawl_ips():
    """
        爬取西刺免费 IP 代理
    Returns:
        None
    """
    url = 'http://www.xicidaili.com/nn/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    for i in range(1, 101):  # 获取 100 页的数据
        response = requests.get(url=url.format(i), headers=headers)
        # 使用 Scrapy 的 Selector 来提取数据
        selector = Selector(text=response.text)

        trs = selector.xpath('//table[@id="ip_list"]//tr')
        # trs = selector.css('#ip_list tr')

        ip_list = []
        for tr in trs[1:]:  # 去掉第一行表头
            ip = tr.xpath('./td[2]/text()').extract_first()
            port = tr.xpath('./td[3]/text()').extract_first()
            speed = tr.xpath('./td[7]/div/@title').extract_first().split('秒')[0]
            proxy_type = tr.xpath('./td[6]/text()').extract_first()

            ip_list.append((ip, port, proxy_type, speed))
        print(ip_list)

        for ip_info in ip_list:
            cursor.execute(
                """
                insert into proxy_ip(ip, port, proxy_type, speed)
                values('{0}', '{1}', '{2}', '{3}')
                """.format(ip_info[0], ip_info[1], ip_info[2], ip_info[3])
            )  # 注意因为数据库字段中这几个值都为 varchar 类型，所以 format 的时候 values 里面的值又要加引号
            conn.commit()


class GetIP(object):
    """
        获取 IP
    """

    def get_random_ip(self):
        """
            从数据库中随机获取一个 IP
        Returns:

        """
        random_sql = """select ip,port from 51auto.proxy_ip where proxy_type='HTTP' order by rand() limit 1"""
        cursor.execute(random_sql)
        ip , port = cursor.fetchone()
        judge_result = self.judge_ip(ip, port)
        if judge_result:
            return 'http://{0}:{1}'.format(ip, port)
        else:
            return self.get_random_ip()

    def judge_ip(self, ip, port):
        """
            判断 IP 是否可用
        """
        http_url = 'http://www.baidu.com'  # 访问百度首页来测试 IP 是否可用
        proxy_url = 'http://{0}:{1}'.format(ip, port)
        proxy_dict = {
            'http': http_url,
            # 'https': ''
        }
        try:
            response = requests.get(http_url, proxies=proxy_dict)
        except Exception as e:
            print('无效 IP')
            self.delete_ip(ip)
            return False
        else:
            code = response.status_code
            if 200 <= code < 300:
                print('可用 IP')
                return True
            else:
                print('无效 IP')
                self.delete_ip(ip)
                return False

    def delete_ip(self, ip):
        """
            删除数据库中无效 IP
        """
        delete_sql = """delete from proxy_ip where ip='{0}'""".format(ip)
        cursor.execute(delete_sql)
        conn.commit()
        return True


if __name__ == '__main__':
    # crawl_ips()
    get_ip = GetIP()
    print(get_ip.get_random_ip())
