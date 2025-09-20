from sample_module import Sample

def test_sample():
    sample = Sample(10)
    assert sample.get_value() == 10

    sample.set_value(20)
    assert sample.get_value() == 20

    assert repr(sample) == "Sample(value=20)"
