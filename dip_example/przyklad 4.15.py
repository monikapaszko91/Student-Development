import test
def output(data, format="text"):

    output_function = getattr(test, "output_%s" % format, test.output_text)
    return output_function(data)