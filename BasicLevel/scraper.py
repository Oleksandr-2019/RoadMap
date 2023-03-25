import requests
from bs4 import BeautifulSoup

base_url_link = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page="

# List for all laptops
list_laptops = []

# Cycle through all pagination pages
for item in range(21):
    # Adding to the base link - pagination number
    full_link = base_url_link + str(item)

    response = requests.get(full_link)

    soup = BeautifulSoup(response.content, "lxml")

    # I select all divs that have the thumbnail class - that is, we take all laptops from this page
    all_leptops = soup.findAll("div", class_="thumbnail")

    # The loop goes through the all_leptops list and selects
    # the name and description of the laptop from it
    for one_laptop in all_leptops:
        text_title = one_laptop.find("a", class_="title").text
        text_description = one_laptop.find("p", class_="description").text
        laptop = [text_title, text_description]
        list_laptops.append(laptop)

number_laptop = 1
for laptop in list_laptops:
    print("Ноутбук №" + str(number_laptop))
    print("Назва ноутбука: " + laptop[0])
    print("Опис ноутбука: " + laptop[1])
    print("---------------------------------------------------")
    number_laptop = number_laptop + 1