# Document

Types:

```python
from legalesign_sdk.types import (
    DocumentStatusEnum,
    ListMeta,
    PdfFieldValidationEnum,
    DocumentCreateResponse,
    DocumentRetrieveResponse,
    DocumentListResponse,
    DocumentGetFieldsResponse,
)
```

Methods:

- <code title="post /document/">client.document.<a href="./src/legalesign_sdk/resources/document.py">create</a>(\*\*<a href="src/legalesign_sdk/types/document_create_params.py">params</a>) -> <a href="./src/legalesign_sdk/types/document_create_response.py">DocumentCreateResponse</a></code>
- <code title="get /document/{docId}/">client.document.<a href="./src/legalesign_sdk/resources/document.py">retrieve</a>(doc_id) -> <a href="./src/legalesign_sdk/types/document_retrieve_response.py">DocumentRetrieveResponse</a></code>
- <code title="get /document/">client.document.<a href="./src/legalesign_sdk/resources/document.py">list</a>(\*\*<a href="src/legalesign_sdk/types/document_list_params.py">params</a>) -> <a href="./src/legalesign_sdk/types/document_list_response.py">DocumentListResponse</a></code>
- <code title="delete /document/{docId}/">client.document.<a href="./src/legalesign_sdk/resources/document.py">archive</a>(doc_id) -> None</code>
- <code title="get /document/{docId}/fields/">client.document.<a href="./src/legalesign_sdk/resources/document.py">get_fields</a>(doc_id) -> <a href="./src/legalesign_sdk/types/document_get_fields_response.py">DocumentGetFieldsResponse</a></code>
- <code title="delete /document/{docId}/delete/">client.document.<a href="./src/legalesign_sdk/resources/document.py">permanently_delete</a>(doc_id) -> None</code>

# Group

Types:

```python
from legalesign_sdk.types import GroupRetrieveResponse, GroupListResponse
```

Methods:

- <code title="post /group/">client.group.<a href="./src/legalesign_sdk/resources/group.py">create</a>(\*\*<a href="src/legalesign_sdk/types/group_create_params.py">params</a>) -> None</code>
- <code title="get /group/{groupId}/">client.group.<a href="./src/legalesign_sdk/resources/group.py">retrieve</a>(group_id) -> <a href="./src/legalesign_sdk/types/group_retrieve_response.py">GroupRetrieveResponse</a></code>
- <code title="get /group/">client.group.<a href="./src/legalesign_sdk/resources/group.py">list</a>(\*\*<a href="src/legalesign_sdk/types/group_list_params.py">params</a>) -> <a href="./src/legalesign_sdk/types/group_list_response.py">GroupListResponse</a></code>

# Pdf

Methods:

- <code title="get /pdf/{docId}/">client.pdf.<a href="./src/legalesign_sdk/resources/pdf.py">retrieve</a>(doc_id) -> BinaryAPIResponse</code>

# Signer

Types:

```python
from legalesign_sdk.types import (
    SignerStatusEnum,
    SignerRetrieveResponse,
    SignerRetrieveFieldsResponse,
)
```

Methods:

- <code title="get /signer/{signerId}/">client.signer.<a href="./src/legalesign_sdk/resources/signer.py">retrieve</a>(signer_id) -> <a href="./src/legalesign_sdk/types/signer_retrieve_response.py">SignerRetrieveResponse</a></code>
- <code title="get /signer/{signerId}/new-link/">client.signer.<a href="./src/legalesign_sdk/resources/signer.py">get_access_link</a>(signer_id) -> None</code>
- <code title="get /signer/{signerId}/fields1/">client.signer.<a href="./src/legalesign_sdk/resources/signer.py">retrieve_fields</a>(signer_id) -> <a href="./src/legalesign_sdk/types/signer_retrieve_fields_response.py">SignerRetrieveFieldsResponse</a></code>
- <code title="post /signer/{signerId}/send-reminder/">client.signer.<a href="./src/legalesign_sdk/resources/signer.py">send_reminder</a>(signer_id, \*\*<a href="src/legalesign_sdk/types/signer_send_reminder_params.py">params</a>) -> None</code>

# Status

Types:

```python
from legalesign_sdk.types import StatusRetrieveResponse
```

Methods:

- <code title="get /status/{docId}/">client.status.<a href="./src/legalesign_sdk/resources/status.py">retrieve</a>(doc_id) -> <a href="./src/legalesign_sdk/types/status_retrieve_response.py">StatusRetrieveResponse</a></code>

# Template

Types:

```python
from legalesign_sdk.types import TemplateRetrieveResponse, TemplateListResponse
```

Methods:

- <code title="post /template/">client.template.<a href="./src/legalesign_sdk/resources/template.py">create</a>(\*\*<a href="src/legalesign_sdk/types/template_create_params.py">params</a>) -> None</code>
- <code title="get /template/{templateId}/">client.template.<a href="./src/legalesign_sdk/resources/template.py">retrieve</a>(template_id) -> <a href="./src/legalesign_sdk/types/template_retrieve_response.py">TemplateRetrieveResponse</a></code>
- <code title="patch /template/{templateId}/">client.template.<a href="./src/legalesign_sdk/resources/template.py">update</a>(template_id, \*\*<a href="src/legalesign_sdk/types/template_update_params.py">params</a>) -> None</code>
- <code title="get /template/">client.template.<a href="./src/legalesign_sdk/resources/template.py">list</a>(\*\*<a href="src/legalesign_sdk/types/template_list_params.py">params</a>) -> <a href="./src/legalesign_sdk/types/template_list_response.py">TemplateListResponse</a></code>

# Templatepdf

Types:

```python
from legalesign_sdk.types import (
    TemplatePdf,
    TemplatepdfListResponse,
    TemplatepdfGetEditLinkResponse,
)
```

Methods:

- <code title="post /templatepdf/">client.templatepdf.<a href="./src/legalesign_sdk/resources/templatepdf/templatepdf.py">create</a>(\*\*<a href="src/legalesign_sdk/types/templatepdf_create_params.py">params</a>) -> None</code>
- <code title="get /templatepdf/{pdfId}/">client.templatepdf.<a href="./src/legalesign_sdk/resources/templatepdf/templatepdf.py">retrieve</a>(pdf_id) -> <a href="./src/legalesign_sdk/types/template_pdf.py">TemplatePdf</a></code>
- <code title="get /templatepdf/">client.templatepdf.<a href="./src/legalesign_sdk/resources/templatepdf/templatepdf.py">list</a>(\*\*<a href="src/legalesign_sdk/types/templatepdf_list_params.py">params</a>) -> <a href="./src/legalesign_sdk/types/templatepdf_list_response.py">TemplatepdfListResponse</a></code>
- <code title="get /templatepdf/{pdfId}/edit-link/">client.templatepdf.<a href="./src/legalesign_sdk/resources/templatepdf/templatepdf.py">get_edit_link</a>(pdf_id) -> str</code>

## Fields

Types:

```python
from legalesign_sdk.types.templatepdf import FieldListResponse
```

Methods:

- <code title="post /templatepdf/{pdfId}/fields/">client.templatepdf.fields.<a href="./src/legalesign_sdk/resources/templatepdf/fields.py">create</a>(pdf_id, \*\*<a href="src/legalesign_sdk/types/templatepdf/field_create_params.py">params</a>) -> None</code>
- <code title="get /templatepdf/{pdfId}/fields/">client.templatepdf.fields.<a href="./src/legalesign_sdk/resources/templatepdf/fields.py">list</a>(pdf_id) -> <a href="./src/legalesign_sdk/types/templatepdf/field_list_response.py">FieldListResponse</a></code>
