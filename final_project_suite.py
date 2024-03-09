import unittest
import HtmlTestRunner

from test_log_in_invalid_credentials import Log_in_invalid
from test_log_in_log_out_with_valid_credentials import Log_in_out
from test_cellphones_selection import Cellphones_selection
from test_brand_sorting import Brand_sorting
from test_access_terms import Access_terms
from test_faq_access import FAQ_access
from test_payment_methods import Payment_methods
from test_instagram import Instagram_check
from test_pinterest import Pinterest_check
from test_standard_warranty import Warranty_check

class TestSuite(unittest.TestCase):

    def test_suite(self):
        tests_to_be_run = unittest.TestSuite()
        tests_to_be_run.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Log_in_invalid),
                                  unittest.defaultTestLoader.loadTestsFromTestCase(Log_in_out),
                                  unittest.defaultTestLoader.loadTestsFromTestCase(Cellphones_selection),
                                  unittest.defaultTestLoader.loadTestsFromTestCase(Brand_sorting),
                                  unittest.defaultTestLoader.loadTestsFromTestCase(Access_terms),
                                  unittest.defaultTestLoader.loadTestsFromTestCase(FAQ_access),
                                  unittest.defaultTestLoader.loadTestsFromTestCase(Payment_methods),
                                  unittest.defaultTestLoader.loadTestsFromTestCase(Instagram_check),
                                  unittest.defaultTestLoader.loadTestsFromTestCase(Pinterest_check),
                                  unittest.defaultTestLoader.loadTestsFromTestCase(Warranty_check)])

        runner = HtmlTestRunner.HTMLTestRunner \
                (
                combine_reports=True,
                report_title="Test execution report",
                report_name="Test results"
            )

        runner.run(tests_to_be_run)