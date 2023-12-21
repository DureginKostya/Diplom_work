from selenium.webdriver.common.by import By


class BackCallPageLocators:
    LOCATOR_TITLE_LEAVE_CONTACTS = (By.XPATH, '/html/body/div[2]/h2')
    LOCATOR_SUBTITLE_LEAVE_CONTACTS = (By.XPATH, '/html/body/div[2]/div/p')
    LOCATOR_FIELD_NAME = (By.XPATH, '/html/body/div[2]/div/form/div[1]/input')
    LOCATOR_FIELD_PHONE = (By.XPATH, '/html/body/div[2]/div/form/div[2]/input')
    LOCATOR_BUTTON_SELL = (By.XPATH, '/html/body/div[2]/div/form/button')
    LOCATOR_TITLE_POLICY = (By.XPATH, '/html/body/div[2]/div/form/p')
    LOCATOR_BUTTON_POLICY = (By.XPATH, '/html/body/div[2]/div/form/p/a')
    LOCATOR_TITLE_POLICY_PAGE = (By.XPATH, '//*[@id="modal-privacy-policy"]/h2')
    LOCATOR_TITLE_THANK_YOU_PAGE = (By.XPATH, '//*[@id="modal-success"]/h2')


class ChooseUsPageLocators:
    LOCATOR_ICON_BEST_PRICE = (By.XPATH, '/html/body/main/section[2]/div[2]/div[2]/div[1]/div')
    LOCATOR_ICON_FREE_SUPPORT = (By.XPATH, '/html/body/main/section[2]/div[2]/div[2]/div[2]/div')
    LOCATOR_ICON_ALL_MONEY = (By.XPATH, '/html/body/main/section[2]/div[2]/div[2]/div[3]/div')
    LOCATOR_TITLE = (By.XPATH, '/html/body/main/section[2]/div[2]/div[1]/h2')
    LOCATOR_EXPLANATION = (By.XPATH, '/html/body/main/section[2]/div[2]/div[1]/p')
    LOCATOR_TITLE_BEST_PRICE = (By.XPATH, '/html/body/main/section[2]/div[2]/div[2]/div[1]/h3')
    LOCATOR_TITLE_FREE_SUPPORT = (By.XPATH, '/html/body/main/section[2]/div[2]/div[2]/div[2]/h3')
    LOCATOR_TITLE_ALL_MONEY = (By.XPATH, '/html/body/main/section[2]/div[2]/div[2]/div[3]/h3')
    LOCATOR_DESCRIPTION_BEST_PRICE = (By.XPATH, '/html/body/main/section[2]/div[2]/div[2]/div[1]/p')
    LOCATOR_DESCRIPTION_FREE_SUPPORT = (By.XPATH, '/html/body/main/section[2]/div[2]/div[2]/div[2]/p')
    LOCATOR_DESCRIPTION_ALL_MONEY = (By.XPATH, '/html/body/main/section[2]/div[2]/div[2]/div[3]/p')


class DesiredAmountPageLocators:
    LOCATOR_ICON_NOTE = (By.XPATH, '/html/body/main/section[6]/div[2]/div/div[2]/div')
    LOCATOR_TITLE = (By.XPATH, '/html/body/main/section[6]/div[2]/h2')
    LOCATOR_QUESTION_1 = (By.XPATH, '/html/body/main/section[6]/div[2]/div/div[1]/div[1]/h3')
    LOCATOR_ANSWER_1 = (By.XPATH, '/html/body/main/section[6]/div[2]/div/div[1]/div[1]/p')
    LOCATOR_QUESTION_2 = (By.XPATH, '/html/body/main/section[6]/div[2]/div/div[1]/div[2]/h3')
    LOCATOR_ANSWER_2 = (By.XPATH, '/html/body/main/section[6]/div[2]/div/div[1]/div[2]/p')
    LOCATOR_NOTE = (By.XPATH, '/html/body/main/section[6]/div[2]/div/div[2]/p')
    LOCATOR_TITLE_FIELD_PHONE = (By.XPATH, '/html/body/main/section[7]/div[2]/h2')
    LOCATOR_FIELD_PHONE = (By.XPATH, '/html/body/main/section[7]/div[2]/div/form/div/div/input')
    LOCATOR_BUTTON_SELL = (By.XPATH, '/html/body/main/section[7]/div[2]/div/form/div/button')
    LOCATOR_TITLE_POLICY = (By.XPATH, '/html/body/main/section[7]/div[2]/div/form/p')
    LOCATOR_BUTTON_POLICY = (By.XPATH, '/html/body/main/section[7]/div[2]/div/form/p/a')
    LOCATOR_FIELD_PHONE_SIZE = (By.XPATH, '/html/body/main/section[7]/div[2]/div/form/div')
    LOCATOR_TITLE_POLICY_PAGE = (By.XPATH, '//*[@id="modal-privacy-policy"]/h2')
    LOCATOR_TITLE_THANK_YOU_PAGE = (By.XPATH, '//*[@id="modal-success"]/h2')
    LOCATOR_NAVIGATION_PAGE = (By.XPATH, '/html/body/main/section[6]/div[2]/div/div[3]/span')


class FooterPageLocators:
    LOCATOR_BUTTON_RANSOM = (By.XPATH, '//*[@id="menu-menu-1"]/li[1]/a')
    LOCATOR_BUTTON_QUESTIONS_ANSWERS = (By.XPATH, '//*[@id="menu-menu-1"]/li[2]/a')
    LOCATOR_BUTTON_REVIEWS = (By.XPATH, '//*[@id="menu-menu-1"]/li[3]/a')
    LOCATOR_BUTTON_CALL = (By.XPATH, '/html/body/footer/section/div/div[1]/div[2]/div/a')
    LOCATOR_BUTTON_CALL_BACK = (By.XPATH, '/html/body/footer/section/div/div[1]/div[2]/button')
    LOCATOR_REGISTERED_SYMBOL = (By.XPATH, '/html/body/footer/section/div/div[2]/span')
    LOCATOR_CREATE_LANDING = (By.XPATH, '/html/body/footer/section/div/div[2]/div/div[1]/a')
    LOCATOR_POLICY = (By.XPATH, '/html/body/footer/section/div/div[2]/div/div[2]/a')
    LOCATOR_VALIDATON_CREATE_LANDING = (By.XPATH, '/html/body/main/h1/a')
    LOCATOR_TITLE_POLICY_PAGE = (By.XPATH, '//*[@id="modal-privacy-policy"]/h2')
    LOCATOR_FAVICON = (By.XPATH, '/html/body/footer/section/div/div[1]/div[1]')


class FormaDataCarLocators:
    LOCATOR_TITLE = (By.XPATH, '//*[@id="form-auto"]/h2')
    LOCATOR_SUBTITLE = (By.XPATH, '//*[@id="form-auto"]/span')
    LOCATOR_FIELD_BRAND = (By.XPATH, '//*[@id="form-auto"]/div[1]/div[1]/input')
    LOCATOR_FIELD_YEAR = (By.XPATH, '//*[@id="form-auto"]/div[1]/div[2]/input')
    LOCATOR_FIELD_PHONE = (By.XPATH, '//*[@id="form-auto"]/div[3]/div/input')
    LOCATOR_BUTTON_SELL = (By.XPATH, '//*[@id="form-auto"]/div[3]/button')
    LOCATOR_TITLE_POLICY = (By.XPATH, '//*[@id="form-auto"]/p')
    LOCATOR_BUTTON_POLICY = (By.XPATH, '//*[@id="form-auto"]/p/a')
    LOCATOR_CHECKBOX_DTP = (By.XPATH, '//*[@id="auto-dtp"]')
    LOCATOR_TITLE_CHECKBOX_DTP = (By.XPATH, '//*[@id="form-auto"]/div[2]/div[1]/label')
    LOCATOR_CHECKBOX_BROKEN = (By.XPATH, '//*[@id="auto-broken"]')
    LOCATOR_TITLE_CHECKBOX_BROKEN = (By.XPATH, '//*[@id="form-auto"]/div[2]/div[2]/label')
    LOCATOR_CHECKBOX_CREDIT = (By.XPATH, '//*[@id="auto-credit"]')
    LOCATOR_TITLE_CHECKBOX_CREDIT = (By.XPATH, '//*[@id="form-auto"]/div[2]/div[3]/label')
    LOCATOR_CHECKBOX_BAN = (By.XPATH, '//*[@id="auto-ban"]')
    LOCATOR_TITLE_CHECKBOX_BAN = (By.XPATH, '//*[@id="form-auto"]/div[2]/div[4]/label')
    LOCATOR_TITLE_POLICY_PAGE = (By.XPATH, '//*[@id="modal-privacy-policy"]/h2')
    LOCATOR_TITLE_THANK_YOU_PAGE = (By.XPATH, '//*[@id="modal-success"]/h2')


class HamburgerMenuPageLocators:
    LOCATOR_BUTTON_HAMBURGER_MENU = (By.XPATH, '//*[@id="menu-btn"]')
    LOCATOR_BUTTON_HAMBURGER_MENU_CLOSE = (By.XPATH, '//*[@id="menu-btn"]/div[2]')
    LOCATOR_BUTTON_CALL_BACK = (By.XPATH, '/html/body/header/section/div/div[2]/button')


class HeaderPageLocators:
    LOCATOR_BUTTON_RANSOM = (By.XPATH, '//*[@id="menu-item-12"]/a')
    LOCATOR_BUTTON_QUESTIONS_ANSWERS = (By.XPATH, '//*[@id="menu-item-13"]/a')
    LOCATOR_BUTTON_REVIEWS = (By.XPATH, '// *[ @ id = "menu-item-14"] / a')
    LOCATOR_BUTTON_CALL = (By.XPATH, '/ html / body / header / section / div / div[3] / a')
    LOCATOR_BUTTON_CALL_BACK = (By.XPATH, '/ html / body / header / section / div / div[3] / button')
    LOCATOR_FAVICON = (By.XPATH, '/html/body/header/section/div/div[1]')


class KartekaOrOtherPageLocators:
    LOCATOR_ICON_SELLING_KARTEKA = (By.XPATH, '/html/body/main/section[5]/div[2]/div/div[1]/div/div')
    LOCATOR_ICON_SELLING_OTHER = (By.XPATH, '/html/body/main/section[5]/div[2]/div/div[2]/div/div')
    LOCATOR_TITLE = (By.XPATH, '/html/body/main/section[5]/div[2]/h2')
    LOCATOR_TITLE_SELLING_KARTEKA = (By.XPATH, '/html/body/main/section[5]/div[2]/div/div[1]/div/h3')
    LOCATOR_TITLE_SELLING_OTHER = (By.XPATH, '/html/body/main/section[5]/div[2]/div/div[2]/div/h3')
    LOCATOR_SELLING_KARTEKA_PARAGRAPH_1 = (By.XPATH, '/html/body/main/section[5]/div[2]/div/div[1]/ul/li[1]')
    LOCATOR_SELLING_KARTEKA_PARAGRAPH_2 = (By.XPATH, '/html/body/main/section[5]/div[2]/div/div[1]/ul/li[2]')
    LOCATOR_SELLING_KARTEKA_PARAGRAPH_3 = (By.XPATH, '/html/body/main/section[5]/div[2]/div/div[1]/ul/li[3]')
    LOCATOR_SELLING_KARTEKA_PARAGRAPH_4 = (By.XPATH, '/html/body/main/section[5]/div[2]/div/div[1]/ul/li[4]')
    LOCATOR_SELLING_KARTEKA_PARAGRAPH_5 = (By.XPATH, '/html/body/main/section[5]/div[2]/div/div[1]/ul/li[5]')
    LOCATOR_SELLING_OTHER_PARAGRAPH_1 = (By.XPATH, '/html/body/main/section[5]/div[2]/div/div[2]/ul/li[1]')
    LOCATOR_SELLING_OTHER_PARAGRAPH_2 = (By.XPATH, '/html/body/main/section[5]/div[2]/div/div[2]/ul/li[2]')
    LOCATOR_SELLING_OTHER_PARAGRAPH_3 = (By.XPATH, '/html/body/main/section[5]/div[2]/div/div[2]/ul/li[3]')
    LOCATOR_SELLING_OTHER_PARAGRAPH_4 = (By.XPATH, '/html/body/main/section[5]/div[2]/div/div[2]/ul/li[4]')
    LOCATOR_SELLING_OTHER_PARAGRAPH_5 = (By.XPATH, '/html/body/main/section[5]/div[2]/div/div[2]/ul/li[5]')


class MainPageLocators:
    LOCATOR_TITLE = (By.XPATH, '/html/body/main/section[1]/div[2]/h1')
    LOCATOR_SUBTITLE = (By.XPATH, '/html/body/main/section[1]/div[2]/span')
    LOCATOR_BENEFITS_URGENTLY = (By.XPATH, '/html/body/main/section[1]/div[2]/ul/li[1]')
    LOCATOR_BENEFITS_EXPENSIVE = (By.XPATH, '/html/body/main/section[1]/div[2]/ul/li[2]')
    LOCATOR_BENEFITS_AROUND_CLOCK = (By.XPATH, '/html/body/main/section[1]/div[2]/ul/li[3]')
    LOCATOR_TITLE_FIELD_PHONE = (By.XPATH, '/ html / body / main / section[1] / div[2] / div / span')
    LOCATOR_FIELD_PHONE = (By.XPATH, '//*[@id="sell-phone"]')
    LOCATOR_BUTTON_SELL = (By.XPATH, '//*[@id="form-sell"]/div/button')
    LOCATOR_TITLE_POLICY = (By.XPATH, '//*[@id="form-sell"]/p')
    LOCATOR_BUTTON_POLICY = (By.XPATH, '//*[@id="form-sell"]/p/a')
    LOCATOR_FIELD_PHONE_SIZE = (By.XPATH, '// *[ @ id = "form-sell"] / div')
    LOCATOR_TITLE_POLICY_PAGE = (By.XPATH, '//*[@id="modal-privacy-policy"]/h2')
    LOCATOR_TITLE_THANK_YOU_PAGE = (By.XPATH, '//*[@id="modal-success"]/h2')


class QuestionsAnswersPageLocators:
    LOCATOR_TITLE_QUESTIONS_ANSWERS = (By.XPATH, '/html/body/main/section[9]/div/h2')
    LOCATOR_TITLE_QUESTION_1 = (By.XPATH, '/html/body/main/section[9]/div/div/div[1]/button/span[1]')
    LOCATOR_TITLE_ANSWER_1 = (By.XPATH, '/html/body/main/section[9]/div/div/div[1]/div/div/p[1]')
    LOCATOR_BUTTON_QUESTION_1 = (By.XPATH, '/html/body/main/section[9]/div/div/div[1]/button/span[2]')
    LOCATOR_BUTTON_QUESTION_1_EXPAND = \
        (By.CSS_SELECTOR, "[class='list-faq'] > :nth-child(1) [class='question'] [class='icon'] svg:nth-child(1)")
    LOCATOR_BUTTON_QUESTION_1_COLLAPSE = \
        (By.CSS_SELECTOR, "[class='list-faq'] > :nth-child(1) [class='question'] [class='icon'] svg:nth-child(2)")
    LOCATOR_TITLE_QUESTION_2 = (By.XPATH, '/html/body/main/section[9]/div/div/div[2]/button/span[1]')
    LOCATOR_TITLE_ANSWER_2 = (By.XPATH, '/html/body/main/section[9]/div/div/div[2]/div/div/p')
    LOCATOR_BUTTON_QUESTION_2 = (By.XPATH, '/html/body/main/section[9]/div/div/div[2]/button/span[2]')
    LOCATOR_BUTTON_QUESTION_2_EXPAND = \
        (By.CSS_SELECTOR, "[class='list-faq'] > :nth-child(2) [class='question'] [class='icon'] svg:nth-child(1)")
    LOCATOR_BUTTON_QUESTION_2_COLLAPSE = \
        (By.CSS_SELECTOR, "[class='list-faq'] > :nth-child(2) [class='question'] [class='icon'] svg:nth-child(2)")
    LOCATOR_TITLE_QUESTION_3 = (By.XPATH, '/html/body/main/section[9]/div/div/div[3]/button/span[1]')
    LOCATOR_TITLE_ANSWER_3 = (By.XPATH, '/html/body/main/section[9]/div/div/div[3]/div/div/p')
    LOCATOR_BUTTON_QUESTION_3 = (By.XPATH, '/html/body/main/section[9]/div/div/div[3]/button/span[2]')
    LOCATOR_BUTTON_QUESTION_3_EXPAND = \
        (By.CSS_SELECTOR, "[class='list-faq'] > :nth-child(3) [class='question'] [class='icon'] svg:nth-child(1)")
    LOCATOR_BUTTON_QUESTION_3_COLLAPSE = \
        (By.CSS_SELECTOR, "[class='list-faq'] > :nth-child(3) [class='question'] [class='icon'] svg:nth-child(2)")
    LOCATOR_TITLE_QUESTION_4 = (By.XPATH, '/html/body/main/section[9]/div/div/div[4]/button/span[1]')
    LOCATOR_TITLE_ANSWER_4 = (By.XPATH, '/html/body/main/section[9]/div/div/div[4]/div/div/p')
    LOCATOR_BUTTON_QUESTION_4 = (By.XPATH, '/html/body/main/section[9]/div/div/div[4]/button/span[2]')
    LOCATOR_BUTTON_QUESTION_4_EXPAND = \
        (By.CSS_SELECTOR, "[class='list-faq'] > :nth-child(4) [class='question'] [class='icon'] svg:nth-child(1)")
    LOCATOR_BUTTON_QUESTION_4_COLLAPSE = \
        (By.CSS_SELECTOR, "[class='list-faq'] > :nth-child(4) [class='question'] [class='icon'] svg:nth-child(2)")
    LOCATOR_TITLE_QUESTION_5 = (By.XPATH, '/html/body/main/section[9]/div/div/div[5]/button/span[1]')
    LOCATOR_TITLE_ANSWER_5 = (By.XPATH, '/html/body/main/section[9]/div/div/div[5]/div/div/p')
    LOCATOR_BUTTON_QUESTION_5 = (By.XPATH, '/html/body/main/section[9]/div/div/div[5]/button/span[2]')
    LOCATOR_BUTTON_QUESTION_5_EXPAND = \
        (By.CSS_SELECTOR, "[class='list-faq'] > :nth-child(5) [class='question'] [class='icon'] svg:nth-child(1)")
    LOCATOR_BUTTON_QUESTION_5_COLLAPSE = \
        (By.CSS_SELECTOR, "[class='list-faq'] > :nth-child(5) [class='question'] [class='icon'] svg:nth-child(2)")
    LOCATOR_TITLE_QUESTION_6 = (By.XPATH, '/html/body/main/section[9]/div/div/div[6]/button/span[1]')
    LOCATOR_TITLE_ANSWER_6 = (By.XPATH, '/html/body/main/section[9]/div/div/div[6]/div/div/p')
    LOCATOR_BUTTON_QUESTION_6 = (By.XPATH, '/html/body/main/section[9]/div/div/div[6]/button/span[2]')
    LOCATOR_BUTTON_QUESTION_6_EXPAND = \
        (By.CSS_SELECTOR, "[class='list-faq'] > :nth-child(6) [class='question'] [class='icon'] svg:nth-child(1)")
    LOCATOR_BUTTON_QUESTION_6_COLLAPSE = \
        (By.CSS_SELECTOR, "[class='list-faq'] > :nth-child(6) [class='question'] [class='icon'] svg:nth-child(2)")
    LOCATOR_TITLE_QUESTION_7 = (By.XPATH, '/html/body/main/section[9]/div/div/div[7]/button/span[1]')
    LOCATOR_TITLE_ANSWER_7 = (By.XPATH, '/html/body/main/section[9]/div/div/div[7]/div/div/p')
    LOCATOR_BUTTON_QUESTION_7 = (By.XPATH, '/html/body/main/section[9]/div/div/div[7]/button/span[2]')
    LOCATOR_BUTTON_QUESTION_7_EXPAND = \
        (By.CSS_SELECTOR, "[class='list-faq'] > :nth-child(7) [class='question'] [class='icon'] svg:nth-child(1)")
    LOCATOR_BUTTON_QUESTION_7_COLLAPSE = \
        (By.CSS_SELECTOR, "[class='list-faq'] > :nth-child(7) [class='question'] [class='icon'] svg:nth-child(2)")


class RansomAllPageLocators:
    LOCATOR_TITLE = (By.XPATH, '/html/body/main/section[3]/div/h2')
    LOCATOR_TITLE_BLOCK_NEW_OLD = (By.XPATH, '/ html / body / main / section[3] / div / div / div[1] / h3')
    LOCATOR_IMAGE_BLOCK_NEW_OLD = (By.XPATH, '/ html / body / main / section[3] / div / div / div[1] / div / img')
    LOCATOR_TITLE_BLOCK_PREMIUM = (By.XPATH, '/html/body/main/section[3]/div/div/div[2]/h3')
    LOCATOR_IMAGE_BLOCK_PREMIUM = (By.XPATH, '/html/body/main/section[3]/div/div/div[2]/div/img')
    LOCATOR_TITLE_BLOCK_BROKEN = (By.XPATH, '/html/body/main/section[3]/div/div/div[3]/h3')
    LOCATOR_IMAGE_BLOCK_BROKEN = (By.XPATH, '/html/body/main/section[3]/div/div/div[3]/div/img')
    LOCATOR_TITLE_BLOCK_CREDIT = (By.XPATH, '/html/body/main/section[3]/div/div/div[4]/h3')
    LOCATOR_IMAGE_BLOCK_CREDIT = (By.XPATH, '/html/body/main/section[3]/div/div/div[4]/div/img')
    LOCATOR_TITLE_BLOCK_EMERGENCY = (By.XPATH, '/html/body/main/section[3]/div/div/div[5]/h3')
    LOCATOR_IMAGE_BLOCK_EMERGENCY = (By.XPATH, '/html/body/main/section[3]/div/div/div[5]/div/img')
    LOCATOR_TITLE_BLOCK_DUPLICATE_PTS = (By.XPATH, '/html/body/main/section[3]/div/div/div[6]/h3')
    LOCATOR_IMAGE_BLOCK_DUPLICATE_PTS = (By.XPATH, '/html/body/main/section[3]/div/div/div[6]/div/img')
    LOCATOR_TITLE_BLOCK_ARRESTED = (By.XPATH, '/html/body/main/section[3]/div/div/div[7]/h3')
    LOCATOR_IMAGE_BLOCK_ARRESTED = (By.XPATH, '/html/body/main/section[3]/div/div/div[7]/div/img')
    LOCATOR_TITLE_BLOCK_PROBLEM = (By.XPATH, '/html/body/main/section[3]/div/div/div[8]/h3')
    LOCATOR_IMAGE_BLOCK_PROBLEM = (By.XPATH, '/html/body/main/section[3]/div/div/div[8]/div/img')


class RansomPageLocators:
    LOCATOR_TITLE_PAGE = (By.XPATH, '// *[ @ id = "section-buyback"] / div[2] / h2')
    LOCATOR_ICON_APPLICATION_EVALUATION = (By.XPATH, '//*[@id="section-buyback"]/div[2]/div/div[1]/div/div')
    LOCATOR_ICON_DEPARTURE_INSPECTION = (By.XPATH, '//*[@id="section-buyback"]/div[2]/div/div[2]/div/div')
    LOCATOR_ICON_REGISTRATION_REDEMPTION = (By.XPATH, '//*[@id="section-buyback"]/div[2]/div/div[3]/div/div')
    LOCATOR_ICON_CASH_BACK = (By.XPATH, '//*[@id="section-buyback"]/div[2]/div/div[4]/div/div')
    LOCATOR_NUMBER_STEP_1 = (By.CSS_SELECTOR, "[data-step='1']")
    LOCATOR_TITLE_APPLICATION_EVALUATION = (By.XPATH, '//*[@id="section-buyback"]/div[2]/div/div[1]/div/h3')
    LOCATOR_DESCRIPTION_APPLICATION_EVALUATION = (By.XPATH, '//*[@id="section-buyback"]/div[2]/div/div[1]/p')
    LOCATOR_NUMBER_STEP_2 = (By.CSS_SELECTOR, "[data-step='2']")
    LOCATOR_TITLE_DEPARTURE_INSPECTION = (By.XPATH, '//*[@id="section-buyback"]/div[2]/div/div[2]/div/h3')
    LOCATOR_DESCRIPTION_DEPARTURE_INSPECTION = (By.XPATH, '//*[@id="section-buyback"]/div[2]/div/div[2]/p')
    LOCATOR_NUMBER_STEP_3 = (By.CSS_SELECTOR, "[data-step='3']")
    LOCATOR_TITLE_REGISTRATION_REDEMPTION = (By.XPATH, '//*[@id="section-buyback"]/div[2]/div/div[3]/div/h3')
    LOCATOR_DESCRIPTION_REGISTRATION_REDEMPTION = (By.XPATH, '//*[@id="section-buyback"]/div[2]/div/div[3]/p')
    LOCATOR_NUMBER_STEP_4 = (By.CSS_SELECTOR, "[data-step='4']")
    LOCATOR_TITLE_CASH_BACK = (By.XPATH, '//*[@id="section-buyback"]/div[2]/div/div[4]/div/h3')
    LOCATOR_DESCRIPTION_CASH_BACK = (By.XPATH, '//*[@id="section-buyback"]/div[2]/div/div[4]/p')


class ReviewsPageLocators:
    LOCATOR_TITLE_REVIEWS = (By.XPATH, '/html/body/main/section[10]/div[2]/h2')
    LOCATOR_BUTTON_BACK = (By.XPATH, '/html/body/main/section[10]/div[3]/div[3]')
    LOCATOR_BUTTON_FORWARD = (By.XPATH, '/html/body/main/section[10]/div[3]/div[4]')
    LOCATOR_BUTTON_SLIDER_1 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[2]/span[1]')
    LOCATOR_TITLE_BLOCK_REVIEW_1 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[2]/div[1]/div[1]/h3')
    LOCATOR_TEXT_REVIEW_1 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[2]/div[1]/div[1]/p')
    LOCATOR_BUTTON_EXPAND_REVIEW_1 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[2]/div[1]/div[1]/a')
    LOCATOR_TITLE_FULL_REVIEW_1 = (By.XPATH, '/html/body/div[4]/div/h3')
    LOCATOR_IMAGE_REVIEW_1 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[2]/div[2]/img')
    LOCATOR_ICON_PRICE_1 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]')
    LOCATOR_TITLE_PRICE_KARTEKA_1 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]')
    LOCATOR_PRICE_KARTEKA_1 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]')
    LOCATOR_TITLE_PRICE_OTHER_1 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]')
    LOCATOR_PRICE_OTHER_1 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]')
    LOCATOR_BUTTON_SLIDER_2 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[2]/span[2]')
    LOCATOR_TITLE_BLOCK_REVIEW_2 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[3]/div[1]/div[1]/h3')
    LOCATOR_TEXT_REVIEW_2 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[3]/div[1]/div[1]/p')
    LOCATOR_BUTTON_EXPAND_REVIEW_2 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[3]/div[1]/div[1]/a')
    LOCATOR_TITLE_FULL_REVIEW_2 = (By.XPATH, '/html/body/div[4]/div/h3')
    LOCATOR_IMAGE_REVIEW_2 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[3]/div[2]/img')
    LOCATOR_ICON_PRICE_2 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]')
    LOCATOR_TITLE_PRICE_KARTEKA_2 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]')
    LOCATOR_PRICE_KARTEKA_2 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]')
    LOCATOR_TITLE_PRICE_OTHER_2 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]')
    LOCATOR_PRICE_OTHER_2 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]')
    LOCATOR_BUTTON_SLIDER_3 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[2]/span[3]')
    LOCATOR_TITLE_BLOCK_REVIEW_3 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[4]/div[1]/div[1]/h3')
    LOCATOR_TEXT_REVIEW_3 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[4]/div[1]/div[1]/p')
    LOCATOR_BUTTON_EXPAND_REVIEW_3 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[4]/div[1]/div[1]/a')
    LOCATOR_TITLE_FULL_REVIEW_3 = (By.XPATH, '/html/body/div[4]/div/h3')
    LOCATOR_IMAGE_REVIEW_3 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[4]/div[2]/img')
    LOCATOR_ICON_PRICE_3 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]')
    LOCATOR_TITLE_PRICE_KARTEKA_3 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[4]/div[1]/div[2]/div[1]/div[2]/div[1]')
    LOCATOR_PRICE_KARTEKA_3 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[4]/div[1]/div[2]/div[1]/div[2]/div[2]')
    LOCATOR_TITLE_PRICE_OTHER_3 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[4]/div[1]/div[2]/div[2]/div[1]')
    LOCATOR_PRICE_OTHER_3 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[4]/div[1]/div[2]/div[2]/div[2]')
    LOCATOR_BUTTON_SLIDER_4 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[2]/span[4]')
    LOCATOR_TITLE_BLOCK_REVIEW_4 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[5]/div[1]/div[1]/h3')
    LOCATOR_TEXT_REVIEW_4 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[5]/div[1]/div[1]/p')
    LOCATOR_BUTTON_EXPAND_REVIEW_4 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[5]/div[1]/div[1]/a')
    LOCATOR_TITLE_FULL_REVIEW_4 = (By.XPATH, '/html/body/div[4]/div/h3')
    LOCATOR_IMAGE_REVIEW_4 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[5]/div[2]/img')
    LOCATOR_ICON_PRICE_4 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[5]/div[1]/div[2]/div[1]/div[1]')
    LOCATOR_TITLE_PRICE_KARTEKA_4 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[5]/div[1]/div[2]/div[1]/div[2]/div[1]')
    LOCATOR_PRICE_KARTEKA_4 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[5]/div[1]/div[2]/div[1]/div[2]/div[2]')
    LOCATOR_TITLE_PRICE_OTHER_4 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[5]/div[1]/div[2]/div[2]/div[1]')
    LOCATOR_PRICE_OTHER_4 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[5]/div[1]/div[2]/div[2]/div[2]')
    LOCATOR_BUTTON_SLIDER_5 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[2]/span[5]')
    LOCATOR_TITLE_BLOCK_REVIEW_5 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[6]/div[1]/div[1]/h3')
    LOCATOR_TEXT_REVIEW_5 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[6]/div[1]/div[1]/p')
    LOCATOR_BUTTON_EXPAND_REVIEW_5 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[6]/div[1]/div[1]/a')
    LOCATOR_TITLE_FULL_REVIEW_5 = (By.XPATH, '/html/body/div[4]/div/h3')
    LOCATOR_IMAGE_REVIEW_5 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[6]/div[2]/img')
    LOCATOR_ICON_PRICE_5 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[6]/div[1]/div[2]/div[1]/div[1]')
    LOCATOR_TITLE_PRICE_KARTEKA_5 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[6]/div[1]/div[2]/div[1]/div[2]/div[1]')
    LOCATOR_PRICE_KARTEKA_5 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[6]/div[1]/div[2]/div[1]/div[2]/div[2]')
    LOCATOR_TITLE_PRICE_OTHER_5 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[6]/div[1]/div[2]/div[2]/div[1]')
    LOCATOR_PRICE_OTHER_5 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[6]/div[1]/div[2]/div[2]/div[2]')
    LOCATOR_BUTTON_SLIDER_6 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[2]/span[6]')
    LOCATOR_TITLE_BLOCK_REVIEW_6 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[7]/div[1]/div[1]/h3')
    LOCATOR_TEXT_REVIEW_6 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[7]/div[1]/div[1]/p')
    LOCATOR_BUTTON_EXPAND_REVIEW_6 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[7]/div[1]/div[1]/a')
    LOCATOR_TITLE_FULL_REVIEW_6 = (By.XPATH, '/html/body/div[4]/div/h3')
    LOCATOR_IMAGE_REVIEW_6 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[7]/div[2]/img')
    LOCATOR_ICON_PRICE_6 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[7]/div[1]/div[2]/div[1]/div[1]')
    LOCATOR_TITLE_PRICE_KARTEKA_6 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[7]/div[1]/div[2]/div[1]/div[2]/div[1]')
    LOCATOR_PRICE_KARTEKA_6 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[7]/div[1]/div[2]/div[1]/div[2]/div[2]')
    LOCATOR_TITLE_PRICE_OTHER_6 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[7]/div[1]/div[2]/div[2]/div[1]')
    LOCATOR_PRICE_OTHER_6 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[7]/div[1]/div[2]/div[2]/div[2]')
    LOCATOR_BUTTON_SLIDER_7 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[2]/span[7]')
    LOCATOR_TITLE_BLOCK_REVIEW_7 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[8]/div[1]/div[1]/h3')
    LOCATOR_TEXT_REVIEW_7 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[8]/div[1]/div[1]/p')
    LOCATOR_BUTTON_EXPAND_REVIEW_7 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[8]/div[1]/div[1]/a')
    LOCATOR_TITLE_FULL_REVIEW_7 = (By.XPATH, '/html/body/div[4]/div/h3')
    LOCATOR_IMAGE_REVIEW_7 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[8]/div[2]/img')
    LOCATOR_ICON_PRICE_7 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[8]/div[1]/div[2]/div[1]/div[1]')
    LOCATOR_TITLE_PRICE_KARTEKA_7 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[8]/div[1]/div[2]/div[1]/div[2]/div[1]')
    LOCATOR_PRICE_KARTEKA_7 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[8]/div[1]/div[2]/div[1]/div[2]/div[2]')
    LOCATOR_TITLE_PRICE_OTHER_7 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[8]/div[1]/div[2]/div[2]/div[1]')
    LOCATOR_PRICE_OTHER_7 = \
        (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[8]/div[1]/div[2]/div[2]/div[2]')
    LOCATOR_BLOCK_REVIEW_1 = (By.XPATH, '/html/body/main/section[10]/div[3]/div[1]/div[2]')


class TerritoryPageLocators:
    LOCATOR_TITLE = (By.XPATH, '/html/body/main/section[11]/div[2]/h2')
    LOCATOR_LIST_CITIES = (By.XPATH, '/html/body/main/section[11]/div[2]/div[1]/ul')
    LOCATOR_TITLE_FIELD_PHONE = (By.XPATH, '/html/body/main/section[11]/div[2]/div[2]/span')
    LOCATOR_FIELD_PHONE = (By.XPATH, '/html/body/main/section[11]/div[2]/div[2]/div/form/div/div/input')
    LOCATOR_BUTTON_SELL = (By.XPATH, '/html/body/main/section[11]/div[2]/div[2]/div/form/div/button')
    LOCATOR_TITLE_POLICY = (By.XPATH, '/html/body/main/section[11]/div[2]/div[2]/div/form/p')
    LOCATOR_BUTTON_POLICY = (By.XPATH, '/html/body/main/section[11]/div[2]/div[2]/div/form/p/a')
    LOCATOR_FIELD_PHONE_SIZE = (By.XPATH, '/html/body/main/section[11]/div[2]/div[2]/div/form/div')
    LOCATOR_TITLE_POLICY_PAGE = (By.XPATH, '//*[@id="modal-privacy-policy"]/h2')
    LOCATOR_TITLE_THANK_YOU_PAGE = (By.XPATH, '//*[@id="modal-success"]/h2')


class ThankYouWindowPageLocators:
    LOCATOR_TITLE = (By.XPATH, '/html/body/div[3]/h2')
    LOCATOR_SUBTITLE = (By.XPATH, '/html/body/div[3]/div/p')
    LOCATOR_ICON = (By.XPATH, '/html/body/div[3]/div/div')
