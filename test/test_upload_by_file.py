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

from postmypost_rest_sdk.models.upload_by_file import UploadByFile

class TestUploadByFile(unittest.TestCase):
    """UploadByFile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UploadByFile:
        """Test UploadByFile
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UploadByFile`
        """
        model = UploadByFile()
        if include_optional:
            return UploadByFile(
                id = 1283466,
                name = 'test.jpg',
                size = 259390,
                action = 'https://uploads.s3.amazonaws.com/',
                fields = [{key=acl, value=public-read}, {key=key, value=1/79811084-92e0-4cf1-805c-18cc4ec20339}, {key=X-Amz-Credential, value=YCAJEPIarUtoUSiatyjuLTsqh/20250630/ru-central1/s3/aws4_request}, {key=X-Amz-Algorithm, value=AWS4-HMAC-SHA256}, {key=X-Amz-Date, value=20250630T064654Z}, {key=Policy, value=eyJleHBpcmF0aW9uIjoiMjAyNS0wNi0zMFQwODo0Njo1NFoiLCJjb25kaXRpb25zIjpbeyJhY2wiOiJwdWJsaWMtcmVhZCJ9LHsiYnVja2V0IjoicG9zdG15cG9zdC11cGxvYWQifSxbInN0YXJ0cy13aXRoIiwiJGtleSIsIjFcLyJdLHsiWC1BbXotRGF0ZSI6IjIwMjUwNjMwVDA2NDY1NFoifSx7IlgtQW16LUNyZWRlbnRpYWwiOiJZQ0FKRVBJYXJVdG9VU2lhdHlqdUxUc3FoXC8yMDI1MDYzMFwvcnUtY2VudHJhbDFcL3MzXC9hd3M0X3JlcXVlc3QifSx7IlgtQW16LUFsZ29yaXRobSI6IkFXUzQtSE1BQy1TSEEyNTYifV19}, {key=X-Amz-Signature, value=a9e1927a56145161345903c8c081a3194d90f641fed0bc49a651debd2e66a946}],
                status = 1
            )
        else:
            return UploadByFile(
                id = 1283466,
                name = 'test.jpg',
                size = 259390,
                action = 'https://uploads.s3.amazonaws.com/',
                fields = [{key=acl, value=public-read}, {key=key, value=1/79811084-92e0-4cf1-805c-18cc4ec20339}, {key=X-Amz-Credential, value=YCAJEPIarUtoUSiatyjuLTsqh/20250630/ru-central1/s3/aws4_request}, {key=X-Amz-Algorithm, value=AWS4-HMAC-SHA256}, {key=X-Amz-Date, value=20250630T064654Z}, {key=Policy, value=eyJleHBpcmF0aW9uIjoiMjAyNS0wNi0zMFQwODo0Njo1NFoiLCJjb25kaXRpb25zIjpbeyJhY2wiOiJwdWJsaWMtcmVhZCJ9LHsiYnVja2V0IjoicG9zdG15cG9zdC11cGxvYWQifSxbInN0YXJ0cy13aXRoIiwiJGtleSIsIjFcLyJdLHsiWC1BbXotRGF0ZSI6IjIwMjUwNjMwVDA2NDY1NFoifSx7IlgtQW16LUNyZWRlbnRpYWwiOiJZQ0FKRVBJYXJVdG9VU2lhdHlqdUxUc3FoXC8yMDI1MDYzMFwvcnUtY2VudHJhbDFcL3MzXC9hd3M0X3JlcXVlc3QifSx7IlgtQW16LUFsZ29yaXRobSI6IkFXUzQtSE1BQy1TSEEyNTYifV19}, {key=X-Amz-Signature, value=a9e1927a56145161345903c8c081a3194d90f641fed0bc49a651debd2e66a946}],
                status = 1,
        )
        """

    def testUploadByFile(self):
        """Test UploadByFile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
