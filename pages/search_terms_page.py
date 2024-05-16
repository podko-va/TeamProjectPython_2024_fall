from selene import query, have, browser
from selene.support.shared.jquery_style import s, ss
from pages.locators import SearchTermsLocators as ST, BaseLocators as BL


def order_search_terms():
    keyword_elements = ss(ST.LIST_OF_SEARCH_TERMS)
    keyword_texts = [k.get(query.attribute("text")).replace('\n', '') for k in keyword_elements]
    keyword_elements.should(have.exact_texts(sorted(keyword_texts)))


def visit():
    browser.open(ST.LINK_SEARCH_TERMS)


def title_is_correct():
    s(BL.PAGE_TITLE).should(have.text("Popular Search Terms"))


def search_terms_list_have_100():
    ss(ST.TERMS_FOR_SEARCH_LIST_QTY).should(have.size(100))


def collect_all_search_terms():
    terms = ss(ST.LIST_OF_SEARCH_TERMS)
    return terms


def extract_font_sizes_from_search_terms(terms):
    list_font_sizes = []
    for g in terms:
        g_font, g_size = g.get(query.attribute("style")).split(": ")
        g_size = float(g_size.replace("%;", ""))
        list_font_sizes.append(g_size)
    return list_font_sizes


def check_min_and_max_font_sizes(list_font_sizes):
    assert min(list_font_sizes) <= 76 and max(list_font_sizes) >= 136, "Font sizes not between 76 and 136"


def extract_keywords_from_search_terms_as_it_is(terms):
    # список ключевых,вытаскиваемых с помощью selene, выглядит не так, как при selenium.
    # Теперь есть лишние пробелы, перевод строки, слова с малой буквы неправильно сортируются.
    # С selenium тест = ОК
    list_of_goods_nonsorted = []  # words from terms applied lower()
    for keyword in terms:
        keyword = keyword.get(query.attribute("text")).strip().replace(" ", "").lower()
        list_of_goods_nonsorted.append(keyword.lower())
    return list_of_goods_nonsorted


def extract_keywords_from_search_terms_sorted(terms):
    list_of_goods = []  # good : strip, lower, no spaces
    for keyword in terms:
        keyword = keyword.get(query.attribute("text")).strip().replace(" ", "").lower()
        list_of_goods.append(keyword)
    list_of_goods_sorted = sorted(list_of_goods)
    return list_of_goods_sorted


def compare_list_sorted_stripped_and_original(list_of_goods_nonsorted, list_of_goods_sorted):
    assert list_of_goods_nonsorted == list_of_goods_sorted


def select_specific_words_and_terms(terms):
    words = ["hoodie", "jacket", "pants", "shirt"]
    goods = {}
    for keyword in terms:
        word = keyword.get(query.attribute("text")).strip().replace(" ", "").lower()
        if word in words:
            g_font, g_size = keyword.get(query.attribute("style")).split(": ")
            g_size = float(g_size.replace("%;", ""))
            goods[word] = g_size
    return goods


def compare_selected_words_and_their_sizes(goods):
    specific_goods = []
    specific_fonts = []
    words = ["hoodie", "jacket", "pants", "shirt"]
    for k, v in goods.items():
        specific_goods.append(k)
        specific_fonts.append(v)
    assert set(specific_goods) == set(words) and all(
        [size > 88 for size in specific_fonts]), "Selected words have font size bigger than 88%"


def check_size_of_5_last_words_in_sorted_list(list_font_sizes):
    sizes_sorted = sorted(list_font_sizes, reverse=True)
    for size in range(0, 5):
        if sizes_sorted[size] < 88:
            assert False, "List of search terms has not 5 elements which size is bigger than 88%"
