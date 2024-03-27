import os
import json

def merge_json_files(directory):
    merged_data = {"links": []}
    
    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                merged_data['links'].extend(data['links'])

    # Sort the links alphabetically
    merged_data['links'] = sorted(merged_data['links'])

    return merged_data

def save_merged_data(merged_data, output_file):
    with open(output_file, 'w') as outfile:
        json.dump(merged_data, outfile, indent=4)

if __name__ == "__main__":
    directory = "separated"
    output_file = "websites.json"
    
    merged_data = merge_json_files(directory)
    save_merged_data(merged_data, output_file)
    print("Merged JSON files and saved as", output_file)

