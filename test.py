from docling.document_converter import DocumentConverter

source = "https://access.redhat.com/sites/default/files/attachments/openshift_virtualization_reference_implementation_guide.pdf"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)
with open("output.md", "w") as file:
	file.write(result.document.export_to_markdown())

