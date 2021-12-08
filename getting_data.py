from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
from xlwt import Workbook

STT = 0
wb = Workbook()
sheet1 = wb.add_sheet("crawl")
sheet1.write(0, 0, "STT")
sheet1.write(0, 1, "Tiêu Đề")
sheet1.write(0, 2, "Mô tả")
sheet1.write(0, 3, "Nội Dung")
sheet1.write(0, 4, "Ảnh Minh Họa")
sheet1.write(0, 5, "Thể Loại")

driver = webdriver.Chrome()
menu = ["thoi-su/", "tu-phap/", "quoc-te/", "kinh-te/", "tai-chinh/", "doanh-nhan/", "xa-hoi/", "moi-truong/", "giao-thong/", "do-thi/", "van-hoa/", "giai-tri/", "the-thao/", "suc-khoe/", "tu-van-sk/", "thuoc/", "phap-luat/", "tin-nong/", "phap-dinh/", "ho-so/", "dieu-tra/",
        "tieu-dung-va-du-luan/", "thi-truong-360/", "canh-bao/", "tieu-dung-thong-minh/", "xe-co/", "ban-doc/", "goc-nhin-ban-doc/", "tu-van-365/", "chinh-xach-moi/", "bat-dong-san/", "chinh-sach/", "tin-dat-lanh/", "doanh-nghiep/", "thi-truong/", "phong-thuy/", "khong-gian-xanh/", "nha-dep/", "san-giao-dich/", "the-gioi-cong-nghe/", "chuyen-doi-so/", "vien-thong/", "nhip-song-hom-nay/", "cau-chuyen-phap-luat/", "toa-an/", "dao-va-doi/",  "4-phuong/", "kham-pha/", "ho-so-tu-lieu/", "su-kien-ban-luan/", "song-xanh/"]

n = 0
for i in range(len(menu)):
    url = ("https://baophapluat.vn/" + menu[i])
    driver.get(url)
    for j in range(10):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

        watch_more_bnt = driver.find_element_by_class_name("text-center")

        try:
            watch_more_bnt.click()

        except:
            pass
    page_source = BeautifulSoup(driver.page_source)
    # print(page_source)
    titles = page_source.findAll("article", class_="story story--timeline")
#     links = [link.find("a").attrs["href"] for link in titles]
    links = []
    for link in titles:
        a = link.find("a").attrs["href"]
        if a not in links:
            links.append(a)
#     n = n + len(links)
#     print(n)

        # getting data
    for link in links:
        STT = STT + 1
        driver.get(url + link)
        page_source = BeautifulSoup(driver.page_source, "html.parser")

        # getting title
        try:
            title = page_source.find(
                "h1", class_="article__title cms-title").text
        except:
            title = "NULL"
        # getting abstract
        try:
            abstract = page_source.find(
                "div", class_="article__summary cms-desc").text
        except:
            abstract = "NULL"
        body = page_source.find("div", class_="article__body cms-body")
        # getting content
        try:
            content = (
                body.findChildren("p", recursive=False)[0].text
                + body.findChildren("p", recursive=False)[1].text
            )
        except:
            content = "NULL"

        # getting image
        try:
            image = body.find("img").attrs["data-src"]
        except:
            image = "NULL"
        # getting category
        try:
            category = page_source.find("h1", class_="cate").text
        except:
            category = "NULL"

        sheet1.write(int(STT), 0, STT)
        sheet1.write(int(STT), 1, title)
        sheet1.write(int(STT), 2, abstract)
        sheet1.write(int(STT), 3, content)
        sheet1.write(int(STT), 4, image)
        sheet1.write(int(STT), 5, category)

        wb.save("Data.xlsx")
        print("Tiêu đề: " + title)
        print("Mô tả: " + abstract)
        print("Nội dung: " + content)
        print("Ảnh minh họa: " + image)
        print("\n================================\n")
        print(STT)
