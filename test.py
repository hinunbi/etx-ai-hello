from docling.document_converter import DocumentConverter

source = "https://access.redhat.com/sites/default/files/attachments/openshift_virtualization_reference_implementation_guide.pdf"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())  # output: "## Docling Technical Report[...]"

