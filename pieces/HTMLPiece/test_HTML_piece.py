from domino.testing import piece_dry_run

def test_HTMLPiece_piece():
    input_data = dict(
        html_title="Nathan",
    )
    output_data = piece_dry_run(
        "HTMLPiece",
        input_data
    )

    assert output_data["base64_content"] is not None