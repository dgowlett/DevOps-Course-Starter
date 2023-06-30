import os
import pytest

#from importlib import reload
import importlib
import requests
importlib.reload(requests)

import json
from threading import Thread
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.firefox.options import Options as FirefoxOptions
from dotenv import load_dotenv, find_dotenv
from todo_app import app

#options = FirefoxOptions()
#options.add_argument('-headless')

@pytest.fixture(scope='module')
def app_with_temp_board():
    # Load our real environment variables
    #file_path = find_dotenv('.env')
    file_path = find_dotenv('.env')
    load_dotenv(file_path,override=True)
    #load_dotenv(override=True)

    # Create the new board & update the board id environment variable
    board_id = create_trello_board()
    os.environ['TRELLO_BOARD_ID'] = board_id

    # Construct the new application
    application = app.create_app()

    # Start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    
    # Give the app a moment to start
    sleep(1)

    # Return the application object as the result of the fixture
    yield application

    # Tear down
    thread.join(1)
    delete_trello_board(board_id)

def create_trello_board():

    # TODO Create a new board in Trello and return the id
    query = {   
        'key': os.environ.get('TRELLO_API_KEY'),
        'token': os.environ.get('TRELLO_API_TOKEN')
    }
    
    url = "https://api.trello.com/1/boards/?name=e2eTesting"
    response = requests.request("POST",url,params=query)
    jsonResponse = response.json()
    print("board id " + jsonResponse["shortUrl"].split("/")[4])
    return jsonResponse["shortUrl"].split("/")[4]

def delete_trello_board(board_id):

    # TODO Delete the Trello board with id board_id
    query = {   
        'key': os.environ.get('TRELLO_API_KEY'),
        'token': os.environ.get('TRELLO_API_TOKEN')
    }

    url = "https://api.trello.com/1/boards/" + board_id
    response = requests.request("DELETE",url,params=query)

    return None

@pytest.fixture(scope="module")
def driver():
    #options = FirefoxOptions()
    #options.add_argument('-headless')
    with webdriver.Firefox() as driver:
        yield driver

def test_task_journey(driver, app_with_temp_board):
    driver.get('http://localhost:5000/')

    print(dir(driver))
    assert driver.title == 'To-Do App'
    driver.implicitly_wait(5)

    test_text = "Happy Testing"
    todo_text_field = driver.find_element(By.NAME, 'new_item')
    todo_text_field.send_keys(test_text)

    
    sleep(1)

    driver.find_element(By.NAME, "submit").click()
    sleep(2)

    test_text = "Happy Testing2"
    todo_text_field = driver.find_element(By.NAME, 'new_item')
    todo_text_field.send_keys(test_text)
    sleep(2)

    driver.find_element(By.NAME, "submit").click()
    sleep(2)

def test_task_journey_complete(driver, app_with_temp_board):
    driver.get('http://localhost:5000/')

    assert driver.title == 'To-Do App'
    driver.implicitly_wait(5)

    # Click on Not started button to complete
    driver.find_element(By.NAME, "todo_0").click()
    sleep(1)

    driver.implicitly_wait(5)
    
    # Click on Not started button to complete
    driver.find_element(By.NAME, "todo_0").click()
    sleep(1)

def test_task_journey_notstarted(driver, app_with_temp_board):
    driver.get('http://localhost:5000/')

    assert driver.title == 'To-Do App'
    driver.implicitly_wait(5)
    
    # Click on Completed button to change to Not started
    driver.find_element(By.NAME, "done_0").click()
    sleep(1)

def test_task_journey_delete(driver, app_with_temp_board):
    driver.get('http://localhost:5000/')

    assert driver.title == 'To-Do App'
    driver.implicitly_wait(5)
    
    # Delete Todo item found in Not Started
    driver.find_element(By.NAME, "todo_delete_0").click()
    sleep(1)

    # Delete Todo item found in Completed
    driver.find_element(By.NAME, "done_delete_0").click()
    sleep(1)


