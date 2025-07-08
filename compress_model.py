import gzip
import shutil

# Input and output file paths
input_path = r"C:\Users\Shaik MudassirAhamad\Customer churn prediction\model.pkl"
output_path = r"C:\Users\Shaik MudassirAhamad\Customer churn prediction\model.pkl.gz"

# Compress the .pkl file
with open(input_path, "rb") as f_in:
    with gzip.open(output_path, "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)

print("Compression complete: model.pkl.gz")
