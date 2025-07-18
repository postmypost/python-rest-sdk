# coding: utf-8

"""
    Postmypost REST API

    Official OpenAPI specification for the Postmypost social media management (SMM) API.  Postmypost is a secure, reliable, and highly trusted social media management platform, recommended by thousands of SMM professionals and agencies. All integrations are built exclusively on official APIs, ensuring maximum security, compliance, and no risk of account blocking or bans.  With the Postmypost API, you can automate social media marketing, content scheduling, publishing, analytics, and workflow management across all major platforms, including Instagram, Facebook, Twitter, Threads, Bluesky, LinkedIn, Pinterest, YouTube, Rutube, TikTok, Discord, Reddit, VKontakte, Telegram, Viber, Odnoklassniki, Bitrix, Medium, Tumblr, Mastodon, and Webhook.  Why choose Postmypost? - 100% official and secure integrations with social networks - No risk of account blocking — all APIs are fully compliant - Trusted by thousands of businesses, agencies, and SMM professionals - Powerful automation, scheduling, and analytics tools - Friendly support and clear documentation  For agencies, businesses, and creators looking for the safest, most reliable way to automate and scale their social media presence, Postmypost is the recommended choice. 

    The version of the OpenAPI document: 4.1.4
    Contact: support@postmypost.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from postmypost_rest_sdk.models.upload_by_file import UploadByFile
from postmypost_rest_sdk.models.upload_by_url import UploadByUrl
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

UPLOADINIT_ONE_OF_SCHEMAS = ["UploadByFile", "UploadByUrl"]

class UploadInit(BaseModel):
    """
    UploadInit
    """
    # data type: UploadByUrl
    oneof_schema_1_validator: Optional[UploadByUrl] = None
    # data type: UploadByFile
    oneof_schema_2_validator: Optional[UploadByFile] = None
    actual_instance: Optional[Union[UploadByFile, UploadByUrl]] = None
    one_of_schemas: Set[str] = { "UploadByFile", "UploadByUrl" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = UploadInit.model_construct()
        error_messages = []
        match = 0
        # validate data type: UploadByUrl
        if not isinstance(v, UploadByUrl):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UploadByUrl`")
        else:
            match += 1
        # validate data type: UploadByFile
        if not isinstance(v, UploadByFile):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UploadByFile`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in UploadInit with oneOf schemas: UploadByFile, UploadByUrl. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in UploadInit with oneOf schemas: UploadByFile, UploadByUrl. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into UploadByUrl
        try:
            instance.actual_instance = UploadByUrl.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UploadByFile
        try:
            instance.actual_instance = UploadByFile.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into UploadInit with oneOf schemas: UploadByFile, UploadByUrl. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into UploadInit with oneOf schemas: UploadByFile, UploadByUrl. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], UploadByFile, UploadByUrl]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


