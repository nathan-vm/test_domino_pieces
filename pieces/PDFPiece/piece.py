from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import base64
from io import BytesIO
from reportlab.pdfgen import canvas


class PDFPiece(BasePiece):
    
    def piece_function(self, input_data: InputModel):
        # Create a BytesIO buffer to hold the PDF content
        pdf_buffer = BytesIO()

        # Create a PDF using reportlab
        pdf_canvas = canvas.Canvas(pdf_buffer)
        pdf_canvas.drawString(100, 100, f"{input_data.pdf_title} Hello, this is a PDF generated in Python!")
        pdf_canvas.showPage()
        pdf_canvas.save()

        # Get the PDF content from the buffer
        pdf_content = pdf_buffer.getvalue()

        # Encode the PDF content as base64
        base64_pdf = base64.b64encode(pdf_content).decode('utf-8')

        # Finally, results should return as an Output model
        return OutputModel(
            pdf=base64_pdf,
        )