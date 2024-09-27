#!/usr/bin/python3
import sys
from subprocess import PIPE, Popen

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        stderr=PIPE,  # Capture standard error to see if tshark is complaining
        shell=True,
        universal_newlines=False  # Handle as binary to avoid issues with non-printable characters
    )
    stdout, stderr = process.communicate()
    
    # Print stderr if there's any error or warning
    if stderr:
        print("tshark stderr:", stderr.decode('utf-8'))
    
    return stdout

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 tcp_stream_aggregator.py <pcap_file>")
        sys.exit(1)

    pcap_file = sys.argv[1]
    output_file_name = pcap_file.split('.')[0] + '_streams.txt'

    # Open the output file for writing in binary mode
    with open(output_file_name, 'wb') as output_file:
        count = 0
        max_streams = 100  # Prevent infinite loop by limiting the number of streams

        while count < max_streams:
            cmd = f'tshark -r {pcap_file} -z follow,tcp,ascii,{count}'
            print(f"Running tshark command for stream {count}: {cmd}")  # Debugging info
            stream = cmdline(cmd)

            # Debugging: Show the length of the stream output and first 200 bytes
            print(f"Stream {count} output length: {len(stream)}")
            print(stream[:200])

            # Check for encrypted streams and skip them
            if b'TLSv1.2' in stream:
                print(f"Skipping encrypted stream {count}")
                count += 1
                continue

            delimiter = b'===================================================================\n'

            if delimiter not in stream:
                print(f"No more streams found at count {count}.")
                break

            try:
                # Split the stream based on the delimiter and take the part after it
                stream_parts = stream.split(delimiter, 1)
                if len(stream_parts) > 1:
                    stream = stream_parts[1]
                else:
                    print(f"Delimiter not found correctly in stream {count}.")
                    break
            except IndexError:
                print(f"Error processing stream {count}.")
                break

            stream += b'\n---------------------------\n'
            output_file.write(stream)
            count += 1

    print(f"Finished processing {count} streams. Output written to {output_file_name}")

if __name__ == "__main__":
    main()

