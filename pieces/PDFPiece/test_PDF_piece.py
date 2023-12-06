from domino.testing import piece_dry_run

def test_PDF_piece():
    input_data = dict(
        pdf_title="Nathan",
    )
    output_data = piece_dry_run(
        "PDFPiece",
        input_data
    )

    assert output_data["pdf"] is not None