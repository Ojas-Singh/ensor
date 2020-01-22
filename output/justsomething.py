import subprocess
# process = subprocess.Popen(['ping', '-c 4', '1.1.1.1'], 
#                            stdout=subprocess.PIPE,
#                            universal_newlines=True)

# while True:
#     output = process.stdout.readline()
#     print(output.strip())
#     # Do something else
#     return_code = process.poll()
#     if return_code is not None:
#         print('RETURN CODE', return_code)
#         # Process has finished, read rest of the output 
#         for output in process.stdout.readlines():
#             print(output.strip())
#         break


subprocess.call(["cat","requirements.txt"])