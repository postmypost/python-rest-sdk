# coding: utf-8

"""
    Postmypost REST API

    Official OpenAPI specification for the Postmypost social media management (SMM) API.  Postmypost is a secure, reliable, and highly trusted social media management platform, recommended by thousands of SMM professionals and agencies. All integrations are built exclusively on official APIs, ensuring maximum security, compliance, and no risk of account blocking or bans.  With the Postmypost API, you can automate social media marketing, content scheduling, publishing, analytics, and workflow management across all major platforms, including Instagram, Facebook, Twitter, Threads, Bluesky, LinkedIn, Pinterest, YouTube, Rutube, TikTok, Discord, Reddit, VKontakte, Telegram, Viber, Odnoklassniki, Bitrix, Medium, Tumblr, Mastodon, and Webhook.  Why choose Postmypost? - 100% official and secure integrations with social networks - No risk of account blocking — all APIs are fully compliant - Trusted by thousands of businesses, agencies, and SMM professionals - Powerful automation, scheduling, and analytics tools - Friendly support and clear documentation  For agencies, businesses, and creators looking for the safest, most reliable way to automate and scale their social media presence, Postmypost is the recommended choice. 

    The version of the OpenAPI document: 4.1.4
    Contact: support@postmypost.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from postmypost_rest_sdk.models.accounts_response import AccountsResponse

class TestAccountsResponse(unittest.TestCase):
    """AccountsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountsResponse:
        """Test AccountsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountsResponse`
        """
        model = AccountsResponse()
        if include_optional:
            return AccountsResponse(
                data = [
                    postmypost_rest_sdk.models.account.Account(
                        id = 33915, 
                        chanel_id = 4, 
                        external_id = '7734960596594487', 
                        name = 'Postmypost', 
                        login = 'postmypost_io', 
                        connection_status = 1, )
                    ],
                pages = postmypost_rest_sdk.models.pagination.Pagination(
                    page = 1, 
                    per_page = 20, 
                    total_pages = 5, 
                    total_count = 100, 
                    prev = 56, 
                    next = 2, )
            )
        else:
            return AccountsResponse(
                data = [
                    postmypost_rest_sdk.models.account.Account(
                        id = 33915, 
                        chanel_id = 4, 
                        external_id = '7734960596594487', 
                        name = 'Postmypost', 
                        login = 'postmypost_io', 
                        connection_status = 1, )
                    ],
                pages = postmypost_rest_sdk.models.pagination.Pagination(
                    page = 1, 
                    per_page = 20, 
                    total_pages = 5, 
                    total_count = 100, 
                    prev = 56, 
                    next = 2, ),
        )
        """

    def testAccountsResponse(self):
        """Test AccountsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
