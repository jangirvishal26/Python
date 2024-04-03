from tempfile import mktemp

def generate_temp_filename():
    # Source: Generates a unique temporary filename
    return mktemp()

def write_results_to_file(results):
    # Sink: Writes results to a file
    filename = generate_temp_filename()
    with open(filename, "w+") as f:
        f.write(results)
    print("Results written to", filename)

# Example usage
results_data = "Your results here"
write_results_to_file(results_data)
