from domino.base_piece import BasePiece
from .models import InputModel, OutputModel

class HTMLPiece(BasePiece):
    
    def piece_function(self, input_data: InputModel ):

        self.logger.info("Starting html_content process...")
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{input_data.html_title}</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>This is a simple HTML page generated by a Python function.</p>
        </body>
        </html>
        """
        return OutputModel(
            html=html_content,
        )