import aiohttp
import asyncio
import random
from bs4 import BeautifulSoup
BASE_URL = 'https://www.awel.ua'


async def parse_sub_category(sub_category: list, session):
    random_cat = random.choice(sub_category)
    button = random_cat.find('div', class_='fnc--center--catalog--item__button')
    cat_link = button.find('a')['href']
    async with session.get(f"{BASE_URL}{cat_link}") as response:
        print("Status:", response.status)
        html = await response.read()
        soup = BeautifulSoup(html, 'html.parser')
        return soup



async def parse_random_part():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL) as response:
            print("Status:", response.status)
            html = await response.read()
            soup = BeautifulSoup(html, 'html.parser')
            block_categories = soup.find('div', class_='active')
            categories = block_categories.find_all("div", class_='category-tab')
            random_category = random.choice(categories)
            cat_link = random_category.find('a')['href']
        async with session.get(f"{BASE_URL}{cat_link}") as response:
            print("Status:", response.status)
            html = await response.read()
            soup = BeautifulSoup(html, 'html.parser')
            sub_category = soup.find_all('div', class_="fnc--center--catalog__list--item")
            if sub_category:
                # тут ще підкатегорії
                soup = await parse_sub_category(sub_category, session)
            items = soup.find_all('div', class_='fnc--products--listitem')
            if items:
                random_item = random.choice(items)
                item_card = random_item.find('div', class_='fnc--products--listitem__image').find('a')['href']
                image_link = random_item.find('img')['src']
                item_name = random_item.find('div', class_='fnc--products--listitem__name').text.strip()
                item_price = random_item.find('div', class_='roz-price').text.strip().replace("\xa0", ' ')
                return {"item_card": f"{BASE_URL}{item_card}",
                        "image_link": f"{BASE_URL}{image_link}", 'item_name': item_name,
                        "item_price": item_price}
            else:
                print("Not found")



