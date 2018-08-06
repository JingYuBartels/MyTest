import unittest
import HTMLTestRunner
import time
from send_mail import send_mail, new_report
import os

test_dir = './TestReport'
testcase_dir = './TestCase'

smoke_tests = unittest.defaultTestLoader.discover(testcase_dir, pattern='test*.py')

if __name__ == "__main__":
    #file_dir = os.path.join(os.getcwd(), 'SmokeTestReport.html')
    now = time.strftime('%Y_%m_%d %H:%M:%S')
    filename = os.path.join(test_dir, now+'result.html')

    with open(filename, 'wb') as outfile:

        runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Test Report', description='Smoke Test')
        runner.run(smoke_tests)

    new_report = new_report(test_dir)
    send_mail(new_report)
