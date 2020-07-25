# python_assertions
Examples of how to write good tests using Arrange/Act/Assert framework.

For this example, **ChromeDriver** version is 83 and should be located inside your downloads folder ("\\Users\\user_name\\Downloads\\chromedriver_win32\\chromedriver.exe"). Make sure to replace "user_name" with a suitable name from your file path.
Please update it according to your version of Google Chrome installed on your machine when running locally.

**Pre-requisites:**

I am using the [DuckDuckGo instant answer API](https://api.duckduckgo.com/?q=) to search for products like MacBook, iPhone etc. 

**Environment setup:**

Please make sure you have **Python** installed [link](https://www.python.org/downloads/)

Please make sure you have **PyCharm** installed [link](https://www.jetbrains.com/pycharm/download/)

To install the necessary packages using **PyCharm** (on **Windows 10**):

1. Open your project in **PyCharm**.
2. Click on **File -> Settings**.
3. In the search field type in **Interpreter**.
4. In the new window, click on **+** sign to add new packages.
5. Type in **selenium** and click on **Install Package**.
6. Type in **pytest** and click on **Install Package**.
7. Close Packages and Settings windows.
 

Make sure you have the packages installed otherwise you won't be able to import the modules and run your tests.

Edit your Run/Debug configurations so that you canuse pytest to run your assertion tests. Click on the **+** icon and select "pytest" under "Python tests". Make sure that you change the target for your script path. It should be the path to the python file that you want to test.

![RUN/DEBUG CONFIGURATIONS IN PYCHARM](screenshots/assert3.png)


If your test has passed, you will get a message on the console similar to the one below:

![TEST PASSED](screenshots/assert4.png)

You can run your test via terminal. Type **pytest -v filename** or **pytest -v** to run all other tests you have in the folder.
