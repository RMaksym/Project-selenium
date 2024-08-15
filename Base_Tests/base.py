class StartRegistrationPage:
    """
    Base class for each page
    """
    def __init__(self, driver):
        self.driver = driver


    def _verify_page (self):
        return