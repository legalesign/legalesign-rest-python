# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from legalesign_sdk import LegalesignSDK, AsyncLegalesignSDK
from legalesign_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPdf:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: LegalesignSDK, respx_mock: MockRouter) -> None:
        respx_mock.get("/pdf/docId/").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        pdf = client.pdf.retrieve(
            "docId",
        )
        assert pdf.is_closed
        assert pdf.json() == {"foo": "bar"}
        assert cast(Any, pdf.is_closed) is True
        assert isinstance(pdf, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: LegalesignSDK, respx_mock: MockRouter) -> None:
        respx_mock.get("/pdf/docId/").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        pdf = client.pdf.with_raw_response.retrieve(
            "docId",
        )

        assert pdf.is_closed is True
        assert pdf.http_request.headers.get("X-Stainless-Lang") == "python"
        assert pdf.json() == {"foo": "bar"}
        assert isinstance(pdf, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: LegalesignSDK, respx_mock: MockRouter) -> None:
        respx_mock.get("/pdf/docId/").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.pdf.with_streaming_response.retrieve(
            "docId",
        ) as pdf:
            assert not pdf.is_closed
            assert pdf.http_request.headers.get("X-Stainless-Lang") == "python"

            assert pdf.json() == {"foo": "bar"}
            assert cast(Any, pdf.is_closed) is True
            assert isinstance(pdf, StreamedBinaryAPIResponse)

        assert cast(Any, pdf.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: LegalesignSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            client.pdf.with_raw_response.retrieve(
                "",
            )


class TestAsyncPdf:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncLegalesignSDK, respx_mock: MockRouter) -> None:
        respx_mock.get("/pdf/docId/").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        pdf = await async_client.pdf.retrieve(
            "docId",
        )
        assert pdf.is_closed
        assert await pdf.json() == {"foo": "bar"}
        assert cast(Any, pdf.is_closed) is True
        assert isinstance(pdf, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncLegalesignSDK, respx_mock: MockRouter) -> None:
        respx_mock.get("/pdf/docId/").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        pdf = await async_client.pdf.with_raw_response.retrieve(
            "docId",
        )

        assert pdf.is_closed is True
        assert pdf.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await pdf.json() == {"foo": "bar"}
        assert isinstance(pdf, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncLegalesignSDK, respx_mock: MockRouter) -> None:
        respx_mock.get("/pdf/docId/").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.pdf.with_streaming_response.retrieve(
            "docId",
        ) as pdf:
            assert not pdf.is_closed
            assert pdf.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await pdf.json() == {"foo": "bar"}
            assert cast(Any, pdf.is_closed) is True
            assert isinstance(pdf, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, pdf.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncLegalesignSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            await async_client.pdf.with_raw_response.retrieve(
                "",
            )
