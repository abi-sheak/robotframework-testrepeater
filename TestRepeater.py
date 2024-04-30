from robot.api import SuiteVisitor

class TestRepeater(SuiteVisitor):
    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self, count):
        self.count = int(count)

    def start_suite(self, suite, result):
        testcases = []
        for iter in range(1, self.count+1):
            for test in suite.tests:
                copy = test.copy(name=f"{iter} - {test.name}")
                testcases.append(copy)
        suite.tests = testcases

    def end_suite(self, suite, result):
        pass

    def start_test(self, test, result):
        pass

    def end_test(self, test, result):
        pass

    def start_keyword(self,test, result):
        pass

    def end_keyword(self,test, result):
        pass
