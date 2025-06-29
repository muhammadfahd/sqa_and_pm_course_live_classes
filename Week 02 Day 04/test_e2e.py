from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Get full path to the HTML file
file_path = os.path.abspath("grade_calculator.html")
url = f"file:///{file_path}"

# Setup WebDriver
driver = webdriver.Chrome()
driver.get(url)  # open local HTML file in browser

def test_grade(marks, expected_grade):
    input_box = driver.find_element(By.ID, "marks")
    input_box.clear()
    input_box.send_keys(str(marks))

    button = driver.find_element(By.TAG_NAME, "button")
    button.click()

    time.sleep(1)  # wait for JS to update result
    result = driver.find_element(By.ID, "result").text

    print(f"Input: {marks} | Output: {result} | Expected: Grade: {expected_grade}")
    assert result == f"Grade: {expected_grade}"

# Test Cases
test_grade(95, "A")
test_grade(81, "B")
test_grade(30, "F")
test_grade(89, "B")     # Just below A
test_grade(90, "A")     # Boundary A
test_grade(79, "C")     # Just below B
test_grade(80, "B")     # Boundary B
test_grade(69, "D")     # Just below C
test_grade(70, "C")     # Boundary C
test_grade(59, "F")     # Just below D
test_grade(60, "D")     # Boundary D
test_grade(0, "F")      # Lowest valid input
test_grade(100, "A")    # Highest valid input
test_grade(105, "Invalid marks!")  # Above max
test_grade("", "Invalid marks!")   # Empty input
test_grade("abc", "Invalid marks!")  # Non-numeric input

print("All tests passed!")


driver.quit()
