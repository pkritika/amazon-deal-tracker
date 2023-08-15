import requests
import smtplib
r=requests.get("""https://www.amazon.com/Sony-WH-1000XM5-Headphones-Hands-Free-
WH1000XM5/dp/B0BXYCS74H/?_encoding=UTF8&pd_rd_w=oc90v&content-id=amzn1.sym.5f7e0a27-
49c0-47d3-80b2-fd9271d863ca%3Aamzn1.symc.e5c80209-769f-4ade-a325-2eaec14b8e0e&pf_rd_p=5f7e0a27-
49c0-47d3-80b2-fd9271d863ca&pf_rd_r=714XRJ1RBCAQAY50A6RX&pd_rd_wg=BbS7j&pd_rd_r=7752e11b-d77f-4a43-
857e-0ca76868ea44&ref_
=pd_gw_ci_mcx_mr_hp_atf_m""", headers = { 'Accept-Language' : "en-US,en;q=0.9",'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15"})

from bs4 import BeautifulSoup
contents = BeautifulSoup(r.text,"html.parser")
# print(contents.prettify())
price = contents.find(class_="a-price-whole").get_text().strip(".")

print(price)
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    result = connection.login("kritikapant2003@gmail.com", "Kp@20031008")
    connection.sendmail(
        from_addr="kritikapant2003@gmail.com",
        to_addrs="biraj.dahal@bison.howard.edu",
        msg=f"Subject:Amazon Price Alert!\nThe price of the headphone has is {price}".encode("utf-8")
    )

    







