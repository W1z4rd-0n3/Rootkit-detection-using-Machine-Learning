import subprocess

#For python 3.7
def run_volatility_plugin(plugin, args):
    command = f"volatility -f /path/to/memory_dump {plugin} {args}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

# For python 3.6
def run_volatility_plugin(plugin, args):
    command = f"volatility -f /path/to/memory_dump {plugin} {args}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode('utf-8')

if __name__ == "__main__":
    plugins = [
        ("modules", ""),
        ("modscan", ""),
        ("driverscan", ""),
        ("threads", ""),
        ("threads", "-F OrphanThread"),
        ("driverirp", ""),
        ("ssdt", ""),
        ("ssdt", "--verbose"),
        ("callbacks", ""),
        ("timers", ""),
        ("devicetree", "")
    ]

    consolidated_output_file = "consolidated_output.txt"
    
    # Extracting the features to an output file
    with open(consolidated_output_file, 'w') as consolidated_output:
        for plugin, args in plugins:
            plugin_output = run_volatility_plugin(plugin, args)
            consolidated_output.write(f"\n\n\n== {plugin} {args} ==\n")
            consolidated_output.write(plugin_output)

    print("Extraction and consolidation completed.")
