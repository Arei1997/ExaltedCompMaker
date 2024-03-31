
def parse_variants(text):
    # Split the text into lines for processing
    lines = text.strip().split('\n')
    
    combinations = {}
    
    # Temporary storage for the current variant being processed
    current_variant = ""
    current_urls = []
    
    for line in lines:
        if line.startswith("Exalted Variant"):
            # Process the previous variant
            if current_variant:
                # Sort the variant names alphabetically and join them as a single string
                variant_names_sorted = ', '.join(sorted(current_variant.split(', ')))
                combinations[variant_names_sorted] = [variant_number] + current_urls
            
            # Reset for the next variant
            current_urls = []
            
            # Extract the variant number and names
            parts = line.split(" (")
            variant_number = int(parts[0].split(" ")[-1].replace(":", ""))
            current_variant = parts[1].split("):")[0]
        
        elif "https://" in line:
            # Extract URL
            url = line.split(" ")[0]
            current_urls.append(url)
        elif line == "?":
            # Handle missing URLs with "NULL"
            current_urls.append("NULL")
    
    # Don't forget to add the last variant
    if current_variant:
        variant_names_sorted = ', '.join(sorted(current_variant.split(', ')))
        combinations[variant_names_sorted] = [variant_number] + current_urls

    return combinations
