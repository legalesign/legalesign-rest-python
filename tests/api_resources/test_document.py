# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from legalesign_sdk import LegalesignSDK, AsyncLegalesignSDK
from legalesign_sdk.types import (
    DocumentListResponse,
    DocumentCreateResponse,
    DocumentRetrieveResponse,
    DocumentGetFieldsResponse,
)
from legalesign_sdk._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocument:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: LegalesignSDK) -> None:
        document = client.document.create(
            group="https://example.com",
            name="x",
            signers=[
                {
                    "email": "dev@stainless.com",
                    "firstname": "firstname",
                    "lastname": "lastname",
                }
            ],
        )
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LegalesignSDK) -> None:
        document = client.document.create(
            group="https://example.com",
            name="x",
            signers=[
                {
                    "email": "dev@stainless.com",
                    "firstname": "firstname",
                    "lastname": "lastname",
                    "attachments": ["/api/v1/attachment/IK-GV--w1tvt/"],
                    "behalfof": "behalfof",
                    "decide_later": True,
                    "expires": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "message": "message",
                    "order": 0,
                    "reviewers": [
                        {
                            "email": "dev@stainless.com",
                            "firstname": "firstname",
                            "include_link": True,
                            "lastname": "lastname",
                        }
                    ],
                    "role": "witness",
                    "sms": "sms",
                    "subject": "subject",
                    "timezone": "timezone",
                }
            ],
            append_pdf=True,
            auto_archive=True,
            cc_emails="cc_emails",
            convert_sender_to_signer=True,
            do_email=True,
            footer="footer",
            footer_height=0,
            header="header",
            header_height=0,
            pdf_password="pdf_password",
            pdf_password_type=1,
            pdftext={"foo": "string"},
            redirect="https://",
            reminders="",
            return_signer_links=True,
            signature_type=0,
            signers_in_order=True,
            signertext={"foo": "string"},
            strict_fields=True,
            tag="tag",
            tag1="tag1",
            tag2="tag2",
            template="https://example.com",
            templatepdf="https://example.com",
            text="text",
            user="https://example.com",
        )
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LegalesignSDK) -> None:
        response = client.document.with_raw_response.create(
            group="https://example.com",
            name="x",
            signers=[
                {
                    "email": "dev@stainless.com",
                    "firstname": "firstname",
                    "lastname": "lastname",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LegalesignSDK) -> None:
        with client.document.with_streaming_response.create(
            group="https://example.com",
            name="x",
            signers=[
                {
                    "email": "dev@stainless.com",
                    "firstname": "firstname",
                    "lastname": "lastname",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentCreateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LegalesignSDK) -> None:
        document = client.document.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentRetrieveResponse, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LegalesignSDK) -> None:
        response = client.document.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentRetrieveResponse, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LegalesignSDK) -> None:
        with client.document.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentRetrieveResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LegalesignSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            client.document.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: LegalesignSDK) -> None:
        document = client.document.list(
            group="group",
        )
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LegalesignSDK) -> None:
        document = client.document.list(
            group="group",
            archived="archived",
            created_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="email",
            limit=0,
            modified_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            nosigners="nosigners",
            offset=0,
            status=0,
        )
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LegalesignSDK) -> None:
        response = client.document.with_raw_response.list(
            group="group",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LegalesignSDK) -> None:
        with client.document.with_streaming_response.list(
            group="group",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentListResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_archive(self, client: LegalesignSDK) -> None:
        document = client.document.archive(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: LegalesignSDK) -> None:
        response = client.document.with_raw_response.archive(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: LegalesignSDK) -> None:
        with client.document.with_streaming_response.archive(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: LegalesignSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            client.document.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_fields(self, client: LegalesignSDK) -> None:
        document = client.document.get_fields(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentGetFieldsResponse, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_fields(self, client: LegalesignSDK) -> None:
        response = client.document.with_raw_response.get_fields(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentGetFieldsResponse, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_fields(self, client: LegalesignSDK) -> None:
        with client.document.with_streaming_response.get_fields(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentGetFieldsResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_fields(self, client: LegalesignSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            client.document.with_raw_response.get_fields(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_permanently_delete(self, client: LegalesignSDK) -> None:
        document = client.document.permanently_delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_permanently_delete(self, client: LegalesignSDK) -> None:
        response = client.document.with_raw_response.permanently_delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_permanently_delete(self, client: LegalesignSDK) -> None:
        with client.document.with_streaming_response.permanently_delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_permanently_delete(self, client: LegalesignSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            client.document.with_raw_response.permanently_delete(
                "",
            )


class TestAsyncDocument:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLegalesignSDK) -> None:
        document = await async_client.document.create(
            group="https://example.com",
            name="x",
            signers=[
                {
                    "email": "dev@stainless.com",
                    "firstname": "firstname",
                    "lastname": "lastname",
                }
            ],
        )
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLegalesignSDK) -> None:
        document = await async_client.document.create(
            group="https://example.com",
            name="x",
            signers=[
                {
                    "email": "dev@stainless.com",
                    "firstname": "firstname",
                    "lastname": "lastname",
                    "attachments": ["/api/v1/attachment/IK-GV--w1tvt/"],
                    "behalfof": "behalfof",
                    "decide_later": True,
                    "expires": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "message": "message",
                    "order": 0,
                    "reviewers": [
                        {
                            "email": "dev@stainless.com",
                            "firstname": "firstname",
                            "include_link": True,
                            "lastname": "lastname",
                        }
                    ],
                    "role": "witness",
                    "sms": "sms",
                    "subject": "subject",
                    "timezone": "timezone",
                }
            ],
            append_pdf=True,
            auto_archive=True,
            cc_emails="cc_emails",
            convert_sender_to_signer=True,
            do_email=True,
            footer="footer",
            footer_height=0,
            header="header",
            header_height=0,
            pdf_password="pdf_password",
            pdf_password_type=1,
            pdftext={"foo": "string"},
            redirect="https://",
            reminders="",
            return_signer_links=True,
            signature_type=0,
            signers_in_order=True,
            signertext={"foo": "string"},
            strict_fields=True,
            tag="tag",
            tag1="tag1",
            tag2="tag2",
            template="https://example.com",
            templatepdf="https://example.com",
            text="text",
            user="https://example.com",
        )
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLegalesignSDK) -> None:
        response = await async_client.document.with_raw_response.create(
            group="https://example.com",
            name="x",
            signers=[
                {
                    "email": "dev@stainless.com",
                    "firstname": "firstname",
                    "lastname": "lastname",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLegalesignSDK) -> None:
        async with async_client.document.with_streaming_response.create(
            group="https://example.com",
            name="x",
            signers=[
                {
                    "email": "dev@stainless.com",
                    "firstname": "firstname",
                    "lastname": "lastname",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentCreateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLegalesignSDK) -> None:
        document = await async_client.document.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentRetrieveResponse, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLegalesignSDK) -> None:
        response = await async_client.document.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentRetrieveResponse, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLegalesignSDK) -> None:
        async with async_client.document.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentRetrieveResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLegalesignSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            await async_client.document.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLegalesignSDK) -> None:
        document = await async_client.document.list(
            group="group",
        )
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLegalesignSDK) -> None:
        document = await async_client.document.list(
            group="group",
            archived="archived",
            created_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="email",
            limit=0,
            modified_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            nosigners="nosigners",
            offset=0,
            status=0,
        )
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLegalesignSDK) -> None:
        response = await async_client.document.with_raw_response.list(
            group="group",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLegalesignSDK) -> None:
        async with async_client.document.with_streaming_response.list(
            group="group",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentListResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncLegalesignSDK) -> None:
        document = await async_client.document.archive(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncLegalesignSDK) -> None:
        response = await async_client.document.with_raw_response.archive(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncLegalesignSDK) -> None:
        async with async_client.document.with_streaming_response.archive(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncLegalesignSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            await async_client.document.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_fields(self, async_client: AsyncLegalesignSDK) -> None:
        document = await async_client.document.get_fields(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentGetFieldsResponse, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_fields(self, async_client: AsyncLegalesignSDK) -> None:
        response = await async_client.document.with_raw_response.get_fields(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentGetFieldsResponse, document, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_fields(self, async_client: AsyncLegalesignSDK) -> None:
        async with async_client.document.with_streaming_response.get_fields(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentGetFieldsResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_fields(self, async_client: AsyncLegalesignSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            await async_client.document.with_raw_response.get_fields(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_permanently_delete(self, async_client: AsyncLegalesignSDK) -> None:
        document = await async_client.document.permanently_delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_permanently_delete(self, async_client: AsyncLegalesignSDK) -> None:
        response = await async_client.document.with_raw_response.permanently_delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert document is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_permanently_delete(self, async_client: AsyncLegalesignSDK) -> None:
        async with async_client.document.with_streaming_response.permanently_delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_permanently_delete(self, async_client: AsyncLegalesignSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            await async_client.document.with_raw_response.permanently_delete(
                "",
            )
