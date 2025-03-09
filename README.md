[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Selenium: WebDriver](https://img.shields.io/badge/Selenium-WebDriver-green.svg)](https://www.selenium.dev/)

# Selenium Learning Project

This repository contains a collection of Python scripts demonstrating various Selenium WebDriver functionalities, designed for learning and practical application. Each script focuses on a specific aspect of web automation, from basic browser commands to handling complex UI elements and data-driven testing.

## Table of Contents

* [Introduction](#introduction)
* [Files Overview](#files-overview)
* [Setup and Installation](#setup-and-installation)
* [Usage](#usage)
* [Data-Driven Testing](#Data-Driven-Testing)
* [Handling UI Elements](#handling-ui-elements)
* [Waits and Synchronization](#waits-and-synchronization)
* [Browser Handling](#browser-handling)
* [Additional Notes](#additional-notes)
* [Contributing](#contributing)
* [License](#license)

## Introduction

This project is a personal learning journey into the world of Selenium WebDriver with Python. It covers a wide range of scenarios, from simple login automation to handling intricate web elements and data-driven testing. The scripts serve as practical examples and can be used as a foundation for more complex automation tasks.

## Files Overview

Here's a breakdown of the scripts and data files included in this repository:

**Core Selenium Functionality:**

* `firstTest.py`: A basic "Hello, World!" example demonstrating the initialization of a WebDriver.
* `BrowserCommands.py`: Shows how to use various browser commands like navigation, window management, and getting page information.
* `Login.py`: A simple login script showcasing form filling and submission.
* `webtable.py`: Demonstrates how to interact with and extract data from web tables.
* `iframe.py`: Handles interactions within iframes.
* `Nestedframe.py`: Deals with nested iframes.
* `drag_n_drop.py`: Automates drag-and-drop actions.
* `dropdown1.py`: Shows how to interact with dropdown menus.
* `HandlingMouseHover.py`: Simulates mouse hover actions.
* `Handling_Resizable_element.py`: Handles resizable elements.
* `Handling_Slider.py`: Automates slider interactions.
* `Handling_tabs.py`: Shows how to switch between browser tabs.
* `JavaScript_alerts.py`: Handles JavaScript alerts, confirms, and prompts.
* `basic_auth.py`: Demonstrates handling basic authentication dialogs.
* `datepicker1.py` & `datepicker2.py`: Examples of automating date pickers, with different approaches.
* `viewport.py`: shows how to change the viewport size of the browser.

**Waits and Synchronization:**

* `ImplicitWait.py`: Illustrates the use of implicit waits.
* `ExplicitWait.py`: Shows how to use explicit waits for specific conditions.

**Data-Driven-Testing:**

* `DataDrivenLogin.py`: Implements a simple data-driven login using hardcoded data.
* `CSVDataDrivenLogin.py`: Demonstrates data-driven login using a CSV file (`testdata.csv`).
* `DataDrivenJSON.py`: Demonstrates data-driven login using a JSON file (`testdata.JSON`).
* `testdata.csv`: CSV file containing test data.
* `testdata.JSON`: JSON file containing test data.
* `testdata.xlsx`: Excel file containing test data.

**Error Handling and Utility:**

* `Brokenlinks.py`: Checks for broken links on a webpage.
* `Broken_images.py`: Checks for broken images on a webpage.
* `requirements.txt`: Lists the Python packages required for this project.
* `test.txt`: A simple text file used for testing file operations.

**Browser Configuration:**

* `incognito_mode.py`: Shows how to launch the browser in incognito mode.

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone [repository_url]
    cd selenium-learning-project
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

    * **Windows:** `venv\Scripts\activate`
    * **macOS/Linux:** `source venv/bin/activate`

3.  **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Download the WebDriver:**

    * Ensure you have the appropriate WebDriver (e.g., ChromeDriver, GeckoDriver) for your browser and place it in a directory accessible to your system's PATH, or specify the webdriver location in your python scripts.

## Usage

To run a script, simply execute it using Python:

```bash
python Brokenlinks.py






# **Introduction to Selenium**

- Selenium is a web browser automation tool.
- It allows us to open browser of our choice and perform tasks as a human being would like:
    - Clicking buttons.
    - Entering information in forms.
    - Searching for information on web pages

Uses a web-driver package that can take control of the browser and mimic user-oriented actions.

## **Beautiful Soup vs Selenium**

**BeautifulSoup**

- A module that can be used for pulling data out of HTML and XML documents.
- Depends heavily on other libraries like requests or urllib for sending web requests.
- Dose not have a document parser; we need to choose one like, `html.parser`, 'HTML5lib'.
- It is difficult to scrap websites which return Java script code.
- It does not automate the web browser. It saves a copy of web page source and then does further processing

**Selenium**

- A tool developed for web application automated testing.
- Can send web requests on its own
- It comes with a parser.
- Loads JavaScript and can help access data behind JavaScript files as well.
- Faster that BeautifulSoup, while interacting with webpages.
- Comes handy when handling Java script featured websites.


## **Getting started with Selenium**

**Setup**

- **Selenium** - we need to install selenium package.

```python
pip install selenium
```

- **Selenium Drivers** - These web drivers enable python to control the browser for interactions.

    - The browser that you will use, chrome or Firefox, should be pre installed.
    - Check the version of your browser.
    - visit - `chromedriver.chromium.org/downloads`
    - Download the version of chromedriver that matches the version of your browser.
    - Keep a check of the path where the chromedriver is downloaded.

## **Locating Web Elements in Selenium**

Selenium offers a wide variety of functions to locate an element on the web page:

- **find_element_by_id**: Uses id to find an element.
- **find_element_by_name**: Uses name to find an element.
- **find_element_by_xpath**: Uses xpath to find and element.
- **find_element_by_tag_name**: Uses tag name to find an element.
- **find_element_by_class_name**: Uses value of class attribute to find an element.
- **CSS selector**
- **Link Text**
- **Partial Link Text**

There are other functions as well which help us locate elements on the web page.


## **XPath Syntax**

- **XPath known as the XML** path is a language that helps to query the XML documents. <br>
It consits of expression for a path along with certain conditions to locate a particular element.

- The basic format of Xpath is mentioned below:

![Xpath_Syntax](https://github.com/user-attachments/assets/3c453fdc-4cbc-44a2-ab36-5a2b0a942d3c)

## **Types of XPaths**

- There are two types of XPath:
    - Absolute XPath
    - Relative XPath

- **Absolute XPath**: Begins with the single forward slash (/), means we select the element from the root node and go all the way down to the element needed.

```
/html/body/div[2]/div[1]/div/h4[1]/b/html[1]/body[1]/div[2]/h4[1]/b[1]
```

- **Relative XPath**: starts from the middle of the HTML structure. Starts with double forward slash (//) an can search elements anywhere on the webpage without writting the long absolute xpath.

```
//div[@class='featured-box columnsize1']//h4[1]//b[1]
```

## **XPath Functions**

**1) Basic Xpath**: XPath expression select nodes or list of nodes on the basis of attributes like ID, Name, Classname, etc. from the XML document like shown below:

```
XPath= //input[@name='uid']

XPath= //a[@href='http://google.com/']
```

**2) Contains()**: used when the value of any attribute changes dynamically, example, login information. It can find the element with partial text.

for finding 'submit' button where Type= 'submit':

```
XPath= //*[contains(@type, 'sub')]

XPath= //img[contains(@src, 'content')]
```

**3) Using OR & AND**: Here, two conditions are used, whether 1st condition OR 2nd condition should be true. Means any one condition should be true to find the element.

```
XPath= //*[@type='submit' or @name='btnReset']
```

in AND expression, two conditions are used, both condiitons should be true to find the element.
if fails to find element if any one condition is flase.

```
XPath= //input[@type='submit' and @name='btnlogin']
```

**4) starts-with()**: Used to find a web element whose value of an attribute changes on the refresh or on any other dynamic operaiton on the web page.
we mathch the starting text of the attribute to locate an element whose attribute has changed dynamically.

```
XPath= //img[starts-with(@src,'https')]
```

**5) text()**: Used with the text function to locate an element with exact text.

Here, it go anywhere inside the document, irrespective of the tag, but, it must contain a text whose value is Seach Google or type a URL. The asterisk(*) implies any tag with the same
value.

```
XPath= //*[text()='Search Google or type a URL']
```

# **Web Scrapping**

- It's a technique which is used to extract large amounts of data from websites.
- The data extracted can be stored in structured fromats like CSV.
- Then we can use the extracted data according to our need.

- For example we can collect data from e-commerce portals, social media platforms to understand the customer behaviours, sentiments, buying patterns which are critical insights for any business.

## **What is Web Scraping?**

- web scraping is an automated technique used to extract large amounts of data from websites.
- The data on the websites are unstructured. Web scraping helps collect these unstructured data and store it in a structured form.
- There are different ways to scrape websites such as online Services, APIs or writting your own code.

## **How does Web Scraping works?**

- We write code that sends a requests to the server that's hosting the page we specified.
- Our code downloads that page's source code
- It filters through the page looking for HTML elements we've specified, and extracting whatever content we've instructed it to extract in the code.

For example if we want to get all of the titles inside H2 tags from a website, we could write some code to do that and the code will work as shown in the following steps:

1. Our code would request the site's content from it's server and downloading it. <br>
2. Then it would go through the page's HTML code and looks for the H2 tags. <br>
3. Whenever it finds and H2 tag, it would copy whatever text is inside the tag, and save it in whatever format we have specified.

## **Components of a Web Page**

A web page is made by generally 4 types of files: <br>
**1. HTML file:** It contains the main content of the web page <br>
**2. CSS file:** This file is for the styling of the web page. <br>
**3. JS file:** JavaScript file brings interactivity to the web page. <br>
**4. Images file:** JPG/PNG file formats for showing images in the web page 

As we are interested in extracting data from the web page , we will be using the html file for extracting data as the html file contains the main content of the web page.


## `assert` Statement:

- This is a built-in Python keyword used for debugging.  
- It checks whether a given condition is `True`.  
- If the condition is `False`, Python raises an `AssertionError`.  

## `"Selenium" in title`:

- This checks whether the string `"Selenium"` is present in the variable `title`.  
- If `"Selenium"` exists inside `title`, the assertion passes, and the program continues running normally.  
- If `"Selenium"` is **not** in `title`, an `AssertionError` is raised.  

# **SYNCHRONIZATION ISSUES**

Synchronization issues in Selenium with Python primarily refer to challenges related to the timing misalignment between the automation script and the web applicaiton being tested. These issues arise due to the asynchronous nature of web applications where elements may load or change dynamically, and the automation script may not synchronize with these changes.

## **COMMON ISSUES**

- **Element Visibility**: The script tries to interact with an element before it is visible on the page, leading to NoSuchElementException or ElementVisibleException.

- **Element Interactability**: The script attempts to interact with an element before it becomes interactable, such as Clicking a button or typing in a text field.

- **Page Load**: The script proceeds with actions before the page has finished loading completly, resulting in StaleElementReferenceException or ElementNotInteractableException.

- **asynchronous operaitons**: Web applicaitons often use asynchronous operaitons such as  AJAX requests or JavaScript timers to update content dynamically. The script needs to wait for these opeations to complete before proceeding.

- **Dynamic Content**: Element on the page may load or change dynamically after a certain period or due to user interacts . The script needs to wait for these changes to reflect before performing actions.

## **IMPLICIT WAIT**

- Selenium has a built-in way to automatically wait for elements called an implicit wait.

- An implicit wait value can be set either with the timeouts capability in the  browser options, or with a driver method

- This is a global setting that applies to every element location call for the entire session.

- The dafault value is 0, which means that if the element is not found, it will immediately return an error.

- If an implicit wait is set, the driver will wait for the duration of the provided value before retuuning the error

## **EXPLICIT WAIT**

The syntax for explicit waits in Selenium Python involves two main parts:

### **Creating a WebDriverWait object**

```
from selenium.webdriver.support.ui import WebDriverWait

wait = WebDriverWait(driver, timeout)
```

### **Using ExpectedConditons**

```
from selenium.webdriver.support import expected_conditions as EC

Element = wait.until(EC.presence_of_element_located((By.ID, "my_element_id")))
```


## **IMPLICIT VS EXPLICIT WAIT**

| Feature    | Implicit Wait | Explicit Wait |
| -------- | ------- | ------- |
| Scope | Global (applies to all element find operations) | Specific to a particular element |
| Waits For | Element presence in the DOM | Specific conditions (presence, visibility, etc.) |
| Syntax | Simpler (set a global timeout value) | More complex (use ExpectedConditions functions) |
| Control | Less control over waiting behavior | More control over waiting logic |
| Readability | Less readable (unclear what you're waiting for) | More readable (explicitly states wait conditions) |



## **docs:**

- openpyxl: https://openpyxl.readthedocs.io/en/stable/

- Selenium: https://www.selenium.dev/documentation/webdriver/
