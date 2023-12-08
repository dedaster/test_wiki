import pytest
import re

# задаем переменные для сравнения значений
@pytest.mark.parametrize(
    "test, ask_popularity",
    [('Test 1: 10^7', 10000000),
     ('Test 2: 1.5 * 10^7', 15000000),
     ('Test 3: 5 * 10^7', 50000000),
     ('Test 4: 10^8', 100000000),
     ('Test 5: 5 * 10^8', 500000000),
     ('Test 6: 10^9', 1000000000),
     ('Test 7: 1.5 * 10^9', 1500000000)])

@pytest.mark.regression
@pytest.mark.smoke
# тест проверяет значение "Popularity" в таблице "Programming languages used in most popular websites"
def test_popularity_count(browser, test, ask_popularity):
    tr = 1
    err = []
    table = browser.find('caption', string=re.compile("Programming languages used in most popular websites*")).parent
    for x in table.select('sup'): x.decompose()

    while tr < 17:
        take_popularity = table.find_all('tr')[tr].find_all('td')[1].text
        take_popularity = int(''.join(x for x in take_popularity if x.isdigit()))
        if take_popularity < ask_popularity:
            take_website = table.find_all('tr')[tr].find_all('td')[0].text[:-1]
            take_frontend = table.find_all('tr')[tr].find_all('td')[2].text[:-1]
            take_backend = table.find_all('tr')[tr].find_all('td')[3].text[:-1]
            message = (take_website + " (Frontend:" + take_frontend + "|Backend:" + take_backend + ") has "
                       + str(take_popularity) + " unique visitors per month. (Expected more than "
                       + str(ask_popularity) + ")")
            err.append(message)
        tr += 1

    assert len(err) == 0, print('\n'.join(err))