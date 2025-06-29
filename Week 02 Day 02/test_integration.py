# test_integration.py

# --- Your actual code (app logic) ---
def square(x):
    return x * x

def get_side_length(shape):
    if shape == "square":
        return 6
    elif shape == "small-square":
        return 2
    else:
        raise ValueError("Unknown shape")

def calculate_area(shape):
    side = get_side_length(shape)
    return square(side)


# --- Integration Tests using pytest ---
def test_calculate_area_for_square():
    # This tests interaction of get_side_length + square
    assert calculate_area("square") == 16

def test_calculate_area_for_small_square():
    assert calculate_area("small-square") == 4

def test_calculate_area_invalid_shape():
    try:
        calculate_area("circle")
        assert False  # Should not reach here
    except ValueError:
        assert True
