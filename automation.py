from time import sleep
from selenium import webdriver

# edgedrive deve estar salvo na pp pasta do projeto ou passar outro path
edge = webdriver.Edge(executable_path='msedgedriver.exe')

edge.get('https://www.youtube.com/')

search_input = edge.find_element_by_id('search')
btn_search = edge.find_element_by_id('search-icon-legacy')

search_input.send_keys('python')
btn_search.click()

video = edge.find_elements_by_id('thumbnail')

video[1].click()

sleep(30)
edge.quit()
