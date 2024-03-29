import subprocess
import time
import logging
import psutil
import GPUtil

def measure_execution_time_and_resources(software_path, log_file):
    """
    Measure the execution time of a software and log resource usage.

    Args:
    - software_path (str): The path to the software executable.
    - log_file (str): The path to the log file.
    """
    start_time = time.time()

    try:
        # Launch the software
        subprocess.run(software_path, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing '{software_path}': {e}")
        return

    end_time = time.time()
    execution_time = end_time - start_time
    logging.info(f"Execution time of '{software_path}': {execution_time:.2f} seconds")

    # Measure CPU, GPU, and RAM usage
    cpu_usage = psutil.cpu_percent()
    gpu_usage = GPUtil.getGPUs()[0].load * 100  # Assuming single GPU
    ram_usage = psutil.virtual_memory().percent

    logging.info(f"CPU Usage: {cpu_usage:.2f}%")
    logging.info(f"GPU Usage: {gpu_usage:.2f}%")
    logging.info(f"RAM Usage: {ram_usage:.2f}%")

if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(filename='execution_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Replace "path/to/software.exe" with the actual path to the software executable
    software_path = "path/to/software.exe"
    measure_execution_time_and_resources(software_path, 'execution_log.txt')
